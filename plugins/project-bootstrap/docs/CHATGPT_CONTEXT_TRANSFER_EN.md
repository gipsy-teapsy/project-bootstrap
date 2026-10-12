# CHATGPT_CONTEXT_TRANSFER_EN.md

**Project Bootstrap — Cloud Conversation Context Transfer**

## Purpose

This document provides a standalone procedure for transferring the meaningful context of a long ChatGPT conversation into a new conversation.

It is intended especially for Project Bootstrap Cloud Manager discussions, but it must also work independently, without requiring Project Bootstrap to be installed or active.

**This procedure is invoked manually by the user.**

Do not monitor context-window consumption, introduce automatic transfer triggers, create a new workflow manager, or change the user's project as part of this procedure.

### Primary objective

Create a **meaning-preserving archive** that allows a new conversation to continue with the least possible loss of relevant knowledge, decisions, reasoning, constraints, history, and current discussion state.

Do not produce merely a short summary.

Preserve:

- Significant facts, parameters, and established knowledge.
- User goals, requirements, preferences, and constraints.
- Decisions and the reasons behind them.
- Important alternatives considered and reasons for rejecting them.
- Investigations, tests, experiments, and their results.
- Failed approaches, disproven hypotheses, and negative findings.
- Meaningful chronology and changes in understanding.
- Unresolved questions and relevant uncertainty.
- The current discussion and its exact continuation point.

**Preserve meaning and decision rationale rather than the complete sequence of messages.**

Include enough history to understand why important decisions were made, but do not reproduce every intermediate step.

Accuracy and meaningful completeness take priority over arbitrary brevity.

---

# Part I — Transfer Preparation

## 1. Required outputs

Produce two standalone Markdown documents.

### REFERENCE.md — Durable meaning archive

REFERENCE preserves information that remains useful beyond the current discussion.

It should explain:

- What the project or discussion concerns.
- What is known.
- Which conditions and constraints matter.
- What has been decided.
- Why significant decisions were made.
- Which alternatives were considered or rejected.
- What has already been investigated or tested.
- Which findings should not be lost.
- What preferences and limitations must remain understood.

REFERENCE is not a chronological chat transcript.

### HANDOFF.md — Current discussion snapshot

HANDOFF preserves the state of the conversation immediately before transfer.

It should explain:

- What is being discussed now.
- How the current situation arose.
- What has been completed or established.
- Which decisions and restrictions currently apply.
- What remains unresolved.
- What work, if any, has already been explicitly agreed upon.
- What the last meaningful discussion point was.
- How the new conversation should continue.

HANDOFF complements REFERENCE without unnecessarily duplicating it.

### HISTORY — Optional original transcript archive

The user may independently preserve the complete original conversation.

HISTORY is optional and is **not a required output**.

Do not attempt to reconstruct a verbatim transcript from memory or spend the old conversation's remaining capacity generating HISTORY.

Do not require HISTORY to create or use REFERENCE and HANDOFF.

If an original transcript is later available, it may be consulted when additional details are needed.

If no transcript exists, normal continuation must remain possible.

**REFERENCE and HANDOFF must be self-sufficient for continuing the conversation and must not depend on HISTORY.**

## 2. Available information

Use all conversation history and supporting material that is actually accessible.

Consider, when relevant:

- User messages and assistant responses.
- Decisions accepted or rejected by the user.
- Results of previous tasks and investigations.
- Available attachments and reports.
- Existing project knowledge and documented constraints.
- Context inherited from earlier conversation transfers.
- Verified information available from relevant project sources.

Do not focus only on recent messages.

However, recognize that earlier messages may no longer be accessible in a long conversation.

Do not claim to have reviewed the entire transcript unless this is actually supported.

Do not invent inaccessible messages, explanations, decisions, or facts.

If a known gap materially affects the transfer, identify it honestly. Do not manufacture speculative gaps merely to fill a completeness checklist.

## 3. Repeated transfers

This conversation may have started with REFERENCE and HANDOFF documents from a previous conversation.

For every new transfer:

