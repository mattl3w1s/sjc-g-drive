from selenium import webdriver
from g_drive.locators import LoginPageLocators

try:
    from g_drive.sensitive import USER_NAME, PASSWORD
except:
    USER_NAME = ''
    PASSWORD = ''

class Site(object):

    G_DRIVE_MAIN_PAGE_URL = "https://secure.sjcd.edu/dana/fb/smb/wfb.cgi?t=p&v=resource_1432750742.394407.2&si=0&ri=0&pi=0"

    def __init__(self,download_destination="./data"):
        options = webdriver.ChromeOptions()
        profile = {"plugins.plugins_list": 
                [
                    {"enabled":False,"name":"Chrome PDF Viewer"}
                ],
                "download.default_directory" : download_destination}
        options.add_experimental_option("prefs",profile)
        self.driver = webdriver.Chrome(options = options)
        self.driver.get("https://secure.sjcd.edu")
        self._login()

    def _login(self):
        """
        Login to the Compliance Assist site using credentials imported from
        sensitive module (which is .gitignored).
        """
        # Fetch login fields and submit button
        username_field = self.driver.find_element(
            *LoginPageLocators.USER_NAME_LOCATOR)
        password_field = self.driver.find_element(
            *LoginPageLocators.PASSWORD_LOCATOR)
        submit_button = self.driver.find_element(
            *LoginPageLocators.SUBMIT_LOCATOR)
        # Send username and password to fields
        username_field.send_keys(USER_NAME)
        password_field.send_keys(PASSWORD)

        # Click submit button
        submit_button.click()
        
        # If G-drive complains of multiple sessions, click through:
        try:
            self._click_through_session_complaint()
        except:
            pass
        self.goto(self.G_DRIVE_MAIN_PAGE_URL)


    def _click_through_session_complaint(self):
        session_toggle = self.driver.find_element(
                *LoginPageLocators.SESSION_CHECKBOX_LOCATOR
            )
        close_button = self.driver.find_element(
                *LoginPageLocators.CLOSE_SESSION_LOCATOR
            )
        session_toggle.click()
        close_button.click()

    def goto(self,url):
        """
        Navigate to url.
        
        Note: this can be used to download files.
        """
        self.driver.get(url)

    def download(self, url):
        """
        Method to download files at supplied `url` from Compliance Assist and
        save file in local `destination`. 
        
        Note: this method utilizes chromes automatic downloading for files. 
        If the url points to a page chrome wants to load, it will load it.
        """
        self.goto(url)

    def _find_element(self,LOCATOR):
        """
        Exposes driver for the purpose of locating elements on site.
        """
        return self.driver.find_element(*LOCATOR)

    def close(self):
        self.driver.close()
