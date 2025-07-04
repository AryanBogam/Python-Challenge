Question 4: Network Security Challenge
Question: You have three sets of IP addresses:

Allowed IPs: {"192.168.1.10", "192.168.1.20", "10.0.0.5"}
Blocked IPs: {"192.168.1.15", "10.0.0.10", "192.168.1.20"}
Incoming requests: {"192.168.1.10", "192.168.1.15", "192.168.1.20", "10.0.0.5", "203.0.113.1"}

Determine: 
1 Which requests should be accepted? 
2 Which should be blocked? 
3 Which are unknown (not in allowed or blocked)?

Expected Logic:
Use intersection and difference operations
Handle overlapping conditions
Think about security logic