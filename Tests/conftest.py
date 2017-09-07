import pytest
from Base.webdriver_factory import WebDriverFactory
from Pages.home_test_package.login_page import LoginPage


@pytest.yield_fixture(scope="class")
def set_up(request, browser):
    print("Running method level Set Up")
    webdriver_factory = WebDriverFactory(browser)
    driver = webdriver_factory.get_webdriver_instance()
    login_page = LoginPage(driver)
    login_page.login("test@gmail.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running method level Tear Down")


@pytest.yield_fixture(scope="class")
def one_time_setup():
    print("Running one time setUp")
    yield
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
