from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time as t
import os




def download_sql():
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
                    
    base_url = "https://github.com/"
    driver = webdriver.Chrome(service= Service())
    driver.get(base_url+"login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.NAME, "commit").click()
    driver.maximize_window()
    driver.get(base_url+user+"/database-exercises")
    count = 0
    for i in range(len(driver.find_elements(By.XPATH, '''//a[@class = 'js-navigation-open Link--primary']'''))):
        
        if count > 0:
            driver.find_elements(By.XPATH, '''//a[@class = 'js-navigation-open Link--primary']''')[i].click()
            t.sleep(3)
            driver.find_elements(By.XPATH, '''//button[@data-component= 'IconButton']''')[6].click()
            t.sleep(3)
            driver.find_elements(By.XPATH, '''//a[@data-testid="breadcrumbs-repo-link"]''')[0].click()
            t.sleep(3)

            
        count +=1
        
    print('Done!')
    driver.close()
    driver.quit()


def pull_all_ipynb():
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
    base_url = "https://github.com/"
    driver = webdriver.Chrome(service= Service())
    driver.get(base_url+"login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.NAME, "commit").click()
    driver.maximize_window()
    driver.find_element(By.XPATH, '''//button[@aria-label="Open user account menu"]''').click()
    t.sleep(3)
    driver.find_elements(By.XPATH, '''//span[@class="ActionListItem-label"]''')[20].click()
    t.sleep(3)
    # driver.find_elements(By.XPATH, '''//a[@itemprop="name codeRepository"]''')[0].click()
    for i in range(len(driver.find_elements(By.XPATH, '''//a[@itemprop="name codeRepository"]'''))):
        t.sleep(3)
        driver.find_elements(By.XPATH, '''//a[@itemprop="name codeRepository"]''')[i].click()
        t.sleep(3)
        for j in range(len(driver.find_elements(By.XPATH, '''//a[@class="js-navigation-open Link--primary"]'''))):
            try:
                
                if 'ipynb' in driver.find_elements(By.XPATH, '''//a[@class="js-navigation-open Link--primary"]''')[j].text:
                    driver.find_elements(By.XPATH, '''//a[@class="js-navigation-open Link--primary"]''')[j].click()
                    t.sleep(3)
                    driver.find_elements(By.XPATH, '''//span[@class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-n"]''')[0].click()
                    t.sleep(3)
                    driver.find_elements(By.XPATH, '''//a[@class="Link__StyledLink-sc-14289xe-0 iJtJJh" ]''')[0].click()
                    t.sleep(3)
            except: 
                t.sleep(5)
                if 'ipynb' in driver.find_elements(By.XPATH, '''//a[@class="js-navigation-open Link--primary"]''')[j].text:
                    driver.find_elements(By.XPATH, '''//a[@class="js-navigation-open Link--primary"]''')[j].click()
                    t.sleep(3)
                    driver.find_elements(By.XPATH, '''//span[@class="Tooltip__TooltipBase-sc-uha8qm-0 fCnxTL tooltipped-n"]''')[0].click()
                    t.sleep(3)
                    driver.find_elements(By.XPATH, '''//a[@class="Link__StyledLink-sc-14289xe-0 iJtJJh" ]''')[0].click()
                    t.sleep(3)
        driver.find_element(By.XPATH, '''//button[@aria-label="Open user account menu"]''').click()
        t.sleep(3)
        driver.find_elements(By.XPATH, '''//span[@class="ActionListItem-label"]''')[19].click()
        t.sleep(3)
    print('Done!')
    driver.close()
    driver.quit()