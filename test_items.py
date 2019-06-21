from selenium.webdriver.remote.errorhandler import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_cart_button(browser):
    browser.get(link)
    try:
        assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")

    except NoSuchElementException:
        assert False, "ButtonError"
