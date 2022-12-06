import schedule
import time
import requests
from bs4 import BeautifulSoup
import gc 
import time


# def job(): #scrapes and prints info from the reuters news site


# schedule.every().hour.do(job) #schedules any task, in our case to webscrape, every hour

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()
URL = "https://www.worldometers.info/gdp/gdp-by-country/?fbclid=IwAR3sBdY5PPw5pipLkIqmQ9mmAjpYt3K4oN78IdNHIFQ5tXrnd0MZmBgiyPk"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find(id = 'example2')
# print(table1)
print("--- %s seconds ---" % (time.time() - start_time))
# headers = []
# for i in table1.find_all('th'):
#     title = i.text
#     headers.append(title)
#     print(title)

# print(table1)


