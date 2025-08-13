def check_ip_access(allowed_ips, ip_address):
    if ip_address in allowed_ips:
        return "Access granted"
    else:
        return "Access denied"

allowed_ips = ["192.168.1.1", "10.0.0.5"]
test_ip = "192.168.1.1"

result = check_ip_access(allowed_ips, test_ip)
print(f'IP {test_ip}: {result}')

test_ips = [
    "192.168.1.1",
    "10.0.0.5",
    "192.168.1.2",
    "10.0.0.1"]

for ip in test_ips:
    result = check_ip_access(allowed_ips, ip)
    print(f'IP {ip}: {result}')

def show_whitelist(allowed_ips):
    print("Allowed IPs:")
    for ip in allowed_ips:
        print(f"  - {ip}")

print("\nCurrent whitelist:")
show_whitelist(allowed_ips)