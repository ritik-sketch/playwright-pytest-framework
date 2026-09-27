# Playwright + pytest E2E Test Automation Framework

![tests](https://github.com/ritik-sketch/playwright-pytest-framework/actions/workflows/tests.yml/badge.svg)

End-to-end test automation framework in Python: Playwright UI tests against
[Swag Labs](https://www.saucedemo.com) and a requests-based API layer against
[JSONPlaceholder](https://jsonplaceholder.typicode.com), with the same Postman
checks run by Newman in CI.

It mirrors the way I work as a QA engineer on a production SaaS product - test
plan, test cases, automation, defect reporting and root cause analysis - rebuilt
from scratch on a public site so the whole thing can be shared.

## What is in here

| Part | Where | What it shows |
|---|---|---|
| Test plan | `docs/test-plan.md` | Scope, approach, entry/exit criteria, risks |
| Test cases | `docs/test-cases.md` | 25 cases (P0-P2), UI and API, mapped to the automated tests |
| UI automation | `pages/`, `tests/`, `conftest.py` | Page Object Model, fixtures, data-driven and E2E tests |
| API automation | `api/`, `tests/api/`, `data/schemas/` | requests client, service objects, JSON schema validation, negative cases |
| Postman + Newman | `postman/` | Postman collection with test scripts, executed in CI |
| Network interception | `tests/test_network.py` | `page.route()` to simulate failing requests |
| Defect reporting | `docs/defect-report-template.md` | Template + a real example from the app |
| Root cause analysis | `docs/rca-template.md` | Template + a worked flaky-test example |
| CI | `.github/workflows/tests.yml` | Runs on every push, screenshots and HTML report as artifacts |
| AI-assisted workflow | `docs/ai-assisted-testing.md`, `prompts/`, `CLAUDE.md` | Where AI fits in the QA cycle, the prompt templates I use, and agent instructions for this repo |

## Stack

- Python 3.13, pytest, pytest-playwright, pytest-html
- Playwright (Chromium) for UI
- requests + jsonschema for API
- Postman collection run with Newman
- GitHub Actions

## Project structure

```
playwright-pytest-framework/
├── pages/                     # Page Object Model: one class per page
│   ├── base_page.py           #   shared goto/url helpers
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── api/                       # API layer
│   ├── client.py              #   requests.Session wrapper with logging
│   └── posts_api.py           #   service object for /posts (API "page object")
├── tests/
│   ├── test_smoke.py          # app is up
│   ├── test_login.py          # valid + data-driven invalid logins
│   ├── test_inventory.py      # cart badge, sorting
│   ├── test_checkout.py       # full purchase journey (e2e)
│   ├── test_network.py        # route interception
│   └── api/
│       └── test_posts.py      # status, schema, data integrity, 404s
├── postman/
│   └── jsonplaceholder.postman_collection.json
├── data/
│   ├── users.json             # test users and expected errors
│   ├── checkout.json          # products and customer info
│   ├── posts.json             # API payloads and invalid ids
│   └── schemas/post.json      # JSON schema for a Post
├── utils/
│   ├── config.py              # BASE_URL / API_BASE_URL from environment
│   └── data_loader.py         # JSON loader
├── docs/                      # test plan, test cases, defect + RCA, AI-assisted workflow
├── prompts/                   # reusable prompt templates (test design, triage, RCA)
├── CLAUDE.md                  # conventions for AI coding agents working in this repo
├── conftest.py                # shared fixtures (users, logged_in_page)
├── pytest.ini                 # markers, paths, default flags
├── requirements.txt
└── .github/workflows/tests.yml
```

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate           # Windows
# source .venv/bin/activate      # macOS / Linux

pip install -r requirements.txt
playwright install chromium

pytest                           # everything (UI + API)
pytest -m api                    # API tests only, no browser, ~1 s
pytest -m smoke                  # only smoke tests
pytest -m "not e2e"              # skip the long journey
pytest --headed                  # watch the browser
pytest --html=reports/report.html --self-contained-html

npx newman run postman/jsonplaceholder.postman_collection.json   # Postman collection (needs Node)
```

Run against another environment without touching code:

```bash
BASE_URL=https://staging.example.com pytest            # macOS / Linux
$env:BASE_URL="https://staging.example.com"; pytest    # PowerShell
API_BASE_URL=https://api.example.com pytest -m api     # API layer
```

## Design decisions

- **Page Object Model** - tests call actions like `login_page.login(...)`; selectors
  live only inside `pages/`. A UI change is a one-file fix.
- **Locators created in `__init__`** - built once per page object and reused by every
  action, instead of re-querying selectors inside each method.
- **Fixtures for state, not for logic** - `logged_in_page` gives every test a logged-in
  browser so tests describe behaviour, not setup.
- **Data-driven negatives** - the login validation matrix lives in `data/users.json`;
  adding a case is one JSON row, no new test code.
- **Service objects for APIs** - `api/posts_api.py` is to endpoints what a page object is
  to screens: tests call `posts.create(payload)`, never build URLs. One `requests.Session`
  per run, every call logged with status and latency.
- **Contract first for APIs** - every response is checked for status code, JSON schema
  (`data/schemas/`) and data integrity, plus negative cases for unknown ids.
- **`expect()` over manual reads** - Playwright's `expect` auto-waits, which removes
  the most common source of flaky tests (see the RCA example in `docs/`).
- **Environment from variables** - `BASE_URL` switches environments; nothing is
  hard-coded in tests.
- **AI drafts, engineer verifies** - AI is used for test design, triage and RCA drafts
  (`docs/ai-assisted-testing.md`); every output is validated before it enters the suite.
- **Screenshots on failure, report in CI** - `--screenshot=only-on-failure` and
  pytest-html are uploaded as artifacts so a red run can be debugged without re-running.

## Roadmap

- [x] Project setup, smoke test
- [x] Page Objects for login, inventory, cart, checkout
- [x] Shared fixtures, data-driven login tests
- [x] Network interception with `page.route()`
- [x] Test plan, test cases, defect and RCA templates
- [x] GitHub Actions CI with HTML report
- [x] API test layer (requests + pytest) with JSON schema validation
- [x] Postman collection executed by Newman in CI
- [ ] Allure or similar reporting
- [ ] Parallel runs with pytest-xdist

## Author

Ritik Chaturvedi - QA Engineer, Bengaluru
[LinkedIn](https://www.linkedin.com/in/ritik-chaturvedi-qa)
