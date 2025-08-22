"""
Demo Project: Selenium PyTest Cross-Browser Framework
-----------------------------------------------------

Project Owner: Anup Sharma
Skills Showcased:
- Python Programming
- PyTest Automation Framework
- Selenium WebDriver
- Cross-Browser Testing (Chrome, Firefox, Edge)
- Fixture & Command-Line Integration

Tools Used:
- Python 3
- PyTest
- Selenium
- WebDriver Manager (Optional)

Description:
This file (conftest.py) is the configuration file for PyTest.
It adds a command-line option `--browser_name` that allows
test execution on multiple browsers. Supported browsers are:
    - Chrome
    - Firefox
    - Microsoft Edge

Result:
- Enables **cross-browser compatibility testing** with a single command.
- Promotes **reusability & modular framework design**.
- Recruiter-friendly demonstration of Selenium + PyTest integration.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser option: chrome, firefox, or edge"
    )


@pytest.fixture()
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService())

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())

    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService())

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()
