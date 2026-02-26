*** Settings ***
Library     SeleniumLibrary

*** Variables ***
#${URL}      https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account
${URL}      https://globalsqa.com/angularJs-protractor/BankingProject/#/login
${Name}     Harry Potter
${Manager_login_Btn}        //button[normalize-space()='Bank Manager Login']
${Add_customer_Btn}     //button[normalize-space()='Add Customer']
${Open_account_Btn}     //button[normalize-space()='Open Account']
${Customers_Btn}        //button[normalize-space()='Customers']
${New_firstname}        //input[@placeholder='First Name']
${New_firstname_value}      Shivanshu
${New_lastname}     //input[@placeholder='Last Name']
${New_lastname_value}       Patel
${New_postalcode}       //input[@placeholder='Post Code']
${New_postalcode_value}     209868
${Add_cust_submit_Btn}      //button[@type='submit']


${Process_btn}          //button[@type='submit']
${Currency_dropdown}        //select[@id='currency']
${Customer_dropdown}        xpath://select[@id='userSelect']


#Withdraw
${Withdraw_tab}     //button[contains(text(),'Withdrawl')]
${Withdraw_message}     //span[@class='error ng-binding']


${Deposit_tab}      //button[contains(text(),'Deposit')]
${Amount_input}     //input[@placeholder='amount']
${Deposit_submit}   //button[@type='submit']
${Message}          //span[contains(text(),'Deposit Successful')]

${Full_Name}    Shivanshu Patel
${Balance_field}    //strong[@class='ng-binding'][2]


*** Keywords ***
Customer_Login
        Wait Until Element Is Visible    xpath://button[normalize-space()='Customer Login']
        Click Element    xpath://button[normalize-space()='Customer Login']
        Sleep    3s
        Select From List By Label    xpath://select[@id='userSelect']      ${Name}
#        Click Element    xpath://select[@id='userSelect']
#        Select From List By Label    xpath://select[@id='userSelect']      ${Name}
        Wait Until Element Is Visible    xpath://button[normalize-space()='Login']
        Click Element    xpath://button[normalize-space()='Login']
        Sleep    3s
        Element Should Contain    xpath://strong[contains(text(),'Welcome')]    Welcome ${Name}

New_Customer_Login
        Wait Until Element Is Visible    xpath://button[normalize-space()='Customer Login']
        Click Element    xpath://button[normalize-space()='Customer Login']
        Sleep    3s
        Select From List By Label    xpath://select[@id='userSelect']      ${Full_Name}
#        Click Element    xpath://select[@id='userSelect']
#        Select From List By Label    xpath://select[@id='userSelect']      ${Name}
        Wait Until Element Is Visible    xpath://button[normalize-space()='Login']
        Click Element    xpath://button[normalize-space()='Login']
        Sleep    3s
        Element Should Contain    xpath://strong[contains(text(),'Welcome')]    Welcome ${Full_Name}


Manager_Login
        Wait Until Element Is Visible    ${Manager_login_Btn}
        Click Element    ${Manager_login_Btn}
        Wait Until Element Is Visible    xpath://div[@class='center']
        Sleep    2s



Add_Customer
        Wait Until Element Is Visible    ${Add_customer_Btn}
        Click Element    ${Add_customer_Btn}
        Sleep    3s
        Input Text    ${New_firstname}    ${New_firstname_value}
        Input Text    ${New_lastname}    ${New_lastname_value}
        Input Text    ${New_postalcode}    ${New_postalcode_value}
        Sleep    2s
        Click Element    ${Add_cust_submit_Btn}

        # Wait for alert

        Sleep    2s

        ${alert_text}=    Handle Alert    action=ACCEPT
        Log    ${alert_text}
        Capture Page Screenshot     C://Users//LENOVO//Desktop//selenium with python wipro//ss//abc1.png
        ${customer_id}=    Evaluate    __import__('re').search(r'\d+', """${alert_text}""").group()
        Log    Customer ID is: ${customer_id}
        
        Sleep    3s

Open_Account
        Click Element    ${Open_account_Btn}
        Sleep    3s

        # Select customer (by name)
        Select From List By Label       xpath://select[@id='userSelect']        ${Full_Name}

        # Select currency
        Select From List By Label    ${Currency_dropdown}    Dollar

        Click Element    ${Process_btn}

        ${alert_text}=    Handle Alert    action=ACCEPT
        Log    ${alert_text}

Customer_Login_After_Account
        Click Element    xpath://button[normalize-space()='Home']
        Customer_Login



Withdraw_Amount
        Wait Until Element Is Visible       ${Withdraw_tab}
        Click Element    ${Withdraw_tab}
        Wait Until Element Is Visible      ${Withdraw_tab}
        Sleep    2s
        Input Text      xpath://input[@placeholder='amount']       400
        Sleep    2s
        Click Element       xpath://button[normalize-space()='Withdraw']
        Wait Until Page Contains    Transaction successful    5s
        Sleep    2s
        #Element Should Be Visible    ${Withdraw_message}
        Element Should Contain    ${Withdraw_message}    Transaction successful
        ${withdraw_msg}=    Get Text    //span[contains(@class,'ng-binding')]
        Log    Withdraw Message: ${withdraw_msg}




Deposit_Amount
        Sleep    3s
        Click Element    ${Deposit_tab}
        Wait Until Element Is Visible    ${Amount_input}
        Input Text    ${Amount_input}    1000
        Click Element    ${Deposit_submit}

        Element Should Be Visible    ${Message}



Validate_Balance_After_Deposit
        Sleep    3s
        ${balance}=    Get Text    ${Balance_field}
        Log    Current Balance: ${balance}
        Should Be Equal As Strings    ${balance}    1000


Validate_Balance_After_Withdraw
        Sleep    3s
        ${balance}=    Get Text    ${Balance_field}
        Sleep    3s
        Log    Balance After Withdraw: ${balance}
        Should Be Equal As Strings    ${balance}    600