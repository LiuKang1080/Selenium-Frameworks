"""
Package: Base

WebDriver Factory class implementation.
Creates a webdriver instance based on various browser configurations.

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        """
        Initialize WebDriverFactory class.
        :param browser: specified browser.
        """
        self.browser = browser

    """
    Set Chrome Driver and Iexplorer environment based on OS. 

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        Iexplore.exe follows the same structure as Chrome setup.
        PREFERRED: Set the PATH environment variables on the machine where browser will be executed.
    """

    def get_webdriver_instance(self):
        """
        Get WebDriver Instance based on the browser configuration.
        :return: Webdriver instance.
        """
        base_url = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
            print("Running test on IE")
        elif self.browser == "firefox":
            # Set Firefox driver
            driver = webdriver.Firefox()
            print("Running test on Firefox")
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
            print("Running test on Chrome")
        else:
            driver = webdriver.Chrome()
            print("Running test on Chrome")

        # Setting Driver Implicit wait time for all elements on a web page.
        driver.implicitly_wait(5)
        # Maximize the window.
        driver.maximize_window()
        # Load browser with the provided URL.
        driver.get(base_url)

        return driver
