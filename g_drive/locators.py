from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should be
    added here.
    """
    USER_NAME_LOCATOR = (By.NAME, 'username')
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.ID, "btnSubmit_6")

    SESSION_CHECKBOX_LOCATOR = (By.ID,"postfixSID_1")
    CLOSE_SESSION_LOCATOR = (By.NAME, "btnContinue")


    CONFIRMATION_LOCATOR = (By.ID, "")