import schedule
import time
import requests
from bs4 import BeautifulSoup


# def job(): #scrapes and prints info from the reuters news site


# schedule.every().hour.do(job) #schedules any task, in our case to webscrape, every hour

# while True:
#     schedule.run_pending()
#     time.sleep(1)

URL = "https://www.ndbc.noaa.gov/station_page.php?station=46054"
page = requests.get(URL)
print(page)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find('table',class_ = 'dataTable')
headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
    print(title)

