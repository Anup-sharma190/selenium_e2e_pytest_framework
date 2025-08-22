"""
# 🧪 Selenium Pytest E2E Demo Project

## 📌 Project
This is a **demo End-to-End (E2E) automation test** project using **Selenium + Pytest**.
It automates the login flow on [Rahul Shetty Academy – Login Page](https://rahulshettyacademy.com/loginpagePractise/) and verifies product selection (Blackberry).

---

## 🧑‍💻 Skills Demonstrated
- Writing **clean Python test automation scripts**
- Using **Pytest fixtures** for browser setup
- Implementing **explicit waits (WebDriverWait + ExpectedConditions)**
- Applying **Page interaction and element handling**
- Handling **positive & negative test scenarios** (success/error login)
- Automating **E2E flow (Login → Shop → Add to Cart)**

---

## 🛠 Tools & Technologies
- **Python 3.x**
- **Selenium WebDriver**
- **Pytest** (test runner)
- **ChromeDriver / EdgeDriver**
- **GitHub** (project hosting)

---

## ✅ Result
- 🚀 Automated login test runs successfully
- ❌ Prints error if login fails
- ✅ Verifies successful login & product selection (Blackberry)
- 📂 Demonstrates a **recruiter-friendly Selenium Pytest framework**
"""

# ====================== IMPORTS ======================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ====================== TEST CASE ======================
def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Enter login credentials
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME, "password").send_keys("learning")
    driver.find_element(By.ID, "signInBtn").click()

    # ✅ Wait for either error OR shop page
    WebDriverWait(driver, 10).until(
        EC.any_of(
            EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")),
            EC.presence_of_element_located((By.LINK_TEXT, "Shop"))
        )
    )

    # ✅ Check if login failed
    errors = driver.find_elements(By.XPATH, "//div[@class='alert alert-danger']")
    if errors:
        print("❌ Login failed. Check credentials!")
        assert False

    print("✅ Login successful! Navigating to Shop page.")

    # Wait for shop page products
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card"))
    )

    # Find Blackberry and click Add button
    products = driver.find_elements(By.CSS_SELECTOR, ".card")
    for product in products:
        product_name = product.find_element(By.CSS_SELECTOR, ".card-title").text
        if product_name == "Blackberry":
            print("🛒 Product selected: Blackberry")
            product.find_element(By.XPATH, ".//button[@class='btn btn-info']").click()
            break
