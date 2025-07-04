 Question 2: Duplicate Data Cleaner – Customer CRM Tool

Scenario: You run a startup and have customer data from 2 sources:

Email list from Facebook Ads: {"a@gmail.com", "b@gmail.com", "c@gmail.com"}
Email list from Website Signups: {"b@gmail.com", "c@gmail.com", "d@gmail.com"}
Master CRM list: {"a@gmail.com", "b@gmail.com"}

Determine:
Which emails are duplicates across both platforms?
Which new emails should be added to CRM?
Which customers already exist and need no update?

Expected Logic:
Use intersection() for duplicates
Use union() and difference() for CRM sync
Think like you're building a data hygiene system