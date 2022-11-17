*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  abc  abcdefg1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  abcdefg1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  abcdefg1
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  abc  abcdef1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abc  abcdefgh
    Output Should Contain  Password must also contain numbers or symbols

# My own test just for fun
Register With Username Containing Numbers And Valid Password
    Input Credentials  abc1  abcdefg1
    Output Should Contain  Username must only contain characters a-z

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command