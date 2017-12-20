from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should be
    added here.
    """
    USER_NAME_LOCATOR = (By.NAME, 'username')
    PASSWORD_LOCATOR = (By.NAME, "password")

    CONFIRMATION_LOCATOR = (By.ID, "")