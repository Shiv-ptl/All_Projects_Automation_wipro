*** Settings ***

Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Varify Links
        Open Browser        ${url}      chrome

        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        @{links}=       Get WebElements    xpath://a
        FOR    ${link}    IN    @{links}
            ${text}=        Get Text    ${link}
            ${Url}=     Get Element Attribute    ${link}    href
            Log To Console    ${text}
            Log To Console    ${Url}


        END
        
        Close Browser