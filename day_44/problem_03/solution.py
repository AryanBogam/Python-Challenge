def check_tag_exists(resource_tags, tag_name):
    if tag_name in resource_tags:
        return "Tag found"
    else:
        return "Tag not found"

resource_tags = {"env": "prod", "owner": "Aryan"}
tag_to_find = "env"

result = check_tag_exists(resource_tags, tag_to_find)
print(f'Looking for tag "{tag_to_find}": {result}')

test_tags = ["env", "owner", "project", "cost-center"]

for tag in test_tags:
    result = check_tag_exists(resource_tags, tag)
    print(f'Tag "{tag}": {result}')

def get_tag_value(resource_tags, tag_name):
    if tag_name in resource_tags:
        return resource_tags[tag_name]
    else:
        return "Tag not found"

print("\nTag values:")
for tag in ["env", "owner", "missing"]:
    value = get_tag_value(resource_tags, tag)
    print(f'{tag}: {value}')