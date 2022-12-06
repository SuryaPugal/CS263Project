#https://en.tutiempo.net/climate/06-2022/ws-723925.html
import schedule
import time
import requests
import gc
from bs4 import BeautifulSoup


# def job(): #scrapes and prints info from the reuters news site


# schedule.every().hour.do(job) #schedules any task, in our case to webscrape, every hour

# while True:
#     schedule.run_pending()
#     time.sleep(1)


gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()

URL = "https://www.billboard.com/charts/hot-100/"
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find(class_ = 'chart-results-list')
print("--- %s seconds ---" % (time.time() - start_time))
print(gc.get_stats())
# print(table1)
# headers = []
# for i in table1.find_all('th'):
#     title = i.text
#     headers.append(title)
#     print(title)

# print(table1)