1. Produce a new, complete REFERENCE and HANDOFF pair from the meaningful context currently available.
2. Preserve accessible inherited knowledge and decision rationale.
3. Do not generate only a list of changes since the previous transfer.
4. Do not require comparison of multiple large REFERENCE documents.
5. Do not require the user to upload all historical archives again.
6. Do not automatically overwrite or delete earlier archived documents.

A new REFERENCE must be a usable meaning archive in its own right, not merely a delta.

Previous transfer documents should remain separately archived whenever possible. They may be supplied later if an important historical detail needs to be recovered.

If earlier documents are available, use their relevant content without unnecessary rereading of material already represented in the current context.

If they are not available, proceed using what is known.

The absence of an old REFERENCE or HISTORY is not a transfer failure.

## 4. Protect the capacity of the outgoing conversation

The current conversation may already be experiencing context limitations.

Therefore:

- Do not start unrelated research.
- Do not perform a fresh project audit.
- Do not reread entire Codex workspaces merely for this transfer.
- Do not require transcript exports.
- Do not create additional plans, status systems, or intermediary files.
- Do not reopen settled product decisions.
- Do not ask optional clarification questions when available information is sufficient.

Prioritize accurate REFERENCE and HANDOFF generation.

Do not shrink important information merely to produce short documents.

If significant information is inaccessible, describe the limitation rather than inventing content.

---

# Part II — Meaning Preservation Rules

## 5. Determine the nature of the conversation

Identify the actual subject, main themes, and current purpose of the discussion.

Distinguish:

- Durable project knowledge.
- User decisions and requirements.
- Temporary task details.
- Historical developments.
- Currently unresolved matters.

Adapt the structure to the real conversation.

A software project, technical investigation, research discussion, creative project, and long-term planning conversation may require different sections.

Do not force every conversation into a fixed generic template.

Do not create empty sections solely for structural consistency.

## 6. Preserve why decisions were made

For significant decisions, preserve enough information to answer:

- What problem was being solved?
- What was selected?
- Which major alternatives were considered?
- What evidence or arguments mattered?
- Why was the selected approach preferred?
- Why were important alternatives rejected?
- Which conditions or constraints influenced the outcome?
- What circumstances could justify reconsideration, if discussed?

Do not reconstruct every intermediate message.

**Preserve the minimum sufficient history needed to understand and reasonably reconsider a significant decision.**

If the reason is unknown, say so.

Do not invent alternative options or motivations simply to complete a template.

A user decision made without an explained rationale remains a valid decision.

## 7. Separate facts, decisions, and uncertainty

Preserve distinctions when they materially affect interpretation:

- Independently verified facts.
- Facts reported by the user.
- Accepted decisions.
- Actual test or investigation results.
- Supported inferences.
- Hypotheses and assumptions.
- Open questions.
- Unknown or unavailable information.

Never transform:

- A request into a completed action.
- A plan into an observed outcome.
- An assistant suggestion into an accepted user decision.
- An old test result into current verification.
- Another agent's report into independent verification.
- Missing evidence into proof that no problem exists.

Use explicit status labels where helpful, but avoid labeling every sentence mechanically.

## 8. Preserve precise information

Retain exact values whenever important:

- Project and component names.
- Versions, identifiers, and commit hashes.
- Dates, timelines, and deadlines.
- Relevant numbers and measurements.
- Important filenames and paths.
- Specifications and technical parameters.
- Test results and their scope.
- User-defined terms.
- Exact restrictions and prohibitions.

Do not replace important specifics with vague generalizations.

Do not copy complete logs when their significant outcomes can be accurately preserved more efficiently.

## 9. Preserve meaningful chronology

When information changed over time, explain the important transition.

For example:

- Initially, approach A was considered.
- A test exposed a limitation.
- Approach B was evaluated.
- New evidence supported approach C.
- C is the latest accepted decision.

Distinguish historical states from the latest supported state.

Do not automatically treat the most recent statement as the most reliable. Consider provenance, evidence, and whether it represents a new decision or merely an assumption.

Preserve earlier states when they explain present decisions.

## 10. Preserve negative findings

Record significant outcomes that prevent repeated mistakes or wasted work:

