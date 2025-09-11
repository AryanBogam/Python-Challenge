from datetime import datetime, timedelta

logged_in_users = ["john", "jane", "bob"]
scheduled_posts = []
published_posts = []
next_post_id = 1

def schedule_post(username, content, schedule_time):
    global next_post_id
    if username not in logged_in_users:
        return "Please log in first!"
    
    try:
        schedule_datetime = datetime.strptime(schedule_time, "%Y-%m-%d %H:%M")
    except:
        return "Invalid time format! Use YYYY-MM-DD HH:MM"
    
    if schedule_datetime <= datetime.now():
        return "Cannot schedule post in the past!"
    
    post = {
        "id": next_post_id,
        "author": username,
        "content": content,
        "scheduled_time": schedule_datetime,
        "status": "scheduled"
    }
    scheduled_posts.append(post)
    next_post_id += 1
    return "Post scheduled successfully!"

def cancel_scheduled_post(username, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    for i, post in enumerate(scheduled_posts):
        if post["id"] == post_id and post["author"] == username:
            scheduled_posts.pop(i)
            return "Scheduled post cancelled!"
    
    return "Scheduled post not found or not yours!"

def check_and_publish_scheduled_posts():
    current_time = datetime.now()
    published_count = 0
    
    posts_to_remove = []
    for i, post in enumerate(scheduled_posts):
        if post["scheduled_time"] <= current_time:
            published_post = {
                "id": post["id"],
                "author": post["author"],
                "content": post["content"],
                "published_time": current_time,
                "originally_scheduled": post["scheduled_time"]
            }
            published_posts.append(published_post)
            posts_to_remove.append(i)
            published_count += 1
    
    for i in reversed(posts_to_remove):
        scheduled_posts.pop(i)
    
    return f"{published_count} posts published!"

def get_user_scheduled_posts(username):
    if username not in logged_in_users:
        return "Please log in first!"
    
    user_scheduled = []
    for post in scheduled_posts:
        if post["author"] == username:
            user_scheduled.append(post)
    
    return user_scheduled

def get_all_scheduled_posts():
    return scheduled_posts

def get_posts_scheduled_for_date(date):
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    posts_for_date = []
    
    for post in scheduled_posts:
        if post["scheduled_time"].date() == target_date:
            posts_for_date.append(post)
    
    return posts_for_date

tomorrow = datetime.now() + timedelta(days=1)
schedule_time = tomorrow.strftime("%Y-%m-%d %H:%M")

print(schedule_post("john", "Good morning everyone!", schedule_time))
print(schedule_post("jane", "Weekly Python tips coming up!", schedule_time))

print("John's scheduled posts:", len(get_user_scheduled_posts("john")))
print("Total scheduled posts:", len(get_all_scheduled_posts()))

print(check_and_publish_scheduled_posts())
print("Published posts:", len(published_posts))