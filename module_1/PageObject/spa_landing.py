from selenium.common import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module_1.PageObject.spa_callback_forms import CallbackForm
from module_1.PageObject.spa_courses_page import FilterCourses
from module_1.PageObject.spa_qa_page import QaPage
from module_1.PageObject.spa_search_form import SearchForm
from module_1.PageObject.spa_code_page import CodePage


class Landing(object):
    def __init__(self, driver):
        self.URL = "https://skillbox.ru/"
        self.driver: WebDriver = driver
        self.search_form = SearchForm(driver)
        self.callback_form = CallbackForm(driver)
        self.code_page = CodePage(driver)
        self.courses_page = FilterCourses(driver)
        self.header = "//h1[@class='faculty-blank__title h h--1']"
        self.qa = QaPage(driver)

    def open(self):
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        if not self.driver.current_url.startswith(f"{self.URL}/courses/"):
            return False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.header)
            )
        except WebDriverException:
            return False