- Approaches that failed.
- Hypotheses that were disproven.
- Rejected architectures.
- Important limitations.
- Incorrect earlier interpretations.
- Experiments with negative results.
- Previously fixed defects and their lessons.
- Reasons for rejecting a proposed solution.

Explain what was tested and what was concluded when possible.

Do not turn a context-specific failure into a universal prohibition without evidence.

## 11. Preserve user preferences and requirements

Include preferences and constraints relevant to the discussion:

- Goals and priorities.
- Quality criteria.
- Preferred participation and decision-making style.
- Accepted approaches.
- Unacceptable approaches.
- Technical, resource, or timing constraints.
- Communication preferences.
- Previously accepted requirements.
- Decisions not to reopen without new reasons.

Do not invent a psychological, professional, or personal profile.

Do not include unrelated personal details.

## 12. Preserve authority boundaries

Clearly distinguish permission to:

- Read information.
- Modify files or resources.
- Create commits.
- Push changes.
- Publish or deploy.
- Perform other externally consequential actions.

Preserve task-specific restrictions and exclusions.

A prior permission for one task must not be generalized into permanent permission for unrelated work.

If the user agreed to investigation only, the new conversation must not treat this as permission to implement changes.

## 13. Respect existing project state without losing reasoning

The working project may already have durable documentation, decisions, code, tests, and task records.

Do not unnecessarily duplicate entire technical documents.

However, **never omit important decision reasoning merely because the final technical decision is already recorded elsewhere**.

Preserve the essential reasoning, alternatives, user agreements, and relevant context.

You may reference an existing project document as the authoritative location for technical state while preserving discussion-specific meaning in REFERENCE.

Remember that the next ChatGPT conversation may not have direct access to Codex or local project files.

If information would otherwise be unavailable, include enough detail for meaningful continuation.

Do not create a competing source of truth for mutable files, Git state, running services, or task execution.

REFERENCE is a durable archive of discussion meaning, not a replacement for the actual working project.

## 14. Preserve uncertainty

Distinguish:

- Accepted decisions.
- Provisional preferences.
- Plausible hypotheses.
- Required verification.
- User decisions still pending.
- Insufficient evidence.
- Information that may have become stale.

Do not make an unfinished discussion appear resolved for the sake of a clean summary.

## 15. Remove informational noise

Omit material that does not affect understanding:

- Greetings and thanks.
- Repeated statements.
- Incidental conversation.
- Unimportant intermediate attempts.
- Superseded proposals with no lasting relevance.
- Redundant tool-output detail.
- Unnecessary chronological narration.

Do not discard information solely because it is old.

A historical restriction, decision, or failed experiment may remain important long afterwards.

---

# Part III — REFERENCE.md

## 16. Objective

Create a durable, organized meaning archive.

Imagine that the next assistant has never seen the previous conversation.

After reading REFERENCE, it should understand:

- The subject and intended outcome.
- Important starting conditions.
- Established knowledge.
- The relevant organization or architecture.
- Accepted decisions.
- Reasons behind those decisions.
- Important rejected alternatives.
- Investigations and findings.
- Meaningful historical changes.
- User preferences and constraints.
- What is known, inferred, or unresolved.

The document must stand on its own without relying on the old chat.

## 17. Organize by subject

Choose headings appropriate to the actual discussion.

Potential sections include:

- Project context and objectives.
- Initial conditions and significant facts.
- Architecture or working arrangements.
- Accepted decisions and rationale.
- Important alternatives and rejected approaches.
- Relevant history and development.
- Research, tests, and findings.
- Negative results and lessons.
- User preferences and constraints.
- Relevant source documents.
- Long-term open questions.

These are examples, not mandatory headings.

Combine, replace, or omit them as appropriate.

## 18. Record important decisions meaningfully

Where helpful, represent a decision with:

**Decision:** what was selected.

**Context:** what problem it addressed.

**Alternatives:** which major options were considered.

**Rationale:** why the choice was made.

**Rejections:** why other significant options were not selected.

**Status:** accepted, conditional, provisional, or superseded.

Do not impose this detailed format on trivial decisions.

Do not invent missing elements.

## 19. Use meaningful detail rather than arbitrary length

