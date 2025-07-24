import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.support.wait import WebDriverWait

# university_dict = dict()

# prototype 1

# Chrome_bot = webdriver.Chrome()
# Chrome_bot.get('https://www.gosuslugi.ru/vuznavigator/universities')
#
# wait = WebDriverWait(Chrome_bot, 10)  # 10 секунд максимальное время ожидания
# element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "a")))
# # links = Chrome_bot.find_elements(By.CSS_SELECTOR, ".title-h4.organization-card__title")
#
# links = Chrome_bot.find_elements(By.TAG_NAME, "a")
#
# href_list = []
#
# # Перебираем все найденные ссылки и извлекаем их атрибуты href
# for link in links:
#     href = link.get_attribute("href")
#     if href:  # Проверяем, что ссылка не пустая
#         href_list.append(href)
#
# Chrome_bot.quit()
# print(href_list)


# with open('Universities_prototype.json', 'w') as f:
#     json.dump(university_dict, f, indent=4) # Записываем словарь в файл с отступом 4 пробела для читаемости

# prototype 2



#     i = 10_240
#     url = f'https://www.gosuslugi.ru/vuznavigator/universities/{str(i)}'
#
#     options = Options()
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
#     # options.add_argument("user-data-dir=/path/to/profile")  # Путь к профилю
#     # options.add_argument("--proxy-server=185.162.229.216:80")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.page_load_strategy = 'eager'
#
#     Chrome_bot = webdriver.Chrome(options=options)
#
#     Chrome_bot.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#         "source": """
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#         """
#     })
#
#     Chrome_bot.get(url)
#
#
#     wait = WebDriverWait(Chrome_bot, 2)  # 10 секунд максимальное время ожидания
#     element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title-h3.flex-1")))
#     element = element.text
#
#     question = f'Какое сокращенное название у {element}? Дай ответ одним словом'
#     # Chrome_bot.quit()
#
#     Chrome_bot.get('https://www.google.com')
#
#     # Находим поле поиска
#     search_box = Chrome_bot.find_element(By.NAME, 'q')
#
#     # Вводим запрос
#     search_query = question
#     # for char in search_query:
#         # search_box.send_keys(char)
#         # time.sleep(random.uniform(0.1, 0.3))
#     search_box.send_keys(search_query)
#
#     # Нажимаем Enter
#     search_box.send_keys(Keys.RETURN)
#
#     # Даем странице немного времени на загрузку результатов
#
#     # wait = WebDriverWait(Chrome_bot, 5)  # 10 секунд максимальное время ожидания
#     # _ = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "span")))
#     element = [i.text for i in Chrome_bot.find_elements(By.CSS_SELECTOR, '.rPeykc > span:nth-child(1) > span:nth-child(1)')]
#
#     vuz = ''
#     for i in element:
#         if i[0].isupper() and i[-1].isupper():
#             vuz = i
#     if vuz == '':
#         print('Error')
#
#     print(vuz)
#     university_dict[1024] = vuz
# except TimeoutError:
#     print('error')
# except:
#     print('Error', 1)
#
# print(university_dict)

# prototype 3

# err = 0
# try:
#     for vuz_counter in range(2719,10_000):
#         err = vuz_counter
#         url = f'https://www.gosuslugi.ru/vuznavigator/universities/{str(vuz_counter)}'
#
#         options = Options()
#
#         options.add_argument(
#             "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
#         options.add_argument("--disable-blink-features=AutomationControlled")
#         options.page_load_strategy = 'eager'
#
#         Chrome_bot = webdriver.Chrome(options=options)
#
#         Chrome_bot.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#             "source": """
#                 delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#                 delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#                 delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#                 """
#         })
#
#         Chrome_bot.get(url)
#         Chrome_bot.maximize_window()
#         try:
#             wait = WebDriverWait(Chrome_bot, 6)  # 10 секунд максимальное время ожидания
#             element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title-h3.flex-1")))
#             element = element.text
#
#         except TimeoutException:
#             Chrome_bot.quit()
#             continue
#
#         question = f'Напиши ответ только одной аббревиатурой: "Какое официальное название {element}"? Пиши правильно, очень желательно поменьше слов, чтобы можно было расшифровать аббревиатуру и не спутать с другим вузом.'
#
#         Chrome_bot.get('https://gptdaisy.com/chat/auth/')
#         time.sleep(3)
#
#         search_box = Chrome_bot.find_element(By.CSS_SELECTOR, '.core-field__message-input')
#         search_box.send_keys(question)
#         time.sleep(1)
#         search_box.send_keys(Keys.ENTER)
#
#         # search_box = Chrome_bot.find_element(By.CLASS_NAME,
#         # '.resize-on-load.resize-on-input.chat-input')
#         #
#         # search_box.send_keys(question)
#
#         time.sleep(5)
#
#         # [elem for elem in Chrome_bot.find_elements(By.CSS_SELECTOR,
#         # '#page-0 > div:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)')][-1].click()
#         element = Chrome_bot.find_element(By.CLASS_NAME, 'system-message__text-block.markdown-content').text
#         print(element)
#         Chrome_bot.quit()
#
#         for char in r'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\/:*?"<>|.':
#             element = element.replace(char,'')
#         for char in element:
#             if char not in ' _0123456789-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
#                 element = element.replace(char,'')
#         element = element.replace(' ', '_')
#         vuz = ''
#
#
#         try:
#             if element == '':
#                 print('Error')
#                 break
#             else:
#                 vuz = element
#
#         except IndexError:
#             print(element)
#             break
#         finally:
#             university_dict[vuz_counter] = vuz
#
#     print(university_dict)
#     with open('Universities_prototype.json', 'w', encoding='utf-8') as f:
#         json.dump(university_dict, f, indent=4, ensure_ascii=False) # Записываем словарь в файл с отступом
#
# except:
#     with open('Universities_prototype.json', 'w', encoding='utf-8') as f:
#         json.dump(university_dict, f, indent=4, ensure_ascii=False) # Записываем словарь в файл с отступом
#     print('Error', err)

