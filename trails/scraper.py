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


trail_keywords = ["Activities", "Riding Area", "Difficulty Rating", "Local Popularity"]
stats_keywords = ["Altitude start", "Altitude end", "Grade"]



def scrape_basic_stats(url, basic_vars_dict):
    driver.get(url)
    
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





def scrape_trail_details_variables(url, trail_details_vars):
    driver.get(url)
    
    li_elements = driver.find_elements("xpath", "//ul[contains(@id, 'traildetails_display')]/li")
    element_dict = {}
    for li_element in li_elements:
        definition_div = li_element.find_elements(By.CLASS_NAME, "definition")
        term_div = li_element.find_elements(By.CLASS_NAME, "term")
        
        for idx, val in enumerate(definition_div):
            element_dict[term_div[idx].text] = val.text
        
    print(element_dict)
    
    return element_dict

#        tag_names = set()
#
##  Loop through each element and grab its tag name
#        for li_element in li_elements:
#            child_elements = li_element.find_elements("xpath",".//*")
#
#            for child_element in child_elements:
#                class_name = child_element.get_attribute("class")
#                id_name = child_element.get_attribute("id")
#                tag_names.add("TAG: " +child_element.tag_name)
#                tag_names.add("CLASS: "+class_name)
#                tag_names.add("ID: "+id_name)
#
#        print(tag_names)
        
      
       
       
        #variable_value = definition_div.text
        #variable_name = term_div.text
        #print(variable_value, variable_name)
        #for present_vars in variable_name:
        #    if variable_name in trail_stats_vars:
        #        trail_stats_vars[variable_name] = variable_value
        
       
        
#        if variable_name in trail_details_vars:
#            if variable_name == "Activities":
#                activities_list = variable_value.split("\n")
#                activities_list = [activity.split()[-1] for activity in activities_list]
#                trail_details_vars[variable_name] = activities_list
#            elif variable_name == "Local Popularity":
#                popularity_value = definition_div.find_element("xpath", "//span[contains(@class, 'badgesquare')]").text
#                trail_details_vars[variable_name] = popularity_value
                

def scrape_trail_stats_variables(url,trail_stats_vars):
    driver.get(url)
    
    li_elements = driver.find_elements("xpath", "//ul[contains(@id, 'trailstats_display')]//li")
    
    element_dict = {}
    for li_element in li_elements:
        definition_div = li_element.find_elements(By.CLASS_NAME, "definition")
        term_div = li_element.find_elements(By.CLASS_NAME, "term")
        
        for idx, val in enumerate(definition_div):
            element_dict[term_div[idx].text] = val.text
        
    return element_dict
        
        #for present_vars in variable_name:
        #    if variable_name in trail_stats_vars:
        #        trail_stats_vars[variable_name] = variable_value


def scrape_tables(var_list, element_id, var_dict):
    li_elements = driver.find_elements("xpath", f"//ul[contains(@id, '{element_id}')]//li")
    element_dict = {}
    for li_element in li_elements:
        term_div = li_element.find_elements(By.CLASS_NAME, "term")
        definition_div = li_element.find_elements(By.CLASS_NAME, "definition")
        for idx, terms in enumerate(term_div):
            if terms.text in var_list:
                var_dict[terms.text] = [definition_div[idx].text]
        
        
        #for idx, val in enumerate(term_div):
        #    print(val.text, "THIS IS VAL TEXT\n")
        #    print(definition_div[idx].text, "THIS IS DEF DIV TEXT\n")
        #    if val.text in var_list:
        #        var_dict[val] = [definition_div[idx].text]
                
    return var_dict

def state_scraper(state_name):
    
    start_url = f"https://www.trailforks.com/region/{state_name}/trails/?activitytype=6&difficulty=2,3,4,5,6,8"
    url_list = [start_url]
    for page_num in range(state_page_dict[state_name]):
        url_list.append(start_url + f"&page={page_num+2}")
    for page_num in range(state_page_dict[state_name]):
        href_list = []
        driver.get(url_list[page_num])
        green_links = driver.find_elements("xpath","//tr//a[contains(@class, 'green')]")
        #ul id = trailstats_display
        #each li is a clearfix
        #each clearfix has a div term and div definition
        
        for green in green_links:
            href = green.get_attribute("href") #Grab URLs--otherwise this doesn't work
            href_list.append(href)
        print(href_list)
        for idx, url in enumerate(href_list):
            if idx == 0:
                trail_frame = pd.DataFrame({'Name':['name_test'], 'Coords':['coord_test'],"Distance": ["NA"], "Avg time": ["NA"], "Climb": ["NA"], "Descent": ["NA"], "Activities": ["NA"], "Riding Area": ["NA"], "Difficulty Rating": ["NA"], "Local Popularity": ["NA"]})
            
            
            driver.get(url)
            name_coord_dict = {'Name':['name_test'], 'Coords':['coord_test']}
            basic_vars_dict = {"Distance": ["NA"], "Avg time": ["NA"], "Climb": ["NA"], "Descent": ["NA"]}
            trail_details_vars = {"Activities": ["NA"], "Riding Area": ["NA"], "Difficulty Rating": ["NA"], "Local Popularity": ["NA"]}
            trail_stats_vars = { "Altitude start": ["NA"], "Altitude end": ["NA"], "Grade": ["NA"]}
         #Got o trail page
            
            try:
                name_raw = driver.find_element("xpath", "//span[contains(@class, 'translate')][1]") #Get name
                print("Hello! Tried Successfully.")
                name_coord_dict['Name'] = [name_raw.text]
            except:
                name_coord_dict['Name'] = "NA"
            try:
                coord_raw = driver.find_element("xpath", "//div[contains(@class, 'margin-bottom-15 grey')]/span[contains(@class, 'grey2')][2]") #Get coords
                name_coord_dict['Coords'] = coord_raw.text
            except:
                name_coord_dict['Coords'] = "NA"
            scrape_basic_stats(url, basic_vars_dict)
            
            trail_stats_vars = scrape_tables(url,stats_keywords ,'trailstats_display',trail_stats_vars)
            #scrape_trail_stats_variables(url,trail_stats_vars)
            #scrape_trail_details_variables(url,trail_details_vars)
            trail_details_vars = scrape_tables(url, trail_keywords,'traildetails_display',trail_details_vars)
            
            
            all_stats_dict = {**name_coord_dict,**basic_vars_dict, **trail_details_vars, **trail_stats_vars}
            print(all_stats_dict)
            trail_frame = pd.concat([trail_frame, pd.DataFrame(all_stats_dict)], ignore_index = True)
            
        database_info.add_trails(trail_frame,state_name)
        time.sleep(10)
    driver.quit()

state_scraper("Louisiana")
    