Do not impose a fixed word, character, or section limit.

Use as much space as significant context requires.

Prefer:

- Concrete facts over vague abstractions.
- Organized knowledge over transcript-like narration.
- Decision rationale over complete argument transcripts.
- Verified outcomes over every intermediate command.
- Relevant detail over document duplication.

REFERENCE should be neither a superficial summary nor a verbatim transcript.

## 20. Context provenance

Include concise metadata when known and useful:

- Project or conversation subject.
- Transfer date.
- Relevant previous transfer material.
- Known limitations in historical availability.
- Established user-facing communication language.

Do not invent dates, conversation identifiers, source references, or completeness claims.

Avoid unnecessary metadata.

---

# Part IV — HANDOFF.md

## 21. Objective

Create an accurate snapshot of the conversation immediately before transfer.

HANDOFF must allow the next assistant to resume the current discussion without repeating the introductory stages.

It supplements REFERENCE rather than replacing it.

Adapt headings where appropriate, but cover the following substantive questions.

## 22. Current topic and objective

Explain:

- What is being discussed now.
- What outcome the user wants.
- Which stage the work has reached.
- Whether the current discussion differs from the project's original topic.

Be specific enough to support immediate continuation.

## 23. Relevant background of the current discussion

Summarize how the conversation reached this particular question.

Include only the events and reasoning that explain the current situation.

Do not duplicate the entire REFERENCE.

## 24. Completed work and established findings

Record significant:

- Completed actions.
- Prepared artifacts.
- Available reports.
- Executed checks.
- Established facts.
- Accepted intermediate decisions.
- Known limitations of reported results.

Separate completed actions from intentions or plans.

Distinguish another agent's reported result from independently verified evidence.

## 25. Failed attempts and negative outcomes

Where relevant, explain:

- What was attempted.
- Why it was attempted.
- What happened.
- What conclusion followed.
- Why repeating it without new evidence would be inappropriate.

Keep this section focused on the current discussion.

Durable lessons belong in REFERENCE.

## 26. Currently accepted decisions

Record decisions governing the current discussion.

Include their essential rationale where needed to prevent misinterpretation.

Do not promote assistant suggestions into accepted user decisions.

## 27. Current state

This information is essential.

Explain the state at the moment the conversation ends:

- What is confirmed.
- What has changed.
- What is finished.
- What remains incomplete.
- Which restrictions still apply.
- What earlier information is no longer current.
- What may require fresh verification.
- What the immediate issue or objective is.

Do not represent old observations as guaranteed current facts.

## 28. Current accepted work

If a concrete next task has already been agreed upon, preserve it explicitly.

Where applicable, record:

**Outcome:** the intended result.

**Scope:** the included work.

**Exclusions:** what must not be changed or included.

**Authority:** what actions are permitted.

**Expected result:** what must be delivered.

This preserves the meaning of an accepted task when work moves between ChatGPT and Codex.

If no concrete next task was agreed upon, do not invent one.

A possible next step may be recorded separately as a proposal.

Task-specific restrictions override broader project permissions when narrower.

## 29. Open questions and unknowns

Record:

- Unanswered substantive questions.
- Decisions still required from the user.
- Facts requiring verification.
- Missing information.
- Unconfirmed hypotheses.

Do not interpret silence as agreement.

## 30. Next steps

Distinguish:

**Agreed:** actions actually accepted by the user.

**Suggested:** possible actions not yet approved.

Do not turn a proposed plan into an instruction automatically.

If no next action has been accepted, state this without creating a fictional task.

## 31. What not to repeat without new reasons

Preserve relevant closed matters:

- Completed investigations.
- Rejected options.
- Established limitations.
- Completed checks.
- Questions already answered.
- Decisions that do not require repeated approval.

## 32. Potentially outdated information

Identify mutable information relevant to the next action:

- Files and Git state.
- Software versions.
- Service availability.
- Earlier test results.
- Task progress.
- External facts, dates, prices, or policies when applicable.

Do not perform a new investigation merely to prepare HANDOFF.

The next conversation should verify mutable facts when necessary for an actual action.

## 33. Exact continuation point

