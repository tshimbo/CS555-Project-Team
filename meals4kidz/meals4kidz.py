import unittest
#Terry Shim Contribution
#Story Name:  View measurements
#Task 1: Get measurements of recipe of a specific meal
#Task 2: Print measurements of recipe
#Task 3: Recipe meal cannot be a number

#-------------------------------------------------------------------------------



recipesValid = {
        'Rice paper wraps': '1 carrot, 1 avocado, 1/2 cucumber, 8 mint leaves, 50g rice vermicelli noodles',
        'Spinach savoury muffins': '200g fresh spinach, 100g cheddar, 1 tbsp dried thyme, 2 eggs',
        'Omelette': '1 knob of butter, 1 tomato deseeded and diced, 1 tsp dried oregano',
    }

testRecipe = {
        'Rice paper wraps': '1 carrot'
}

def checkValidMeal(meal):
    if meal.isnumeric():
        return False
    else:
        return True

def measurementList(recipes, meal):
    try:
        # Iterating over values
       
        print('Measurements of: ' + str(meal) + '\n')
        for meal, ingredient in recipes.items():   
            assert checkValidMeal(meal) == True
            
            return print(ingredient)
    except:
        raise Exception("Meal cannot be a number!")
        


class Test(unittest.TestCase):

    def test_checkValidMeal(self):
        self.assertTrue(checkValidMeal('omelette'), 'omelette')
        self.assertFalse(checkValidMeal('123'), '123')

    def test_measurementList(self):
        self.assertFalse(measurementList(recipesValid,'Omelette'), "432")
       
      


if __name__ == '__main__':
    unittest.main()
    
    
#------------------------------------------------------------------------------------------
