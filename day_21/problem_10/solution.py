def recommend_best_route(routes):
    traffic_scores = {"low": 3, "medium": 2, "high": 1}
    best_score = -1
    best_route = None

    for route in routes:
        traffic_score = traffic_scores.get(route["traffic"], 0)
        distance_score = max(1, 15 - route["distance"])
        total_score = traffic_score + distance_score

        if total_score > best_score:
            best_score = total_score
            best_route = route["name"]

    return best_route

routes = [
    {"name": "Route A", "distance": 10, "traffic": "high"},
    {"name": "Route B", "distance": 12, "traffic": "low"}
]
print("Best Route:", recommend_best_route(routes))
