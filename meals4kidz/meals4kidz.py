import unittest
#Terry Shim Contribution
#Story Name:  View measurements
#Task 1: Get measurements of recipe of a specific meal
#Task 2: Print measurements of recipe
#Task 3: Recipe meal cannot be a number

#-------------------------------------------------------------------------------

#Example dictionaries for testing purposes

recipesValid = {
        'Rice paper wraps': '1 carrot, 1 avocado, 1/2 cucumber, 8 mint leaves, 50g rice vermicelli noodles',
        'Spinach savoury muffins': '200g fresh spinach, 100g cheddar, 1 tbsp dried thyme, 2 eggs',
        'Omelette': '1 knob of butter, 1 tomato deseeded and diced, 1 tsp dried oregano',
    }

testRecipe = {
        'Rice paper wraps': '1 carrot'
}


#----------------------------------------------------------------------------------------------------


def checkValidMeal(meal): #checking that a meal cannot be a number
    if meal.isnumeric():
        return False
    else:
        return True

def measurementList(recipes, meal): #parse through a dictionary of recipes in order to find the measurements of the ingredients
    try:
        # Iterating over values
        assert checkValidMeal(meal) == True   #error checking
        print('Measurements of: ' + str(meal) + '\n') #specify which meal you are taking from
        for meal, ingredient in recipes.items():   #iterate through the recipes to find the correct one 
           
            
            return print(ingredient)     #print only the measurement list
    except:
        raise Exception("Meal cannot be a number!")   #error if the meal is a number
        

#------------------------------------------------------------------------------------------


#############################################################
# Ryan Lee Contribution
# Story Name: Allergies
# Task 1: Ask user if child has allergies
# Task 2: Ask user to input child's allergy
# Task 3: Check if child's allergy is a valid
##############################################################
import unittest

commonAllergies = ['dairy', 'fish', 'shellfish',
                   'tree nuts', 'peanuts', 'wheat', 'soy']


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


# check if allergy is valid
def validAllergy(allergy):
    valid = True
    if (allergy not in commonAllergies):
        print("This is not a valid allergy")
        valid = False
    return valid


#_____________________________________________________________

# Maksym Perozhak Contribution

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



#--------------------------------------
#Testing functions
class Test(unittest.TestCase):
    def test_checkValidUserAge(self):
        print("\n")
        print(checkValidUserAge(date(2000, 10, 10)))
        print(checkValidUserAge(date(2010, 1, 1)))
        print(checkValidUserAge(date(2030, 1, 1)))
        print("\n")

    def test_checkValidMeal(self):
        self.assertTrue(checkValidMeal('omelette'), 'omelette')
        self.assertFalse(checkValidMeal('123'), '123')

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