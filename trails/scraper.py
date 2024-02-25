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
state_page_dict = database_info.state_dictionary

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
#used to create state dictionary
#for state in states:
#    start_url = f"https://www.trailforks.com/region/{state}/trails/?activitytype=6&difficulty=2,3,4,5,6,8"
#    driver.get(start_url)
#    page_num = driver.find_element("xpath", "//ul[contains(@class, 'paging-middle centertext')]//li[last()]//a")
#    state_page_dict[state] = int(page_num.text)
#


# Each state's trailpark list
# Number of hiking trails per list
# Total distance
# Average difficulty (get by doing a weighted average)
#Start on: https://www.trailforks.com/region/16-acre-forest-58516/?activitytype=6
#Get the link for each park in the tr

#For each link, add "?activitytype=6" to the end
#From park page, get:
#City name at the top
#Trails per difficulty by "region details"
#Total distance in "Hike stats"
#State ranking in "Hike stats"
#Grab coordinates based on first trail



def scrape_basic_stats(basic_vars_dict):
    """
    This function should be called within the `state_scraper` function.
    
    Inputs:
    ``basic_vars_dict``: a dictionary with the relevant variable names as keys and, by default,
    `NA` as values.
    
    On a given trail's website, it will find a `div` element of id `basicTrailStats`.
    This is a table containing information about the trail's length, average time to
    completion, ascent, and descent, if those variables are available.
    The function looks for `div`s of ID `padded10` which contain `col-3` class `div`s.
    The name of each variable is the `text` of the `small.grey` class within each `col-3`.
    The variable's value is stored in the `text` of `div` `large` or `large hovertip`
    
    The function uses conditional statements as not all of the variables are available.
    """
    basic_stats_div = driver.find_element(By.ID, "basicTrailStats")
    
    padded10_divs = basic_stats_div.find_elements(By.CLASS_NAME, "padded10")
    
    for padded10_div in padded10_divs:
        col_3_divs = padded10_div.find_elements(By.CLASS_NAME, "col-3")
        for col_3_div in col_3_divs:
            small_grey_div = col_3_div.find_element(By.CLASS_NAME, "small.grey")
            variable_name = small_grey_div.text
            large_div = col_3_div.find_element(By.CSS_SELECTOR, ".large, .large.hovertip")
            variable_value = large_div.text
            if variable_name in basic_vars_dict:
                basic_vars_dict[variable_name] = variable_value
                
    return basic_vars_dict
                

def scrape_tables(var_list, element_id, var_dict):
    """
    This function is used within `state_scraper` to access `ul`s with variable information.
    
    Inputs:
    ``var_list``: a list ofthe relevant variable names.
    ``element_id``: the `id` of the `ul` in question--there are two which need to be scraped.
    ``var_dict``: a dictionary with the relevant variable names as keys and, by default,
    `NA` as values.
    
    Each `ul` contains `li`s formatted like a dictionary with a `div` of class `term`,
    which stores variable names, and a `div` of class `definition` which stores variable
    values. Both `div`s store the key information in their `text`. Since not all variables
    are needed, we check if they are in ``var_list`` before assigning them to
    ``var_dict``'s values.
    
    """
    li_elements = driver.find_elements("xpath", f"//ul[contains(@id, '{element_id}')]//li")
    for li_element in li_elements:
        term_div = li_element.find_elements(By.CLASS_NAME, "term")
        definition_div = li_element.find_elements(By.CLASS_NAME, "definition")
        for idx, terms in enumerate(term_div):
            if terms.text in var_list:
                var_dict[terms.text] = [definition_div[idx].text]
                
    return var_dict


def get_names_coords(name_coord_dict):
    """
    This function is used within `state_scraper` to access each trail's name and coordinates.
    
    Inputs:
    ``name_coord_dict``: a dictionary with keys `Name` and `Coords`. By default, the values are `NA`
    
    The function grabs the trail's name from a `span` of class `translate` from the top of the page.
    It also grabs the coordinates from a `span` of class `grey2` within a `div` of class
    `margin-bottom-15`. The coordinates are stored in the `span`'s `text`.
    """
    try:
        name_raw = driver.find_element("xpath", "//span[contains(@class, 'translate')][1]")
        name_coord_dict['Name'] = [name_raw.text]
    except:
        name_coord_dict['Name'] = "NA"
    try:
        coord_raw = driver.find_element("xpath", "//div[contains(@class, 'margin-bottom-15 grey')]/span[contains(@class, 'grey2')][2]") #Get coords
        name_coord_dict['Coords'] = coord_raw.text
    except:
        name_coord_dict['Coords'] = "NA"
        
    return name_coord_dict
                
def state_scraper(state_name):
    """
    This is the primary scraping function used inside of `main`.
    
    Inputs:
    ``href_list``: A list of each state's current page's trail urls, compiled by `main`
    ``state_name``: The name of the state in question.
    
    The function iterates through each url in ``href_list`` and using selenium's Chrome
    driver, it gets the `url` and calls the 3 individual scraping function: `scrape_basic_stats`,
    `scrape_tables` (twice--once for trail information and one for trail statistics), and
    `get_names_coords`. Once all of the information is gathered into dictionaries, they are
    combined and added into `trails.db`.
    
    """
    start_url = f"https://www.trailforks.com/region/{state_name}/trails/?activitytype=6&difficulty=2,3,4,5,6,8"
    url_list = [start_url]
    
    for page_num in range(state_page_dict[state_name]):
        url_list.append(start_url + f"&page={page_num+2}")
        
    for page_num in range(state_page_dict[state_name]):
        href_list = []
        driver.get(url_list[page_num])
        green_links = driver.find_elements("xpath","//tr//a[contains(@class, 'green')]")
        
        for green in green_links:
            href = green.get_attribute("href") #Grab URLs--otherwise this doesn't work
            href_list.append(href)
        

        for url in href_list:
            trail_keywords = ["Activities", "Riding Area", "Difficulty Rating", "Local Popularity"]
            stats_keywords = ["Altitude start", "Altitude end", "Grade"]
            basic_vars_dict = {"Distance": ["NA"], "Avg time": ["NA"], "Climb": ["NA"], "Descent": ["NA"]}
            trail_details_vars = {"Activities": ["NA"], "Riding Area": ["NA"], "Difficulty Rating": ["NA"], "Local Popularity": ["NA"]}
            trail_stats_vars = { "Altitude start": ["NA"], "Altitude end": ["NA"], "Grade": ["NA"]}
            name_coord_dict = {'Name': ["NA"],'Coords': ["NA"]}
            print(url)
            driver.get(url)
            basic_vars = scrape_basic_stats(basic_vars_dict)
            trail_stats = scrape_tables(stats_keywords, 'trailstats_display', trail_stats_vars)
            trail_details = scrape_tables(trail_keywords, 'traildetails_display', trail_details_vars)
            names_coords = get_names_coords(name_coord_dict)
    
            database_info.add_trails(pd.DataFrame({**names_coords,**basic_vars, **trail_details, **trail_stats}),state_name)
            
    driver.quit()


state_scraper("Oklahoma")



