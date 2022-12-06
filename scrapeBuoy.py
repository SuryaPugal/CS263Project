import schedule
import time
import requests
from bs4 import BeautifulSoup
import gc 
import time



gc.set_debug(gc.DEBUG_STATS)

start_time = time.time()
URL = "https://www.ndbc.noaa.gov/station_page.php?station=46054"
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find('table',class_ = 'dataTable')
print("--- %s seconds ---" % (time.time() - start_time))


print(gc.get_stats())



# headers = []
# for i in table1.find_all('th'):
#     title = i.text
#     headers.append(title)
#     print(title)

# print(table1)


# df = pandas.read_csv("data.csv")
# X = df[['WVHT', 'DPD','MWD','WDIR','WSPD']]
# y = df['surf']

# regr = linear_model.LinearRegression()
# regr.fit(X, y)
# predictedSurf = regr.predict([[live WVHT, live DPD,live MWD,live WDIR,live WSPD]]) #get live data from webscraping

# print(predictedSurf)