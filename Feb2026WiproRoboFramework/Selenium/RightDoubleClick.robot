*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***

${url}      https://www.amazon.in/

*** Test Cases ***
Varify RightClick
        Open Browser        ${url}      chrome

        Maximize Browser Window

        Sleep    2s

        Wait Until Element Is Visible    xpath://a[normalize-space()='Sell']

        Open Context Menu    link=Sell
        Sleep    2s

        Double Click Element    xpath://a[normalize-space()='Mobiles']

        Sleep    2s

        Close Browser