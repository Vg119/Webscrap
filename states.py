from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/stores")
# driver.implicitly_wait(0.5)

grid = driver.find_element(By.ID, "storeListingBase")
links = grid.find_elements(By.TAG_NAME, "a")

ans = []

for link in links :
    ans.append (link.get_attribute("href"))
    # d = webdriver.Chrome()
    # d.get (link.get_attribute("href"))
    # g = driver.find_element(By.ID, "storeListingState")
    # ls = g.find_elements(By.TAG_NAME, "a")
    # for l in ls :
    #     print (l.get_attribute("href"))
    # d.quit()

answer = []

for i in ans :
    driver.get(i)
    g = driver.find_element(By.ID, "storeListingState")
    ls = g.find_elements(By.TAG_NAME, "a")
    for l in ls :
        answer.append(l.get_attribute("href"))
        # print (l.get_attribute("href"))
    # print (i)
    driver.back()

for i in answer :
    print (i)

driver.quit()