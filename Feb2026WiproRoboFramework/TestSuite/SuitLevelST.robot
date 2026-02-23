*** Settings ***
#setting we add the external library details ,resources,set up and tear down commands
Library  SeleniumLibrary
Resource    ./../Resources/Resource1.robot
Suite Setup     OpenDB
Suite Teardown      CloseDB
*** Test Cases ***
#name of the testcase
Varify login with valid credentials
        Login


Varify Add To Cart with valid credentials
        Login
        Log    User selects the product
        Log    user click on add to cart button
        Log    prodect added to add to cart