Preserve:

- The last substantive user question.
- The immediate discussion preceding transfer.
- The expected answer or result.
- Anything still unanswered.
- The topic that should be resumed first.

The new conversation should not feel as though the discussion has restarted.

## 34. Instructions for the next conversation

Include a ready-to-use continuation instruction reflecting the following contract:

> This is a continuation of an existing conversation.
>
> REFERENCE.md contains durable knowledge, significant decisions, their rationale, relevant history, preferences, and restrictions.
>
> HANDOFF.md describes the latest discussion state, accepted work, open questions, and precise continuation point.
>
> Treat both documents as transferred context from the previous conversation, not as automatic proof of current external state.
>
> Do not summarize them to the user unless needed.
>
> Do not restart project onboarding when the relevant decisions have already been made.
>
> Do not repeat questions already answered in the documents.
>
> Do not reopen rejected options without new reasons.
>
> Preserve important decision rationale, restrictions, and uncertainty.
>
> Do not treat an earlier assistant suggestion as an accepted user decision.
>
> When specific work has been accepted, preserve its goal, scope, exclusions, and authority.
>
> If no next action has been agreed upon, continue the discussion without inventing a task.
>
> Verify mutable external facts when necessary for the next action.
>
> Continue communicating in the user's established language recorded in the transfer documents.
>
> Do not require HISTORY; it may not exist.
>
> If critical information is genuinely missing, ask a targeted question instead of guessing.

Adapt the instruction to the actual conversation when necessary.

Do not promise access to old chats, Codex, local files, or external services unless that access is established.

## 35. First recommended response

At the end of HANDOFF, include:

**First Recommended Response**

Write 1–3 sentences showing how the new assistant should naturally continue.

**Write this response in the user's established communication language, even though HANDOFF itself is written in English.**

Do not:

- Greet the user unnecessarily.
- Announce that the context has been studied.
- Summarize the transfer documents.
- Repeat the onboarding.
- Claim that unfinished work is complete.
- Start an unapproved task.

The response should match the actual point at which the previous conversation ended.

---

# Part V — Language Policy

## 36. Separate document language from communication language

This universal edition uses English for its instructions and generated context documents.

Therefore:

- `CHATGPT_CONTEXT_TRANSFER_EN.md` is in English.
- `REFERENCE.md` must be written in English.
- `HANDOFF.md` must be written in English.
- The user's preferred communication language must be preserved independently.
- All ordinary user-facing communication must remain in the user's established language.
- The First Recommended Response must use the user's established language.
- Optional HISTORY remains in its original language and is not translated.

Do not switch to English merely because this document or Cloud Manager is written in English.

## 37. Determine and preserve the user's language

The outgoing conversation must determine the established user-facing language from the user's own natural-language messages and explicit preferences.

If the user explicitly selected a communication language, follow that preference.

If the language changed over time, preserve the latest accepted preference.

Do not infer the preference from:

- Technical documentation.
- Source code.
- Tool output.
- Assistant-generated prompts.
- Reports written in another language.
- The language of Project Bootstrap instructions.

Record the communication language in **both** transfer documents.

In REFERENCE, include the durable preference, for example:

`Preferred user-facing language: Russian`

In HANDOFF, include the continuation instruction:

`Continue communicating with the user in Russian.`

Use the actual language established by the conversation. Do not copy the example mechanically.

Do not ask the user to identify their language when it is already clear.

If the preference genuinely cannot be established, indicate that it is unknown. The next conversation should infer it from the user's first natural-language message, asking only if necessary.

A later explicit user request to change language overrides the transferred preference.

## 38. Preserve meaning across languages

When translating discussion context into English:

- Preserve exact technical identifiers, paths, versions, and values.
- Translate explanations accurately.
- Preserve explicit negations, restrictions, and permissions.
- Preserve uncertainty.
- Do not strengthen hypotheses into conclusions.
- Do not change the intended scope of accepted work.
- Retain important original-language phrases or quotations when their wording matters.
- Preserve user-defined terminology where it affects understanding.

The purpose is to transfer meaning, not to rewrite decisions into more convenient English interpretations.

