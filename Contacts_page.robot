**Settings**
Documentation  Test cases for contacts page

Library  Selenium2Library
Library  Contacts_page.py
Test Teardown  Close All Browsers  

**Variables**
${user_mail}  horira4696@onetag.org
${user_pass}  12021985

***Test Cases***
The logined user fill in all fields of "change animal data form" and submit
    Singin with existing user  ${user_mail}  ${user_pass}
    User navigates to contacts page
    User select change animal data
    User fill in chip field
    User fill in descr field
    User submit form
    Verify succes submission message
