from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .locators import CatalogPageLocators
import time


class CatalogPage(BasePage):

    def push_catalog(self):
        '''Нажимаем на Catalog'''
        push_catalog = self.browser.find_element(*CatalogPageLocators.FIND_COMPUTERS)
        push_catalog.click()

    def move_mouse(self):
        asset = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[1]/span[2]")
        ActionChains.move_to_element(asset).click()
        button = self.browser.find_element_by_xpath("//span[contains(@class, 'DesktopMenu__SectionTitle')]")
        button.click()

    def hover(self):
        action = ActionChains(browser)
        firstLevelMenu = self.browser.find_element_by_xpath("first_level_menu_id_in_your_web_page")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = self.browser.find_element_by_xpath("second_level_menu_id_in_your_web_page")
        action.move_to_element(secondLevelMenu).perform()

    def add_names_book(self):
        '''Находим называние, добавленной в корзину книги'''
        name2 = self.browser.find_element(*CatalogPageLocators.ADD_NAME_BOOK)
        book2 = name2.text
        print(f"\n\tBook in basket: {book2}")

    def price_book(self):
        '''Находим цену книги'''
        css_price =  self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price = css_price.text
        print(f"\n\tThe book`s price: {price}")

    def add_price_book(self):
        '''Находим цену книги, добавленной в корзину'''
        css_price = self.browser.find_element(*ProductPageLocators.ADD_PRICE_BOOK)
        price = css_price.text
        print(f"\n\tThe basket`s price: {price}")
