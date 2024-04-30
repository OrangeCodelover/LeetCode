import unittest
# to delete _pycache_
import shutil
import os
##
from valid_parentheses import isValid

class TestIsValid(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertTrue(isValid("()"))
        self.assertTrue(isValid("()[]{}"))
        self.assertTrue(isValid("{[]}"))
        self.assertTrue(isValid("[{}]"))
    
    def test_invalid_parentheses(self):
        self.assertFalse(isValid("("))
        self.assertFalse(isValid(")"))
        self.assertFalse(isValid("(]"))
        self.assertFalse(isValid("([)]"))
        self.assertFalse(isValid("]"))
        self.assertFalse(isValid("["))
        self.assertFalse(isValid("{"))
        self.assertFalse(isValid("}"))
        self.assertFalse(isValid("{["))
    
    def test_empty_string(self):
        self.assertFalse(isValid(""))
    
    def test_single_character(self):
        self.assertFalse(isValid("("))
        self.assertFalse(isValid("["))
        self.assertFalse(isValid("{"))

if __name__ == '__main__':
    unittest.main()


# Cleanup _pycache_ directory
shutil.rmtree("__pycache__", ignore_errors=True)