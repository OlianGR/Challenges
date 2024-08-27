import unittest
from datetime import datetime, date

"""
Ejercio
"""

def sum(a, b):
    if not isinstance(a,(int,float)or not isinstance(b,(int,float))):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    return  a + b 

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5,7),12)
        self.assertEqual(sum(5,-7),-2)
        self.assertEqual(sum(0,0),0)
        self.assertEqual(sum(2.5,2.5),5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5",7)
        with self.assertRaises(ValueError):
            sum("5","5")
        with self.assertRaises(ValueError):
            sum(None,"5")



"""
Extra
"""

class TestData(unittest.TestCase):

    def setUp(self) -> None:
        
        self.data = {
            "name": "angel",
            "age": 27,
            "birth_date": datetime.strptime("04-03-97", "%d-%m-%y").date(),
            "languages": ["Python", "Java", "Swift"]

        }   
        

    def test_fields_exits(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["languages"], list)

unittest.main()
