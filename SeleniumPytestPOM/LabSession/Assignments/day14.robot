*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://jqueryui.com/selectmenu/
${BROWSER}    chrome


*** Test Cases ***
Handle Select Menu Dropdowns
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Switch to iframe
    Select Frame    css=.demo-frame

    # Select Speed
    Click Element    id=speed-button
    Click Element    xpath=//div[text()='Fast']

    # Select File
    Click Element    id=files-button
    Click Element    xpath=//div[text()='Some unknown file']

    # Select Number
    Click Element    id=number-button
    Click Element    xpath=//div[text()='10']

    # Select Title
    Click Element    id=salutation-button
    Click Element    xpath=//div[text()='Dr.']

    Sleep    2
    Unselect Frame
    Close Browser