import csv
import requests
from bs4 import BeautifulSoup
from csv import QUOTE_NONE
from csv import writer


response = requests.get('https://www.worldometers.info/coronavirus/#news').content

soup = BeautifulSoup(response,'lxml')

tbody=soup.find('table', id='main_table_countries_today').find('tbody').find_all('tr')[100:110]

replacement_pattern = {
    ",": "",
    "N/A": "0",
    "\n": ""
}

with open('corona1.csv','w') as csv_file:
    csv_writer = writer(csv_file, escapechar=' ', quoting=csv.QUOTE_NONE)
    csv_writer.writerow(['countries','total_cases','total_deaths','total_recovered','active_cases','total_cases_in_1m','deaths_in_1m','population'])



    for value in tbody:
            countries = value.find_all('td')[1].text.replace(",", "").strip()
            total_cases= value.find_all('td')[2].text.replace(",", "").strip()
            total_deaths=value.find_all('td')[4].text.replace(",", "").strip()
            
            total_recovered_raw=value.find_all('td')[6].text
            for _key in [*replacement_pattern]:
                total_recovered_raw.replace(_key, replacement_pattern[_key])
            total_recovered = total_recovered_raw.strip()
            print(total_recovered_raw)
            active_cases=value.find_all('td')[8].text.replace(",", "").strip()
            total_cases_in_1m=value.find_all('td')[10].text.replace(",", "").strip()
            deaths_in_1m=value.find_all('td')[11].text.replace(",", "").strip()
            population=value.find_all('td')[14].text.replace(",", "").strip()


            csv_writer.writerow([countries,total_cases,total_deaths,total_recovered,active_cases,total_cases_in_1m,deaths_in_1m,population])


