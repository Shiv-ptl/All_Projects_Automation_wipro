*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***
Varify login scenarios with valid credentials
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        #wait till the element is loaded
        Wait Until Element Is Visible       xpath://input[@value='radio1']

        #click login button
        Click Element    xpath://input[@value='radio1']

        Click Element        id=checkBoxOption3

        Close Browser