# Stage lifecycle

Read when starting coordination and consult the relevant transition for
handoffs, returns, pauses, and resumptions. The orchestrator records decisions
in `log.md` and maintains current state in `summary.md` and the index.

## States and transitions

Canonical state identifiers remain identical across languages.

| Verified situation | Action and next state |
| --- | --- |
| Missions, resources, and execution authorized | Start executor; `executando` (executing). |
| One executor's part delivered | Record release; await other necessary parts. |
| All parts delivered | Transfer to integrator; remain `executando`. |
| Integrated version identified and stable | Start reviewer; `em_revisao` (under review). |
| Reviewer approved and version unchanged | Start validator; `em_validacao` (under validation). |
| Reviewer or validator found failure | Return to responsible executor; `executando`. |
| Essential evidence, context, or resource missing | Seek information or proof; `bloqueada` (blocked) for the dependent part, preserving authorized independent work. |
| All criteria proved and no open findings | Check closure and record `aceita` (accepted). |
| User requests pausing the entire stage | Interrupt requested scope; stage `pausa_solicitada` (pause requested) until confirmed, then `pausada` (paused). |
| User requests pausing one part | Part becomes `pausa_solicitada`, then `pausada`; stage remains `executando` if another authorized part continues. |
| User ends without acceptance | Confirm stopping and record `encerrada_sem_aceite` (closed without acceptance). |

If one executor already delivers the integrated version, forward it directly
to review; do not open another integration round. If one part is blocked while
another continues, keep the stage `executando` and describe the partial blockage
in the summary.

A stage starts `preparada` (prepared). An `inconclusivo` verdict is not approval
and does not permit acceptance. A scope change requires reconciling criteria
and missions; a requirement already included in the request may be clarified
without new authorization. Actual expansion depends on the user.

## Handoff and delivery identity

Receive agent completion and check report, fields, and version. Return an
incomplete handoff to its author for completion; do not restart the task.
For repetition without correction or new context, record the blockage instead
of creating an unlimited cycle of form adjustments.

Before review, validation, and acceptance, compare the complete inventory to
the recorded manifest under [verifiable identity](contracts.md). Check
additions, removals, and changes; repeating only known hashes does not prove
equality. Record actual comparison results before invoking the next role.
If the product changed, identify affected resources and obtain review and
validation of its impact. Meanwhile, previous approval applies only to the
previous version. Updating reports does not change product version.

Executors receive integration resources only after necessary releases.
Silence, timeout, and requested interruption are not release.

## Corrections and progress

Consolidate reviewer and validator findings by identifier, severity, criterion,
version, and status. Fixing a finding does not automatically close it: the
role that raised it confirms resolution in the relevant round. Cross-reference
duplicate reports of the same problem without hiding any.

Authorize another attempt with a diagnosis or specific action and a check
capable of determining its result. Progress is a proved criterion, resolved
finding, or evidence clarifying the cause; raw finding counts do not determine
continuation. Assess regressions by severity even if total findings decrease.

When the same condition returns without a new hypothesis, evidence, or
condition, stop dependent attempts, record partial results, and identify
needed intervention. Replacing an agent does not reset history. Continue
independent parts that remain authorized and have a useful action defined.
Respect available resource limits; do not impose an arbitrary deadline to
classify a long task as failed.

Prefer resuming the responsible agent to correct the same delivery. Replace
it if unavailable, after an authorized model change, or for another documented
technical reason. Transfer context and resources only after confirming the
previous owner is no longer acting. Reviewer and validator remain independent
of the executor even after replacement.

## Pause, cancellation, and pending operations

1. Identify scope: blocked part, whole stage, or request to stop the entire
   team. For an explicit stop request, suspend new invocations and interrupt
   affected agents through the native tool.
2. Check returned state. If the tool confirms only the request, keep affected
   scope `pausa_solicitada` until there is evidence of interruption. Separate
   stage and part states in the summary; a partial pause does not turn active
   independent work into a global pause. Declare inability to confirm; do not
   announce that everyone stopped.
3. Check operations that may survive an agent turn: commands, test services,
   or external tasks. Interrupt or monitor only operations within authorized
   scope; preserve others' work. Record operations without cancellation and
   effects with uncertain outcomes.
4. Check resource states and save partial results. Record agents, pending
   operations, version, and reserved resources. Release resources only with
   evidence that no previous owner continues modifying them.
5. Update summary and index with confirmed state. Stop the requested part;
   independent work continues only outside the stop scope.

Interrupting an agent does not undo completed effects. Inspect the destination
before retrying an external operation; use idempotency mechanisms when
available. An uncertain outcome prevents blind repetition.

## Resumption and closure

On resumption, read the index, summary, mission, and necessary records. Check
actual agents, pending operations, resources, and version. Preserve current
authorizations; an explicit user pause is revoked only by the user's
resumption. Technical blockages may be resolved within existing authorization.

Reuse valid decisions and evidence, recording changes. After losing a session,
confirm the previous agent is inactive before replacement. If this cannot
be determined, keep resources reserved and record the dependency. Reconcile
legacy contracts by reading them; preserve history.

To close, check each agent's state. Close it if the tool provides that operation;
otherwise record confirmed completion or interruption without claiming session
removal. Check remaining processes, release safe resources, update summary
and index, and remove only your own temporary resources without purpose.
Blocked criteria require partial state, not acceptance.
