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

        Capture Page Screenshot     C://User//rpbo5.png

        Capture Element Screenshot    xpath://input[@id='file-upload']      C://User//rpbo6.png
        Sleep    3s
        Close Browser