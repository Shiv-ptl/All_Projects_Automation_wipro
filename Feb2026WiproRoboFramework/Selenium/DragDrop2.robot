*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***

${url}      https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Varify DragDrop
        Open Browser        ${url}      firefox

        Maximize Browser Window

        Sleep    2s
        Wait Until Element Is Visible    xpath://div[@id='draggable']

        Sleep    2s
        Drag And Drop       xpath://div[@id='draggable']        xpath://div[@id='droppable']
        Sleep    2s

        Close Browser