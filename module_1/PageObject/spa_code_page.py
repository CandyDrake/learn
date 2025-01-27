from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory
import time


class CodePage(PageFactory):
    URL = "https://skillbox.ru/code/"

    locators = {
        "course_group_button": (
            By.XPATH,
            f"//span[contains(text(), 'IT-инфраструктура')]",
        ),
        "professions_title": (By.XPATH, "//h2[contains(text(), 'Профессии')]"),
        "other_professions_button": (
            By.XPATH,
            "//button[contains(@class, 'ui-load-more courses-block')][contains(text(), 'професс')]",
        ),
        "professions_elements": (
            By.XPATH,
            "(//section[@class='courses-block courses-section__block'])[1]//a[@class='ui-product-card-main__wrap']",
        ),
    }

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def open(self):
        self.driver.get(self.URL)
        return self

    def scroll(self, button):
        actions = ActionChains(self.driver)
        actions.move_to_element(button).perform()
        return self

    def other_professions(self):
        try:
            while True:
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.other_professions_button)
                )
                button.click()
                time.sleep(1)
        except Exception:
            print("Кнопка не найдена, все элементы на странице")

    def block_count(self):
        elements = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*self.locators["professions_elements"])
        )
        return len(elements)

    def profession_count(self):
        title_text = self.professions_title.text
        count = [char for char in title_text if char.isdigit()]
        return int("".join(count)) if count else 0

    def filter_professions(self):
        filter_button = self.course_group_button
        self.scroll(filter_button)
        filter_button.click()
        time.sleep(3)

    @staticmethod
    def is_filtred(before_filter, after_filter):
        return before_filter > after_filter

    def is_correct_url(self):
        return self.driver.current_url.endswith("it-infrastructure/")
