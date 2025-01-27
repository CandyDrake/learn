import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_argument("--headless")
options.add_argument("window-size=1600,1400")

#
# @pytest.fixture(scope="module", autouse=True)
# def driver():
#     # Instantiate the WebDriver (in this case, using Chrome)
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()), options=options
#     )
#     yield driver
#     # Close the WebDriver
#     driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChrOpt
from selenium.webdriver.firefox.options import Options as FireOpt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import logging
logging.basicConfig(encoding='utf-8')

"""Для работы с selenoid"""


# @pytest.fixture(scope="class")
# def driver(pytestconfig):
#     options = ChrOpt()
#     # options.add_argument('--headless')
#     options.page_load_strategy = 'normal'
#     driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=options)
#     # driver.implicitly_wait(30)
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="class")
def driver(pytestconfig):
    chromedriver_path = "C:/Users/tanai/Downloads/operadriver_win64/operadriver_win64/operadriver.exe"  # Укажите путь к ChromeDriver

    options = ChromeOptions()
    options.add_argument('--start-maximized')  # Запуск в максимальном размере
    options.add_argument('--no-sandbox')  # Если нужно
    options.add_argument('--disable-dev-shm-usage')  # Если нужно


    # Создание экземпляра WebDriver для Chrome
    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
