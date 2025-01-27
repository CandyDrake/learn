from module_1.PageObject.spa_review_page import ReviewPage


def test_review(driver):
    review_page = ReviewPage(driver)
    review_page.get()
    review_page.is_reviews()
