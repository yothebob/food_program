from selenium import webdriver
import re

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
website_alt = "https://www.foodnetwork.com/recipes/food-network-kitchen/carbonara-fried-rice-7437183"
website = "https://www.foodnetwork.com/recipes/spinach-tortellini-soup-recipe-1958087"


def start_scrape(times,website_alt):
    if times > 0:
        driver.get(website_alt)
        recipe = driver.find_elements_by_class_name('o-Ingredients__a-Ingredient')
        file = open("recipe_scrape.txt","w")
        for val in recipe:
            file.write(val.text)
        file.write("\n")
        file.close()




        if recipe !=[]:
            for i in recipe:
                print(i.text)
            next_recipe = driver.find_element_by_class_name("o-AssetNavigation__a-Button").click()
            recipe = []
            recipe = driver.find_elements_by_class_name('o-Ingredients__a-Ingredient')
            for i in recipe:
                print(i.text)
            times -= 1
            print(times)
            driver.quit()
            
            


start_scrape(2,website_alt)


driver.quit()# = close browser




