import re
import unittest
#Terry Shim Contribution
#Story Name:  View measurements
#Task 1: Get measurements of recipe of a specific meal
#Task 2: Print measurements of recipe
#Task 3: Recipe meal cannot be a number

#Sprint 2 Tasks
#Task 4: Must be at least one ingredient per recipe
#Task 5: Recipe must be valid string for ingredient (not a number)
#Task 6: Must have at least one recipe


#-------------------------------------------------------------------------------

#Example dictionaries for testing purposes

recipesValid = {
        'Rice paper wraps': '1 carrot, 1 avocado, 1/2 cucumber, 8 mint leaves, 50 grams rice vermicelli noodles',
        'Spinach savoury muffins': '200 g fresh spinach, 100g cheddar, 1 tbsp dried thyme, 2 eggs',
        'Omelette': '1 knob of butter, 1 tomato deseeded and diced, 1 tsp dried oregano',
    }

testRecipe = {
        'Rice paper wraps': '1 carrot'
}

recipesInvalidEmptyCase = {
}


recipesInvalidNoIngredients= {
    'Rice paper wraps'
}

recipesInvalidIngredient = {
       'Rice paper wraps': 123
}


#----------------------------------------------------------------------------------------------------


def checkValidMeal(meal): #checking that a meal cannot be a number
    if meal.isnumeric():
        return False
    else:
        return True
def checkValidRecipe(recipes): #checking that a recipe is valid
    if len(recipes.values()) < 1:
        raise ValueError('Recipe must have at least one ingredient')
    if len(recipes.keys()) < 1:
         raise KeyError('No recipes found')
    for ingredients in recipes.values():
        if ingredients[0].isdigit() :
            return True
        else:
            return False
    for recipe in recipes.keys():
        if isinstance(recipe[0], str):
            return True
        else:
            return False 
        
    return True
        

def measurementList(recipes, meal): #parse through a dictionary of recipes in order to find the measurements of the ingredients
    try:
        # Iterating over values
        assert checkValidMeal(meal) == True   #error checking
        assert checkValidRecipe(recipes) == True 
        print('Measurements of: ' + str(meal) + '\n') #specify which meal you are taking from
        for meal, ingredient in recipes.items():   #iterate through the recipes to find the correct one 
           
            
            return print(ingredient)     #print only the measurement list
    except:
        raise Exception("Meal cannot be a number!")   #error if the meal is a number
        

#------------------------------------------------------------------------------------------


#############################################################
# Ryan Lee Contribution
# Story Name: Allergies
#
# Sprint #1:
# Task 1: Ask user if child has allergies
# Task 2: Ask user to input child's allergy
# Task 3: Check if child's allergy is a valid
#
# Sprint #2:
# Task 4: Check if child's allergy was already added
# Task 5: Ask user if child has another allergy
# Task 6: Get list of child's allergies
##############################################################
import unittest

commonAllergies = ['dairy', 'eggs', 'fish', 'shellfish',
                   'tree nuts', 'peanuts', 'wheat', 'soy']
allergyList = []


