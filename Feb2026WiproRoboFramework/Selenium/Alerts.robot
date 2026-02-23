*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${url}      https://the-internet.herokuapp.com/javascript_alerts
*** Test Cases ***
Varify drop down
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Wait Until Element Is Visible    xpath:(//button)[1]
        Click Element    xpath:(//button)[1]
        Handle Alert        action=ACCEPT       timeout=3
        Sleep    5s
        Click Element    xpath:(//button)[2]
        Handle Alert        action=DISMISS       timeout=3
        Sleep    5s
        Click Element    xpath:(//button)[3]
        Input Text Into Alert    Hello
        Sleep    5s

        Close Browser