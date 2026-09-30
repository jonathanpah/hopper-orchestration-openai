# Native Codex operation

Read before the first invocation and when tools or environment change. Use
capabilities actually exposed by the session. API or SDK documentation does
not define arguments for local tools.

## Preparation

1. Check tools for creating, monitoring, continuing, and interrupting agents.
   Identify what the available limit means: active agents or open sessions,
   including or excluding the orchestrator. An idle agent may still occupy
   an open session; account for it before creating another.
2. Check accepted OpenAI models and efforts, inherited configuration, working
   directory, and access to mission paths. References must exist and be
   readable by the agent.
3. Check effective permissions and limits on writing, execution, network,
   and accounts. A mission bounds responsibility but creates no technical
   barrier.
4. If an essential capability is missing, prepare independent work and record
   the limitation. Do not silently replace the native mechanism with terminal
   processes, an API, an SDK, or another executor.

Preserve the main conversation's model and effort. If the displayed effort
is outside `high`, `xhigh`, and `max`, report the conflict before starting
the team; the skill does not change conversation configuration. If effort
is not visible, record `not confirmed` without inferring it from the model name.

## Selecting subagents

Preserve explicit choices for the task. Otherwise, select an available OpenAI
model appropriate to the role; the main model is a starting option when
supported. Consider difficulty, resources, and existing evaluations without
assuming superiority from a model name.

Use `high` as this skill's default for new subagents. Use `xhigh` or `max` when
difficulty or evaluations support the choice. This is a local policy, not a
universal OpenAI recommendation. Validate the combination before offering or
applying it. If unsupported, report alternatives; an explicit user choice
changes only through a new user decision.

State team composition with a brief reason. Start with one executor. Increase
the count when parts can advance independently without resource contention
and within capacity. Reviewer and validator are separate instances from the
executor; start them at the corresponding handoffs. Team configuration does
not create subdelegation: only the orchestrator invokes agents.

Record resource limits already set by the user or environment. Estimate cost
or duration only with sufficient grounds. A long wait does not prove failure;
an actually reached limit requires recording partial results.

## Profile with `collaboration` tools

When this surface is available, check its schema and use:

| Operation | Tool and condition |
| --- | --- |
| Create | `collaboration.spawn_agent`: `task_name`, `fork_turns`, `model`, `reasoning_effort`, `message`, according to the exposed schema. |
| Supplement active work | `collaboration.send_message`; a message does not itself start a new round. |
| Start a new round | `collaboration.followup_task`, preferably after the idle agent's handoff. |
| Wait | `collaboration.wait_agent`; distinguish notification, final result, user interruption, and timeout. |
| Check state | `collaboration.list_agents`, for a concrete doubt or transition to confirm. |
| Interrupt | `collaboration.interrupt_agent`, according to the stop scope and lifecycle. |

Invoke these tools directly when required by the environment, without wrapping
them in `functions.exec`. Use the returned canonical name or identifier in
later calls. Task names must be unique in the session; on this surface, use
lowercase letters, digits, and `_`.

Start with `fork_turns: "none"` and a self-contained mission. The creation
message states the authorized root and first read before any search. Use
actual paths, for example:

> Act as reviewer. Your working root is /project; use it as workdir for searches
> and commands. First read
> /project/docs-by-hopper-orchestration-openai/stage/mission-reviewer.md and
> only the references listed there. Use the skill copy identified in that
> mission; do not start another orchestration. Respect inherited higher-priority
> instructions. Deliver the report at the specified path and return its path
> and state.

This format reduces copied history; it does not isolate files, tools,
credentials, or inherited general instructions. Check `fork_turns` restrictions
before combining inheritance with model or effort overrides. Supply necessary
evidence and context without suggesting the expected verdict.

Other Codex versions may expose different tools and identifiers. Map the
operations above to the actual schema and record the difference. Do not invent
arguments or assume a tool exists to close agents.

## Confirmation and waiting

For each agent, record its identifier, requested model and effort, what the
tool reported applying, and what metadata can confirm. Missing metadata means
`not confirmed`, not proved application. If exact configuration is an acceptance
criterion, absence prevents confirming it but does not turn a successful call
into a failure.

Creation confirms invocation, not delivery. Await the final message and check
the corresponding report and version. Use event-based waits within environment
limits; a wait timeout does not authorize recreating or interrupting an agent.
Update the user at the cadence required by the environment without turning
updates into repeated agent-status queries.

For ambiguous creation failure, check whether the agent already exists before
retrying. For an incomplete result, request only the missing information.

## Profiles and permissions

`agents/openai.yaml` configures skill presentation and invocation. It does not
configure subagent models, efforts, or permissions.

Compatible clients may load custom agents from `.codex/agents/` or
`~/.codex/agents/`. Use existing profiles when selection is supported, checking
effective configuration: profile values and environment overrides can affect
the result. Do not install profiles or modify global configuration implicitly
as part of this skill's execution.

Prefer a reviewer unable to modify the delivery and a validator with access
only to resources needed for proof. If a read-only profile prevents writing
reports, the agent returns content and the orchestrator transcribes it
faithfully, identifying author and writer. Do not weaken protection merely
to meet the document format.

When tools lack isolation by role, record the limitation. If the task requires
that isolation, suspend the dependent part.
