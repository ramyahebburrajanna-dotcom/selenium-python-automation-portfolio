from utils.driver_setup import get_driver
from pages.login_page import LoginPage
import time

# Step 1: open browser
driver = get_driver()

# Step 2: open website
driver.get("https://www.saucedemo.com")

# Step 3: create object of login page
login = LoginPage(driver)

# Step 4: perform login
login.login("standard_user", "secret_sauce")

time.sleep(3)

print("Login Test Passed")

# Step 5: close browser
driver.quit()