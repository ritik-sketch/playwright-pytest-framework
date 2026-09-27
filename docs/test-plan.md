# Test Plan - Swag Labs (saucedemo.com)

| Field | Value |
|---|---|
| Application | Swag Labs demo e-commerce web app |
| Environment | https://www.saucedemo.com (public demo, treated as "staging") |
| Prepared by | Ritik Chaturvedi |
| Version | 1.0 |

## 1. Objective

Verify that a customer can log in, browse products, manage a cart and complete a
purchase, and that the app fails safely on invalid input. Automate the stable,
repeatable checks so they run on every push.

## 2. Scope

### In scope
- Login: valid user, locked-out user, wrong password, empty fields
- Inventory: product list, add/remove to cart, cart badge, sorting
- Cart: items shown match selection, proceed to checkout
- Checkout: customer info validation, order summary, order completion
- Resilience: page renders when image requests fail

### Out of scope
- Performance / load testing
- Cross-browser (Chromium only for this framework)
- Accessibility audit
- Mobile app (no mobile app exists for this demo)

## 3. Test approach

| Layer | What | How |
|---|---|---|
| Manual / exploratory | New areas, UX and edge cases | Test cases in `docs/test-cases.md` |
| Automated UI (Playwright) | Stable, repeatable flows | `tests/` folder, Page Object Model |
| Data-driven | Login validation matrix | `data/users.json` + `pytest.mark.parametrize` |
| Network interception | Failure simulation | `page.route()` in `tests/test_network.py` |
| CI | Every push and pull request | GitHub Actions, screenshots on failure |

## 4. Test users (provided by the app)

| User | Purpose |
|---|---|
| standard_user | happy path |
| locked_out_user | blocked login |
| problem_user | UI defects (used for defect-report example) |

## 5. Entry / exit criteria

Entry: environment reachable, test users valid, latest code deployed.
Exit: all P0/P1 test cases executed, no open P0 defects, automated suite green in CI.

## 6. Risks

| Risk | Mitigation |
|---|---|
| Public demo site changes without notice | Selectors centralised in Page Objects; failures surface in CI first |
| Tests depend on network | Timeouts kept at Playwright defaults; retry policy can be added in CI |

## 7. Deliverables

- `docs/test-cases.md` - manual test cases with automation mapping
- `tests/` - automated suite
- `docs/defect-report-template.md`, `docs/rca-template.md` - reporting formats
- CI run history on GitHub Actions
