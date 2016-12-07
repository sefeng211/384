'''
Unit tests for IMeal
'''

import unittest
from cspModel import *
from cspbase import *


def create_meals(domain):

    meal_1 = Variable('Meal_1', domain)
    meal_2 = Variable('Meal_2', domain)
    meal_3 = Variable('Meal_3', domain)
    meal_4 = Variable('Meal_4', domain)
    meal_5 = Variable('Meal_5', domain)
    meal_6 = Variable('Meal_6', domain)

    meals = [meal_1, meal_2, meal_3, meal_4, meal_5, meal_6]
    return meals

class IMealTests(unittest.TestCase):

    def setUp(self):
        self.food_data ={
            'Cheese':
                {
                    'water': 1,
                    'energy': 1,
                    'protein': 1
                },
            'Milk':
                {
                    'water': 1,
                    'energy': 1,
                    'protein': 1
                },
            'Bread':
                {
                    'water': 1,
                    'energy': 1,
                    'protein': 1
                }
        }
        self.domain = create_domain(self.food_data)
        self.meals = create_meals(self.domain)
    def test_split_meals_into_days(self):
        '''
        Test the split_meals_into_days function
        '''

        result = split_meals_into_days(self.meals)

        self.assertEqual(result, [self.meals[0:3], self.meals[3:]])

    def test_domain_creation(self):
        '''
        Test the create_domain function
        '''
        food_list = []
        for name in self.food_data.keys():
            food = Food(name, self.food_data[name])
            food_list.append(food)

        food_list = list(powerset(food_list))
        ret = create_domain(self.food_data)
        self.assertEqual(len(food_list), len(ret))

    def test_find_tuples_protein(self):

        days_meals = split_meals_into_days(self.meals)
        pass
        # find_tuples_protein(days_meals[0])




if __name__ == '__main__':
    unittest.main()