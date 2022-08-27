import requests
import time
from bs4 import BeautifulSoup
import random

# for i in range(2,17):
#     i = int(i)
#     url = (f'/{i}/')

#     headers = { 
#         
#     }
#     req = requests.get(url, headers=headers)
#     src = req.text
#     with open((f"index{i}.html"), "w") as file:
#         file.write(src)

for i in range(1,40):
    with open((f"/Users/sozin/Documents/parser_for_marine_companies_cv_sender/companies/{i}company.html")) as file:
        src = file.read()
    
    soup = BeautifulSoup(src, "lxml")
    company_name = soup.find("h1", class_="title is-1 has-text-weight-bold").text
    company_info = soup.find_all("div", class_="column is-4")
    fleet_info = soup.find("h4", {"id": "типи-судів"})
    if fleet_info:
        fleet_info = fleet_info.next_element.next_element.next_element.find_all("li")
    cadet_program = soup.find("em")
    if cadet_program:
        cadet_program = cadet_program.text
    contact_info = soup.find("div", {"class":"column"}).find_all("a")
    print(company_name)
    
    for item in company_info:
        adress= item.find("span", {"class": "icon is-medium"}).find_next_sibling().find_next_sibling().find_next_sibling().find_next().find_next().text
        print(adress)
    if fleet_info:
        for item in fleet_info:
            print(item.text)
    if cadet_program:             
        print(cadet_program)

    for item in contact_info:
        link = item.get("href")
        if "/"  in link:
            pass
        elif "#" in link:
            pass
        elif "mail" or "@" in link:
            link = link.replace("mailto:", "http://www.")
            print(link)
        else:
            print(link)