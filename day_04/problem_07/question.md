 Question 7: Bank Fraud Detector

Scenario: You are working on a banking fraud detection system. Sets:

Verified Transactions: {"TXN101", "TXN102", "TXN103", "TXN104"}
Reported Fraudulent: {"TXN103", "TXN105", "TXN106"}
Incoming Transactions: {"TXN101", "TXN103", "TXN105", "TXN107"}

Determine:

Which transactions are clean?
Which are flagged?
Which are suspicious (not verified or known fraud)?

Expected Logic:
Use intersection() and difference()
Think like you're building a real-time fraud alert system