"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts

class Contacts:
    number_of_contacts = 0
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        Contacts.number_of_contacts += 1
        
    def check_email(self):
        if "@" in self.email:
            print(f"{self.email} is valid")
        else:
            print(f"{self.email} is invalid")
            
    @classmethod
    def get_contact_number(cls):
        return Contacts.number_of_contacts
    
    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"

        '''
contact1 = Contacts("Bill Smith", "350285", "billsmith@cheese.com")
contact2 = Contacts("Grug Williams", "135187", "grug123@a.site.com")
 
contact1.check_email()
Contacts.get_contact_number()

print(contact1)
'''