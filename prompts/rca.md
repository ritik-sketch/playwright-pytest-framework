# Prompt: root cause analysis draft

## Role
You are a QA engineer writing a root cause analysis for a defect that has been
reproduced and fixed.

## Context
Defect: <ID and one-line summary>
Symptom: <what the user or test saw>
Reproduction: <steps or test name>
Investigation notes:
<what was checked at UI, API and data level, with findings>
Fix applied: <one line, PR link if any>

## Task
Draft the RCA using the template below, filling only what the notes support.

## Output format
Use exactly these headings: Issue, Impact, Timeline, Reproduction, Investigation
(UI / API / Data), Root cause, Why it escaped, Fix, Prevention.
Root cause must be one specific sentence. Prevention must name a concrete test,
check or process change.

## Constraints
- Do not guess a root cause the investigation notes do not support; write
  "unconfirmed - needs <check>" instead.
- Keep it under 250 words.
