#!/usr/bin/python3

import subprocess
import csv
import json

# subprocess.run(['docker exec -it 26530f40fefdecc276a93741592c14dfba4596d54afae73a731db67c7f7cfc11 /bin/sh'] , shell = True)

# subprocess.run(['psql -h localhost -p 5432 -U postgres -d djangodb_marinecv'] , shell = True)

# subprocess.run(['\d cvsender_company', 'SELECT * FROM cvsender_company;'] , shell = True)
    
dict_from_csv = {}

def return_bool(x):
    y = json.loads(x.lower())
    return y 

def remoove_nbsp(x:str):
    z = x.replace(u'\xa0', u' ')
    return z

with open('Companies_not_done.csv', mode='r') as inp:
    with open('Test.sql', 'w') as file:
        reader = csv.reader(inp)
        counter = 0
        for rows in reader:
            
            dict_from_csv = {'name':rows[0], 'adress':remoove_nbsp(rows[1]), 'website_info':rows[2], 'email':rows[3], 'phone_number':rows[4], 'cadet_program':return_bool(rows[5]), 'container':return_bool(rows[6]), 'bulk':return_bool(rows[7]), 'tanker':return_bool(rows[8]), 'gas_carrier':return_bool(rows[9]), 'reefer':return_bool(rows[10]), 'ro_ro':return_bool(rows[11]), 'heavy_lift':return_bool(rows[12]), 'passenger':return_bool(rows[13]), 'off_shore':return_bool(rows[14]), 'yachts':return_bool(rows[15]), 'fishing':return_bool(rows[16]), 'tug':return_bool(rows[17]), 'ferry':return_bool(rows[18])}
            
            counter +=1
            
            load_data = f"INSERT INTO cvsender_company (name, adress, website_info, email, phone_number, cadet_program, container, bulk, tanker, gas_carrier, reefer, ro_ro, heavy_lift, passenger, off_shore, yachts, fishing, tug, ferry) VALUES ('{dict_from_csv.get('name')}', '{dict_from_csv.get('adress')}', '{dict_from_csv.get('website_info')}', '{dict_from_csv.get('email')}', '{dict_from_csv.get('phone_number')}', {dict_from_csv.get('cadet_program')}, {dict_from_csv.get('container')}, {dict_from_csv.get('bulk')}, {dict_from_csv.get('tanker')}, {dict_from_csv.get('gas_carrier')}, {dict_from_csv.get('reefer')}, {dict_from_csv.get('ro_ro')}, {dict_from_csv.get('heavy_lift')}, {dict_from_csv.get('passenger')}, {dict_from_csv.get('off_shore')}, {dict_from_csv.get('yachts')}, {dict_from_csv.get('fishing')}, {dict_from_csv.get('tug')}, {dict_from_csv.get('ferry')});\n"
            
            file.write(load_data)
            print(rows)
# load_data = subprocess.run(["INSERT INTO cvsender_company (name, adress, website_info, email, phone_number, cadet_program, container, bulk, tanker, gas_carrier, reefer, ro_ro, heavy_lift, passenger, off_shore, yachts, fishing, tug, ferry) VALUES ('name', 'adress', 'http://a1lbs.com?utm_source=ukrcrewing.com&utm_medium=link&utm_campaign=crewing_page', 'email@mail.com', 'phone_number', True, True, True, True, True, True, True, True, True, True, True, True, True, True);"] , shell = True)
