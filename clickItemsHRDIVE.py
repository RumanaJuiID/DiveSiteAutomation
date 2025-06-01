from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings


warnings.filterwarnings("ignore", category=UserWarning)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://www.hrdive.com/")

    wait = WebDriverWait(driver, 15)

    # Wait for the desktop menu bar to load
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.desktop-menu-main")))

    # Find all top-level menu items
    nav_items = driver.find_elements(By.CSS_SELECTOR, "ul.desktop-menu-main > li > a")

    print(f"Found {len(nav_items)} top nav items.")

    for i in range(len(nav_items)):

        nav_items = driver.find_elements(By.CSS_SELECTOR, "ul.desktop-menu-main > li > a")
        nav_text = nav_items[i].text.strip()
        print(f"Clicking nav item: {nav_text or '[no text]'}")

        nav_items[i].click()
        time.sleep(2)


        print(f"Now at: {driver.title}")


        driver.get("https://www.hrdive.com/")
        time.sleep(2)

finally:
    driver.quit()
