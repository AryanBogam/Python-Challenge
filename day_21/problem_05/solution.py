def find_parking(slots):
    available = [slot for slot in slots if not slot["occupied"]]
    next_available = available[0]["id"] if available else None
    return {"next_available": next_available, "total_free": len(available)}

slots = [{"id": 1, "occupied": False}, {"id": 2, "occupied": True}]
print(find_parking(slots))
