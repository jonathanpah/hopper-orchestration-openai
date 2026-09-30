# Contracts and records — version 2

The orchestrator reads this reference before creating a stage. Each agent
receives it with its mission. Templates in `assets/` are starting points;
replace fields in braces in actual missions and never invent unavailable values.

## Destination and identity

Use `docs-by-hopper-orchestration-openai/` at the serviced project root,
confirmed by the mission. The skill root is the destination only when the
skill itself is the serviced project. Without a project, use an authorized
working directory and state its location.

```text
docs-by-hopper-orchestration-openai/
  index.md
  YYYYMMDD-HHMMSS-topic/
    mission-executor.md
    mission-reviewer.md
    mission-validator.md
    r1-executor.md
    r1-reviewer.md
    r1-validator.md
    log.md
    summary.md
    evidence/
```

Use the local start date and time and a short lowercase, hyphenated topic.
Record the time zone and UTC offset. Avoid collisions without overwriting
existing stages. Additional roles use `executor-2`, `executor-3`, etc.
Each role's round starts at 1 and increases with new deliveries. Create records
as they are used; an absent report means the role has not run, never approval.

## Mission

The [mission template](../assets/mission-template.md) must contain:

- **Identity:** contract version, stage, role, round, working root, report path,
  and absolute references to the contracts, role, and result template. Separate
  creation time (`criada_em`), revision (`revisao`), and revision time
  (`revisada_em`), using observed time with its zone. Updating a mission
  preserves its creation time and changes its revision and revision time.
  Declare unavailable time; never present an old date as a current observation.
- **Objective and input:** applicable request and decisions, expected delivery,
  starting version, input files, and dependencies.
- **Criteria:** stable identifiers `C1`, `C2`, etc., observable condition,
  environment or destination, proof method, and authority for external effects.
- **Resources:** items the agent may read, modify, or execute; temporary
  resources, accounts, restrictions, and integration owner. Anything the tool
  does not isolate must appear as a limitation, not a confirmed protection.
- **Handoff:** report path, expected state, required evidence, and recipient.
  Each agent returns to the orchestrator without creating other agents.

Local or external criteria describe the proof environment; neither removes
validation. If proving a criterion may cause an external effect, document
authorization, destination, and how to observe the result without duplicating
the operation.

## Ownership and version

Assign one owner at a time to each modifiable resource. Include shared
resources outside Git: databases, services, ports, accounts, and published
destinations. Transfer ownership in `log.md` after release and a check for
pending activity. Separate files or working environments when parallelism
requires it; Git worktrees do not isolate external services.

The orchestrator maintains the index, missions, log, and summary. Agents write
their own reports and evidence, as well as resources authorized by their
mission. Evidence uses `evidence/r<N>-<role>-*`; the orchestrator uses
`evidence/orchestrator-*`. When an agent cannot write, the orchestrator's
faithful transcription identifies both parties and preserves original content.

## Verifiable identity

Identify the delivery in a verifiable way. A commit suffices only if it contains
the entire delivery and no relevant changes remain outside it. Otherwise,
record paths and hashes, including new and removed files and uncommitted
changes. Include artifact composition to detect later additions; hashes of
selected files do not prove that the complete delivery stayed unchanged.
Exclude orchestration records from product identity unless they are part of
the requested delivery. For external destinations, also record the installed
revision, publication identifier, or another observable identity.

For a stable local tree, use the deterministic helper
[`scripts/manifest.py`](../scripts/manifest.py), with Python 3.9 or newer.
After writers release resources, record a baseline once and verify it before
every handoff. Replace these example absolute paths:

```bash
python3 /skill/scripts/manifest.py snapshot /project /project/docs-by-hopper-orchestration-openai/stage/evidence/product-v1.json --exclude .git --exclude docs-by-hopper-orchestration-openai
python3 /skill/scripts/manifest.py verify /project /project/docs-by-hopper-orchestration-openai/stage/evidence/product-v1.json
```

