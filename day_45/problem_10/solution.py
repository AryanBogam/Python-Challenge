def check_chrome_version(version, minimum_version=100):
    if version >= minimum_version:
        return "Version Supported"
    else:
        return "Version Not Supported"

version = 110
result = check_chrome_version(version)
print(f"Chrome version {version}: {result}")

test_versions = [110, 95, 100, 120, 85]

for ver in test_versions:
    result = check_chrome_version(ver)
    print(f"Version {ver}: {result}")

def check_version_custom(version, min_required):
    if version >= min_required:
        return f"Version Supported (minimum: {min_required})"
    else:
        return f"Version Not Supported (minimum: {min_required})"

print(f"\nCustom minimum requirements:")
test_cases = [
    (110, 105),
    (90, 95),
    (100, 100)
]

for ver, min_req in test_cases:
    result = check_version_custom(ver, min_req)
    print(f"Version {ver}: {result}")

def version_details(version, minimum=100):
    if version >= minimum:
        print(f"Chrome {version} is supported (minimum: {minimum})")
    else:
        outdated_by = minimum - version
        print(f"Chrome {version} is outdated by {outdated_by} versions")

print(f"\nDetailed version check:")
version_details(110)
version_details(95)
version_details(100)