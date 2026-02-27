*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open Application
Suite Teardown    Close Browser
#Test Setup        Login To Application    Admin    admin123
Test Teardown     Logout From Application


*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com
${BROWSER}    chrome


*** Keywords ***

Login To Application
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//button[@type='submit']
    #Wait Until Page Contains    Dashboard
    Wait Until Element Is Visible    xpath=//h6[text()='Dashboard']


Get Dashboard Title
    #Wait Until Element Is Visible    xpath=//h6[text()='Dashboard']
    ${title}=    Get Text    xpath=//h6[text()='Dashboard']
    [Return]    ${title}


Login And Get Title
    [Arguments]    ${username}    ${password}
    Login To Application    ${username}    ${password}
    ${title}=    Get Dashboard Title
    Log    Dashboard Title: ${title}


Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username


Logout From Application
    Click Element    xpath=//p[@class='oxd-userdropdown-name']
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    name=username


*** Test Cases ***
Verify Login Flow
    Login And Get Title    Admin    admin123