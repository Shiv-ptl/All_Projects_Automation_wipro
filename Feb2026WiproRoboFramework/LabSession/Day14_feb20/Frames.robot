*** Settings ***

Library     SeleniumLibrary
*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/frames.php

*** Test Cases ***
Varify Frames
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    3s

        Select Frame    xpath://body//main//iframe[1]

        ${text1}=    Get Text    xpath://body
        Log To Console    Frame 1 Text

        #${text}     Get Text    xpath://h1[normalize-space()='Selenium - Automation Practice Form']

        Log To Console    ${text1}
        #Click Element    xpath://a[@title='back to Selenium Tutorial']
#        Sleep    5s
#        Scroll Element Into View        link=Online Html Editor

#        Sleep    2s
#        Go Back

        Unselect Frame
#        Click Element    xpath://a[@title='back to Selenium Tutorial']
#        Sleep    5s
#        Wait Until Page Contains    Selenium Tutorial    10s
#        Go Back

        Sleep    5s
        
        Select Frame    xpath://body//main//iframe[2]

        ${text2}=    Get Text    xpath://body
        Log To Console    Frame 2 Text
        #${text}     Get Text    xpath://h1[normalize-space()='Selenium - Automation Practice Form']

        Log To Console    ${text2}
        Unselect Frame


        Sleep    3s
        Close Browser
