*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/alerts.php
*** Test Cases ***
Alerts Practice
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://h1[@class='mb-3 fw-normal border-bottom text-left pb-2 mb-4']
        Click Element    locator