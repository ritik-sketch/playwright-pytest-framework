# Root Cause Analysis (RCA) Template

Used for production issues, escaped defects and flaky automated tests.
The goal is to isolate the failing layer (UI, API or data) before handing off,
so the fix lands in the right place.

```
Issue:              <ID + one-line summary>
Reported by / on:   <who, date>
Impact:             <who was affected, how badly, for how long>
Timeline:
  - <time> first seen
  - <time> reproduced
  - <time> workaround / fix
Reproduction:       <exact steps or test name>
Investigation:
  UI layer:         <what the screen showed, console errors>
  API layer:        <request/response, status codes, payload differences>
  Data layer:       <state of records before/after>
Root cause:         <one sentence, specific>
Why it escaped:     <missing test case, environment gap, timing>
Fix:                <code / config / data change, PR link>
Prevention:         <new automated test, monitoring, process change>
```

## Example - flaky automated test

```
Issue:              test_add_to_cart_updates_badge failed intermittently in CI
Reported by / on:   CI run #14
Impact:             Pipeline red on 2 of 10 runs; no user impact
Timeline:
  - Run #12 first failure
  - Run #14 reproduced locally with `pytest --headed`
  - Same day: fix merged
Reproduction:       pytest tests/test_inventory.py::test_add_to_cart_updates_badge
Investigation:
  UI layer:         Badge text read as "" immediately after click
  API layer:        N/A (client-side state only)
  Data layer:       N/A
Root cause:         Test read badge text with inner_text() before React re-rendered it
Why it escaped:     Passed locally on a fast machine; race condition only visible under CI load
Fix:                Replaced manual read with expect(badge).to_have_text("1"), which auto-waits
Prevention:         Rule added to README: assert with expect() (auto-wait) instead of reading values and comparing
```
