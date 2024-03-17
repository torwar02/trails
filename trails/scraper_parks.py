import selenium
import csv
import asyncio
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium import webdriver
import database_info
from contextlib import asynccontextmanager


service = Service()
state_page_dict = database_info.state_parks_dictionary

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
chrome_options.add_argument('--headless')

trail_difficulties = ["Access Road/Trail","White","Green","Blue","Black","Double Black Diamond", "Proline"]

def state_scraper(state_name):
    """
    This function finds relevant information about different parks listed on
    trailforks.com given a specific state in the US. The characteristics are
    scraped using Selenium.
    Inputs:
    `state_name`: name of the state to be scraped
    Outputs:
    None (see below)
    
    The following data are taken from the park's page
    `Name`: The park's name
    `Location`: A nearby city's name
    `Coords`: The coordinates of a trail at the park
    `Trails`: The number of trails at the park
    `Total Distance`: The total distance of all of the hiking trails.
    `State Ranking`: The popularity of the area in the state.
    
    `Access Road/Trail` ... `Proline`: The number of trails corresponding
    to each difficulty level
    
    Once taken from each page, the relevant information is added to the `trails_new.db` SQL database.
    Any information that cannot be found will be entered as `NA`
    """
    start_url = f"https://www.trailforks.com/region/{state_name}/ridingareas/?activitytype=6"
    url_list = [start_url]

    for page_num in range(database_info.state_dictionary[state_name]):
        url_list.append(start_url + f"&page={page_num+2}")

    for page_num in range(state_page_dict[state_name]):
        href_list = []
        driver.get(url_list[page_num])
        green_links = driver.find_elements("xpath","//tr//a[contains(@class, 'green')]")

        for green in green_links:
            href = green.get_attribute("href") #Grab URLs--otherwise this doesn't work
            href_list.append(href+"/?activitytype=6")


        for url in href_list:
            no_name_found = False
            info_dict = {"Name":["NA"], "Location":["NA"], "Coords":["NA"]}
            stats_dict =  {"Trails (view details)":["NA"],"Total Distance":["NA"], "State Ranking":["NA"],}
            trail_difficulty_count = {"Access Road/Trail":0,"White":0,"Green":0,"Blue":0,"Black":0,"Double Black Diamond":0, "Proline":0}
            print(url)
            driver.get(url)
            area_name_raw = driver.find_element("xpath", "//span[contains(@class, 'translate')][1]")
            info_dict["Name"] = area_name_raw.text
            try:
                city_name_raw = driver.find_element(By.CLASS_NAME, "small.grey2.mobile_hide")
                info_dict["Location"] = city_name_raw.text
            except:
                no_name_found = True
                
            stats_items = ["State Ranking", "Total Distance", "Trails (view details)"]
            dict_category = driver.find_elements("xpath", "//dl//dt")
            dict_information = driver.find_elements("xpath", "//dl//dd")
           
            for idx, terms in enumerate(dict_category):
                if terms.text in stats_items:
                    stats_dict[terms.text] = [dict_information[idx].text]
                    
            try:
                difficulty_ul = driver.find_element(By.CLASS_NAME, 'stats.flex.nostyle.inline.clearfix')

                for li in difficulty_ul.find_elements(By.TAG_NAME, 'li'):
                    difficulty_span = li.find_element(By.XPATH, './/span[contains(@class, "stat-label clickable")]/span')
                    difficulty_name = difficulty_span.get_attribute('title')
                    if difficulty_name in trail_difficulty_count.keys():
                        num_trails_span = li.find_element(By.CLASS_NAME, 'stat-num')
                        num_trails = int(num_trails_span.text)
                        trail_difficulty_count[difficulty_name] = num_trails
            except:
                pass
            
            try:
                green_link = driver.find_element("xpath","//tr//a[contains(@class, 'green')]")
                park_link = green_link.get_attribute("href")
                driver.get(park_link)
                print("we've gotten here!")
            except:
                pass
                
            try:
                coord_raw = driver.find_element("xpath", "//div[contains(@class, 'margin-bottom-15 grey')]/span[contains(@class, 'grey2')][2]") #Get coords
                info_dict['Coords'] = [coord_raw.text]
                if no_name_found:
                    city_name_raw = driver.find_element(By.CLASS_NAME, "weather_date bold green")
                    info_dict["Location"] = city_name_raw.text
            except:
                info_dict['Coords'] = ["NA"]

            database_info.add_trails_new(pd.DataFrame({**info_dict,**stats_dict, **trail_difficulty_count}),state_name)


    driver.quit()
    
    
state_scraper("Wyoming")



#states = database_info.state_name_code_name_dict
#state_parks_dict = {}
#
#for code, name in states.items():
#    start_url = f"https://www.trailforks.com/region/{code}/ridingareas/?activitytype=6"
#    driver.get(start_url)
#    page_num = driver.find_element("xpath", "//ul[contains(@class, 'paging-middle centertext')]//li[last()]//a")
#    state_parks_dict[name] = int(page_num.text)
#
#print(state_parks_dict)
