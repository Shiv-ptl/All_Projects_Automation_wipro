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

        
        Sleep    2s

        Scroll Element Into View        link=Sell on Amazon

        Sleep    2s

        Click Element       link=Sell on Amazon
        #xpath://a[normalize-space()='Sell on Amazon']
        Sleep    2s
        #${title}=       Get Title
        Title Should Be    Amazon.in: Selling on Amazon - Start Selling Now

        #Log    ${title}

        Close Browser