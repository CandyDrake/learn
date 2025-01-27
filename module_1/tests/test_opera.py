from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def test_opera():
    operadriver_path = "C:/Users/tanai/Downloads/operadriver_win64/operadriver_win64/operadriver.exe"
    opera_binary_path = "C:/Program Files/Opera/opera.exe"  # Убедитесь, что указали правильный путь

    options = Options()
    options.binary_location = opera_binary_path
    options.add_argument('--start-maximized')

    # Используйте webdriver.Chrome для запуска Opera
    service = ChromeService(executable_path=operadriver_path)
    driver = webdriver.Chrome(service=service, options=options)



    driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_opera()
