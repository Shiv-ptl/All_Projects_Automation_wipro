*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${URL}      https://www.saucedemo.com/checkout-complete.html

*** Test Cases ***
Varify Full AddToCart
        Open Browser        ${URL}        chrome
        Maximize Browser Window
        Wait Until Element Is Visible    xpath://div[@class='login_wrapper-inner']
        Input Text    id:user-name    standard_user
        Input Password    id:password    secret_sauce
        Click Element    id:login-button


        Click Element    id:add-to-cart-sauce-labs-backpack
        Click Element    id:add-to-cart-sauce-labs-fleece-jacket
        Click Element    id:shopping_cart_container
        Click Element    id:checkout
        Input Text    id:first-name    Shiv
        Input Text    id:last-name    Ptl
        Input Text    id:postal-code    234567
        Click Element    id:continue
        Click Element    id:finish

        Page Should Contain    Thank you for your order!

        Close Browser


        Sleep    5s
