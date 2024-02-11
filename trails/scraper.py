import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from selenium import webdriver
import database_info


service = Service()
state_page_dict = database_info.state_dictionary

# You can use any other WebDriver like Firefox or Edge
chrome_options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
            "profile.managed_default_content_settings.javascript": 2
        }
    )
driver = webdriver.Chrome(
        service=service,
        options=options
    )
chrome_options.add_argument('--no-sandbox')
#used to create state dictionary
#for state in states:
#    start_url = f"https://www.trailforks.com/region/{state}/trails/?activitytype=6&difficulty=2,3,4,5,6,8"
#    driver.get(start_url)
#    page_num = driver.find_element("xpath", "//ul[contains(@class, 'paging-middle centertext')]//li[last()]//a")
#    state_page_dict[state] = int(page_num.text)
#
#print(state_page_dict)

def state_scraper(state_name):
    start_url = f"https://www.trailforks.com/region/{state_name}/trails/?activitytype=6&difficulty=2,3,4,5,6,8"
    url_list = [start_url]
    for page_num in range(state_page_dict[state_name]):
        url_list.append(start_url + f"&page={page_num+2}")
    for page_num in range(state_page_dict[state_name]):
        trail_frame = pd.DataFrame({'Name':['name_test'], 'Coords':['coord_test']})
        driver.get(url_list[page_num])
        green_links = driver.find_elements("xpath","//tr//a[contains(@class, 'green')]")
        href_list = []
        name_list = []
        coords_list = []
        for green in green_links:
            href = green.get_attribute("href") #Grab URLs--otherwise this doesn't work
            href_list.append(href)
        print(href_list)
        for url in href_list:
            driver.get(url) #Got o trail page
            try:
                name_raw = driver.find_element("xpath", "//span[contains(@class, 'translate')][1]") #Get name
                name = name_raw.text
            except:
                name = "NA"
            try:
                coord_raw = driver.find_element("xpath", "//div[contains(@class, 'margin-bottom-15 grey')]/span[contains(@class, 'grey2')][2]") #Get coords
                coord = coord_raw.text
            except:
                coord = "NA"
            print(name,coord)
            trail_frame = pd.concat([trail_frame,pd.DataFrame({'Name':[name], 'Coords': [coord]})], ignore_index = True)
        database_info.add_trails(trail_frame,state_name)
        time.sleep(10)
        
        
state_scraper("Hawaii")
    
driver.quit()



