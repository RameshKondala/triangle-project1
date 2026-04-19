# Project 4: User Testing with Selenium

## Introduction

This project showcases automated testing of user interfaces with **Selenium IDE** in Firefox. The aim was to develop tests that mimic real user actions within a web app, focusing on e-commerce features like product searches, adding items to carts, and checking totals. Selenium testing is vital because it helps developers ensure UI features function properly across various browsers and setups, identifying problems that unit and API tests might overlook.

For this assignment, I opted for **Selenium IDE** (a Firefox extension) instead of programmatic Selenium because it enables quick test creation via recording and playback, making it perfect for illustrating user testing concepts. I conducted tests on a public e-commerce demo site with clearly identifiable elements suited for Selenium automation. The tests include the entire user flow, from selecting a product to verifying the shopping cart.

## Setup

1. **Selenium IDE**: Installed as a Firefox extension from the Add-ons store.
2. **Browser Developer Tools**: Used Firefox Inspector to identify element selectors (IDs, CSS classes, XPath).
3. **Test Site**: Used a public Selenium practice e-commerce site with stable element identifiers.
4. **Test Environment**: Local Firefox browser, no cloud deployment required.

The Selenium IDE project, saved as `SeleniumTests`, includes three automated test cases that mimic real user interactions.

## Test 1 User Story

**As a shopper, I want to find a product and add it to my cart so that I can purchase it later.**

**Test Steps:**
1. Navigate to the product catalog/home page
2. Locate and click on a specific product/item
3. Click the "Add to Cart" button for that product
4. Verify the item was successfully added to the cart

**Expected Result**: Product appears in shopping cart with correct name, price, and quantity.

## Test 2 User Story

**As a shopper, I want to verify my cart contains the correct items and total so that I know I'm being charged properly.**

**Test Steps:**
1. Navigate to the shopping cart page
2. Verify the added product appears in the cart
3. Verify the product name matches what was added
4. Verify the price per item is correct
5. Verify the total quantity is correct

**Expected Result**: Cart displays correct item details matching the test data.

## Test 3 User Story

**As a shopper, I want to search for products and verify search results so that I can find items quickly.**

**Test Steps:**
1. Navigate to the search functionality
2. Enter a search term for a product category
3. Submit the search
4. Verify search results contain relevant products
5. Verify non-matching search returns no results or appropriate message

**Expected Result**: Search returns expected products or appropriate empty results.

## How I Ran the Tests

1. **Recording**: Opened Selenium IDE, started recording mode, manually performed each test scenario while Selenium captured all clicks, typing, and navigation.
2. **Element Selection**: Used Firefox Developer Tools to inspect elements and verify stable selectors (ID, CSS class, XPath).
3. **Test Editing**: Reviewed recorded commands, added assertions (verify text, verify element present), and adjusted waits for dynamic content.
4. **Playback**: Ran each test individually and as a suite, verifying pass/fail status.
5. **Validation**: Each test includes assertions that fail if expected conditions are not met.

The tests run automatically and provide clear pass/fail feedback with screenshots on failure.

## Screenshots

### Selenium IDE Project Overview

![Selenium](/Project4/screenshots/selenium.png)


### Test 1: Search Functionality 
[Cart Verification Results](/Project4/screenshots/verification.png)


### Test 2: Add to Cart Recording

[Add to Cart](/Project4/screenshots/addtocart.png)


### Test 3: Checkout

[checkout](/Project4/screenshots/checkout.png)
[checkout](/Project4/screenshots/checkout1.png)




### Developer Tools Element Inspection

[Inspection](/Project4/screenshots/inspect.png)

### Test Results Summary

[Test Results](/Project4/screenshots/result.png)

## Conclusion

This project demonstrated that Selenium IDE can swiftly generate automated UI tests via recording, making it much faster than manually writing code for straightforward test cases. The recording feature captured authentic user actions like mouse clicks, typing, and navigation, while Developer Tools assisted me in identifying reliable element selectors.

**What I learned:**
Selenium tests are great for confirming end-to-end user experiences that unit tests might miss. Using Browser Developer Tools is really helpful for finding dependable element locators. Including assertions, like checking if an element is present or verifying text, makes your tests much more meaningful. Additionally, recording and editing workflows can be a very efficient way to handle common test scenarios, saving  time and effort.

**Problems encountered:**
To improve the process, we added wait commands for dynamic content loading. Some elements had unstable selectors with changing class names, but we addressed this by using more reliable XPath. Additionally, cart totals sometimes took longer to load, so we fixed this issue with explicit wait conditions.

**Recommendations for improvement:**
Implement more robust waits for AJAX and dynamic content. Include tests to cover error conditions such as an empty cart or failed add-to-cart actions. Consider conducting cross-browser testing on Chrome and Safari. Add data-driven tests that use different products and prices.

Overall, Selenium IDE is a highly effective tool for quickly developing UI tests and is ideal for validating e-commerce user flows. Its visual recording and playback features make it user-friendly while offering robust automation functions.

***


