import time
import urllib.parse
from urllib.parse import urlparse
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from module_1.PageObject.spa_courses_page import FilterCourses


class SearchForm(PageFactory):
    locators = {
        "catalog_button": (
            By.XPATH,
            '//span[@class="ui-tab__text f"][contains(text(), "Каталог")]',
        ),
        "hints": (By.XPATH, '//*[@id="#app"]/header/div[1]/div/div/div/div[1]'),
        "search_input": (By.XPATH, '//input[@name="search"]'),
    }

    def __init__(self, driver):
        self.driver: WebDriver = driver
        super().__init__()

    def open_form(self):
        catalog_button = self.catalog_button
        catalog_button.click()
        return self

    def enter_query(self, query):
        search_box = self.search_input
        search_box.clear()
        search_box.send_keys(query)
        time.sleep(1)

    def get_hints_texts(self):
        elements = self.driver.find_elements(*self.locators["hints"])
        return [text.text for text in elements]

    def relevant_hints(self, query):
        half_query = query[: len(query) // 2]
        texts = self.get_hints_texts()
        return all(half_query.lower() in text.lower() for text in texts)

    def go_to_course_page(self, driver, query):
        self.enter_query(query)
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
        assert FilterCourses(driver)

    def _get_url(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: "search" in driver.current_url
        )
        return self.driver.current_url

    def is_correct_page(self, hint):
        parsed_url = urlparse(self._get_url())
        decoded = urllib.parse.unquote(parsed_url.query)
        query_params = urllib.parse.parse_qs(decoded)
        value = query_params.get("search", [None])[0]
        return value.lower() == hint.lower()

    def is_english(self, text):
        return all(char.isalpha() and char.isascii() for char in text)

    def more_then_4_consonants(self, text, n=4):
        consonants = "bcdfghjklmnpqrstvwxyz"

        consecutive_count = 0
        for char in text:
            if char in consonants:
                consecutive_count += 1
                if consecutive_count >= n:
                    return True
            else:
                consecutive_count = 0
        return False

    def to_russian_layout(self, text):
        eng_to_rus = {
            "a": "ф",
            "b": "и",
            "c": "с",
            "d": "в",
            "e": "у",
            "f": "а",
            "g": "п",
            "h": "р",
            "i": "ш",
            "j": "о",
            "k": "л",
            "l": "д",
            "m": "ь",
            "n": "т",
            "o": "щ",
            "p": "з",
            "q": "й",
            "r": "к",
            "s": "ы",
            "t": "е",
            "u": "г",
            "v": "м",
            "w": "ц",
            "x": "ц",
            "y": "н",
            "z": "я",
        }

        return "".join([eng_to_rus.get(char, char) for char in text])

    def process_text(self, text):
        if self.is_english(text.lower()) and self.more_then_4_consonants(text.lower()):
            return self.to_russian_layout(text)
        return text
