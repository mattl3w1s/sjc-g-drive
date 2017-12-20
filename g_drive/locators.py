from selenium.webdriver.common.by import By

class Locators(object):
    """A class for login page locators. All login page locators should be
    added here.
    """
    USER_NAME_LOCATOR = (By.NAME, 'username')
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.ID, "btnSubmit_6")

    SESSION_CHECKBOX_LOCATOR = (By.ID,"postfixSID_1")
    CLOSE_SESSION_LOCATOR = (By.NAME, "btnContinue")


    LOGIN_CONFIRMATION_LOCATOR = (By.ID, "")

    UPLOAD_BUTTON_LOCATOR = (By.ID,"input_wfb_4")
    UPLOAD_SUBMIT_LOCATOR = (By.ID, "btnUpload_7")

    FILE_ID_LOCATORS = [
        (By.ID,"file1_4"),
        (By.ID,"file2_2"),
        (By.ID,"file3_2"),
        (By.ID,"file4_2"),
        (By.ID,"file5_2")
    ]

