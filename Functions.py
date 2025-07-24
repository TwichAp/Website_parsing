import os, re, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Удаление лишних файлов при скачивании таблиц с сайта Госуслуги
def delete_other_files(directory: str) -> None:
    """
    Удаляет все файлы из директории, кроме файлов .csv
    :param directory: Название директории, куда сохраняются файлы
    :return: None
    """

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            continue
        else:
            filepath = os.path.join(directory, filename)
            try:
                os.remove(filepath)
            except OSError:
                pass


def search_buttons(driver) -> None:
    """
    Ищет на сайте кнопки.
    :param driver: Класс используемого браузера.
    :return: None
    """

    # prototype
    # WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, '//img[@src="//gu-st.ru/epgu-app-vuz-navigator-st/assets/svg/admission.svg"]')))
    # all_buttons = len(driver.execute_script("return Array.from(document.querySelectorAll('button'));"))
    # driver.execute_script("return document.body.scrollHeight;")
    # buttons = driver.find_elements(By.CLASS_NAME, 'panel-header flex-container reset text-left width-full')[:all_buttons]
    # print(buttons)
    # for iter_ in range(all_buttons):
    #     driver.execute_script("arguments[0].scrollIntoView(true);", buttons[iter_])
    #     buttons[iter_].click()
    buttons = [button for button in
               driver.find_elements(By.CLASS_NAME, 'panel-header flex-container reset text-left width-full')]
    for button in buttons:
        if button.get_attribute('aria-expanded') == 'false':
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            button.click()

def download_spreadsheet(driver, url: str) -> None:
    """
    Скачивает .csv таблицу на сайте.
    :param driver: Класс используемого браузера
    :param url: Ссылка на сайт с таблицей
    :return: None
    """

    driver.get(url)
    button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-link.link-plain'))
    )
    button.click() # <- нажатие кнопки 1-й раз
    actions = ActionChains(driver)
    actions.move_to_element(button).pause(1).click().perform() # <- нажатие кнопки 2-й (лучше оставить, так как раздельно нормально не работает)

def scrolling_down(driver) -> None:
    """
    Прокручивает сайт вниз (включая прогружаемые элементы).
    :param driver: Класс используемого браузера
    :return: None
    """

    step, end = 1, 0
    while step != end:
        step = driver.execute_script("return document.body.scrollHeight;")
        driver.execute_script('window.scrollTo(0, window.document.documentElement.scrollHeight - 850);')
        time.sleep(2)
        end = driver.execute_script("return document.body.scrollHeight;")

def rename_for_file(name: str) -> str:
    """
    Выводит строку, подходящую для имени файла.
    :param name: Строка с символами, которые нельзя использовать для названия файла
    :return: Строка, подходящая для переименовывания файла
    """

    if len(re.findall(r'«([^«»]*)»', name)):
        name = re.findall(r'«([^«»]*)»', name)[0]
    else:
        for char in name:
            if char not in 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789- ':
                name = name.replace(char, '')
        name = name.replace(' ', '_').replace('  ',' ').replace('__','_')
    return name


def search_sites_with_spreadsheet(driver, url: str) -> None :
    """
    Ищет по текущей ссылке другие ссылки с надписью "Скачать в виде таблицы".
    :param url: Принимаемое значение ссылки из списка начальных ссылок
    :param driver: Класс используемого браузера
    :return: None
    """

    driver.get(url)
    scrolling_down(driver)
    universities = [target.get_attribute('href') for target in WebDriverWait(driver,30).until(EC.visibility_of_any_elements_located((By.TAG_NAME, 'a'))) if target.get_attribute('href')[-1] in '0123456789']
    driver.maximize_window()

    for site_with_spreadsheet in universities: # <- начало идеи по записи ссылок на сайты с таблицами
        driver.get(site_with_spreadsheet)
        uni_name = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.text-plain.mb-12.pt-12')))
        uni_name = rename_for_file(uni_name.text)

        search_buttons(driver)
        table = [target.get_attribute('href') for target in driver.find_elements(By.CSS_SELECTOR, "a.summary-link:nth-child(2)")]

        for site in table:
            driver.get(site)
            WebDriverWait(driver,20).until(EC.visibility_of_any_elements_located((By.TAG_NAME, 'h2')))
            fin_urls = [site.get_attribute('href') for site in driver.find_elements(By.CSS_SELECTOR, '.p-24.link-plain')]
            with open('Sites_for_downloading.txt', 'wx+', encoding='utf-8') as file:
                for url in fin_urls:
                    file.write(url)


def rename_files(raw_file: str, uni_name: str) -> None:

    """
    Переименовывает файлы .csv по шаблону 'вуз_специальность_программа_дата-обновления(01-01-2025).csv'

    :param raw_file: Название скаченного файла
    :param uni_name: Название вуза к специальности
    :return: None
    """

    raw_file_copy = rename_for_file(raw_file.split('.')[0])
    path = os.path.abspath('Download')

    places_for_admission = ''
    step = ''
    places_for_admission_type = ''

    data = '-'.join(re.findall(r'\d{4}-\d{2}-\d{2}', raw_file_copy)[-1].split('-')[::-1])
    correct_file = f'{step}_{places_for_admission}_{places_for_admission_type}_{raw_file_copy}_{data}.xlsx'
    os.rename(os.path.join(path, raw_file), os.path.join(path, correct_file))

