def azure_cost(vm_hours, storage_gb, bandwidth_gb):
    cost = (vm_hours * 0.04) + (storage_gb * 0.02) + (bandwidth_gb * 0.01)
    return round(cost, 2)


print(azure_cost(720, 100, 50))
