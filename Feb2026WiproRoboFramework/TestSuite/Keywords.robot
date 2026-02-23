*** Settings ***
#setting we add the external library details ,resources,set up and tear down commands
Library  SeleniumLibrary

*** Test Cases ***
#name of the testcase
Varify login with valid credentials
        Login


Varify Add To Cart with valid credentials
        Login
        Log    User selects the product
        Log    user click on add to cart button
        Log    prodect added to add to cart




*** Keywords ***
Login
        Log    Enter username
        Log    Enter password
        Log    click on login button
        Log    user is on the home page

