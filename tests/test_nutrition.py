import unittest
from src.dietsense.nutrition import NutritionRecord,portion_nutrients,mifflin_st_jeor,estimate_tdee

class TestCalculations(unittest.TestCase):
    def test_energy(self):
        x=portion_nutrients(NutritionRecord('demo',130,3,28,0.3),150)
        self.assertEqual(x['kcal'],195.0)
        self.assertEqual(x['protein_g'],4.5)
    def test_mifflin_male(self):
        self.assertAlmostEqual(mifflin_st_jeor(70,170,25,'male'),1642.5)
    def test_mifflin_female(self):
        self.assertAlmostEqual(mifflin_st_jeor(70,170,25,'female'),1476.5)
    def test_tdee(self):
        self.assertAlmostEqual(estimate_tdee(1642.5,1.4),2299.5)
    def test_invalid(self):
        with self.assertRaises(ValueError): portion_nutrients(NutritionRecord('x',1),0)
        with self.assertRaises(ValueError): mifflin_st_jeor(70,170,25,'unknown')

if __name__=='__main__':unittest.main()
