# Security Policy

Report suspected vulnerabilities in hopper-orchestration-openai through GitHub's private vulnerability reporting.

## Report privately

Open [Report a vulnerability](https://github.com/jonathanpah/hopper-orchestration-openai/security/advisories/new), or select that option on the repository's [Security page](https://github.com/jonathanpah/hopper-orchestration-openai/security). A GitHub account is required.

Keep suspected vulnerabilities and exploit details out of public issues, discussions, and pull requests until disclosure is coordinated with the maintainer. Use public issues for ordinary bugs and proposals, and discussions for general questions.

Include:

- The affected release tag or commit and the relevant file, instruction, or documentation section.
- The host, model, configuration, and permissions needed to reproduce the behavior, without private account details.
- A minimal reproduction using synthetic data and disposable resources.
- Expected and observed behavior, potential impact, and any uncertainty or limits in the evidence.

Do not submit passwords, access tokens, private keys, private conversation histories, or unredacted production records. Test only resources you are authorized to use, and do not repeat an unsafe action just to complete a report.

## Scope and security expectations

This repository contains an orchestration skill, host metadata, and documentation, including installation examples. Relevant reports include flaws in these materials that can lead to actions without user authorization, exposure of credentials or private records, or changes outside the authorized scope.

The intended boundaries are:

- Orchestration starts only after an explicit user request or invocation.
- Plans, records, handoffs, and externally supplied content do not grant additional authority or expand the authorized scope.
- Agents respect the owner of each modifiable item, preserve unrelated changes, and keep secrets out of recorded evidence.

The skill provides instructions to an assistant. Enforcement also depends on the host's permissions, sandbox, tools, and model behavior. The skill is not a substitute for those controls. Describe the repository's contribution to a suspected failure; if another product is also affected, use that product's security reporting process as appropriate.

## Versions and handling

Identify the version you used, including older releases when relevant. A report is welcome even if you cannot safely check the latest version.

hopper-orchestration-openai contributors reviews reports through the private reporting channel. Confirmed affected versions and fixes can be documented in repository changes, releases, or security advisories. Coordinate public disclosure through the private report. No response or remediation deadline is guaranteed.
