class ContactBook:
   def __init__(self):
      self.contacts = {}

   def add_contact(self, name, phone_number, email):
      self.contacts[name] = {"phone_number": phone_number, "email": email}
      print(f"Contact {name} added successfully!")

   def view_contacts(self):
      for name, details in self.contacts.items():
         print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}")

   def search_contact(self, name):
      if name in self.contacts:
         print(f"Name: {name}, Phone Number: {self.contacts[name]['phone_number']}, Email: {self.contacts[name]['email']}")
      else:
         print("Contact not found!")

   def delete_contact(self, name):
      if name in self.contacts:
         del self.contacts[name]
         print(f"Contact {name} deleted successfully!")
      else:
         print("Contact not found!")

def main():
   contact_book = ContactBook()

   while True:
      print("\nContact Book Menu:")
      print("1. Add Contact")
      print("2. View Contacts")
      print("3. Search Contact")
      print("4. Delete Contact")
      print("5. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
         name = input("Enter name: ")
         phone_number = input("Enter phone number: ")
         email = input("Enter email: ")
         contact_book.add_contact(name, phone_number, email)
      elif choice == "2":
         contact_book.view_contacts()
      elif choice == "3":
         name = input("Enter name to search: ")
         contact_book.search_contact(name)
      elif choice == "4":
         name = input("Enter name to delete: ")
         contact_book.delete_contact(name)
      elif choice == "5":
         break
      else:
         print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()