import time
import pytest
from module_1.PageObject.spa_landing import Landing


@pytest.mark.parametrize(
    "query", ["программир", "тестирование", "programming", "ghjuhfvvbh"]
)
def test_hints(driver, query):
    landing = Landing(driver)
    landing.open()
    landing.search_form.open_form()
    landing.search_form.enter_query(query)
    new_query = landing.search_form.process_text(query)
    print(new_query)
    assert landing.search_form.relevant_hints(new_query)


@pytest.mark.parametrize("query", ["дизайн", "программирование"])
def test_url(driver, query):
    landing = Landing(driver)
    landing.open()
    landing.search_form.open_form()
    landing.search_form.go_to_course_page(driver, query)
    landing.search_form.is_correct_page(query)
