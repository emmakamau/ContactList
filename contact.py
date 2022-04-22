# Class that generates new instances of contacts
class Contact:
    contact_list = [] # Empty contact list

    """
    1. __init__ method that helps us define properties for our objects.
    2. Data inside the brackets are called arguments/variables
    3. self is a variable that represents the instance of the object itself.
    """
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    """save_contact method saves contact objects into contact_list. """
    def save_contact(self):
        Contact.contact_list.append(self)

    pass
