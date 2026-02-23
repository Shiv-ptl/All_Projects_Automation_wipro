#Lab session
#
#Create a scalar variable ${NAME} and print it.
#Assign two numbers to variables and print their sum.
#Create a variable ${CITY} and use it inside a sentence.
#Reassign a variable value inside a test case and log the updated value.
#Create a list variable @{FRUITS} and print the first item.
#Loop through a list variable and print each element.
#Find the length of a list variable.
#Create a dictionary variable &{USER} and print one key value.
#Add a new key-value pair to a dictionary variable.
#Access dictionary values inside a loop and print key and value.

*** Settings ***
Library     SeleniumLibrary
Library    Collections

*** Variables ***
${name}     Shivanshu Patel
${num1}     234
${num2}     266
${city}     Lucknow
@{FRUITS}       apple       banana      grapes
&{USER}     username=admin      password=admin1234



*** Test Cases ***
Variable LabSession1

        Log    ${name}
        ${sum}      Evaluate    ${num1} + ${num2}
        Log    sum is : ${sum}
        Log    ${city} is known as Nawaboon ka Shahar
        ${city}=        Set Variable        Kanpur
        Log    Updated city is ${city}
        Log    ${FRUITS}[0]
        FOR    ${element}    IN    @{FRUITS}
            Log    ${element}
             
        END

        ${length}=      Get Length      ${FRUITS}
        Log    Length of list FRUITS is ${length}


        Log    ${USER}[username]

        Set To Dictionary       ${USER}     email=shiv@gmail.com
        Log    ${USER}[email]

        FOR    ${key}       ${value}    IN    &{USER}
            Log    ${key} : ${value}

        END