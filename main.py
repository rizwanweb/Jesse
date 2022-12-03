from bs4 import BeautifulSoup
import requests

URL = "https://www.fatsecret.com/calories-nutrition/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

main_food_table = soup.find("table", class_='generic common')

food_category = main_food_table.find_all('td') # Getting main Category

for td in food_category: # Loop through main Categories to get their name and URLs
    category = td.find("a", class_="prominent", href=True)
    # print(category.text.strip())
    # print('https://www.fatsecret.com'+ category['href'])
    # print()

    # get each url and loop through their pages
    cat_page = requests.get('https://www.fatsecret.com'+ category['href'])
    cat_soup = BeautifulSoup(cat_page.content, 'html.parser')

    holder = cat_soup.find('div', class_="secHolder")

    for h in holder.find_all("a", href=True):
        print(f"{h.text}---{h['href']}")