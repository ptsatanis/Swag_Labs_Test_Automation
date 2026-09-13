# Swag_Labs_Test_Automation

🧪 E-Shop Selenium Automation Testing

A Python-based Selenium automation testing project designed to test the functionality of a fake e-commerce website.

The project contains automated UI tests covering some of the most important user flows of an online shop, including authentication, shopping cart functionality, purchasing products, and product sorting/filtering.
📌 Project Overview

The purpose of this project is to demonstrate web UI test automation using Python and Selenium WebDriver.

The automated tests interact with the e-shop in the same way a real user would, validating that the website behaves as expected under different scenarios.
🧪 Tested Functionality

The test suite currently covers:

🔐 Login
    Valid login credentials
    Invalid login credentials
    Verification of successful/unsuccessful authentication

🛒 Shopping Cart
    Adding products to the cart
    Verifying that products are added correctly
    Checking cart functionality

💳 Product Purchase
    Selecting a product
    Adding it to the cart
    Proceeding through the checkout/purchase flow
    Verifying that the purchase is completed successfully

🔎 Sorting & Filtering
    Testing the shop's sorting functionality
    Testing available product filters
    Verifying that the displayed products match the selected criteria

🛠️ Technologies Used

Python
Selenium WebDriver
Chrome WebDriver
HTML/CSS selectors & ID selectors

⚙️ Installation
1. Clone the repository


        git clone https://github.com/your-username/your-repository.git
        cd your-repository

3. Create a virtual environment


        python -m venv venv

    Activate it:


        source venv/bin/activate


3. Install dependencies

        pip install selenium
        pip install pytest

▶️ Running the Tests

    pytest name_of_test.py


🌐 Browser

The tests are currently designed to run using Google Chrome and Selenium WebDriver.

Make sure Chrome is installed on your machine before running the tests.

Depending on the Selenium version and configuration, the appropriate WebDriver can be managed automatically by Selenium Manager.

🧪 Test Scenarios
🔐 Login

Valid Login: Verify that users can log in with valid credentials.
Invalid Login: Verify that login fails with invalid credentials.

🛒 Shopping Cart

Add Product: Verify that products can be added to the cart.


💳 Purchase

Buy Product: Verify that a user can successfully complete a product purchase.

🔎 Sorting

Sorting: Verify that products are displayed in ascending price.


🚀 Future Improvements

Some possible improvements for the project include:

Add more negative test cases
Add explicit waits instead of relying on static delays
Introduce the Page Object Model (POM)
Improve test data management
Add screenshots when a test fails
Generate HTML test reports
Add cross-browser testing
Integrate the tests into a CI/CD pipeline
Add parallel test execution
Improve assertions and test coverage

