*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Varify upload File
        Open Browser        ${url}      chrome

        Maximize Browser Window

        Wait Until Element Is Visible    xpath://input[@id='file-upload']
        
        Choose File    xpath://input[@id='file-upload']    C:/Users/LENOVO/Desktop/selenium with python wipro/locators.png
        
        Click Element    xpath://input[@id='file-submit']
        Sleep    3s
        Element Text Should Be    xpath://h3[normalize-space()='File Uploaded!']        File Uploaded!

        Sleep    2s
        Close Browser
