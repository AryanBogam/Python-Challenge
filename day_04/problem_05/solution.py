# Given.
facebook_emails = {"a@gmail.com", "b@gmail.com", "c@gmail.com"}
website_emails = {"b@gmail.com", "c@gmail.com", "d@gmail.com"}
crm_emails = {"a@gmail.com", "b@gmail.com"}

# Duplicates between Facebook and Website
duplicates = facebook_emails & website_emails  

# New emails to add to CRM 
all_leads = facebook_emails | website_emails    
new_emails = all_leads - crm_emails             

# Already in CRM 
already_in_crm = all_leads & crm_emails         