import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_teenage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_middle_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)
      
      
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()