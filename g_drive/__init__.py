import math
from selenium import webdriver
from g_drive.locators import Locators

try:
    from g_drive.sensitive import USER_NAME, PASSWORD
except:
    USER_NAME = ''
    PASSWORD = ''

class Site(object):

    G_DRIVE_MAIN_PAGE_URL = "https://secure.sjcd.edu/dana/fb/smb/wfb.cgi?t=p&v=resource_1432750742.394407.2&si=0&ri=0&pi=0"
    current_page = "https://secure.sjcd.edu"

    def __init__(self,download_destination="./data"):
        options = webdriver.ChromeOptions()
        profile = {"plugins.plugins_list": 
                [
                    {"enabled":False,"name":"Chrome PDF Viewer"}
                ],
                "download.default_directory" : download_destination}
        options.add_experimental_option("prefs",profile)
        self.driver = webdriver.Chrome(options = options)
        self.driver.get(self.current_page)
        self._login()

    def _login(self):
        """
        Login to the Compliance Assist site using credentials imported from
        sensitive module (which is .gitignored).
        """
        # Fetch login fields and submit button
        username_field = self.driver.find_element(
            *Locators.USER_NAME_LOCATOR)
        password_field = self.driver.find_element(
            *Locators.PASSWORD_LOCATOR)
        submit_button = self.driver.find_element(
            *Locators.SUBMIT_LOCATOR)
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
                *Locators.SESSION_CHECKBOX_LOCATOR
            )
        close_button = self.driver.find_element(
                *Locators.CLOSE_SESSION_LOCATOR
            )
        session_toggle.click()
        close_button.click()

    def goto(self,url):
        """
        Navigate to url.
        
        Note: this can be used to download files.
        """
        try:
            self.driver.get(url)
            self.current_page = url
        except Exception as e:
            raise e

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

    def upload_files(self,source_directory,file_list,destination_directory=""):
        print('\tUploading files...')
        no_files = len(file_list)
        no_cycles = int(math.floor(no_files/5.0))
        remainder = no_files%5

        for i in range(no_cycles):
            print("test!")
            self._find_element(Locators.UPLOAD_BUTTON_LOCATOR).click()
            for j in range(5):
                file_field = self._find_element(Locators.FILE_ID_LOCATORS[j])
                file_field.send_keys(source_directory+"/"+file_list[5*i+j])
            self._find_element(Locators.UPLOAD_SUBMIT_LOCATOR).click()
            self._close_window_when_done()
        
        if(remainder):
            self._find_element(Locators.UPLOAD_BUTTON_LOCATOR).click()
            for j in range(remainder):
                file_field = self._find_element(Locators.FILE_ID_LOCATORS[j])
                file_field.send_keys(source_directory+"/"+file_list[5*no_cycles+j])
            self._find_element(Locators.UPLOAD_SUBMIT_LOCATOR).click()
            self._close_window_when_done()
    
    def create_folder(folder_name):
        # TODO: Implement this method.
        pass

    def _close_window_when_done(self):
        # TODO: Implement this method.
        pass

    def close(self):
        self.driver.close()
