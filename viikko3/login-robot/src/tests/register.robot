*** Settings ***
Resource  resource.robot
Test Setup  Create New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  hhhenni  moikkuli123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  hennipenni  salasana1
    Output Should Contain  User with username hennipenni already exists

Register With Too Short Username And Valid Password
    Input Credentials  he  salasana1
    Output Should Contain  Username is too short
    
Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  henzzuu123  salasana1
    Output Should Contain  Username needs to only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  hehenni  sala1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  hehehenni  salasalas
    Output Should Contain  Password can't only contain letters a-z. Add i.e number
    


*** Keywords ***
Create New Command And Create User
    Create User  hennipenni  moikkuli123
    Input New Command
