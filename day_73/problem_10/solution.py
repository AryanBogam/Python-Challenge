users = {
    "john": {"email": "john@email.com", "posts": 15, "comments": 32, "likes_received": 150, "friends": ["jane", "bob"], "groups": ["python_lovers", "book_club"]},
    "jane": {"email": "jane@email.com", "posts": 8, "comments": 18, "likes_received": 95, "friends": ["john", "alice"], "groups": ["python_lovers"]},
    "bob": {"email": "bob@email.com", "posts": 22, "comments": 45, "likes_received": 200, "friends": ["john"], "groups": ["book_club"]}
}

groups = {
    "python_lovers": {"members": ["john", "jane", "alice"], "posts": 25, "total_likes": 180},
    "book_club": {"members": ["john", "bob", "charlie"], "posts": 12, "total_likes": 85}
}

events = {
    "john": {"created": 3, "participated": 7},
    "jane": {"created": 1, "participated": 4},
    "bob": {"created": 2, "participated": 5}
}

activity_data = {
    "john": {"2023-06-01": 5, "2023-06-02": 3, "2023-06-03": 8, "2023-06-04": 2},
    "jane": {"2023-06-01": 2, "2023-06-02": 4, "2023-06-03": 1, "2023-06-04": 6},
    "bob": {"2023-06-01": 7, "2023-06-02": 2, "2023-06-03": 4, "2023-06-04": 3}
}

def get_user_analytics(username):
    if username not in users:
        return "User not found!"
    
    user = users[username]
    analytics = {
        "posts_created": user["posts"],
        "comments_made": user["comments"],
        "likes_received": user["likes_received"],
        "total_friends": len(user["friends"]),
        "groups_joined": len(user["groups"]),
        "events_created": events.get(username, {}).get("created", 0),
        "events_participated": events.get(username, {}).get("participated", 0)
    }
    
    analytics["engagement_score"] = user["posts"] + user["comments"] + (user["likes_received"] // 10)
    return analytics

def get_group_analytics(group_name):
    if group_name not in groups:
        return "Group not found!"
    
    group = groups[group_name]
    analytics = {
        "total_members": len(group["members"]),
        "total_posts": group["posts"],
        "total_likes": group["total_likes"],
        "average_likes_per_post": group["total_likes"] / max(group["posts"], 1),
        "member_list": group["members"]
    }
    return analytics

def get_daily_activity_summary(username):
    if username not in activity_data:
        return "No activity data found!"
    
    user_activity = activity_data[username]
    total_activity = sum(user_activity.values())
    avg_daily = total_activity / len(user_activity)
    
    most_active_day = max(user_activity.keys(), key=lambda k: user_activity[k])
    
    return {
        "total_activities": total_activity,
        "average_daily": round(avg_daily, 2),
        "most_active_day": most_active_day,
        "daily_breakdown": user_activity
    }

def get_platform_analytics():
    total_users = len(users)
    total_posts = sum(user["posts"] for user in users.values())
    total_comments = sum(user["comments"] for user in users.values())
    total_likes = sum(user["likes_received"] for user in users.values())
    
    most_active_user = max(users.keys(), key=lambda u: users[u]["posts"] + users[u]["comments"])
    most_liked_user = max(users.keys(), key=lambda u: users[u]["likes_received"])
    
    return {
        "total_users": total_users,
        "total_posts": total_posts,
        "total_comments": total_comments,
        "total_likes": total_likes,
        "most_active_user": most_active_user,
        "most_liked_user": most_liked_user,
        "average_posts_per_user": total_posts / total_users,
        "total_groups": len(groups)
    }

def compare_users(user1, user2):
    if user1 not in users or user2 not in users:
        return "One or both users not found!"
    
    analytics1 = get_user_analytics(user1)
    analytics2 = get_user_analytics(user2)
    
    comparison = {}
    for key in analytics1:
        if isinstance(analytics1[key], (int, float)):
            comparison[key] = {
                user1: analytics1[key],
                user2: analytics2[key],
                "winner": user1 if analytics1[key] > analytics2[key] else user2
            }
    
    return comparison

def get_top_users_by_metric(metric, limit=3):
    if metric not in ["posts", "comments", "likes_received"]:
        return "Invalid metric!"
    
    sorted_users = sorted(users.items(), key=lambda x: x[1][metric], reverse=True)
    return [(user, data[metric]) for user, data in sorted_users[:limit]]

john_analytics = get_user_analytics("john")
print("John's Analytics:")
for key, value in john_analytics.items():
    print(f"  {key}: {value}")

group_analytics = get_group_analytics("python_lovers")
print("\nPython Lovers Group Analytics:")
for key, value in group_analytics.items():
    print(f"  {key}: {value}")

platform_stats = get_platform_analytics()
print("\nPlatform Analytics:")
for key, value in platform_stats.items():
    print(f"  {key}: {value}")

top_posters = get_top_users_by_metric("posts")
print("\nTop Posters:")
for user, posts in top_posters:
    print(f"  {user}: {posts} posts")