# ask user if child has allergies
def haveAllergy():
    while True:
        try:
            x = str(input("Does your child have allergies? (y/n): "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'y'):
                print('Here are some allergies your child may have: ')
                print(commonAllergies)
                have = True
                break
            elif (x == 'n'):
                have = False
                break
            else:
                print('Please enter y for yes or n for no.')
                continue
    return have


# ask user to input child's allergy
def getAllergy():
    while True:
        try:
            allergy = str(input("Enter your child's allergy: "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            break
    return allergy


# check if allergy is valid or is already added
def validAllergy(allergy):
    valid = True
    if (allergy not in commonAllergies):
        print("This is not a valid allergy")
        valid = False
    if (allergy in allergyList):
        print("You've already added this allergy")
        valid = False
    return valid


# ask user if child has another allergy
def anotherAllergy():
    while True:
        try:
            x = str(input("Does your child have another allergy? (y/n): "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if (x == 'y'):
                another = True
                break
            elif (x == 'n'):
                another = False
                break
            else:
                print('Please enter y for yes or n for no.')
                continue
    return another


# get list of child's allergies (our main function)
def allergies():
    if not haveAllergy():
        return
    allergy = getAllergy()
    while not validAllergy(allergy):
        allergy = getAllergy()
    if validAllergy(allergy):
        allergyList.append(allergy)
    while anotherAllergy():
        allergy = getAllergy()
        while not validAllergy(allergy):
            allergy = getAllergy()
        if validAllergy(allergy):
            allergyList.append(allergy)
    return allergyList


#_____________________________________________________________

# Maksym Perozhak Contribution

# Sprint 1
# Story Name: Choose Age
# Sprint 1 Task 1: Identify the age of the user
# Sprint 1 Task 2: Identify if age of user old enough for app authorization
# Sprint 1 Task 3: Identify if age of user is valid

#_____________________________________________________________

from datetime import datetime, date
 
def checkValidUserAge(birthdate):
    today = date.today()
    #birthdate = datetime.fromisoformat(input("Enter Your Birthdate in YYYY-MM-DD Format: "))
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 18:
        return ("User Age Verified!")
    elif age < 18 and age > 0:
        return ("Sorry, you are not eligable")
    elif age <= 0:
        return ("Please Enter A Valid Date")
    else:
        return ("Please Enter Your Birthdate in YYYY-MM-DD Format")

#_____________________________________________________________

# Sprint 2
# Story Name: Choose Age
# Sprint 2 Task 1: Identify the age of the child
# Sprint 2 Task 2: Identify what age range category diet the child belongs to
# Sprint 2 Task 3: Identify if age of the child is valid

#_____________________________________________________________

def childAge(birthdate):
    dietRange = ""
    today = date.today()
    #birthdate = datetime.fromisoformat(input("Enter Your Birthdate in YYYY-MM-DD Format: "))
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age < 1:
        dietRange = "baby"
        return("Your child is less than a year old \n Reccomended Diet For: Baby")
    elif age < 4 and age >= 1:
        dietRange = "toddler"
        return("Your child is " + str(age) + " years old \n Reccomended Diet For: Toddler")
    elif age < 12 and age >= 4:
        dietRange = "young"
        return ("Your child is " + str(age) + " years old \n Reccomended Diet For: Young Child")
    elif age < 18 and age >= 12:
        dietRange = "teen"
        return("Your child is " + str(age) + " years old \n Reccomended Diet For: Teen")
    elif age >= 18:
        dietRange = "adult"
        return ("Your child is 18 years old or older and should be considered for adult diets")
    else:
        return ("Please Enter Your Birthdate in YYYY-MM-DD Format")



#--------------------------------------
#Testing functions
class Test(unittest.TestCase):
    def test_checkValidUserAge(self):
        print("\n")
        print(checkValidUserAge(date(2000, 10, 10)))
        print(checkValidUserAge(date(2010, 1, 1)))
        print(checkValidUserAge(date(2030, 1, 1)))
        print("\n")
    
    def test_childAge(self):
        print("\n")
        print(childAge(date(2002, 1, 1)))
        print(childAge(date(2008, 1, 1)))
        print(childAge(date(2014, 1, 1)))
        print(childAge(date(2019, 1, 1)))
        print(childAge(date(2022, 1, 1)))
        print("\n")

    def test_checkValidMeal(self):
        self.assertTrue(checkValidMeal('omelette'), 'omelette')
        self.assertFalse(checkValidMeal('123'), '123')
    
    def test_checkValidRecipe(self):
        self.assertTrue(checkValidRecipe(recipesValid))
        with self.assertRaises(ValueError):
            checkValidRecipe(recipesInvalidEmptyCase)
        with self.assertRaises(AttributeError):   
            checkValidRecipe(recipesInvalidNoIngredients)
        with self.assertRaises(TypeError):
            checkValidRecipe(recipesInvalidIngredient)
        
    def test_measurementList(self):
        self.assertFalse(measurementList(recipesValid,'Omelette'), "432")

    def test_validAllergy(self):
        self.assertTrue(validAllergy("fish"), "fish")
        self.assertTrue(validAllergy("soy"), "soy")
        self.assertFalse(validAllergy("555"), "fish")

if __name__ == '__main__':
    unittest.main()

#_______________________________________________________________________________________________

import unittest
#Pratik Kadam contribution
#Story name: Find recipes
#Task 1 : Define the dishes
#Task 2: Define the ingredients of the respective dishes
#Task 3: Ask the user to choose their desired dish

dishes=['chicken','oatmeal','bagel','omlette','breadtoast']
chicken=['salt','pepper','chicken breast']
oatmeal=['oats','milk','berries','nuts','fruits']
bagel=['bagel','creamcheese']
omlette=['eggs','salt','tomato','oregano']
breadtoast=['bread','butter']

def validRecipes():
    while True:
        try:
            print(f"{dishes}")
            x= str(input("Select the dish of your choice: ")) #taking input from user for the choice of dish
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if(x=='chicken'):
                print(f"{chicken}")
                break
            elif(x=='oatmeal'):
                print(f"{oatmeal}")
                break
            elif(x=='bagel'):
                print(f"{bagel}")
                break
            elif(x=='omlette'):
                print(f"{omlette}")
                break
            elif(x=='breadtoast'):
                print(f"{breadtoast}")
                break
            else:
                print('Please enter valid dish')
                continue
    return validRecipes

validRecipes()

class Test(unittest.TestCase):

    def test_ValidRecipes(self):
        self.assertTrue(validRecipes('chicken'), 'chicken')
        self.assertTrue(validRecipes('oatmeal'), 'oatmeal')
        self.assertTrue(validRecipes('bagel'), 'bagel')
        self.assertTrue(validRecipes('omlette'), 'omlette')
        self.assertTrue(validRecipes('breadtoast'), 'breadtoast')
        self.assertFalse(validRecipes('123'), '123')

if __name__=='__main__':
    unittest.main()

#----------------------------------------------------------------------------------------------------------------------------
#Michael Moreno
#Story Name: Nutrition facts

#Task 1: Define the dish
#Task 2: retrieve ingredient list and assign caloric values to ingredients
#Task 3: calculate total calories as sum of ingredients
import unittest

#Sprint 2
#Task 1: display list of recipes instead of asking for input
#Task 2: add more recipes
#Task 3: make sure a valid dish is entered

#define dish
#retrieve ingredient list and assign caloric values to ingredients
#arbitrary values for ingredients
recipe_list = ['oatmeal', 'parfait', 'acai', 'pancakes', 'waffles', 'omelette']

oatmeal = {
    'oats': 100,
    'milk': 500,
    'sugar': 200,
    'strawberries': 150}

parfait = {
    'yogurt': 300,
    'strawberries': 100,
    'blueberries': 150,
    'granola': 100}

acai = {
    'acai puree': 200,
    'bananas': 150,
    'strawberries': 150,
    'blueberries': 150,
    'granola': 100,
    'kiwi': 100
    }

pancakes = {
    'pancakes': 400,
    'syrup': 150,
    'bananas': 100
    }

waffles = {
    'waffles': 400,
    'syrup': 150,
    'sugar': 200,
    'strawberries': 200
    }

omelette = {
    'eggs': 500,
    'tomatoes': 100,
    'ham': 300,
    'salt': 100,
    'pepper': 100,
    }

#calculate calorie total by adding caloric values of ingredients
def CalcCals():
    print(recipe_list)
    while True:
        try:recipe= str(input("Please choose a recipe from the list: "))
        except ValueError:
            print("Please enter a string")
            continue
        else:
            if recipe=='oatmeal':
                print(sum(oatmeal.values()), 'Calories')
                break
            elif recipe=='parfait':
                print(sum(parfait.values()), 'Calories')
                break
            elif recipe=='acai':
                print(sum(acai.values()), 'Calories')
                break
            elif recipe=='pancakes':
                print(sum(pancakes.values()), 'Calories')
                break
            elif recipe=='waffles':
                print(sum(waffles.values()), 'Calories')
                break
            elif recipe=='omelette':
                print(sum(omelette.values()), 'Calories')
                break
            else: print('please enter a valid dish.')
            continue

CalcCals()

class Test(unittest.TestCase):

    def test_CalcCals(self):
        self.assertEqual(CalcCals, 950)
        self.assertEqual(CalcCals, 1000)
        self.assertEqual(CalcCals, 0)
       
if __name__ == '__main__':
    unittest.main()
