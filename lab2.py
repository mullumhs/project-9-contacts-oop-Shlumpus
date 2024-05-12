"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.

class Contacts:
    number_of_contacts = 0
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        Contacts.number_of_contacts += 1
        
contact1 = Contacts("Bill Smith", "350285", "billsmith@cheese.com")
contact2 = Contacts("Grug Williams", "135187", "grug123@a.site.com")

        # Create at least two instances of the Contact class with different data.



# Write code that prints out the details of each contact you have created.

print(contact1.name)

