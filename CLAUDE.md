# Working in this repo with an AI coding agent

This file is read by Claude Code (and similar agents) when working in this repository.

## What this project is
Playwright + pytest E2E test framework (Python) for https://www.saucedemo.com.
Page Object Model in `pages/`, tests in `tests/`, shared fixtures in `conftest.py`,
test data in `data/`, environment config in `utils/config.py`.

## Conventions to follow
- One page = one class in `pages/`, inheriting from `BasePage`. Locators are created
  in `__init__`; actions are methods. No selectors inside `tests/`.
- Assert with Playwright `expect(...)` (auto-waits). Do not read a value and compare
  it with `assert` unless the value is not a locator.
- New negative login cases go in `data/users.json`, not as new test functions.
- Mark every test: `@pytest.mark.smoke`, `regression` or `e2e`.
- Keep `docs/test-cases.md` in sync: a new automated test gets a TC row with its
  function name in the "Automated" column.

## How to verify a change
```
pytest -m smoke          # fast check
pytest                   # full suite, must be green before commit
```
CI runs the full suite on every push; check the Actions tab.

## Do not
- Do not change selectors in tests; change them in the page object.
- Do not add sleeps; use `expect` or `wait_for_load_state`.
- Do not commit anything under `test-results/` or `reports/`.
