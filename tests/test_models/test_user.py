#!/usr/bin/python3
"""
Testing the User model by unittest
"""

import unittest
from models.user import User
from datetime import datetime

class Test_class_attributes(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_default_initialization(self):
        """
        Test the default initialization of the User class.
        """
        user = User()
        
        self.assertIsInstance(user, User)
        self.assertEqual(user, None)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_types(self):
        """
        tests with random attributes
        """
        user1 =  User(name="test")
        user2 = User(name="test", value=18)
        self.assertIsInstance(user1.name, str)
        self.assertIsInstance(user2.name, str)
        self.assertIsInstance(user2.value, int)

    def test_all_required_fields(self):
        """
        Test all required fields in the User class.
        """
        user = User("test@email.com", "password")
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@email.com')
        self.assertEqual(user.password, 'password')

    def test_attributes_assignment(self):
        """
        Test the assignment of attributes in the User class.
        """
        user = User(email="test@example.com", password="sectest", first_name="harry", last_name="potter")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "sectest")
        self.assertEqual(user.first_name, "harry")
        self.assertEqual(user.last_name, "potter")

    def test_to_dict_method(self):
        """
        Test the to_dict method in the User class.
        """
        user = User(email="test@example.com", password="securepass", first_name="John", last_name="Doe")
        user_dict = user.to_dict()

        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('id', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('__class__', user_dict)
        