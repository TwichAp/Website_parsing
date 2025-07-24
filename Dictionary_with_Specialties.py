import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

"""
Процесс сбора всех возможных специальностей на сайте Госуслуги, записывая данные в формате .json 
(специальность: [номер направления, ступень высшего образования]
Все данные записаны в файле specialties.json
"""

dictionary_with_specialties = dict()

option = Options()
# option.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
option.add_argument("--disable-blink-features=AutomationControlled")
option.page_load_strategy = 'eager'

Searcher = webdriver.Chrome(options=option)

Searcher.get('https://www.gosuslugi.ru/vuznavigator/specialties')

time.sleep(3)

while not len(webdriver.Chrome.find_elements(Searcher, By.CSS_SELECTOR, 'app-specialty-card.animate-by-hover:nth-child(1026) > div:nth-child(1) > a:nth-child(1) > p:nth-child(1) > span:nth-child(1)')):
    Searcher.execute_script('window.scrollTo(0, window.document.documentElement.scrollHeight - 850);')
    time.sleep(1)

urls = [url.get_attribute('href') for url in webdriver.Chrome.find_elements(Searcher, By.TAG_NAME, 'a')][2:]

for url in urls:
    if url[-1] not in '0123456789':
        continue
    Searcher.get(url)
    time.sleep(3)

    text_spec = webdriver.Chrome.find_element(Searcher, By.CLASS_NAME, 'title-h3').text
    text_spec = text_spec.replace(', ','+')
    step, spec, text_spec = text_spec.split('+')[-1], text_spec.split()[0].replace('.','-'), '_'.join(text_spec.split('+')[0].split()[1:])

    dictionary_with_specialties[text_spec] = [spec, step]


with open('specialties.json', 'w+', encoding='utf-8') as file:
    json.dump(dictionary_with_specialties, file, indent=4, ensure_ascii=False)