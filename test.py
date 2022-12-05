from bs4 import BeautifulSoup
import requests
import csv

MAIN_URL = 'https://www.fatsecret.com'

URL = "https://www.fatsecret.com/calories-nutrition/group/beans-and-legumes"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

main_food_table = soup.find("table", class_='common')

# Get All Main Category names and links
for main_category in main_food_table.find_all('a'):

    main_category_page = requests.get(MAIN_URL+main_category['href'])
    mc_soup = BeautifulSoup(main_category_page.content, 'html.parser')
    title = mc_soup.find("h1", class_="title")
    print('*'*20)
    print(title.text)
    print('*'*20)
    with open('Main-Category.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        data = [title.text.strip()]
        writer.writerow(data)
        print(f"{title.text.strip()} added to Main Category Table")

    sub_category_table = mc_soup.find("div", class_="secHolder")

    for sub_category in sub_category_table.find_all("a"):
        ele = sub_category.find_parent()  # Get names of sub category
        if ele.name == 'h2':
            #print("     " + sub_category.text)
            with open('Sub-Category.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                data = [sub_category.text, title.text]
                writer.writerow(data)
                print(f"{sub_category.text} added to Sub-Category Table")
        elif ele.name == 'div':  # Get names and URL of food items
            food_name = sub_category.text
            with open('foods.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                data = [food_name, sub_category.text, title.text]
                writer.writerow(data)
                print(f"{food_name} added to food Table")
            food_url = MAIN_URL+sub_category['href']
            #print("          " + food_name + "---" + food_url)
            food_page = requests.get(MAIN_URL+sub_category['href'])
            food_soup = BeautifulSoup(food_page.content, 'html.parser')

            detail_table = food_soup.find('td', class_="details")
            all_detail_table = detail_table.find_all('table', class_="generic")
            #print("          "+food_name)
            for table in all_detail_table:
                if len(table['class']) == 1:
                    cols = table.find_all('td', class_="borderBottom")
                    for c in cols:  # Get URL of serving size
                        if len(c['class']) == 1:
                            serving_size = c.text.strip()
                            serving_url = MAIN_URL+c.find('a')['href']
                            #print("               "+serving_size)

                            serving_page = requests.get(serving_url)
                            serving_soup = BeautifulSoup(
                                serving_page.content, 'html.parser')

                            serving_table = serving_soup.find(
                                'div', class_="nutrition_facts us")

                            divs = serving_table.find_all(
                                'div', class_="nutrient")

                            # nutriant variables
                            tf_weight = ""
                            tf_value = ""
                            sf_weight = ""
                            pf_weight = ""
                            pf_value = ""
                            mf_weight = ""
                            mf_value = ""
                            cholesterol_weight = ""
                            cholesterol_value = ""
                            sodium_weight = ""
                            sodium_value = ""
                            tc_weight = ""
                            tc_value = ""
                            df_weight = ""
                            df_value = ""
                            sugars_weight = ""
                            sugars_value = ""
                            protien_weight = ""
                            protien_value = ""
                            vd_weight = ""
                            vd_value = ""
                            calcium_weight = ""
                            calcium_value = ""
                            iron_weight = ""
                            iron_value = ""
                            potassium_weight = ""
                            potassium_value = ""
                            va_weight = ""
                            va_value = ""
                            vc_weigt = ""
                            vc_value = ""

                            index = 0
                            with open('nutrition.csv', 'a', newline='') as f:
                                writer = csv.writer(f)
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
                                        if index == 10:
                                            pf_weight = div.text.strip()
                                        # if index == 10:
                                        #     pf_value = div.text.strip()
                                        if index == 12:
                                            mf_weight = div.text.strip()
                                        if index == 13:
                                            mf_value = div.text.strip()
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
                                data = [
                                    food_name, serving_size, calories, tf_weight, tf_value, sf_weight, sf_value, pf_weight, pf_value,
                                    mf_weight, mf_value, cholesterol_weight, cholesterol_value, sodium_weight, sodium_value,
                                    tc_weight, tc_value, df_weight, df_value, sugars_weight, protien_weight, vd_weight, vd_value,
                                    calcium_weight, calcium_value, iron_weight, iron_value, potassium_weight, potassium_value,
                                    va_weight, va_value, vc_weigt, vc_value
                                ]
                                writer.writerow(data)
                                print(
                                    f"{food_name} Nutritians added to database")
