from abc import ABC, abstractmethod
from selenium.common import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class LoadableComponent(ABC):
    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.load()
        self.is_loaded()
        return self

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def is_loaded(self):
        pass


class ReviewPage(PageFactory, LoadableComponent):
    URL = "https://skillbox.ru/otzyvy/?direction=code"

    locators = {
        "reviews": (By.XPATH, "//div[@class = 'ui-text-review__text p p--2']"),
        "header": (By.XPATH, "//h1[@class = 'reviews-first-screen__title h h--1']"),
    }

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.highlight = True
        super().__init__()

    def load(self):
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        if not self.URL == self.driver.current_url:
            return False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators["header"])
            )
        except WebDriverException:
            return False

    def is_reviews(self):
        reviews_elements = self.driver.find_elements(*self.locators["reviews"])
        return len(reviews_elements) if reviews_elements else 0