Exclusions are explicit: do not exclude documents belonging to the product.
The helper compares names, types, permissions, and content, including new files
outside Git. Exit 0 confirms equality; 1 reports differences; 2 means the
comparison could not be completed. Preserve output and manifest; do not create
a fresh baseline merely to erase a discrepancy. A new version needs impact
analysis and the affected handoffs.

The helper does not follow symbolic links or cover services, external
dependencies, or concurrent writers. In those cases, or without Python,
produce a verifiable inventory appropriate to the artifact and dependencies.
Explain the limitation; do not declare equality if relevant composition is
missing. The helper's double read detects observed changes but does not create
a lock or replace resource release.

## Result and evidence

Use the [result template](../assets/result-template.md). Distinguish the
following canonical values, preserved across languages for interoperability:

- **Work state:** `concluido` (completed), `bloqueado` (blocked), or
  `interrompido` (interrupted).
- **Verdict:** `aprovado` (approved), `reprovado` (rejected), `inconclusivo`
  (inconclusive), or `nao_aplicavel` (not applicable). Executors use
  `nao_aplicavel`; reviewers and validators issue the other verdicts.
- **Criterion state:** `comprovado` (proved), `falhou` (failed),
  `inconclusivo`, or `nao_aplicavel`, the latter with a justification accepted
  by the orchestrator. Convenience cannot waive a criterion in the request.

Results identify the agent, role, stage, round, version, evidence, pending
criteria, open findings, released resources, pending operations, report,
and next owner. Also return state and path to the orchestrator.

Every piece of evidence relates a criterion, version, method, environment,
expected result, observed result, and accessible reference. Preserve relevant
output without secrets or unnecessary full transcripts. Use `not confirmed`
for metadata the tool does not expose; do not confuse it with `nao_aplicavel`.

Findings use stable identifiers by role (`R1`, `V1`), requirement or criterion,
evidence, impact, severity, and expected result. Classify severity as critical,
high, medium, or low, justified by concrete impact. Suggestions do not violate
a requirement and do not prevent acceptance; every open finding prevents
acceptance regardless of severity.

## Proportionate records

Keep one canonical source for criteria, manifest, and configuration.
Self-contained missions may reference it with absolute paths; handoffs refer
to existing evidence without copying entire logs and tables. On a new round,
record the difference, affected findings, and reused evidence. Do not create
redundant intermediate reports or repeat proofs to complete a form. Preserve
the relevant command or method when executed.

Cite files and sections actually consulted. Use states defined by the
contract; put explanations in a separate field. Stage state, each part's
state, work state, and verdict are distinct information.

## Orchestrator records

- **`index.md`:** one row per stage, with identifier, objective, state,
  version, summary link, and next action. At the top, identify active stages
  and reserved resources. Preserve earlier stages and an existing legacy
  structure; record each stage's contract version.
- **`log.md`:** events with date/time and UTC offset, action, state `decidido`
  (decided), `tentado` (attempted), or `realizado` (performed), reason, owner,
  and evidence. Include invocations, transfers, mission changes, returns,
  pauses, resumptions, and acceptance. Distinguish event time from record time.
  If exact event time is unavailable, mark it as not confirmed and preserve
  observed sequence; do not present record time as a tool-provided timestamp.
- **`summary.md`:** result, team, version and current state, criteria and
  evidence, findings and limitations, and next action. Record the contract,
  version, and hashes of the skill package used. For the team, record
  identifiers, requested/applied/confirmed model and effort, and each role's
  actual state. For the next action, identify owner and any user dependency.

Record duration and consumption when exposed by the environment, stating
coverage (orchestrator, agents, or total) and avoiding double counting.
Missing data is `not available`; do not estimate tokens from report size.

Records support continuity but do not replace inspection of current state
or grant authority. For records from another vendor, record origin, contract
version, and discrepancies; reuse valid decisions and evidence without
assuming old sessions are agents in the current team.
