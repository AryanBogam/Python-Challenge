def congestion_analyzer(roads):
    result = []
    for road in roads:
        status = "congested" if road["avg_speed"] < 20 else "clear"
        result.append({"name": road["name"], "status": status})
    return result

roads = [{"name": "MG Road", "avg_speed": 12}, {"name": "FC Road", "avg_speed": 35}]
print(congestion_analyzer(roads))
