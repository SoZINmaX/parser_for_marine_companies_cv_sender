
import requests
import time
from bs4 import BeautifulSoup
import random
import json
import csv

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
all_data = []
for i in range(1,300):
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
    website_info = soup.find("i", {"class":"far fa-external-link"})
    # print(company_name)
    if company_info:
        for item in company_info:
            adress= item.find("span", {"class": "icon is-medium"}).find_next_sibling().find_next_sibling().find_next_sibling().find_next().find_next().text  
            adress = (adress)         
    else: 
        adress = "\\N"
    fleet_info_list = []
    if fleet_info:
        container_vsl = False
        bulk_vsl = False
        tanker_vsl = False
        gas_vsl = False
        reefer_vsl = False
        ro_ro_vsl = False
        heavy_lift_vsl = False
        passenger_vsl = False
        off_shore_vsl = False
        yachts_vsl = False
        fishing_vsl = False
        tug_vsl = False
        ferry_vsl = False
        for item in fleet_info:
        # #  selects types of ships
            if "container" in (item.text.lower()) or "контейнер" in (item.text.lower()) or "торговий" in (item.text.lower()) or "вантаж" in (item.text.lower()) or "генерал" in (item.text.lower()):
                container_vsl = True
                
            if "bulk" in (item.text.lower()) or "контейнер" in (item.text.lower()) or "торговий" in (item.text.lower()) or "вантаж" in (item.text.lower()) or "генерал" in (item.text.lower()) or "лісовоз" in (item.text.lower()):
                bulk_vsl = True

            if "tanker" in (item.text.lower()) or "танк" in (item.text.lower()) or "хімо" in (item.text.lower()) or "нафто" in (item.text.lower()) or "oil" in (item.text.lower()) or "chemicals" in (item.text.lower()):
                tanker_vsl = True

            if "lng" in (item.text.lower()) or "lpg" in (item.text.lower()) or "gas" in (item.text.lower()) or "газовоз" in (item.text.lower()) or "генерал" in (item.text.lower()):
                gas_vsl = True

            if "reefer" in (item.text.lower()) or "реф" in (item.text.lower()) or "ріф" in (item.text.lower()):
                reefer_vsl = True

            if "ro-ro" in (item.text.lower()) or "-ро" in (item.text.lower()) or "авто" in (item.text.lower()) or "car" in (item.text.lower()) or "vehicle" in (item.text.lower()):
                ro_ro_vsl = True

            if "heavy" in (item.text.lower()) or "великоваг" in (item.text.lower()) or "негаба" in (item.text.lower()):
                heavy_lift_vsl = True

            if "passenger" in (item.text.lower()) or "пасажир" in (item.text.lower()) or "cruiser" in (item.text.lower()) or "круїз" in (item.text.lower()) or "лайнер" in (item.text.lower()):
                passenger_vsl = True

            if "offshore" in (item.text.lower()) or "офф" in (item.text.lower()) or "постачання" in (item.text.lower()) or "багато" in (item.text.lower()) or "поста" in (item.text.lower()) or "платформ" in (item.text.lower()) or "дослід" in (item.text.lower()) or "спец" in (item.text.lower()) or "офшор" in (item.text.lower()):
                off_shore_vsl = True

            if "yacht" in (item.text.lower()) or "яхт" in (item.text.lower()) or "торговий" in (item.text.lower()) or "вантаж" in (item.text.lower()) or "генерал" in (item.text.lower()):
                yachts_vsl = True

            if "fish" in (item.text.lower()) or "рибо" in (item.text.lower()):
                fishing_vsl = True

            if "tug" in (item.text.lower()) or "буксир" in (item.text.lower()):
                tug_vsl = True

            if "ferry" in (item.text.lower()) or "пором" in (item.text.lower()):
                ferry_vsl = True

    else: 
        container_vsl = False
        bulk_vsl = False
        tanker_vsl = False
        gas_vsl = False
        reefer_vsl = False
        ro_ro_vsl = False
        heavy_lift_vsl = False
        passenger_vsl = False
        off_shore_vsl = False
        yachts_vsl = False
        fishing_vsl = False
        tug_vsl = False
        ferry_vsl = False
    if cadet_program:             
        cadet_program = True
    else:cadet_program = False
    if website_info:
        website_info = website_info.find_next().next_element.next_element.get("href")
    else:
        website_info = "\\N"
    mail = ""
    phones = ""
    for item in contact_info:
        link = item.get("href")
        if "/"  in link:
            pass
        elif "#" in link:
            pass
        elif "mail" in link:
            mail += link.replace("mailto:", "")
        else:
            phones += link +", "
    file_loads ={
        "name": company_name,
        "adress": adress,
        "website_info": website_info,
        "e-mail": mail,
        "phone_number": phones,
        "cadet_program": cadet_program,
        "container": container_vsl,
        "bulk": bulk_vsl,
        "tanker": tanker_vsl,
        "gas_carrier": gas_vsl,
        "reefer": reefer_vsl,
        "ro_ro": ro_ro_vsl,
        "heavy_lift" : heavy_lift_vsl,
        "passenger": passenger_vsl,
        "off_shore": off_shore_vsl,
        "yachts": yachts_vsl,
        "fishing": fishing_vsl,
        "tug": tug_vsl,
        "ferry": ferry_vsl
        }
    all_data.append(file_loads)
    csv_columns = ['name','adress', 'website_info', 'e-mail', 'phone_number', 'cadet_program', 'container', 'bulk', 'tanker', 'gas_carrier', 'reefer', 'ro_ro', 'heavy_lift', 'passenger', 'off_shore', 'yachts', 'fishing', 'tug', 'ferry']
    dict_data = all_data
    csv_file = "Companies_not_done.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    print(i)