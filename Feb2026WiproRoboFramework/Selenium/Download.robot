*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/download

*** Test Cases ***
Varify Download
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://a[normalize=space()='bb.text']
        Click Element       xpath://a[normalize-space()='bb.text']
        #check if the file is present in the folder
        ${files}=       List Files In Directory     C:/Users/LENOVO/Downloads
        List Should Contain Value       ${files}        bb.txt
        Sleep    3s

        Close Browser