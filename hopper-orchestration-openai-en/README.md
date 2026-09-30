# hopper-orchestration-openai

**English** | [Português (Brasil)](../hopper-orchestration-openai-pt-br/README.md)

A skill for coordinating OpenAI agents in Codex CLI and the app, with an
identified delivery, independent review, and proved criteria.

The orchestrator owns the conversation and acceptance decision. The executor
produces the delivery. The reviewer examines correctness and checks. The
validator proves the result, including entirely local results. Only the
orchestrator creates agents.

## Behavior

- Four roles: orchestrator, executor, reviewer, and validator.
- Allowed efforts: `high`, `xhigh`, and `max`. Preserve the main conversation's
  model and effort. Explicit user choices take precedence.
- Without explicit choices, the orchestrator selects available OpenAI models
  and starts subagents at `high`. This is this skill's policy, not a universal
  OpenAI recommendation.
- Start with one executor; parallelize only with concrete benefit and separate
  resources. Routine composition does not require an approval panel.
- Self-contained missions, one resource owner, and explicit transfers.
- Compare complete composition before review, validation, and acceptance.
- Review and validate correction impacts; reuse valid evidence.
- Pauses distinguish agents, processes, parts, and stage state.

Read the [skill](skills/hopper-orchestration-openai/SKILL.md) and
[document index](index.md). Analyzing, translating, publishing, or installing
the skill does not start its orchestration workflow.

## Install in Codex

Distribution uses a plugin with portable `plugin.json`, `skills/`,
`agents/openai.yaml` metadata, and a compatible `.codex-plugin/plugin.json`,
following [OpenAI's documentation](https://developers.openai.com/plugins/build/plugins).
Installed name and display name are `hopper-orchestration-openai`. This folder
is the English package, version `0.2.1`.

To install English, clone the repository and register this language folder:

```sh
git clone https://github.com/jonathanpah/hopper-orchestration-openai.git
codex plugin marketplace add ./hopper-orchestration-openai/hopper-orchestration-openai-en
codex plugin add hopper-orchestration-openai@hopper-orchestration-openai
```

For the published Portuguese package, the repository marketplace provides:

```sh
codex plugin marketplace add jonathanpah/hopper-orchestration-openai --ref v0.2.1
codex plugin add hopper-orchestration-openai@hopper-orchestration-openai
```

Choose one installation method per account. Inspect destination, origin, and
local changes before updating an existing checkout. Do not also install a
standalone copy in `.agents/skills` or `.codex/skills`, or both languages in
one account.

The app and CLI share local configuration for the same account and machine.
Installing on a VPS does not install in the Mac's local account. Check native
discovery at each destination and the app's skill list. Open conversations
may retain earlier instructions; installing does not require interrupting them.

## Names and invocation

Select `hopper-orchestration-openai` in the skill picker or invoke its native
plugin-qualified identifier:

```text
$hopper-orchestration-openai:hopper-orchestration-openai
```

Describe the deliverable and authorized scope. An orchestration request can
also activate the skill: `allow_implicit_invocation: true` permits that matching.
Discussions about the skill itself do not start agents.

Codex may show the qualified identifier
`hopper-orchestration-openai:hopper-orchestration-openai`. The prefix identifies
the plugin; it is not another skill or a language variant. Interface metadata
does not configure subagent models, efforts, or permissions.

## Migration and removal

After verifying the new installation, retire the previous one from Codex only:

```sh
codex plugin remove hopper-orchestration@hopper-orchestration
codex plugin marketplace remove hopper-orchestration
```

Inspect and retire old `hopper-orchestration` copies from Codex skill roots.
Mandatory AGENTS.md references need updating with the owner's authorization;
deleting installation does not fix those instructions. Preserve old task
records and installations in other products outside the scope.

To remove the new version:

```sh
codex plugin remove hopper-orchestration-openai@hopper-orchestration-openai
codex plugin marketplace remove hopper-orchestration-openai
```

## Generated records

Each stage uses `docs-by-hopper-orchestration-openai/YYYYMMDD-HHMMSS-topic/`
at the serviced project root. It contains missions, round reports, `log.md`,
`summary.md`, and `evidence/`. The index is at the collection root. Dates and
times use the observed time zone and UTC offset. The installation root does
not receive records for other projects.

Old `docs-by-hopper-orchestration/` records remain historical. Consult them
when needed for continuity and record their origin; do not rename them or
treat old sessions as current agents.

## Updates and limits

For a registered Git source, inspect the new release, update the marketplace
ref, and run `codex plugin add` again. For a local source, inspect changes,
update the checkout with `git pull --ff-only`, and reinstall. Check version,
content, and discovery after each update.

The workflow depends on native session capabilities. Do not assume models,
agent counts, role isolation, or metadata absent from the tool. The inventory
helper requires Python 3.9 or newer; without it, contracts require another
verifiable identity appropriate to the artifact.

Claude manifests are retained for format compatibility. This release targets
Codex; it does not install or prove the workflow in Claude.



## Participate and license

Use [Issues](https://github.com/jonathanpah/hopper-orchestration-openai/issues)
for reproducible failures and concrete proposals, and
[Discussions](https://github.com/jonathanpah/hopper-orchestration-openai/discussions)
for questions. Read [Contributing](CONTRIBUTING.md), [Security](SECURITY.md),
and [Code of Conduct](CODE_OF_CONDUCT.md).

Copyright (c) 2026 hopper-orchestration-openai contributors. [MIT License](LICENSE).
Independent project; no affiliation with or endorsement by OpenAI is claimed.
