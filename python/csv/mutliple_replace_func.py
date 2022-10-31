import csv
from tokenize import Octnumber
import requests
from bs4 import BeautifulSoup
from csv import QUOTE_NONE
from csv import writer


response = requests.get('https://www.worldometers.info/coronavirus/#news').content

soup = BeautifulSoup(response,'lxml')

tbody=soup.find('table', id='main_table_countries_today').find('tbody').find_all('tr')[100:110]

replacement = {
    ",": "",
    "N/A": "0",
    "\n": "",
    " ": ""
}

def cleanup(webcontent, indecies):
    out = []
    for index in indecies:
        content = webcontent.find_all('td')[index].text
        for k in [*replacement]:
            content = content.replace(k,replacement[k])
        out.append(content)
    return out
     
with open('corona1.csv','w') as csv_file:
    csv_writer = writer(csv_file, escapechar=' ', quoting=csv.QUOTE_NONE)
    csv_writer.writerow(['countries','total_cases','total_deaths','total_recovered','active_cases','total_cases_in_1m','deaths_in_1m','population'])

    for value in tbody:
        csv_writer.writerow(cleanup(value, [1,2,4,6,8,10,11,14]))
        

