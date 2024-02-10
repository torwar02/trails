import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd


from selenium import webdriver

driver = webdriver.Chrome()  # You can use any other WebDriver like Firefox or Edge


page_nums = 151
start_url = "https://www.trailforks.com/region/california/trails/?activitytype=6&difficulty=2,3,4,5,6,8"
url_list = [start_url]
for i in range(page_nums):
    url_list.append(start_url + f"&page={i+2}") #Generates all 152 pages for California


for i in range(page_nums): #For each page
    driver.get(url_list[i]) #Navigate to page
    green_links = driver.find_elements("xpath","//tr//a[contains(@class, 'green')]") #Find trail links
    href_list = []
    name_list = []
    coords_list = []
    for green in green_links:
        href = green.get_attribute("href") #Grab URLs--otherwise this doesn't work
        href_list.append(href)
    print(href_list)
    for url in href_list:
        driver.get(url) #Got o trail page
        name_raw = driver.find_element("xpath", "//span[contains(@class, 'translate')][1]") #Get name
        name = name_raw.text
        name_list.append(name)
        coord_raw = driver.find_element("xpath", "//div[contains(@class, 'margin-bottom-15 grey')]/span[contains(@class, 'grey2')][2]") #Get coords
        coord = coord_raw.text
        coords_list.append(coord)
        print(name,coord)
    trail_frame = pd.DataFrame({'Name':name_list, 'Coords':coords_list})
    trail_frame.to_csv('trails.csv', index = False) #Put coords into csv


driver.quit()



