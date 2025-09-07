def jobScheduling(startTime, endTime, profit):
    jobs = list(zip(startTime, endTime, profit))
    jobs.sort(key=lambda x: x[1])
    
    n = len(jobs)
    dp = [0] * (n + 1)
    
    def find_latest_non_overlapping(i):
        for j in range(i - 1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:
                return j
        return -1
    
    for i in range(n):
        latest = find_latest_non_overlapping(i)
        take_profit = jobs[i][2]
        if latest != -1:
            take_profit += dp[latest + 1]
        
        dp[i + 1] = max(dp[i], take_profit)
    
    return dp[n]

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
result = jobScheduling(startTime, endTime, profit)
print(result)