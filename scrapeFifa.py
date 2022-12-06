import schedule
import time
import requests
from bs4 import BeautifulSoup
import gc 
import time

gc.set_debug(gc.DEBUG_STATS)
start_time = time.time()
URL = "https://olympics.com/en/news/fifa-world-cup-2022-results-scores-football?fbclid=IwAR0Sa3oVPFcRUpffHocfOrjWqdoV7RoJfaGZqNRrnaqOJKOBpzocdMTcJv4"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find_all(class_ = 'TableBasicstyles__Table-sc-1btx7es-1 bROVGk')
# print(table1)
print("--- %s seconds ---" % (time.time() - start_time))


