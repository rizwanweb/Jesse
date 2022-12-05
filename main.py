from bs4 import BeautifulSoup
import requests

MAIN_URL = 'https://www.fatsecret.com'

URL = "https://www.fatsecret.com/calories-nutrition/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

main_food_table = soup.find("table", class_='generic common')

main_category = main_food_table.find_all('td')  # Getting main Category
count = 1
for td in main_category:  # Loop through main Categories to get their name and URLs
    category = td.find("a", class_="prominent", href=True)
    # print(category.text.strip())
    # print('https://www.fatsecret.com'+ category['href'])
    category_name = category.text.upper().strip()
    print('*'*20)
    print(category_name)
    print('*'*20)

    # get each url and loop through their pages
    cat_page = requests.get(MAIN_URL + category['href'])
    cat_soup = BeautifulSoup(cat_page.content, 'html.parser')

    holder = cat_soup.find('div', class_="secHolder")
    hr = cat_soup.find_all('hr')

    # for h in holder.select("h2"):  # GET ALL THE SUB CATEGORIES

    for link in holder.find_all('a'):
        p = link.find_parent()
        if p.name == 'h2':  # H2 heading for sub categories
            sub_category_name = link.text.upper()
            print("     ", sub_category_name)
        else:
            # links for foods in the sub category
            food_name = link.text.strip()
            print("")
            print("          ", food_name, "-----", MAIN_URL+link['href'])
            print("")
            food_url = requests.get(MAIN_URL+link['href'])
            food_soup = BeautifulSoup(food_url.content, 'html.parser')

            mid_panel = food_soup.find('td', class_="details")

            serving_table = mid_panel.find_all('table', class_="generic")

            for p in serving_table:
                if len(p['class']) == 1:
                    a = p.find_all('td', class_="borderBottom")
                    for t in a:
                        if len(t['class']) == 1:
                            s_link = t.find_all('a', href=True)
                            for link in s_link:
                                print(link.text, link['href'])

                            break

        if "view more" in link.text:
            continue
            # link to find more info
            print("Will go to Extra page for this shit")
