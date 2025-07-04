# Given.
verified_txns = {"TXN101", "TXN102", "TXN103", "TXN104"}
reported_fraud = {"TXN103", "TXN105", "TXN106"}
incoming_txns = {"TXN101", "TXN103", "TXN105", "TXN107"}

# Clean transactions 
clean_txns = incoming_txns & (verified_txns - reported_fraud)

# Flagged as fraud
fraudulent_txns = incoming_txns & reported_fraud

# Incoming not in verified and not in fraud
known_txns = verified_txns | reported_fraud
suspicious_txns = incoming_txns - known_txns

print("Clean Transactions:", clean_txns)
print("Flagged as Fraud:", fraudulent_txns)
print("Suspicious / Unknown Transactions:", suspicious_txns)