# prototype 4

# dictionary_with_uni = dict()
#
# option = Options()
# option.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
# option.add_argument("--disable-blink-features=AutomationControlled")
# option.page_load_strategy = 'eager'
#
# Searcher = webdriver.Chrome(options=option)
#
# Searcher.get('https://www.gosuslugi.ru/vuznavigator/universities')
#
# time.sleep(3)
#
# while not len(webdriver.Chrome.find_elements(Searcher, By.XPATH, '/html/body/app-root/div[2]/div/app-universities/div/div[2]/div[2]/app-organization-card[1716]/a/div[1]/p')):
#     Searcher.execute_script('window.scrollTo(0, window.document.documentElement.scrollHeight - 850);')
#     time.sleep(1)
#
# urls = [url.get_attribute('href') for url in webdriver.Chrome.find_elements(Searcher, By.TAG_NAME, 'a')]
# print(urls)



# for url in urls:
#     if url[-1] not in '0123456789':
#         continue
#     vuz_num = url.split('/')[-1]
#
#
#     Searcher.get(url)
#     time.sleep(7)
#     name = webdriver.Chrome.find_element(Searcher, By.CSS_SELECTOR, '.title-h3').text
#     print(name)
#     for char in name:
#         if char not in ' \\"_0123456789-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
#             name = name.replace(char, '')
#     name = name.replace(' ','-')

# for url in urls:
#     if url[-1] not in '0123456789':
#         continue
#     vuz_num = url.split('/')[-1]
#
#     vuz_name_1 = webdriver.Chrome.find_element(Searcher, By.CSS_SELECTOR, f'a[href="{url}"]')
#     vuz_name = vuz_name_1.find_element(By.TAG_NAME, 'p').text
#     dictionary_with_uni[vuz_num] = vuz_name
#     print(dictionary_with_uni, '\n')
#
#     with open('Universities_prototype.json', 'w', encoding='utf-8') as f:
#         json.dump(dictionary_with_uni, f, indent=4, ensure_ascii=False)

    # question = f'Напиши ответ только одной аббревиатурой: "Какое официальное название {name}"? Пиши правильно, очень желательно поменьше слов, чтобы можно было расшифровать аббревиатуру и не спутать с другим вузом.'
    #
    # Searcher.get('https://geekbot.ru/')
    # time.sleep(5)
    #
    # text_area = webdriver.Chrome.find_element(Searcher, By.CSS_SELECTOR, '.resize-on-load')
    # text_area.send_keys(question)
    # time.sleep(3)
    #
    # text_area.send_keys(Keys.CONTROL + Keys.ENTER)
    # time.sleep(7)
    #
    #
    #
    # answer = webdriver.Chrome.find_element(Searcher, By.XPATH, '/html/body/main/div[3]/div[2]/div/div[3]/div[2]/p')
    # answer = answer.text
    #
    # for char in answer:
    #     if char not in ' \\"_0123456789-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
    #         answer = answer.replace(char, '')
    # answer = answer.replace(' ', '-')
    #
    #
    # # ans = [dial.text for dial in text][1]
    #
    # print(answer)
    #
    # dictionary_with_uni[vuz_num] = name
    #
    # with open('Universities_prototype.json', 'w', encoding='utf-8') as f:
    #     json.dump(dictionary_with_uni, f, indent=4, ensure_ascii=False)

    # with open('Universities_prototype.json', 'w', encoding='utf-8') as f:
        # json.dump(dictionary_with_uni, f, indent=4, ensure_ascii=False)