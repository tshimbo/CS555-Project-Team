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


# unit test cases
class Test(unittest.TestCase):

    def test_validAllergy(self):
        self.assertTrue(validAllergy("fish"), "fish")
        self.assertTrue(validAllergy("soy"), "soy")
        self.assertFalse(validAllergy("555"), "fish")


if __name__ == '__main__':
    unittest.main()
