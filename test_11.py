import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class WebDriverHelper:
    def __init__(self, url):
        self.url = url
        self.driver = self._initialize_driver()

    def _initialize_driver(self):
        """Initializes the Chrome WebDriver with specific options."""
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")  # Optional, set window size
        options.add_argument('--start-maximized')
        options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data/Profile 1')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def open_url(self):
        """Opens the initial URL."""
        self.driver.get(self.url)
        self.wait_for_page_to_load()
        sleep(10)
    def wait_for_page_to_load(self):
        """Waits until the page has fully loaded by checking for specific elements."""
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Page is fully loaded.")

    def modify_url_without_reload(self, new_url):
        """Modifies the URL without reloading the page."""
        try:
            self.driver.execute_script(f"window.history.pushState(null, '', '{new_url}');")
            print(f"Successfully modified the URL to: {new_url}")
        except Exception as e:
            print(f"Failed to modify URL: {e}")

    def switch_url(self, initial_url, modified_url):
        """Switches between two URLs of the same website."""
        self.open_url()  # Open the initial URL
        time.sleep(2)  # Allow some time for page to load
        self.modify_url_without_reload(modified_url)  # Modify the URL to the new one
        sleep(10)
        self.driver.refresh()
        sleep(5)
        # Ensure the page is loaded after URL change
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print(f"Successfully switched to URL: {modified_url}")
        
        # Explicitly set the window size and position to avoid it hiding
        self.driver.set_window_position(0, 0)  # Position at the top-left of the screen
        self.driver.set_window_size(1920, 1080)  # Set the size of the window (adjust as needed)

    def update_campaign(self):
        try:
            # Wait for the button to be clickable
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='gridcell']//button[@aria-haspopup='true']"))
            )
            button.click()
            sleep(5)
            #bui301val-1
            button_2 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/ul/button[2]"))
            )
            button_2.click()

            button_3 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/form/div[3]/button"))
            )
            button_3.click()
            # /html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/form/div[3]/button
            sleep(100)            
            print("Simplified selector button clicked successfully!")
        except Exception as e:
            print(f"Error clicking the button: {e}")

if __name__ == "__main__":
    initial_url = "https://merchants.ubereats.com/manager/orders/active"
    modified_url = "https://merchants.ubereats.com/manager/marketing/campaigns"

    # Initialize WebDriverHelper and switch between URLs
    browser = WebDriverHelper(initial_url)
    browser.switch_url(initial_url, modified_url)
    browser.update_campaign()
