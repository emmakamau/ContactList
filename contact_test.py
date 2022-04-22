"""
BDD- expectations which are factors that we will test
1. Allow us to Create new contacts with properties.
2. Save contacts.
3. Display contacts.
4. Delete contacts.
5. Display contact information.
"""

import unittest  # Python test framework
from contact import Contact

"""
Test class that defines test cases for the contact class behaviours.
Args: unittest.TestCase: TestCase class that helps in creating test cases
"""
class TestContact(unittest.TestCase):
    """
    1. SetUp() mthd allows us to define instructions that will be executed before each test method.
    2. We have instructed our setUp() method to create a new instance of Contact class, before each
       test method declared, and stores it in an instance variable in the test class self.new_contact.
    """
    def setUp(self): 
        #Create contact object
        self.new_contact = Contact("James", "Muriuki", "0712345678", "james@ms.com") 

    #Testcase1 => test_init test case to test if the object is initialized properly 
    def test_init(self):
        """
        We see some new syntax here self.assertEqual() this is a TestCase method that checks for an 
        expected result. The first argument is the expected result and the second argument is the 
        result that is actually gotten.Here, we are checking if the name and description of our 
        new object is what we actually inputted.
        """
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "james@ms.com")

    #Testcase2 => test_save_contact test case to test if the contact object is saved into the contact list
    def test_save_contact(self):
        """
        1. Here we created a test called test_save_contact that calls a save_contact method to our newly 
            generated object.
        2. Then we check the length of our contact_list list to confirm an addition has been made to our 
            contact list.
        """
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

"""
1. By defining the condition if __name__ == '__main__': we are confirming that anything inside the 
    if block should run only if this is the file that is currently being run.
2. The unittest.main() provides a command line interface that collects all the tests methods 
    and executes them.
"""
if __name__ == '__main__':
    unittest.main()
