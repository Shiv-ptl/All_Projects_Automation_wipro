#pip install robotframework-datadriver
#pip install openpyxl
#pip install -U robotframework-datadriver[XLS]
*** Settings ***
Library     SeleniumLibrary
#Library     DataDriver      file=C:/Users/LENOVO/PycharmProjects/Feb2026WiproRoboFramework/TestData/ddtLogindataCSV.xlsx     sheet_name=ddtLogindata
Library     DataDriver      file=../TestData/ddtLogindataCSV.xlsx       sheet_name=ddtLogindata

Test Template       Login Test
Test Setup      Open Browser        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login      chrome
Test Teardown       Close Browser



*** Test Cases ***
Login with user     ${username} and     ${password}

*** Keywords ***
Login Test
        [Arguments]     ${username}     ${password}
        Wait Until Element Is Visible    //input[@name='Username']
        
        Input Text    //input[@name='Username']    ${username}
        Input Text    //input[@name='Password']    ${password}
        
        Click Element    xpath://button[normalize-space()='Login']
        #validate the user is on the home page
        Wait Until Element Is Visible    xpath://input[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
        Element Should Be Visible    xpath://input[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']




