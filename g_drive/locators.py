from selenium.webdriver.common.by import By

class Locators(object):
    """A class for site locators. All locators should be
    added here.
    """

    # Login form locators
    USER_NAME_LOCATOR = (By.NAME, 'username')
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.ID, "btnSubmit_6")

    # "Too many sessions" complaint locators
    SESSION_CHECKBOX_LOCATOR = (By.ID,"postfixSID_1")
    CLOSE_SESSION_LOCATOR = (By.NAME, "btnContinue")

    LOGIN_CONFIRMATION_LOCATOR = (By.ID, "")

    # 
    UPLOAD_BUTTON_LOCATOR = (By.ID,"input_wfb_4")
    UPLOAD_SUBMIT_LOCATOR = (By.ID, "btnUpload_7")

    FILE_ID_LOCATORS = [
        (By.ID,"file1_4"),
        (By.ID,"file2_2"),
        (By.ID,"file3_2"),
        (By.ID,"file4_2"),
        (By.ID,"file5_2")
    ]

    CREATE_FOLDER_LOCATOR = (By.ID, "input_wfb_5")
    FOLDER_NAME_LOCATOR = (By.ID, "folder_4")
    FOLDER_SUBMIT_BUTTON_LOCATOR = (By.ID, "create_6") 

