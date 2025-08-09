def check_follower_goal(current_followers, goal_followers):
    if current_followers >= goal_followers:
        return "Goal reached!"
    else:
        followers_left = goal_followers - current_followers
        return f"{followers_left} followers left"

result = check_follower_goal(950, 1000)
print(result)

result2 = check_follower_goal(1200, 1000)
print(result2)

result3 = check_follower_goal(750, 1000)
print(result3)