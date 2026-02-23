*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***

${url}      https://practice.expandtesting.com/hovers

*** Test Cases ***
Varify RightClick
        Open Browser        ${url}      chrome

        Maximize Browser Window

        Sleep    2s

        Wait Until Element Is Visible    xpath://div[@class='example']//div[1]//img[1]
        
        Mouse Over    xpath://div[@class='example']//div[1]//img[1]
        Sleep    2s
        Element Should Be Visible    xpath://h5[contains(text(),'name: user1')]

        Close Browser

        