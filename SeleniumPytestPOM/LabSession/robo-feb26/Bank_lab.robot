*** Settings ***

Library     SeleniumLibrary
Resource        Resource.robot



*** Test Cases ***
Varify_Cust_login
        Open Browser        ${URL}      chrome
        Maximize Browser Window
        Customer_Login
        Sleep    2s
        Close Browser


Varify_add_customer
        Open Browser        ${URL}      chrome
        Maximize Browser Window
        Manager_Login
        Add_Customer
        Sleep    2s
        Close Browser


Full_Banking_Flow
        Open Browser    ${URL}    chrome
        Maximize Browser Window

        Manager_Login
        Add_Customer
        Open_Account

        Click Element    xpath://button[normalize-space()='Home']
        New_Customer_Login

        Deposit_Amount
        Validate_Balance_After_Deposit

        Withdraw_Amount
        Validate_Balance_After_Withdraw

        Sleep    2s
        Close Browser