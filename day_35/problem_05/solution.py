def calculate_storage(hours, num_cameras):
    total_gb = hours * num_cameras * 2
    return total_gb

result = calculate_storage(4, 3)
print(f"{result} GB")

result2 = calculate_storage(8, 5)
print(f"{result2} GB")