#A frame or iframe is an HTML document embedded inside another HTML page.
#frames will have ids framses will have name frames  will class with indexes 0 or 1
*** Settings ***

Library     SeleniumLibrary
*** Variables ***
${url}      https://jqueryui.com/datepicker/

*** Test Cases ***
Varify Frames
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    3s
        
        Select Frame    xpath://iframe[@class='demo-frame']
        
        Click Element    xpath://input[@id='datepicker']
        
        Sleep    2s
        Click Element    xpath://a[contains(text(),'21')]
        
        Sleep    3s
        Close Browser
        