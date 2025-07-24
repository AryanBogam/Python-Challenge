ip_list = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "203.45.67.89", 
           "10.0.0.1", "172.16.0.1", "203.45.67.89", "198.51.100.1"]

unique_ips = set(ip_list)
print("Unique visitors:", len(unique_ips))

print("Blocked duplicate IPs:")
seen = set()
for ip in ip_list:
    if ip in seen:
        print("Blocked:", ip)
    else:
        seen.add(ip)