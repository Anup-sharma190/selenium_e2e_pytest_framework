from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_e2e(browser):
    driver = browser
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME, "password").send_keys("learning")
    driver.find_element(By.ID, "signInBtn").click()

    WebDriverWait(driver, 10).until(
        EC.any_of(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")),
            EC.presence_of_element_located((By.LINK_TEXT, "Shop"))
        )
    )

    errors = driver.find_elements(By.XPATH, "//div[@class='alert alert-danger']")
    if errors:
        assert False, "Login failed"

    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card"))
    )

    for product in products:
        name = product.find_element(By.CSS_SELECTOR, ".card-title").text
        if name == "Blackberry":
            product.find_element(By.XPATH, ".//button[@class='btn btn-info']").click()
            break
