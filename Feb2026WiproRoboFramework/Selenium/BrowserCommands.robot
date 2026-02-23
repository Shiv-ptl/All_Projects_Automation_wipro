*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Varify Scroll
        Open Browser        ${url}      chrome

        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Go Back
        Sleep    3s
        Go To    ${url}
        Sleep    3s
        Reload Page


        Close Browser