English-language transfer documents must not alter how the assistant communicates with the user.

---

# Part VI — Output Quality and Delivery

## 39. Keep the documents distinct

REFERENCE preserves durable meaning.

HANDOFF preserves the current conversation state.

A critical restriction may appear in both if repetition prevents loss of meaning.

Do not duplicate large sections unnecessarily.

## 40. Do not create unrelated artifacts

Do not automatically generate:

- A separate decision register.
- A reconstructed conversation log.
- A new project plan.
- A replacement project-state database.
- Copies of all existing technical documents.
- Extensive command histories.
- Additional status or workflow files.

Preserve important reasoning and context without creating competing project-management infrastructure.

## 41. Confidential information

Do not omit relevant internal project information merely because it is work-related or confidential.

Preserve important information within the intended scope.

However, do not reproduce passwords, tokens, private keys, or other active secret values in REFERENCE or HANDOFF.

Where necessary, preserve non-secret information about the access method, purpose, availability, and restrictions.

Do not disclose secret values merely to make the transfer more complete.

## 42. Final quality review

Before delivering the documents, verify that:

1. A new assistant can understand the discussion without the old chat.
2. Important initial facts are preserved.
3. Significant decisions remain identifiable.
4. Their rationale and major alternatives are retained.
5. Meaningful investigations and results are recorded.
6. Important negative findings are preserved.
7. Relevant chronology is intact.
8. Facts and hypotheses remain distinguishable.
9. Historical results are not misrepresented as current.
10. User preferences and constraints are retained.
11. Authority boundaries and prohibitions remain clear.
12. Previously answered questions need not be repeated.
13. REFERENCE covers durable meaning, not only recent messages.
14. HANDOFF accurately reflects the present discussion.
15. Accepted decisions are distinguished from proposals.
16. The final continuation point is precise.
17. No unsupported information has been invented.
18. Both documents work without HISTORY.
19. The new conversation need not access the original chat.
20. No competing Codex project-state system has been created.
21. The established user-facing language is accurately recorded.
22. The First Recommended Response uses that language.

Correct any significant omissions that can be resolved from available information.

If a gap cannot be resolved, state the limitation rather than inventing an answer.

## 43. Do not claim impossible completeness

Even a careful transfer cannot guarantee preservation of every detail from a very long conversation.

The objective is to minimize loss of **meaningful context**, not to reproduce every message.

If some history was unavailable, do not claim it was processed.

Do not claim to transfer hidden model state or the original context window itself.

The output transfers explicitly recorded knowledge, reasoning, restrictions, decisions, and discussion state.

## 44. Deliver the result

Provide two complete Markdown documents in this order:

### File 1 — REFERENCE.md

The durable meaning archive.

### File 2 — HANDOFF.md

The current discussion snapshot, continuation instructions, and First Recommended Response.

If the environment supports creating files, provide both Markdown files.

Otherwise, provide their complete contents as two clearly separated blocks suitable for saving.

Do not claim files were created when only text was supplied.

Do not create HISTORY as a required third output.

## 45. Explain how to continue

After preparing both documents, briefly instruct the user, in their established language, to:

1. Save REFERENCE.md and HANDOFF.md.
2. Keep earlier transfer documents separately if available.
3. Open a new conversation, or a new conversation within the relevant ChatGPT Project.
4. Ensure Project Bootstrap Cloud Manager is available if it is being used.
5. Provide the new conversation with REFERENCE.md and HANDOFF.md.
6. Continue from the point identified in HANDOFF.

Do not require HISTORY.

Do not require reinstallation or reconfiguration of Cloud Manager when it is already available.

Do not restart accepted project onboarding decisions.

---

# Final Requirement

The transfer succeeds when a new conversation, without access to the original transcript, can understand:

**What the work concerns, what is known, what was decided, why those decisions were made, what was already investigated or rejected, which restrictions remain active, and where the discussion must continue.**

Preserve significant causal reasoning.

Do not reproduce the entire conversation for length.

Do not invent missing context.

Do not repeat settled questions.

Do not change the user's communication language.

**The result is a durable archive of conversation meaning and an accurate handoff of its current state — not merely a summary of messages.**