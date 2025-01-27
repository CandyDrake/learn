from module_1.PageObject.spa_code_page import CodePage
from module_1.PageObject.spa_profession_page import ProfessionPage


def test_filter_counter(driver):
    code_page = CodePage(driver)
    code_page.open()
    before_filter = code_page.profession_count()
    code_page.filter_professions()
    prof_page = ProfessionPage(driver)
    after_filter = prof_page.profession_count()
    prof_page.is_filtred(before_filter, after_filter)


def test_filter_correct_number(driver):
    code_page = CodePage(driver)
    code_page.open()
    code_page.filter_professions()
    prof_page = ProfessionPage(driver)
    elements_count = prof_page.other_professions()
    title_count = prof_page.profession_count()
    prof_page.is_correct_number(elements_count, title_count)


def test_filter_navigation(driver):
    code_page = CodePage(driver)
    code_page.open()
    code_page.filter_professions()
    code_page.is_correct_url()
