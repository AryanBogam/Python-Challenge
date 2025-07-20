def airdrop_nearby_devices(devices):
    nearby = [d for d in devices if d['distance'] <= 10]
    sorted_nearby = sorted(nearby, key=lambda x: x['signal_strength'], reverse=True)
    return sorted_nearby

devices = [
    {"name": "iPhone 13", "distance": 5, "signal_strength": 70},
    {"name": "MacBook", "distance": 12, "signal_strength": 80},
    {"name": "iPad", "distance": 8, "signal_strength": 65}
]

print(airdrop_nearby_devices(devices))
