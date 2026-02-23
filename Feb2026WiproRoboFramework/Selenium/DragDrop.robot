*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***

${url}      https://the-internet.herokuapp.com/drag_and_drop

*** Test Cases ***
Varify DragDrop
        Open Browser        ${url}      firefox
        
        Maximize Browser Window
        
        Sleep    2s
        Wait Until Element Is Visible    xpath://div[@id='column-a']
        
        Sleep    2s
        Drag And Drop       xpath://div[@id='column-a']        xpath://div[@id='column-b']
        Sleep    2s

        Close Browser