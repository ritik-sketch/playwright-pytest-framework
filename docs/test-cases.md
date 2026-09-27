# Test Cases - Swag Labs

Priority: P0 = blocks release, P1 = must fix before release, P2 = should fix.
"Automated" points to the pytest function that covers the case.

## Login

| ID | Title | Steps | Expected result | Priority | Automated |
|---|---|---|---|---|---|
| TC-01 | App loads | Open base URL | Page title is "Swag Labs", login form visible | P0 | test_smoke.py::test_homepage_loads |
| TC-02 | Valid login | Enter standard_user / secret_sauce, click Login | Redirect to /inventory.html, 6 products listed | P0 | test_login.py::test_valid_user_can_login |
| TC-03 | Locked-out user | Enter locked_out_user / secret_sauce, click Login | Error banner: "...this user has been locked out." | P1 | test_login.py::test_invalid_login_shows_error[locked_out_user] |
| TC-04 | Wrong password | Enter standard_user / wrong_password | Error banner: "...do not match any user in this service" | P1 | test_login.py::test_invalid_login_shows_error[wrong_password] |
| TC-05 | Empty username | Leave username blank, enter password, click Login | Error banner: "Username is required" | P1 | test_login.py::test_invalid_login_shows_error[empty_username] |
| TC-06 | Empty password | Enter username, leave password blank, click Login | Error banner: "Password is required" | P1 | test_login.py::test_invalid_login_shows_error[empty_password] |
| TC-07 | Error banner can be dismissed | Trigger any login error, click the X on the banner | Banner disappears, fields keep their values | P2 | manual |

## Inventory

| ID | Title | Steps | Expected result | Priority | Automated |
|---|---|---|---|---|---|
| TC-08 | Add to cart updates badge | Login, click Add to cart on one product | Cart badge shows 1, button changes to Remove | P0 | test_inventory.py::test_add_to_cart_updates_badge |
| TC-09 | Remove from cart | Add a product, click Remove | Badge disappears, button returns to Add to cart | P1 | manual |
| TC-10 | Sort price low to high | Select "Price (low to high)" | Prices ascend top to bottom | P1 | test_inventory.py::test_sort_by_price_low_to_high |
| TC-11 | Sort name Z to A | Select "Name (Z to A)" | Names descend alphabetically | P2 | manual |
| TC-12 | Product detail page | Click a product name | Detail page shows same name, price and description | P2 | manual |

## Cart and checkout

| ID | Title | Steps | Expected result | Priority | Automated |
|---|---|---|---|---|---|
| TC-13 | Cart shows selected items | Add 2 products, open cart | Both products listed with correct names and prices | P0 | test_checkout.py::test_complete_purchase_flow |
| TC-14 | Checkout requires customer info | Click Checkout, click Continue with empty form | Error: "First Name is required" | P1 | manual |
| TC-15 | Order overview totals | Fill customer info, Continue | Item total = sum of prices, tax and total shown | P1 | manual |
| TC-16 | Complete purchase | Click Finish | "Thank you for your order!" and cart badge cleared | P0 | test_checkout.py::test_complete_purchase_flow |
| TC-17 | Cancel from overview | On step two click Cancel | Back to inventory, cart unchanged | P2 | manual |

## Resilience

| ID | Title | Steps | Expected result | Priority | Automated |
|---|---|---|---|---|---|
| TC-18 | Products render without images | Block image requests, login | 6 product cards still render with names and prices | P2 | test_network.py::test_products_render_when_images_fail |

## Coverage summary

- Total: 18 cases; P0: 5, P1: 8, P2: 5
- Automated: 10 (all P0, most P1); manual/exploratory: 8
