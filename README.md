# Selenium-Frameworks
Demo of Selenium Frameworks. Automation testing on various web pages for the website 'https://letskodeit.teachable.com/'.
## Prerequisites
* Python (3.5.3)
* Selenium (3.4.1 or higher)
* PyTest 
* PyTest - HTML
* Unittest
* ddt (Data-Driven / Decorated Tests)
* chromedriver.exe
* gekodriver.exe
* IEDriver.exe
## Installing
Fork or clone project for Zip file.

Install modules using ```$ pip install```

* Download Chrome Driver: https://sites.google.com/a/chromium.org/chromedriver/
* Download InternetExplorer Driver: http://selenium-release.storage.googleapis.com/index.html?path=3.4/
* Download GekoDriver: https://github.com/mozilla/geckodriver/releases

### OS Environment
Ensure that the directory path for these web browser drivers are placed as Environment Variables for the system.

## Running Tests 
__login_page.py__ and __register_courses.py__ are the main scripts that will run automated Test Cases for letskodeit.com

Run tests from command line example:

```
$ py.test -s -v Tests\home_test_package\login_tests.py
```
additional parameters can be added to specify different browsers (chrome, firefox or ie):
```
$ py.test -s -v Tests\home_test_package\login_tests.py --browser firefox
```
