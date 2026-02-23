*** Settings ***
#setting we add the external library details ,resources,set up and tear down commands
Library  SeleniumLibrary

*** Keywords ***
Login
        Log    Enter username
        Log    Enter password
        Log    click on login button
        Log    user is on the home page

Launch Browser
        Log    Launching the Browser...

Close the Browser
        Log    Closing the Browser..

OpenDB
        Log    Opening the database connection

CloseDB
        Log    Closing the database connection