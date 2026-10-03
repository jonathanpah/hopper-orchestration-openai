# Verification and limits — 0.2.2

This release restores the public verification summary, fixes links in language
packages, and synchronizes distribution identity. Orchestration rules and the
inventory helper are unchanged from the previous version. An audit found
different content labelled `0.2.1`; the correction uses a new version without
replacing the old assets again.

## Earlier behavioral evidence

The corrected Portuguese prototype passed three focused scenarios: detecting
a file added after review, independent review and validation of a corrected
CSV delivery, and partial pause/resumption while independent work continued.

The CSV scenario exposed defects in the synthetic delivery. Its final version
passed seven focused checks and ten existing regressions, followed by independent
review and validation. These checks concern that delivery, not seventeen extra
skill scenarios. Two corrections of the test product were needed.

The earlier 21-case campaign used a different prototype and included failures.
It was not repeated in full on the corrected candidate or this release. The
three focused cases passed on their final versions within the trial conditions.
Pause/resumption evidence used partial observation, not a complete trace.

Later packaging changed the version, presentation, record-directory name, and
qualified invocation prompt. The helper stayed unchanged. Translation obligations
were compared; a complete new English campaign was not performed.

## Distribution checks

Verification distinguishes:

- Structure: official skill validator, YAML/JSON, portable schema,
  manifest consistency, and links within each package.
- Integrity: complete composition, content, commit, and ZIP SHA256SUMS.
- Installation: complete plugin content and discovery of a single enabled
  orchestration entry in each checked account and runtime.
- Behavior: decisions, handoffs, execution, and effects actually observed.

Discovery checks use the native app-server's `skills/list` and send no model
requests. They do not establish implicit model selection, complete execution of
the installed skill, or graphical interaction. See the
[release note](https://github.com/jonathanpah/hopper-orchestration-openai/releases/tag/v0.2.2)
for verification coverage of the published distribution.

Before updating, verify the commit and SHA256SUMS. Content changes require a new
version; a version number alone is not proof of identity. Compare the entire
installed package, including manifests and documentation.

## Basis and limits

The design considers official guidance for
[skills](https://learn.chatgpt.com/docs/build-skills),
[packaging](https://developers.openai.com/plugins/build/plugins),
[orchestration](https://developers.openai.com/api/docs/guides/agents/orchestration),
and [multi-agent](https://developers.openai.com/api/docs/guides/agents-api/multi-agent).
Four roles and only `high`, `xhigh`, `max` are project requirements, not universal
OpenAI requirements. `agents/openai.yaml` configures presentation and invocation,
not subagent models, efforts, or sandboxes.

Requested configuration does not prove effective model/effort without metadata.
Instructions do not create technical isolation by role. Local manifests do not
cover external services or concurrent writers. Native discovery is not behavioral
execution. No OpenAI certification or freedom from errors in every task, model,
and environment is claimed.
