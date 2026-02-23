*** Settings ***
Library     SeleniumLibrary

Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://practice.automationtesting.in/

*** Test Cases ***
Varify upload File
        Open Browser        ${url}      chrome

        Maximize Browser Window
        Sleep    3s

        Wait Until Element Is Visible    xpath://img[@title='Mastering JavaScript']

        Wait Until Element Is Visible    xpath://a[@data-product_id='160']    10s
        Execute Javascript    document.querySelector("a[data-product_id='160']").click()

        Execute Javascript    document.querySelector("a[data-product_id='163']").click()

        Execute Javascript    document.querySelector("a[data-product_id='165']").click()

#        Wait Until Element Is Visible    xpath://a[@data-product_id='160']    10s
#        Scroll Element Into View        xpath://a[@data-product_id='160']
#        Click Element    xpath://a[@data-product_id='160']
#
#        Wait Until Element Is Visible    xpath://a[@data-product_id='163']    3s
#        Scroll Element Into View        xpath://a[@data-product_id='163']
#        Click Element    xpath://a[@data-product_id='163']
#
#        Wait Until Element Is Visible    xpath://a[@data-product_id='165']    3s
#        Scroll Element Into View        xpath://a[@data-product_id='165']
#        Click Element    xpath://a[@data-product_id='165']


        Sleep    2s
        
        Click Element    xpath://a[@title='View your shopping cart']

        Sleep    3s
        Click Element    xpath://a[normalize-space()='Proceed to Checkout']
        
        Sleep    5s

#        Select Frame    xpath://form[@name='checkout']

        Input Text    id=billing_first_name    Shiv
        Input Text    id=billing_last_name      ptl
        Input Text    id=billing_company        Wipro
        Input Text    id=billing_email      abcd@gmail.com
        Input Text    id=billing_phone      1234567890
        Input Text    id=billing_address_1      Hazratganj Lucknow UttarPradesh 123123
        Input Text    id=billing_city       Lucknow

        Click Element    id=s2id_billing_state
        Input Text       xpath://input[@id='s2id_autogen2_search']    Uttar Pradesh
        Press Keys       xpath://input[@id='s2id_autogen2_search']    ENTER
        Input Text    id=billing_postcode       123123

        Click Element    id=payment_method_cod
        #Click Element    id=place_order
        Execute Javascript    document.getElementById("place_order").click()
        Sleep    5s
        Page Should Contain    Thank you. Your order has been received.

        Sleep    3s
        ${text}     Get Text    //ul[@class='woocommerce-thankyou-order-details order_details']

        Log To Console    ${text}

        Close Browser
        