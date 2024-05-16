"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Implement the ContactManager class and perform CRUD operations.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Import the ContactManager class here.

from contact_manager import ContactManager

# 2. Go to the 'contact_manager.py' file and implement the TODO in the display_contacts method.

# 3. Create two contacts using the ContactManager.

def main():
    CM = ContactManager()
    CM.add_contact("Drilla", "456", "yes@gmail.com")
    CM.add_contact("Flogeth", "123", "flogethcompost@gmail.com")

# 4. Display all contacts.
    print("Initial list of employees")
    CM.display_contacts()

# 5. Update the email address of one contact.

    CM.update_contact("Flogeth", new_email="flogethcompost@gmail.com")

# 6. Remove one of the contacts.

    CM.remove_contact("Drilla")

# 7. Display all contacts again.
    print("Updated list of employees")
    CM.display_contacts()

    print(CM.get_contact_amount())

if __name__ == "__main__":
    main()

