import unittest
from data_script import traverse_dict  


class test_traverse_dict(unittest.TestCase):

    # Traverse a dictionary with a interger value
    def test1(self):
        data = {'a': {'b': {'c': {'value': 42}}}}
        result = traverse_dict(data, 'a', 'b', 'c')
        self.assertEqual(result, {'value': 42})

    # Traverse a dictionary with a string value
    def test2(self):
        data = {'a': {'b': {'c': {'value': 'hello-world'}}}}
        result = traverse_dict(data, 'a', 'b', 'c')
        self.assertEqual(result, {'value': 'hello-world'})



            # Traverse a dictionary with a list value
    def test3(self):
        data = {'a': {'b': {'c': {'value': [3, 4, 5]}}}}
        result = traverse_dict(data, 'a', 'b', 'c')
        self.assertEqual(result, {'value': [3, 4, 5]})


    # Traverse a dictionary with a missing key 
    def test4(self):
        data = {}
        result = traverse_dict(data, 'x')
        self.assertEqual(result, {}) 

    # Traverse a dictionary with a missing value
    def test5(self):
        data = {'a': {'b': {'c': {}}}}
        result = traverse_dict(data, 'a', 'b', 'c')
        self.assertEqual(result, {})  

if __name__ == '__main__':
    unittest.main()
