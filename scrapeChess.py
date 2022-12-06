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

gc.set_debug(gc.DEBUG_STATS)

start_time = time.time()
URL = "https://www.chess.com/ratings?fbclid=IwAR11GX5nju9ltyf8Sb7h4rbLUUy2EGF4rPNrTH8FfxIJiRe4LD-yi8U3W0M"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find(class_ = 'table-component')
# print(table1)
print("--- %s seconds ---" % (time.time() - start_time))

