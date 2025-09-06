def can_finish(numCourses, prerequisites):
    graph = {}
    for i in range(numCourses):
        graph[i] = []
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    visited = set()
    visiting = set()
    
    def has_cycle(course):
        if course in visiting:
            return True
        if course in visited:
            return False
        
        visiting.add(course)
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        
        visiting.remove(course)
        visited.add(course)
        return False
    
    for course in range(numCourses):
        if has_cycle(course):
            return False
    
    return True

numCourses = 2
prerequisites = [[1,0]]
result = can_finish(numCourses, prerequisites)
print(result)