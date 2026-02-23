*** Settings ***
#setting we add the external library details ,resources,set up and tear down commands
Library  SeleniumLibrary
Resource    ./../Resources/Resource1.robot

*** Test Cases ***
#name of the testcase
Varify login with valid credentials
        Launch Browser
        Login
        Close the Browser


Varify Add To Cart with valid credentials
        Launch Browser
        Login
        Log    User selects the product
        Log    user click on add to cart button
        Log    prodect added to add to cart
        Close the Browser