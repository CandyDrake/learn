import pytest
from module_1.PageObject.spa_landing import Landing
from module_1.PageObject.spa_callback_forms import DATA


@pytest.mark.parametrize("name, phone, email", DATA)
def test_callback_invalid(driver, name, phone, email):
    landing = Landing(driver)
    landing.open()
    landing.callback_form.scroll(driver)
    landing.callback_form.send_data(name, phone, email)
    landing.callback_form.click_submit_button()
    landing.callback_form.is_validation_error()


def test_callback_valid(
    driver, name="testing", phone="+9817654321", email="test1@mail.ru"
):
    landing = Landing(driver)
    landing.open()
    landing.callback_form.scroll(driver)
    landing.callback_form.send_data(name, phone, email)
    landing.callback_form.click_submit_button()
    landing.callback_form.close_modal_window()
    assert landing.callback_form.is_callback_sent()
