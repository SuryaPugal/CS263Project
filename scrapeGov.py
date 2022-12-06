import schedule
import time
import requests
from bs4 import BeautifulSoup
import gc 
import time


gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()
URL = "https://history.house.gov/Institution/Majority-Changes/Majority-Changes/?fbclid=IwAR3sFlOzHsJkgAIN7M4Qw6VyCXCdMBY8TnfXE3GQndhSBGPQqvymmjZTc10"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find(class_ = 'manual-table manual-table-sortable')
# print(table1)
print("--- %s seconds ---" % (time.time() - start_time))
