import schedule
import time
import requests
from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

def job(): #scrapes and prints info from the reuters news site
    i = 1 
    news = "" 
    r = requests.get("https://www.reuters.com/news/technology") 
    soup = BeautifulSoup(r.text, 'html.parser') 
    result = soup.find_all('h3', attrs = {'class':'story-title'}) 
    
    for new in result: 
        news += ("%s- "%i) 
        news += new.text.strip() 
        news += "\n" 
        i += 1 
    
    print(news) 


schedule.every().hour.do(job) #schedules any task, in our case to webscrape, every hour

while True:
    schedule.run_pending()
    time.sleep(1)