"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        """
        Initializes WebDriverFactory class
        :param browser:
        """
        self.browser = browser

    """
    Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
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

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)

        return driver
