def total_views(views_list):
    total = 0
    for views in views_list:
        total += views
    return total

views_list = [1200, 4500, 800]
result = total_views(views_list)
print(result)