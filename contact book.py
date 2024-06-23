class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print("Contact not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print('---')

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
	
