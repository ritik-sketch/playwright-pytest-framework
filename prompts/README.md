# Prompt templates

Reusable prompts for the QA workflow described in `docs/ai-assisted-testing.md`.
Each template has the same structure so it is easy to fill in and easy to compare:

1. **Role** - who the model should act as
2. **Context** - the minimum the model needs (feature, code pattern, log)
3. **Task** - one clear instruction
4. **Output format** - exact shape of the answer, so it can be used directly
5. **Constraints** - what to leave out, what not to invent

Placeholders are in `<angle brackets>`.
