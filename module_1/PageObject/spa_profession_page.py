from selenium.common import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from module_1.PageObject.spa_code_page import CodePage


class ProfessionPage(CodePage):
    URL = "https://skillbox.ru/code/faculty/"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.highlight = True
        super().__init__(driver)

    @staticmethod
    def is_correct_number(elements_count, title_count):
        return elements_count == title_count

    def is_loaded(self):
        if not self.URL == self.driver.current_url:
            return False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators["header"])
            )
        except WebDriverException:
            return False
