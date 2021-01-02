import re
import importlib
importlib.import_module("ingredients")


flavor_profile = ['sweet','sour','salt','bitter','acidic','basic','savory','hotness','spiciness','oily','minty'
,'astringent','starchiness','horseradish','creamy']

ingredient_index = importlib.import_module("ingredients").ingredient_index

def food_to_vec(_food):
    ingredient = []
    vectors = []
    amount = []
    total_ingredients = []
    measurements = []
    total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    file = open(_food,"r")
    for line in file:
        i = re.findall(r"\d*.?\d+\scup|\d*.?\d+\steaspoon|\d*.?\d+\stablespoon|\d*.?\d+\spound",line)
        i = re.findall(r"\d",str(i))
        res = [int(sub.split('.')[0]) for sub in i]
        i = str(res)
        i = i.replace("[","")
        i = i.replace("]","")
        if i == "":
            amount.append(1)
        else:
            amount.append(int(i))
            
        for key in ingredient_index:
            if key in line:
                ingredient.append(key)
    
    for ran in range(len(amount)):
        res = [total_ingredients.append(ingredient[ran]) for i in range(amount[ran])]
        
    for key in total_ingredients:
        vectors.append(ingredient_index[key])

    for i in vectors:
        for j in range(len(i)):
            total[j] += i[j]
            
    for num in range(len(total)):
        total[num] = round(total[num]/(len(total_ingredients)+1),8) * 10
           
    print(total_ingredients)
    print("amount of ingredients...")
    print(amount)
    print("ingredients...")
    print(ingredient)
    for i in range(len(total)):
        print(flavor_profile[i] + ": " + str(total[i]))
    file.close()
     
food_to_vec("food2.txt")
