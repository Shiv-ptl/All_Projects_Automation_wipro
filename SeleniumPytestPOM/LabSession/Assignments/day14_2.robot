*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://jqueryui.com/menu/
${BROWSER}    chrome


*** Test Cases ***
Handle Menu SubMenu
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Switch to iframe
    Select Frame    css=.demo-frame
    

    # Hover Electronics
    #Wait Until Element Is Visible    xpath=//div[text()='Electronics']
    Sleep    2
    Mouse Over    xpath=//div[text()='Electronics']

    # Hover Car Hifi
    #Wait Until Element Is Visible    xpath=//div[text()='Car Hifi']
    Sleep    2
    Mouse Over    xpath=//div[text()='Car Hifi']

    # Click Submenu
    #Wait Until Element Is Visible    xpath=//div[text()='Car Hifi']
    Sleep    2
    Click Element    xpath=//div[text()='Car Hifi']

    Sleep    2
    Unselect Frame
    Close Browser