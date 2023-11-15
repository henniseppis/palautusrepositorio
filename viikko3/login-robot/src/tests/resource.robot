*** Settings ***
Library  ../AppLibrary.py
Library  ../services/user_service.py

*** Keywords ***
Input Login Command
    Input  login

Input New Command
    Input  new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application



