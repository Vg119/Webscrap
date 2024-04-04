# import requests
# from bs4 import BeautifulSoup

# url = "https://www.lenskart.com/stores/location/bareilly"
# r = requests.get(url);

# soup = BeautifulSoup(r.content, 'html.parser')

# links = soup.find_all('a', class_="StoreCard_name__mrTXJ")
# for link in links :
#     print (link)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/stores/location/bengaluru")
# driver.implicitly_wait(0.5)

links = driver.find_elements(By.CLASS_NAME, "StoreCard_name__mrTXJ")

for link in links :
    print (link.get_attribute("href"))

driver.quit()
