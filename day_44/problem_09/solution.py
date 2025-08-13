def check_service_health(service_name):
    service_status = {
        "VM": "Running",
        "Storage": "Running", 
        "Database": "Down",
        "Network": "Running",
        "Functions": "Down"
    }
    
    if service_name in service_status:
        return service_status[service_name]
    else:
        return "Service not found"

service = "VM"
status = check_service_health(service)
print(f'{service}: {status}')

services = ["VM", "Storage", "Database", "Network", "Functions", "InvalidService"]

print("Service Health Status:")
for service in services:
    status = check_service_health(service)
    
    if status == "Running":
        print(f'{service}: {status}')
    elif status == "Down":
        print(f'{service}: {status}')
    else:
        print(f'{service}: {status}')

def get_health_summary():
    service_status = {
        "VM": "Running",
        "Storage": "Running", 
        "Database": "Down",
        "Network": "Running",
        "Functions": "Down"
    }
    
    running = 0
    down = 0
    
    for service, status in service_status.items():
        if status == "Running":
            running += 1
        else:
            down += 1
    
    return running, down

running_count, down_count = get_health_summary()
print(f"\nHealth Summary: {running_count} running, {down_count} down")