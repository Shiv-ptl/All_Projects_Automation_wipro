*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/windows

*** Test Cases ***
Varify TabsSw
        Open Browser        ${url}      chrome

        Maximize Browser Window

        Set Selenium Implicit Wait    5s

        Click Element    link=Click Here

        @{windows}=     Get Window Handles
        Log To Console    ${windows}

        @{titles}=      Get Window Titles
        Log To Console    ${titles}

        Switch Window       title=New Window
        Element Text Should Be    xpath://h3[normalize-space()='New Window']    New Window

        Switch Window       MAIN

        Close Browser