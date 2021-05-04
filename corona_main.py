import requests
from bs4 import BeautifulSoup

URL_world = 'https://www.worldometers.info/coronavirus/'
page_world = requests.get(URL_world)

soup = BeautifulSoup(page_world.content, 'html.parser')

live_death_recover_world = soup.find_all('div', attrs={'id':'maincounter-wrap'})

dict = {}
for i in range(len(live_death_recover_world)):
    dict['text'+str(i+1)] = live_death_recover_world[i].find('div', attrs={'class':'maincounter-number'}).text

total_cases_world = list(dict.values())[0]
total_deaths_world = list(dict.values())[1]
recovered_world = list(dict.values())[2]

while True:
    a = input('Welcome to Corona Tracker.\n').lower()
    print("")

    if a == 'total cases worldwide' or a == "what are the total cases worldwide" or a == "total cases":
        print("Total cases worldwide = "+total_cases_world.strip())
        print("")

    elif a == "total covid death" or a == "total covid deaths" or a == "total deaths" or a == "total death":
        print("Total covid deaths = "+total_deaths_world.strip())
        print("")

    elif a == "total recovered" or a == "total persons recovered":
        print("Total Recovered = "+recovered_world.strip())
        print("")

    elif 'country' in a:
        import re

        txt = a
        x = list(re.split("\s", txt))
        x.reverse()
        country = x[0]
        URL = 'https://www.worldometers.info/coronavirus/country/'+country
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        live_death_recover = soup.find_all('div', attrs={'id':'maincounter-wrap'})

        dict = {}
        for i in range(len(live_death_recover)):
            dict['textcases'+str(i+1)] = live_death_recover[i].find('div', attrs={'class':'maincounter-number'})

        total_cases = list(dict.values())[0]
        total_deaths = list(dict.values())[1]
        recovered = list(dict.values())[2]

        print("Total cases in "+country.capitalize()+" = "+total_cases.text.strip())
        print("")
        print("Total deaths in "+country.capitalize()+" = "+total_deaths.text.strip())
        print("")
        print("Total recovered in "+country.capitalize()+" = "+recovered.text.strip())
        print("")
