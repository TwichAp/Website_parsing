import re
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Functions import *

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.page_load_strategy = 'eager'

Searcher = webdriver.Chrome(options=options)

# Список начальных ссылок
# Searcher.get('https://www.gosuslugi.ru/vuznavigator/specialties')
# time.sleep(3)
#
# while not len(webdriver.Chrome.find_elements(Searcher, By.XPATH, '/html/body/app-root/div[2]/div/app-specialties/div/div[2]/div[2]/app-specialty-card[1026]/div/a/p[1]/span')):
#     Searcher.execute_script('window.scrollTo(0, window.document.documentElement.scrollHeight - 850);')
#     time.sleep(1)
#
# urls = [url.get_attribute('href') for url in webdriver.Chrome.find_elements(Searcher, By.TAG_NAME, 'a')]
# with open('General_Urls.txt', 'wx+') as file:
#     for url in urls:
#         file.write(f'{url}\n')


# Создание списка с полными названиями вузов
# Searcher.get('https://www.gosuslugi.ru/vuznavigator/universities')
# time.sleep(3)
#
# while not len(webdriver.Chrome.find_elements(Searcher, By.XPATH, '/html/body/app-root/div[2]/div/app-universities/div/div[2]/div[2]/app-organization-card[1717]/a/div[1]/p')):
#     Searcher.execute_script('window.scrollTo(0, window.document.documentElement.scrollHeight - 850);')
#     time.sleep(1)
#
# names = [name.text for name in webdriver.Chrome.find_elements(Searcher, By.CLASS_NAME, 'title-h4.organization-card__title')]
# print(names)
# with open('Universities_names.txt', 'wx+', encoding='utf-8') as file:
#     for name in names:
#         name = rename_for_file(name)
#         file.write(f'{name}\n')


# Создание папок с вузами внутри определённой папки ( в данном случае files)
# list_with_uni = [name.replace('\n','') for name in open('Universities_names.txt', encoding='utf-8')]
# for name in list_with_uni:
#     os.makedirs(f'C:\\Users\\roma0\PycharmProjects\Education\files\\{name}', exist_ok=True)

if __name__ == '__main__':
    urls = [url.replace('\n', '') for url in open('General_Urls.txt', 'r', encoding='utf-8')]
    for url in urls:
        search_sites_with_spreadsheet(Searcher, url)

    for site in open('Sites_for_downloading.txt', 'r'):
        download_spreadsheet(Searcher, site)

    map(rename_files, os.listdir('Download'))

# if __name__ == '__main__':
#     sites_with_spreadsheet = [url.replace('\n','') for url in open('Sites_for_downloading.txt', 'r', encoding='utf-8')]
#     map(search_sites_with_spreadsheet, sites_with_spreadsheet)