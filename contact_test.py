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
        # Create contact object
        self.new_contact = Contact(
            "James", "Muriuki", "0712345678", "james@ms.com")

    def tearDown(self):
        """ tearDown method cleans up after each test case has run. Return the list to 0"""
        Contact.contact_list = []

    # Testcase1 => test_init test case to test if the object is initialized properly
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

    # Testcase2 => test_save_contact test case to test if the contact object is saved into the contact list
    def test_save_contact(self):
        """
        1. Here we created a test called test_save_contact that calls a save_contact method to our newly
            generated object.
        2. Then we check the length of our contact_list list to confirm an addition has been made to our
            contact list.
        """
        self.new_contact.save_contact()  # saving the new contact
        self.assertEqual(len(Contact.contact_list), 1)

    #Testcase3 => test_save_multiple_contact to check if we can save multiple contact objects to our list
    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678","test@user.com")  #new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    #Testcase4 => test_delete_contact to test if we can remove a contact from our contact list
    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") #new contact
        test_contact.save_contact()

        self.new_contact.delete_contact()# Deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)

    #Testcase5 => test to check if we can find a contact by phone number and display information
    def test_find_contact_by_number(self):
        """
        We now create a test case that tests if we can find a contact object we use the 
        method find_by_number() that takes on a phone number, and returns a contact object. 
        Then we check if the contact object is equal to the saved contact.
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") #new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)


"""
1. By defining the condition if __name__ == '__main__': we are confirming that anything inside the 
    if block should run only if this is the file that is currently being run.
2. The unittest.main() provides a command line interface that collects all the tests methods 
    and executes them.
"""
if __name__ == '__main__':
    unittest.main()
