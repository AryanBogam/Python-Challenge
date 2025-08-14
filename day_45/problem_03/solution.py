def check_bookmark(bookmarks, website):
    if website in bookmarks:
        return "Bookmarked"
    else:
        return "Not Bookmarked"

bookmarks = ["google.com", "github.com"]
website = "github.com"
result = check_bookmark(bookmarks, website)
print(f'Checking "{website}": {result}')

test_websites = [
    "github.com",
    "google.com",
    "youtube.com",
    "facebook.com"
]
for site in test_websites:
    result = check_bookmark(bookmarks, site)
    print(f'{site}: {result}')

def show_bookmarks(bookmarks):
    print("Your bookmarks:")
    for bookmark in bookmarks:
        print(f"  - {bookmark}")

print("\nBookmark list:")
show_bookmarks(bookmarks)