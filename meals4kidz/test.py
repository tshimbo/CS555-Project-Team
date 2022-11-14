
import json

weights = {}

with open('weightsFile.json') as f:
    weights = json.load(f)

def addWeight(age, weight):
    weights[age] = weight
    return weights

def clearWeight():
    weights.clear()
    open('weightsFile.json', 'w').close()
    
#print(addWeight(6, 80))
#print(addWeight(7, 90))
#print(addWeight(8, 100))
#clearWeight()
#print(weights)

def displayWeightHistory():
    print("{:<10} {:<10}".format('Age', 'Weight'))
    # print each data item.
    for key, value in weights.items():
        weight = value
        print("{:<10} {:<10}".format(key, weight))

with open('weightsFile.json', 'w') as f:
    json.dump(weights, f)

displayWeightHistory()
