from selenium.webdriver.support.wait import WebDriverWait
from module_1.PageObject.spa_landing import Landing


class Steps:
    def __init__(self, driver):
        self.driver = driver

    def open_landing(self):
        self.landing = Landing(self.driver).open()

    def find_course(self, query):
        self.landing.search_form.open_form()
        self.courses = self.landing.search_form.go_to_course_page(self.driver, query)

    def filter_for_newbies(self):
        self.landing.courses_page.click_newbies()

    def select_course(self):
        self.landing.courses_page.click_profession()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_course_price(self):
        assert self.landing.qa.course_price()
