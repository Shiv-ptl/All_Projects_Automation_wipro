*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Varify TabsSw
        Open Browser        ${url}      chrome

        Maximize Browser Window

        Set Selenium Implicit Wait    5s

        Click Element       id=opentab

        @{windows}=     Get Window Handles
        Log To Console    ${windows}

        @{titles}=      Get Window Titles
        Log To Console    ${titles}

        Switch Window       title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
        Element Text Should Be      xpath://h2[normalize-space()='Welcome to QAClick Academy']        Welcome to QAClick Academy

        Switch Window       MAIN

        Close Browser

Varify WindowSwitch
        Open Browser        ${url}      chrome

        Maximize Browser Window

        Set Selenium Implicit Wait    5s

        Click Element       id=openwindow

        @{windows}=     Get Window Handles
        Log To Console    ${windows}

        @{titles}=      Get Window Titles
        Log To Console    ${titles}

        Switch Window       title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
        Element Text Should Be      xpath://h2[normalize-space()='Welcome to QAClick Academy']        Welcome to QAClick Academy

        Switch Window       MAIN



        Close Browser