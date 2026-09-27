# Defect Report Template

Copy the block below for each new defect. Keep steps minimal and reproducible;
attach a screenshot or trace for anything visual.

```
ID:            DEF-000
Title:         <one line: where + what is wrong>
Environment:   <URL, browser + version, OS, build/commit>
User / data:   <test user, product, input used>
Severity:      P0 blocker / P1 major / P2 minor / P3 cosmetic
Priority:      High / Medium / Low
Steps to reproduce:
  1.
  2.
  3.
Expected result:
Actual result:
Evidence:      <screenshot / video / trace / logs>
Layer:         UI / API / data  (from root-cause isolation)
Notes:         <frequency, workaround, related tickets>
```

## Example

```
ID:            DEF-001
Title:         Inventory - problem_user sees the same image on every product card
Environment:   https://www.saucedemo.com, Chromium 153, Windows 11, public demo
User / data:   problem_user / secret_sauce
Severity:      P2 minor
Priority:      Medium
Steps to reproduce:
  1. Open base URL
  2. Login as problem_user / secret_sauce
  3. Observe product images on /inventory.html
Expected result:
  Each of the 6 products shows its own image (backpack, bike light, t-shirt ...)
Actual result:
  All 6 cards show the same dog image
Evidence:      test-results/def-001-problem-user-images.png
Layer:         UI (image src attribute is identical for every card; API/data not involved)
Notes:         100% reproducible; does not occur for standard_user
```
