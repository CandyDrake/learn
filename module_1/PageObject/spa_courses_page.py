import time
import urllib.parse
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from module_1.PageObject.spa_qa_page import QaPage


class FilterCourses(PageFactory):
    URL = "https://skillbox.ru/course/profession-testing-automation-engineer/"

    locators = {
        "grade_button": (
            By.XPATH,
            "//div[@class = 'courses-page__content-wr']//span[contains(text(), 'Для новичков')]",
        ),
        "profession_button": (
            By.XPATH,
            "//a[@href='https://skillbox.ru/course/profession-testing-automation-engineer/']",
        ),
        "programming_filter": (
            By.XPATH,
            "//div[@class = 'filter-directions courses-page__directions']//span[contains(text(), 'Программирование')]",
        ),
    }

    def __init__(self, driver):
        self.driver: WebDriver = driver
        super().__init__()

    def is_loaded(self):
        try:
            if self.URL != urllib.parse.unquote(self.driver.current_url):
                return False

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.locators["course_cost"])
            )
            return True
        except WebDriverException:
            return False

    def _scroll(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self

    def load(self):
        self.driver.get(self.URL)
        return self

    def click_newbies(self):
        self.grade_button.click()
        time.sleep(1)

    def click_prof_filter(self):
        self.programming_filter.click()
        time.sleep(1)

    def click_profession(self):
        self.click_prof_filter()
        time.sleep(1)
        profession = self.profession_button
        self._scroll(profession)
        self.profession_button.click()
        if self.is_loaded():
            return QaPage(self.driver)
