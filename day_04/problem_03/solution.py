# The given info 
Allowed_IPs = {"192.168.1.10", "192.168.1.20", "10.0.0.5"}
Blocked_IPs = {"192.168.1.15", "10.0.0.10", "192.168.1.20"}
Incoming_requests = {"192.168.1.10", "192.168.1.15", "192.168.1.20", "10.0.0.5", "203.0.113.1"}

# Allowed IPs
allow = Allowed_IPs & Incoming_requests
print(f"Requests to be accepted: {allow}")

# Blocked IPS
blocked = Blocked_IPs & Incoming_requests
print(f"Requests to be blocked: {blocked}")

# Unknow Ips
unknown = Incoming_requests.difference(Allowed_IPs.union(Blocked_IPs))
print(f"Requests that are unknown: {unknown}")