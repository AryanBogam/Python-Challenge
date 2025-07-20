def optimize_storage(apps, space_needed):
    # Sort apps by size (largest first).
    sorted_apps = sorted(apps, key=lambda app: app[1], reverse=True)
    
    apps_to_delete = []
    total_freed = 0
    
    for app_name, app_size in sorted_apps:
        if total_freed >= space_needed:
            break
        
        apps_to_delete.append(app_name)
        total_freed += app_size
    
    return apps_to_delete, total_freed

apps = [
    ("Instagram", 2.5),
    ("TikTok", 3.2),
    ("Notes", 0.1),
    ("Games", 5.0),
    ("Photos", 1.8),
    ("Music", 0.5)
]

apps_to_delete, freed_space = optimize_storage(apps, 5)
print(f"Apps to delete: {apps_to_delete}")
print(f"Total space freed: {freed_space} GB")