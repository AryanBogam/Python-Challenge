# Initialize empty dictionary to store contacts
contacts = {}

# Start infinite loop for menu system
while True:
    # Display menu options
    print("\n Contact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. count Contact")
    print("7. Exit")

    # Get user's choice
    choice = input("Enter your choice: ")

    # Create new contact
    if choice == "1":
        # Get contact name from user
        name = input("Enter your name = ")
        # Check if contact already exists
        if name in contacts:
            print(f"Contact name {name} already exists! ")
        else:
            # Get contact details
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile number = ")
            # Store contact in dictionary with nested dictionary structure
            contacts[name] = {"age": int(age), "Email": email, "mobile":mobile}
            print(f"Contact name has been successfully!")

    # View existing contact
    elif choice == "2":
        # Get contact name to view
        name = input("Enter Contact name to view = ")
        # Check if contact exists
        if name in contacts:
            # Get contact details from dictionary
            contact = contacts[name]
            # Display contact information
            print(f"Name:{name}, \nAge:{age}, \nMobile Number:{mobile}")
        else:
            print("Contact not found!")

    # Update existing contact
    elif choice == "3":
        # Get contact name to update
        name = input("Enter name to update contact = ")
        # Check if contact exists
        if name in contacts:
            # Get new contact details
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile number = ")
            # Update contact with new information
            contacts[name] = {"age": int(age), "Email": email, "mobile":mobile}
        else:
            print("Contact not found!")

    # Delete contact
    elif choice == "4":
        # Get contact name to delete
        name = input("Enter contact name to delete = ")
        # Check if contact exists
        if name in contacts:
            # Remove contact from dictionary
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully")
        else:
            print("Contact not found!")