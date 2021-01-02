import re


ingredients = {"vinegar":[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
"oil":[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
"flour":[0,0,0,0,0,.2,0,0,0,0,0,0,.75,0,.05],
"soy sauce":[0,0,1,0,0,0,.5,0,0,0,0,0,0,0,0],
"onion":[.2,0,0,0,.1,0,.2,0,.1,0,0,.1,.1,.5,0],
"garlic":[0,0,0,.1,0,0,.4,0,.1,0,0,.1,0,.5,0],
"salt":[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
"black pepper": [0,0,0,0,0,0,0,0,.7,0,0,0,0,0,0],
"jalapeno": [0,0,0,0,0,0,0,.5,0,0,0,0,0,0,0],
"bell pepper":[.1,0,0,0,.1,0,.2,0,0,0,0,0,0,0,0],
"sugar":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"fish":[0,0,0,0,0,0,.6,0,0,.2,0,0,0,0,0],
"beef":[0,0,0,0,0,0,.8,0,0,.5,0,0,0,0,0],
"tomatoes":[.2,0,0,0,.5,0,.3,0,0,0,0,.1,0,0,0],
"milk": [0,0,0,0,0,.5,0,0,0,0,0,0,0,0,.5],
"lemon":[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
"nut":[.1,0,.1,.05,0,.15,.3,0,0,.3,0,.1,.4,0,.2],
"butter":[0,0,.1,0,0,.25,.25,0,0,1,0,0,0,0,.75],
"cream":[0,0,0,0,0,.75,0,0,0,0,0,0,0,0,1],
"mint":[0,0,0,0,0,0,0,0,0,.1,1,0,0,0,0],
"cheese":[0,0,.2,0,0,.3,.6,0,0,.1,0,0,0,0,.75],
"pickle":[0,.5,.5,0,1,0,.8,0,.5,0,0,0,0,.25,0],
"mushroom":[0,0,0,0,0,.2,.8,0,.1,.1,0,0,.1,0,.1],
"mustard":[0,.2,0,0,.75,0,.5,0,.5,0,0,0,0,1,0],
"bacon":[0,0,.8,0,0,0,1,0,0,.8,0,0,0,0,0],
"noodle":[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
"potato": [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
"seed": [0,0,0,0,0,0,.2,0,0,.1,0,0,.2,0,0],
"lime":[0,1,0,.2,1,0,0,0,0,0,0,0,0,0,0],
"rice":[0,0,0,0,0,0,.1,0,0,0,0,0,1,0,0],
"yogurt":[0,.1,0,0,0,.3,0,0,0,0,0,.1,0,0,.8],
"ginger":[.1,0,0,0,.2,0,0,0,.7,0,0,.2,0,.8,0],
"honey":[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"scallion":[0,0,0,.1,0,0,.2,0,.1,0,0,.1,0,.3,0],
"carrot":[.25,0,0,0,0,0,.1,0,0,0,0,0,.2,0,0],
"chicken":[0,0,0,0,0,0,.4,0,0,.1,0,0,0,0,0],
"squash":[.15,0,0,0,0,.1,.3,0,0,0,0,0,.4,0,.1],
"cinnamon":[.3,0,0,.05,0,0,0,.05,.8,0,0,.1,0,0,0],
"broccoli":[0,0,0,.25,0,.1,.08,0,0,0,0,.2,.3,0,0]
}


def food_to_vec(_food):
    ing_used = []
    vectors = []
    amount = []
    total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    file = open(_food,"r")
    for line in file:
        i = re.findall(r"\d*.?\d+\scup|\d*.?\d+\steaspoon|\d*.?\d+\stablespoon|\d*.?\d+\spound",line)
        i = re.findall(r"\d",str(i))
        res = [int(sub.split('.')[0]) for sub in i]
        i = str(res)
        i = i.replace("[","")
        i = i.replace("]","")
        if i == '':
            i = 1
        if i != []:
            amount.append(int(i))
        else:
            amount.append(1)
        for key in ingredients:
            if key in line:
                ing_used.append(key)
    for values in ing_used:
        vectors.append(ingredients[values])
        for i in vectors:
            for j in range(len(i)):
                total[j] += i[j]
    for num in range(len(total)):
        total[num] = round(total[num]/(len(ing_used)+1),8)
    print("amount of ingredients...")
    print(amount)
    print("ingredients...")
    print(ing_used)
    print("flavor profile...")
    print(total)
    file.close()
     
food_to_vec("food2.txt")
