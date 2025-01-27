from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory


class QaPage(PageFactory):
    URL = "https://skillbox.ru/course/profession-testing-automation-engineer/"

    locators = {"course_cost": (By.XPATH, "//h2[@class = 'price-info__title h h--2']")}

    def __init__(self, driver):
        self.driver: WebDriver = driver
        super().__init__()

    def load(self):
        self.driver.get(self.URL)
        return self

    def _scroll(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self

    def course_price(self):
        locator = self.locators["course_cost"]
        try:
            self._scroll(locator)
            course_cost_elem = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator)
            )
            return course_cost_elem.text.strip() == "Стоимость курса"
        except AssertionError:
            return False
