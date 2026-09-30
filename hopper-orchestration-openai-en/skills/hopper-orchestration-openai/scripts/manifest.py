#!/usr/bin/env python3
"""Snapshot and compare a quiescent artifact tree. Standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys


def exclusions(values):
    result = []
    for value in values:
        path = PurePosixPath(value)
        if not value or path.is_absolute() or '..' in path.parts or str(path) == '.':
            raise ValueError('exclusion must be a nonempty relative path inside the root')
        result.append(path.as_posix())
    return sorted(set(result))


def excluded(name, omitted):
    return any(name == item or name.startswith(item + '/') for item in omitted)


def inventory(root, omitted):
    entries = {'.': {'type': 'directory', 'mode': stat.S_IMODE(root.stat().st_mode)}}

    def visit(directory):
        for path in sorted(directory.iterdir()):
            name = path.relative_to(root).as_posix()
            if excluded(name, omitted):
                continue
            before = path.lstat()
            entry = {'mode': stat.S_IMODE(before.st_mode)}
            if stat.S_ISLNK(before.st_mode):
                # Never traverse symlinks or silently omit an external dependency.
                raise ValueError(f'symlink requires a separate dependency manifest: {name}')
            if stat.S_ISDIR(before.st_mode):
                entry['type'] = 'directory'
                entries[name] = entry
                visit(path)
            elif stat.S_ISREG(before.st_mode):
                digest = hashlib.sha256()
                # O_NOFOLLOW also catches replacement with a symlink during capture.
                descriptor = os.open(path, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0))
                with os.fdopen(descriptor, 'rb') as stream:
                    opened = os.fstat(stream.fileno())
                    if not stat.S_ISREG(opened.st_mode) or (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
                        raise ValueError(f'entry changed during capture: {name}')
                    for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                        digest.update(chunk)
                after = path.lstat()
                if (before.st_ino, before.st_dev, before.st_mode, before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (after.st_ino, after.st_dev, after.st_mode, after.st_size, after.st_mtime_ns, after.st_ctime_ns):
                    raise ValueError(f'entry changed during capture: {name}')
                entry.update(type='file', size=after.st_size, sha256=digest.hexdigest())
                entries[name] = entry
            else:
                raise ValueError(f'unsupported filesystem entry: {name}')

    visit(root)
    return entries


def snapshot(root, omitted):
    if not root.is_dir():
        raise ValueError('artifact root must be an existing directory')
    first = inventory(root, omitted)
    second = inventory(root, omitted)
    if first != second:
        raise ValueError('artifact changed during capture; wait for its writer to release it')
    return {'schema_version': 1, 'root': str(root), 'excluded': omitted, 'entries': first}


def compare(before, after):
    old, new = before['entries'], after['entries']
    return {'added': sorted(new.keys() - old.keys()),
            'removed': sorted(old.keys() - new.keys()),
            'changed': sorted(name for name in old.keys() & new.keys() if old[name] != new[name])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('snapshot')
    create.add_argument('root', type=Path)
    create.add_argument('output', type=Path)
    create.add_argument('--exclude', action='append', default=[], help='Exact relative file/directory, repeatable. No implicit exclusions.')
    verify = commands.add_parser('verify')
    verify.add_argument('root', type=Path)
    verify.add_argument('manifest', type=Path)
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    if args.command == 'snapshot':
        omitted = exclusions(args.exclude)
        output = args.output.resolve()
        if output.is_relative_to(root) and not excluded(output.relative_to(root).as_posix(), omitted):
            raise ValueError('output must be outside the artifact or inside an explicit exclusion')
        document = snapshot(root, omitted)
        # Never replace a reviewed baseline or a preexisting path.
        with output.open('x', encoding='utf-8') as stream:
            json.dump(document, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write('\n')
        print(json.dumps({'manifest': str(output), 'entries': len(document['entries'])}))
        return 0
    before = json.loads(args.manifest.read_text(encoding='utf-8'))
    if not isinstance(before, dict) or type(before.get('schema_version')) is not int or before['schema_version'] != 1 or before.get('root') != str(root):
        raise ValueError('manifest version or artifact root differs')
    if not isinstance(before.get('excluded'), list) or not all(isinstance(item, str) for item in before['excluded']):
        raise ValueError('invalid manifest exclusions')
    omitted = exclusions(before['excluded'])
    if omitted != before['excluded'] or not isinstance(before['entries'], dict):
        raise ValueError('invalid manifest')
    after = snapshot(root, omitted)
    changes = compare(before, after)
    equal = not any(changes.values())
    print(json.dumps({'matches': equal, **changes}, ensure_ascii=False, sort_keys=True))
    return 0 if equal else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'manifest: {error}', file=sys.stderr)
        sys.exit(2)
