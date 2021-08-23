from selenium.webdriver.common.by import By


class CatalogPageLocators():
    CATALOG = (By.XPATH, '//*[@id="container"]/div/div/header/div[2]/div/nav/ul[1]/li[1]/a[2]/span')
    COMPUTERS = (By.XPATH, '//*[@id="container"]/div/div/div/div/div[1]/ul/li[3]/span[2]/span')
    LAPTOPS_OTHER = (By.XPATH, '//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div/div[1]/div[1]')
    LAPTOPS = (By.XPATH, '//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/a[1]')


class ProductPageLocators():
    MAKERS = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[6]/div[2]/div[1]/div/span[2]')
    LENOVO_CHECKBOX = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[6]/div[2]/div[2]/div/div[1]/div[2]/div[16]/label/span[1]/span')
    DELL_CHECKBOX = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[6]/div[2]/div[2]/div/div[1]/div[2]/div[5]/label/span[1]')
    HP_CHECKBOX = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[6]/div[2]/div[2]/div/div[1]/div[2]/div[13]/label/span[1]')
    MIN_PRICE = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[7]/div[2]/div/div[1]/input')
    MAX_PRICE = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[7]/div[2]/div/div[2]/input')
    MIN_SCRIN_DIAGONAL = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[14]/div[3]/div/div[1]/select')
    MAX_SCRIN_DIAGONAL = (By.XPATH, '//*[@id="schema-filter"]/div[3]/div[14]/div[3]/div/div[2]/select')
    ALL_PRODUCTS = (By.XPATH, '//*[@id="schema-filter-button"]/div/div/div[1]')
    NUMBER_OF_PRUDUCTS = (By.XPATH, '//*[@id="schema-filter-button"]/div/div/div[1]/span[2]')


class SortPageLocators():
    SORT_BUTTON = (By.XPATH, '//*[@id="schema-order"]/a')
    SORT_IN_ASCENDING = (By.XPATH, '//*[@id="schema-order"]/div[2]/div/div[2]/span')
    FIRST_ELEMENT_POSITION = (By.XPATH, '//*[@id="schema-products"]/div[1]/div/div[3]/div[2]/div[1]/a/span')
    SORT_IN_DESCENDING = (By.XPATH, '//*[@id="schema-order"]/div[2]/div/div[3]/span')
    GO_TO_END_ONE_STEP = (By.XPATH, '//*[@id="schema-pagination"]/div[1]/div')
    CO_TO_END_TWO_STEP = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[4]/div[3]/div[6]/div[2]/div/div/div[1]/ul/li[3]/a')
    END_ELEMENT_POSITION = (By.XPATH, '(//*[@id="schema-products"]//a/span)[last()]')
