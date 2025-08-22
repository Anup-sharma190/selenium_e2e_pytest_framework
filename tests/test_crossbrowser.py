from selenium.webdriver.common.by import By

def test_google_title(browser):
    driver = browser
    driver.get("https://www.google.com")
    assert "Google" in driver.title
