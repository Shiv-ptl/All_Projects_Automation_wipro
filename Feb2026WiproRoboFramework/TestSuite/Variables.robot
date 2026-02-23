*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${name}     Shivanshu Patel
${city}     Lucknow
${address}      Unnao Utter Pradesh
@{list1}        green       red     blue
@{list2}        apple       banana      grapes
&{creds}        Username=admin      password=admin123


*** Test Cases ***
Verify the variables
        Log    ${name}
        Log    ${city}
        Log    ${address}
#        Log    ${list1}
#        Log    ${list2}
#        Log    ${creds}
        FOR    ${element}    IN    @{list1}
            Log    ${element}
             
        END
        FOR    ${element}    IN    @{list2}
            Log    ${element}
             
        END
        Log    ${list2}[0]
        Log    ${list2}[1]
        Log    ${creds}[Username]
        Log    ${creds}[password]