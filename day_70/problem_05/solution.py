def accountsMerge(accounts):
    email_to_name = {}
    email_graph = {}
    
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name
            if email not in email_graph:
                email_graph[email] = []
        
        for i in range(1, len(account) - 1):
            email_graph[account[i]].append(account[i + 1])
            email_graph[account[i + 1]].append(account[i])
    
    visited = set()
    result = []
    
    def dfs(email, emails):
        if email in visited:
            return
        visited.add(email)
        emails.append(email)
        for neighbor in email_graph[email]:
            dfs(neighbor, emails)
    
    for email in email_graph:
        if email not in visited:
            emails = []
            dfs(email, emails)
            emails.sort()
            result.append([email_to_name[email]] + emails)
    
    return result

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
result = accountsMerge(accounts)
print(result)