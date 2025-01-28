import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

# Path to the folder containing the extension
extension_path = r'proxy_auth_plugin.zip'

# Chrome options
options = uc.ChromeOptions()

# Add extension for proxy authentication
options.add_extension(extension_path)

# Proxy settings
proxy_address = "45.135.38.245"
proxy_port = "50100"

# Set proxy server in Chrome options
options.add_argument(f'--proxy-server=http://{proxy_address}:{proxy_port}')

# Additional options
# options.add_argument("--incognito")  # Run in incognito mode
options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
options.add_argument("--start-maximized")  # Optional: Start maximized

# Initialize Chrome service
chromedriver_path = r"chromedriver.exe"  # Replace with your actual path
service = Service(chromedriver_path)

# Start undetected ChromeDriver with proxy authentication extension
driver = uc.Chrome(service=service, options=options,version_main=130)

# Navigate to a test site
driver.get("https://www.google.com/maps")

# Wait for the page to load
sleep(100)

# Print the body content of the page
print(driver.find_element(By.TAG_NAME, "body").text)

# Close the browser
driver.quit()
