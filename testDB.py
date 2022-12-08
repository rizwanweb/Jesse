from bs4 import BeautifulSoup
import requests
import csv
import db
import mariadb
from time import sleep


MAIN_URL = 'https://www.fatsecret.com'

URL = "https://www.fatsecret.com/calories-nutrition/group/beans-and-legumes"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

main_food_table = soup.find("table", class_='common')

CategoryList = []
SubCategoryList = []
FoodList = []
PortionList = []
try:
    print("Fetching Categories from Database")
    cl = db.getCategory()
    for c in cl:
        CategoryList.append(c[0])
except Exception as e:
    print(e)

try:
    print("Fetching Sub-Categories from Database")
    scl = db.getSubCategory()
    for c in scl:
        SubCategoryList.append(c[0])
except Exception as e:
    print(e)

try:
    print("Fetching Food Names from Database")
    fl = db.getFoodName()
    for c in fl:
        FoodList.append(c[0])
except Exception as e:
    print(e)

try:
    print("Fetching Serving Size from Database")
    pl = db.getPortionName()
    for c in pl:
        PortionList.append(c[0])
except Exception as e:
    print(e)

# sleep(5)


# Get All Main Category names and links
for main_category in main_food_table.find_all('a'):

    main_category_page = requests.get(MAIN_URL+main_category['href'])
    mc_soup = BeautifulSoup(main_category_page.content, 'html.parser')
    title = mc_soup.find("h1", class_="title")
    print('*'*20)
    print(title.text)
    print('*'*20)

    data = [(title.text.strip())]
    if title.text.strip() in CategoryList:
        print(f"{title.text.strip()} Already in Database--Skipping..")
    else:
        db.insertCategory(data)
    CategoryID = db.getCategoryID()
        
    
    sub_category_table = mc_soup.find("div", class_="secHolder")

    for sub_category in sub_category_table.find_all("a"):
        ele = sub_category.find_parent()  # Get names of sub category
        if ele.name == 'h2':
            subCategory = sub_category.text
            if subCategory in SubCategoryList:
                print(f"{subCategory} Already in Database--Skipping..")
            else:
                print(subCategory)            
                scdata = (subCategory, CategoryID[0])
                db.insertSubCategory(scdata)
            SubCategoryID = db.getSubCategoryID()
    
        elif ele.name == 'div':  # Get names and URL of food items
            food_name = sub_category.text
            if food_name in FoodList:
                print(f"{food_name} Already in Database--Skipping..")
            else:                
                fdata = (food_name, SubCategoryID[0])
                db.insertFood(fdata)
                FoodID = db.getFoodID()
                FoodID = FoodID[0]

                food_url = MAIN_URL+sub_category['href']            
                food_page = requests.get(MAIN_URL+sub_category['href'])
                food_soup = BeautifulSoup(food_page.content, 'html.parser')

                detail_table = food_soup.find('td', class_="details")
                all_detail_table = detail_table.find_all('table', class_="generic")
            
                for table in all_detail_table:
                    if len(table['class']) == 1:
                        cols = table.find_all('td', class_="borderBottom")
                        for c in cols:  # Get URL of serving size
                            if len(c['class']) == 1:
                                portion = c.text.strip()
                                purl = c.find('a')['href']
                                serving_url = MAIN_URL+purl                          
                                serving_page = requests.get(serving_url)
                                serving_soup = BeautifulSoup(
                                    serving_page.content, 'html.parser')
                                
                                try:
                                    serving_table = serving_soup.find(
                                        'div', class_="nutrition_facts us")

                                    divs = serving_table.find_all(
                                        'div', class_="nutrient")

                                    # nutriant variables
                                    tf_weight = None 
                                    tf_value = None
                                    sf_weight = None
                                    pf_weight = None
                                    pf_value = None
                                    mf_weight = None
                                    mf_value = None
                                    cholesterol_weight = None
                                    cholesterol_value = None
                                    sodium_weight = None
                                    sodium_value = None
                                    tc_weight = None
                                    tc_value = None
                                    df_weight = None
                                    df_value = None
                                    sugars_weight = None
                                    sugars_value = None
                                    protien_weight = None
                                    protien_value = None
                                    vd_weight = None
                                    vd_value = None
                                    calcium_weight = None
                                    calcium_value = None
                                    iron_weight = None
                                    iron_value = None
                                    potassium_weight = None
                                    potassium_value = None
                                    va_weight = None
                                    va_value = None
                                    vc_weigt = None
                                    vc_value = None
                                    transfat = None

                                    index = 0
                                    calories = serving_soup.find(
                                        'div', class_="hero_value black right").text

                                    for div in divs:
                                        if "% Daily Values*" in div.text:
                                            continue
                                        elif "Amount Per Serving" in div.text:
                                            continue
                                        else:   # Get all the Nutrition weight and values
                                            if index == 2:
                                                tf_weight = div.text.strip()
                                            if index == 3:
                                                tf_value = div.text.strip()
                                            if index == 5:
                                                sf_weight = div.text.strip()
                                            if index == 6:
                                                sf_value = div.text.strip()
                                            if index == 8:
                                                transfat = div.text.strip()
                                            if index == 10:
                                                pf_weight = div.text.strip()
                                            if index == 12:
                                                mf_weight = div.text.strip()
                                            if index == 14:
                                                cholesterol_weight = div.text.strip()
                                            if index == 15:
                                                cholesterol_value = div.text.strip()
                                            if index == 17:
                                                sodium_weight = div.text.strip()
                                            if index == 18:
                                                sodium_value = div.text.strip()
                                            if index == 20:
                                                tc_weight = div.text.strip()
                                            if index == 21:
                                                tc_value = div.text.strip()
                                            if index == 23:
                                                df_weight = div.text.strip()
                                            if index == 24:
                                                df_value = div.text.strip()
                                            if index == 26:
                                                sugars_weight = div.text.strip()
                                            if index == 28:
                                                protien_weight = div.text.strip()
                                            if index == 30:
                                                vd_weight = div.text.strip()
                                            if index == 31:
                                                vd_value = div.text.strip()
                                            if index == 33:
                                                calcium_weight = div.text.strip()
                                            if index == 34:
                                                calcium_value = div.text.strip()
                                            if index == 36:
                                                iron_weight = div.text.strip()
                                            if index == 37:
                                                iron_value = div.text.strip()
                                            if index == 39:
                                                potassium_weight = div.text.strip()
                                            if index == 40:
                                                potassium_value = div.text.strip()
                                            if index == 42:
                                                va_weight = div.text.strip()
                                            if index == 43:
                                                va_value = div.text.strip()
                                            if index == 45:
                                                vc_weigt = div.text.strip()
                                            if index == 46:
                                                vc_value = div.text.strip()
                                            #print(index, div.text.strip())
                                            index += 1
                                    ndata = (
                                        FoodID, portion, calories, tf_weight, tf_value, sf_weight, sf_value, transfat, pf_weight,
                                        mf_weight, cholesterol_weight, cholesterol_value, sodium_weight, sodium_value,
                                        tc_weight, tc_value, df_weight, df_value, sugars_weight, protien_weight, vd_weight, vd_value,
                                        calcium_weight, calcium_value, iron_weight, iron_value, potassium_weight, potassium_value,
                                        va_weight, va_value, vc_weigt, vc_value, purl
                                    )
                                    ntdata = (FoodID, str(portion), calories)
                                    #print(ndata)
                                    if purl in PortionList:
                                        print(f"{portion} Already in Database Skipping")
                                    else:
                                        db.insertPortion(ndata)
                                except Exception as e:
                                    print(str(e))
