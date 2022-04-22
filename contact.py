"""
BDD- expectations
1. Allow us to Create new contacts with properties.
2. Save contacts.
3. Display contacts.
4. Delete contacts.
5. Display contact information.
"""

# Class that generates new instances of contacts
class Contact:
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

    pass
