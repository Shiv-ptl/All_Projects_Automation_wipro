*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php
*** Test Cases ***
Varify login scenarios with valid credentials
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        #wait till the element is loaded
        Wait Until Element Is Visible       xpath://h1[normalize-space()='Check Box']

#        #click login button
#        Click Element       id=c_bs_1
#        Click Element        id=c_bs_2
        ${elements}=        Get WebElement      xpath://input[starts-with(@id,'c_bs_')]

        FOR    ${element}    IN    @{elements}
            Click Element    ${element}
            Sleep    2s
             
        END

        Close Browser