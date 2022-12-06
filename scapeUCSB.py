import schedule
import time
import requests
from bs4 import BeautifulSoup
import gc

# def job(): #scrapes and prints info from the reuters news site


# schedule.every().hour.do(job) #schedules any task, in our case to webscrape, every hour

# while True:
#     schedule.run_pending()
#     time.sleep(1)
gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()
URL = "https://cs.ucsb.edu/education/courses/course-descriptions"
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find(class_ = 'table-responsive')
print("--- %s seconds ---" % (time.time() - start_time))
# print(table1)
# headers = []
# for i in table1.find_all('th'):
#     title = i.text
#     headers.append(title)
#     print(title)

# print(table1)

