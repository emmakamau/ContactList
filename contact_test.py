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
    #test_init test case to test if the object is initialized properly 
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
"""
1. By defining the condition if __name__ == '__main__': we are confirming that anything inside the 
    if block should run only if this is the file that is currently being run.
2. The unittest.main() provides a command line interface that collects all the tests methods 
    and executes them.
"""
if __name__ == '__main__':
    unittest.main()
