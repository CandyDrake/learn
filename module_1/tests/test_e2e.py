from module_1.steps.steps import Steps


def test_e2e(driver):
    search = "Автотесты на Python"
    steps = Steps(driver)
    steps.open_landing()
    steps.find_course(search)
    steps.filter_for_newbies()
    steps.select_course()
    steps.is_course_price()
