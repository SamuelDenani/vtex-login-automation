import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

store_address = 'http://' + str(sys.argv[1])
user_home = str(Path.home()).split('\\')[-1]

_login = os.environ.get('VTEX_Login')
_password = os.environ.get('VTEX_Password')

def login():
    print(f'Logando em: {store_address}')
    
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('disable-infobars')
    options.add_experimental_option('detach', True)
    options.add_argument(f'user-data-dir=C:/Users/{user_home}/AppData/Local/Google/Chrome/User Data')

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.implicitly_wait(4)
    browser.get(store_address)

    browser.find_elements_by_xpath('//*[@id="render-admin.signin"]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div')[0].click()

    if len(browser.find_elements_by_css_selector('div[data-identifier="acesso@agenciaeconverse.com.br"')):
        browser.find_elements_by_css_selector('div[data-identifier="acesso@agenciaeconverse.com.br"')[0].click()
    elif len(browser.find_elements_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li')):
        browser.find_elements_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li')[-1].click()

    browser.find_elements_by_xpath('//input[@name="identifier"]')[0].send_keys(_login)
    browser.find_elements_by_xpath('//*[@id="identifierNext"]')[0].click()

    browser.find_elements_by_xpath('//input[@name="password"]')[0].send_keys(_password)
    browser.find_elements_by_xpath('//*[@id="passwordNext"]')[0].click()

    

if __name__ == '__main__':
    login()