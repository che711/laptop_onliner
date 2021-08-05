from pages.catalog_page import CatalogPage
import time
from pages.locators import CatalogPageLocators
from pages.locators import ProductPageLocators
from pages.locators import SortPageLocators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# pytest -s -vv tests_onliner.py
# pytest -s -v --browser_name=chrome test_onliner.py
# pytest -s -v --browser_name=firefox test_onliner.py

def test_hover(browser):
    link = 'https://www.onliner.by/'
    browser.get(link)
    catalog = browser.find_element(*CatalogPageLocators.CATALOG)
    catalog.click()
    computers = browser.find_element(*CatalogPageLocators.COMPUTERS)
    computers.click()
    laptop_other = browser.find_element_by_xpath('//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div/div[1]/div[1]')
    move_laptop = ActionChains(browser).move_to_element(laptop_other).perform()
    time.sleep(2)
    laptops = browser.find_element(*CatalogPageLocators.LAPTOPS)
    laptops.click()
    print("\n\tПереход на страницу Ноутбуки")
    makers = browser.find_element(*ProductPageLocators.MAKERS)
    time.sleep(2)
    browser.execute_script("arguments[0].click();", makers)
    print("\n\tВыпал список производителей")
    lenovo = browser.find_element(*ProductPageLocators.LENOVO_CHECKBOX)
    lenovo.click()
    dell = browser.find_element(*ProductPageLocators.DELL_CHECKBOX)
    dell.click()
    hp = browser.find_element(*ProductPageLocators.HP_CHECKBOX)
    hp.click()
    min_price = browser.find_element(*ProductPageLocators.MIN_PRICE)
    min_price.send_keys(1500)
    max_price = browser.find_element(*ProductPageLocators.MAX_PRICE)
    max_price.send_keys(3000)
    print("\n\tУказали диапазон цен")
    min_screen_diagonal = browser.find_element(*ProductPageLocators.MIN_SCRIN_DIAGONAL)
    min_screen_diagonal.send_keys(12)
    max_screen_diagonal = browser.find_element(*ProductPageLocators.MAX_SCRIN_DIAGONAL)
    max_screen_diagonal.send_keys('13.4')
    print("\n\tУказали диагональ")
    button_all_products = browser.find_element(*ProductPageLocators.ALL_PRODUCTS)
    button_all_products.click()
    get_number_of_progucts = browser.find_element(*ProductPageLocators.NUMBER_OF_PRUDUCTS)
    time.sleep(2)
    number = get_number_of_progucts.text
    time.sleep(5)
    print(f"\n\t{number}")
    sort_button = browser.find_element(*SortPageLocators.SORT_BUTTON)
    sort_button.click()
    sort_in_ascending = browser.find_element(*SortPageLocators.SORT_IN_ASCENDING)
    sort_in_ascending.click()
    print("\n\tОтсортированно по возрастанию")
    time.sleep(5)
    first_element_position = browser.find_element(*SortPageLocators.FIRST_ELEMENT_POSITION)
    name_first_elem = first_element_position.text
    print(f"\n\tНа первой позиции находится: {name_first_elem}")
    time.sleep(2)
    sort_button = browser.find_element(*SortPageLocators.SORT_BUTTON)
    sort_button.click()
    sort_in_descending = browser.find_element(*SortPageLocators.SORT_IN_DESCENDING)
    sort_in_descending.click()
    print("\n\tОтсортированно по убыванию")
    time.sleep(2)
    go_end = browser.find_element(*SortPageLocators.GO_TO_END_ONE_STEP)
    go_end.click()
    go_to_end_two = browser.find_element(*SortPageLocators.CO_TO_END_TWO_STEP)
    go_to_end_two.click()
    print("\n\tПереход на последнюю страницу")
    time.sleep(2)
    end_element_position = browser.find_element(*SortPageLocators.END_ELEMENT_POSITION)
    name_end_elem = end_element_position.text
    time.sleep(2)
    print(f"\n\tНа последней позиции находится: {name_end_elem}")
    assert (name_end_elem == name_first_elem), 'Имена ноутбуков не совпадают'
    time.sleep(2)


