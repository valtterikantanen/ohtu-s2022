*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  abc
    Set Password  abcdefg1
    Set Password Confirmation  abcdefg1
    Submit User Information
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  abcdefg1
    Set Password Confirmation  abcdefg1
    Submit User Information
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  abc
    Set Password  abcdef1
    Set Password Confirmation  abcdef1
    Submit User Information
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  abc
    Set Password  abcdefg1
    Set Password Confirmation  abcdefgh1
    Submit User Information
    Register Should Fail With Message  Password and password confirmation must match

Login After Successful Registration
    Set Username  abcd
    Set Password  abcdefg1
    Set Password Confirmation  abcdefg1
    Submit User Information
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  abcd
    Set Password  abcdefg1
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ab
    Set Password  abcdefg1
    Set Password Confirmation  abcdefg1
    Submit User Information
    Register Should Fail With Message  Username must be at least 3 characters long
    Go To Login Page
    Login Page Should Be Open
    Set Username  ab
    Set Password  abcdefg1
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit User Information
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}