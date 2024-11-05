import unittest
from app.main import FictionalChocoHouse
import os
class TestChocoHouse(unittest.TestCase):
    def setUp(self):
        """Test database"""
        self.test_db="test_choco_house.db"
        self.app = FictionalChocoHouse(self.test_db)
        
    def tearDown(self):
        """Remove test database"""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
            
    def test_add_flavour(self):
        """Test add flavour"""
        flavour_id = self.app.add_flavour("Milk Chocolate", "Smooth and creamy milk chocolate", False, "")
        self.assertEqual(flavour_id, 1)

    def test_add_ingredient(self):
        """Test add ingredient"""
        ingredient_id = self.app.add_ingredient("Vanilla Extract", 500, "ml", "Contains alcohol")
        self.assertEqual(ingredient_id, 1)

    def test_add_customer_suggestion(self):
        """Test adding customer suggestion"""
        suggestion_id = self.app.add_customer_suggestion("Add more vanilla", "Increase the vanilla flavor", "Ensure the vanilla is pure")
        self.assertEqual(suggestion_id, 1)
        
if __name__=='__main__':
    unittest.main()
    