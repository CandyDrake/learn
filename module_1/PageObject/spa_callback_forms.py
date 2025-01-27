import time
import keyboard
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


DATA = [
    ("test_1", "+9004354321", "test_2@gmail.ru"),
    ("test", "+90076543", "test_3@gmail.ru"),
    ("test", "+9007654321", "test@gmail"),
]


class CallbackForm(object):
    CALLBACK_FORM = (By.XPATH, "//section[@class='subscribe subscribe-form']")
    CALLBACK_BUTTON = (By.XPATH, "//button[@type='submit']")
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    PHONE_FIELD = (By.XPATH, "//input[@name='phone']")
    MAIL_FIELD = (By.XPATH, "//input[@name='email']")
    SUBMIT_INFO = (By.XPATH, "//p[@class='subscribe__message']")
    NAME_ERROR = (
        By.XPATH,
        "//div[@class='ui-field ui-field--grey ui-field--active ui-field--error']",
    )
    PHONE_ERROR = (
        By.XPATH,
        "//div[@class='ui-phone-input ui-phone-input--grey ui-phone-input--active ui-phone-input--error']",
    )
    MAIL_ERROR = (
        By.XPATH,
        "//div[@class='ui-field ui-field--grey ui-field--active ui-field--error']",
    )

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def scroll(self, driver):
        form = self.driver.find_element(*self.CALLBACK_FORM)
        actions = ActionChains(driver)
        actions.move_to_element(form).perform()
        return self

    def send_data(self, name, phone, email):
        name_slot = self.driver.find_element(*self.NAME_FIELD)
        name_slot.clear()
        name_slot.send_keys(name)
        phone_slot = self.driver.find_element(*self.PHONE_FIELD)
        phone_slot.clear()
        phone_slot.send_keys(phone)
        mail_slot = self.driver.find_element(*self.MAIL_FIELD)
        mail_slot.clear()
        mail_slot.send_keys(email)

    def click_submit_button(self):
        self.driver.find_element(*self.CALLBACK_BUTTON).click()
        time.sleep(3)

    @staticmethod
    def close_modal_window():
        keyboard.press("esc")

    def is_callback_sent(self):
        return "Спасибо за заявку!" in self.driver.find_element(*self.SUBMIT_INFO).text

    def is_validation_error(self):
        try:
            return (
                "Неправильная электронная почта"
                in self.driver.find_element(*self.MAIL_ERROR).text
                or "Неправильный номер телефона"
                in self.driver.find_element(*self.PHONE_ERROR).text
                or "Поле не должно содержать цифры"
                in self.driver.find_element(*self.NAME_ERROR).text
            )
        except NoSuchElementException:
            return False
