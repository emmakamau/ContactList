import pyperclip # Pyperclip will allow us to copy and paste items to our clipboard.

# Class that generates new instances of contacts
class Contact:
    contact_list = [] # Empty contact list

    """
    1. __init__ method helps us define properties for our objects.
    2. Data inside the brackets are called arguments/variables.
    3. self is a variable that represents an instance of an object.
    """
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    """save_contact method saves contact objects into contact_list. """
    def save_contact(self):
        Contact.contact_list.append(self)

    """delete_contact method deletes a saved contact from the contact_list"""
    def delete_contact(self):
        Contact.contact_list.remove(self)

    """
    Method that takes in a number and returns a contact that matches that number.
    Args: Phone number to search for
    Returns : Contact of person that matches the number.

    NB: 
        1. Decorators allow you to make simple modifications to callable objects 
            like functions, methods, or classes.
        2. @classmethod Simply informs the python interpreter that this is a method 
            that belongs to the entire class.
        3. cls referred to the entire class, and does not need to be passed in when 
            we call the method.
    """
    @classmethod
    def find_by_number(cls,phone_number):
        for contact in cls.contact_list:
            if contact.phone_number == phone_number:
                return contact
    
    """
    Method that checks if a contact exists from the contact list.
    Args: Phone number to search if it exists
    Returns : True or false depending if the contact exists
    """            
    @classmethod
    def contact_exist(cls,phone_number):
        for contact in cls.contact_list:
            if contact.phone_number == phone_number:
                    return True
        return False

    """
    Method that returns the contact list
    """
    @classmethod
    def display_contacts(cls):
        return cls.contact_list

    @classmethod
    def copy_email(cls,phone_number):
        contact_found = Contact.find_by_number(phone_number)
        pyperclip.copy(contact_found.email)

    pass


