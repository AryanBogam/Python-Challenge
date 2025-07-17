from datetime import datetime, timedelta

def unique_active_users_24h(login_data):

    now = datetime.now()
    twenty_four_hours_ago = now - timedelta(hours=24)
    
    active_users = set()
    
    for user_id, timestamp in login_data:
        # Convert timestamp to datetime if it's a string
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        
        if timestamp >= twenty_four_hours_ago:
            active_users.add(user_id)
    
    return len(active_users)

from datetime import datetime, timedelta
now = datetime.now()

login_data = [
    (1, now - timedelta(hours=2)),
    (2, now - timedelta(hours=5)),
    (1, now - timedelta(hours=8)),  
    (3, now - timedelta(hours=30)), 
    (4, now - timedelta(minutes=30)),
]

result = unique_active_users_24h(login_data)
print(f"Unique active users in last 24 hours: {result}")