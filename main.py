import os
import re
import requests
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
from database.data_json import JsonDataHandler
from datetime import datetime 
import logging
import traceback
from selenium.webdriver.common.proxy import Proxy, ProxyType


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("just_eat_scraper.log"),
        logging.StreamHandler()
    ]
)

class WebDriverManager:
    def __init__(self, url):
        self.url = url
        self.driver = self.instantiate_driver()

    def instantiate_driver(self):
        logging.info(f"Initializing WebDriver for URL: {self.url}")
        print("In Just Eat")
        # Set up proxy
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = "45.135.38.245:50100"  # Replace with your proxy
        proxy.ssl_proxy = "45.135.38.245:50100"   # Replace with your proxy

        # Add proxy to capabilities
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities.update(proxy.to_capabilities())

        options = webdriver.ChromeOptions()
        service = Service("chromedriver.exe")
        # options.add_argument("--headless")  # Run Chrome in headless mode
        # khalid05kKL:KrGQkpmMiQ@45.135.38.245:50100
        # proxy = "45.135.38.245:50100"
        # options.add_extension("proxy_auth_plugin.zip")
        options.add_argument("--proxy-server=http://45.135.38.245:50100")  # Use your proxy
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Optional, for better performance
        options.add_argument("--window-size=1920x1080")  # Optional, set window size
        # options.add_argument("--window-position=-2400,-2400")
        # options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data/Profile 2')
        
        options.add_argument('--user-data-dir=D:/.MoreLogin/cache/chrome_1859162994976038912/Default')

        # Use a unique temp directory for each session
        # temp_dir = tempfile.mkdtemp()
        # options.add_argument(f"--user-data-dir={temp_dir}")
        # base_download_dir = "D:\\work\\automation\\free_map_tools\\final\\Location_analyzer\\app\\downloaded_csv"

        # prefs = {"download.default_directory" :base_download_dir}
        # options.add_experimental_option("prefs",prefs)

        # service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.url)
        logging.info(f"WebDriver successfully initialized for {self.url}")
        sleep(2)
        driver.execute_script("document.body.style.zoom='50%'")
        return driver

    def quit(self):
        logging.info("Quitting the WebDriver session.")
        self.driver.quit()

    def get_orders(self):
        logging.info("Fetching orders...")
        orders = []
        try:
                    # Parse the HTML
            # Find the div containing orders
            sleep(10)
            # orders_div = self.driver.find_element(By.XPATH, "//div[@class='flex flex-col relative order-3 md:order-1 w-full md:w-8/12 lg:w-9/12']")

            # # Use BeautifulSoup to parse the innerHTML of the div
            # soup = BeautifulSoup(orders_div.get_attribute('innerHTML'), 'html.parser')
            # Wait for the element to be present
            # wait = WebDriverWait(self.driver, 100)  # Wait for up to 10 seconds
            orders_div = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='flex flex-col relative order-3 md:order-1 w-full md:w-8/12 lg:w-9/12']")) #This is a dummy element
            )
            # orders_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex flex-col relative order-3 md:order-1 w-full md:w-8/12 lg:w-9/12']")))
            soup = BeautifulSoup(orders_div.get_attribute('innerHTML'), 'html.parser')
            # Now you can proceed to extract data using BeautifulSoup
            print(soup.prettify())
            order_divs = soup.find_all("div", class_="flex flex-col pb-6 border-b border-grey-30 last:border-b-0")
            logging.info(f"Found {len(order_divs)} orders.")
            # print(order_divs.prettify())
            for order_div in order_divs:

                # Extract the order date
                # sleep(10)
                order_date_text = order_div.find('span', {'data-cy': 'orderDate'}).get_text(strip=True)
                order_date = datetime.strptime(order_date_text + " 2024", "%d %b %Y")  # Add the year

                # Find all order cards
                order_cards = order_div.find_all('div', class_='card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed')

                print(order_cards)
                # Extract data for each order
                for card in order_cards:
                    time = card.find('span', {'data-cy': 'orderTime'}).get_text(strip=True)
                    order_id = card.find('span', {'data-cy': 'orderId'}).get_text(strip=True)
                    payment_type = card.find('span', {'data-cy': 'orderPaymentType'}).get_text(strip=True)
                    service_type = card.find('span', {'data-cy': 'orderServiceType'}).get_text(strip=True)
                    status = card.find('span', {'data-cy': 'orderStatus'}).get_text(strip=True)
                    delivery_price = card.find('span', {'data-cy': 'deliveryPrice'}).get_text(strip=True)
                    order_price = card.find('span', {'data-cy': 'orderPrice'}).get_text(strip=True)
                    

                    # Locate the clickable order_id element using Selenium
                    # clickable_element = self.driver.find_element(By.XPATH, f"//span[@data-cy='orderId' and text()='{order_id}']")
                    print("-----------------------------order id",order_id)
                    # Wait for the element to be present in the DOM
                    self.driver.implicitly_wait(10)
                    # clickable_element = WebDriverWait(self.driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, "//span[@data-cy='orderId' and text()='#441965622']"))
                    # )
                    # clickable_element = self.driver.find_element(By.CSS_SELECTOR, f"span[data-cy='orderId']:contains('{order_id}')")
                    # Alternatively, using CSS Selector
                    # Wait for the element to be located (using XPath)
                    order_id=order_id.replace('#', '')

                    order_id_element_xpath = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"//span[@data-cy='orderId' and contains(text(), '{order_id}')]"))
                    )


                    # Extract the text of the order ID
                    order_id = order_id_element_xpath.text
                    # If you used CSS selector instead, you would use:
                    # order_id = order_id_element_css.text

                    print("Order ID:", order_id)

                    # $x("//span[@data-cy='orderId' and contains(text(), '441965622')]")

                    logging.info(f"Extracted Order ID: {order_id}")
                    # Append extracted data as a dictionary
                    orders.append({
                        'date': order_date,  # Include the parsed date
                        'time': time,
                        'order_id': order_id,
                        'payment_type': payment_type,
                        'service_type': service_type,
                        'status': status,
                        'delivery_price': delivery_price,
                        'order_price': order_price,
                        'clickable_element': order_id_element_xpath,  # Add the clickable element
                    })
            # Sort the orders by date
            orders = sorted(orders, key=lambda x: x['date'])
            logging.info(f"Successfully fetched and sorted {len(orders)} orders.")
            return orders
        except TimeoutException as e:
            logging.error("TimeoutException occurred while waiting for order elements: %s", e)
        except NoSuchElementException as e:
            logging.error("NoSuchElementException: Element not found: %s", e)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            logging.debug(traceback.format_exc())

    def click_on_order(self,order_id):
        logging.info(f"Attempting to click on order with ID: {order_id}")
        try:
            order_id_element_xpath = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"//span[@data-cy='orderId' and contains(text(), '{order_id}')]"))
                    ).click()
            logging.info(f"Successfully clicked on order with ID: {order_id}")
            # element.click()
            sleep(5)
            orders_div = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div[1]")

            # Use BeautifulSoup to parse the innerHTML of the div
            soup = BeautifulSoup(orders_div.get_attribute('innerHTML'), 'html.parser')
            print(soup)
            print("#######################################################################################################################")
            return soup
        except TimeoutException as e:
            logging.error(f"TimeoutException: Failed to locate order {order_id}: {e}")
        except NoSuchElementException as e:
            logging.error(f"NoSuchElementException: Order ID {order_id} not found: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while clicking on order {order_id}: {e}")
            logging.debug(traceback.format_exc())        

    def extract_meal_details(self,soup):
        logging.info("Extracting meal details...")
        order_meal_details = []
        try:
            # Find all meal blocks
            meal_blocks = soup.find_all('div', class_=lambda x: x and 'mt-5' in x and 'md:px-4' in x and 'mb-6' in x)

            for meal in meal_blocks:
                # Extract main meal details
                meal_name = meal.find('span', {'data-cy': 'orderDetailsItemName'}).text.strip()
                
                # Clean and parse meal price
                meal_price_text = meal.find('span', {'data-cy': 'orderDetailsItemPrice'}).text.strip()
                meal_price_text = meal_price_text.replace('\xa0', '')  # Remove non-breaking spaces
                meal_price_match = re.search(r"[\d\.]+", meal_price_text)  # Extract numeric value
                
                if meal_price_match:
                    meal_price = float(meal_price_match.group())
                else:
                    meal_price = 0.0  # Default price if extraction fails

                quantity = meal.find('span', {'data-cy': 'orderDetailsItemQuantity'}).text.strip()
                quantity = int(''.join(filter(str.isdigit, quantity))) 
                description_element = meal.find('span', {'data-cy': 'orderDetailsItemDescription'})
                description = description_element.text.strip() if description_element else "No description available"

                # Extract customizations
                customizations = []
                customization_blocks = meal.find_all('span', {'class': 'flex flex-wrap w-full mt-4 justify-end'})
                # Locate all customization blocks of the second type
                customization_blocks_2 = meal.find_all('span', {'class': 'flex flex-wrap w-full mt-4 justify-end text-grey-50'})

                # Locate all customization blocks with both class variations
                
                for customization in customization_blocks:
                    customization_name_element = customization.find('span', {'class': 'w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline'})
                    customization_price_element = customization.find('span', {'data-cy': 'orderDetailsItemTotalPrice'})

                    # Extract customization details if available
                    customization_name = customization_name_element.text.strip() if customization_name_element else "Unknown"
                    customization_price_text = customization_price_element.text.strip().replace('£', '') if customization_price_element else "Free"

                    # Convert customization price to float
                    customization_price = 0.0 if customization_price_text.lower() == "free" else float(customization_price_text)

                    customizations.append({
                        'customization': customization_name,
                        'price': customization_price,
                    })

                # Check if the second type of customization blocks exist and process them
                if customization_blocks_2:
                    for customization in customization_blocks_2:
                        customization_name_element = customization.find('span', {'class': 'w-4/6 md:w-4/12 order-2 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start'})
                        customization_price_element = customization.find('span', {'data-cy': 'orderDetailsItemTotalPrice'})

                        # Extract customization details if available
                        customization_name = customization_name_element.text.strip() if customization_name_element else "Unknown"
                        customization_price_text = customization_price_element.text.strip().replace('£', '') if customization_price_element else "Free"

                        # Convert customization price to float
                        customization_price = 0.0 if customization_price_text.lower() == "free" else float(customization_price_text)

                        customizations.append({
                            'customization': customization_name,
                            'price': customization_price,
                        })



                # Append the meal details
                order_meal_details.append({
                    'meal_name': meal_name,
                    'meal_price': meal_price,
                    'quantity': quantity,
                    'description': description,
                    'customizations': customizations,
                })
                logging.info(f"Successfully extracted meal details for {len(order_meal_details)} meals.")
        except Exception as e:
                logging.error(f"Error occurred while extracting meal details: {e}")
                logging.debug(traceback.format_exc())
        return order_meal_details

    def extract_price_details(self,soup):
        # Extract order price details
        price_details = {}

        # Extract Service Charges
        service_fee_element = soup.find('span', {'data-cy': 'orderDetailsserviceFee'})
        if service_fee_element:
            price_details['service_fee'] = service_fee_element.text.strip()
        else:
            price_details['service_fee'] = 'N/A'

        # Extract Delivery Fee
        delivery_fee_element = soup.find('span', {'data-cy': 'orderDetailsDeliveryFee'})
        if delivery_fee_element:
            # Extract the text inside the parent span
            delivery_fee_text = delivery_fee_element.find_next('span').text.strip()
            price_details['delivery_fee'] = delivery_fee_text
        else:
            price_details['delivery_fee'] = 'N/A'

        # Extract Total Price
        total_price_element = soup.find('span', {'data-cy': 'orderDetailsTotal'})
        if total_price_element:
            price_details['total'] = total_price_element.text.strip()
        else:
            price_details['total'] = 'N/A'

        return price_details

    def controller(self,orders,json_handler):
        for order in orders:
            logging.info(f"Processing Order ID: {order_id}")
            print(order)
            order['order_id']=order['order_id'].replace('#', '')
            order_id=order['order_id']
            print("%%%%%%%%%%%%%%%%%%%%%55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",order_id)

            check=json_handler.check_order_exists(order_id)
            print("#####################################     Check        #####################################################",check)
            if not check:
                try:
                    soup=self.click_on_order(order_id)
                    # order_Details_div=
                    # soup = BeautifulSoup(html_content, 'html.parser')
                    meal_details=self.extract_meal_details(soup)
                    price_details=self.extract_price_details(soup)
                    print(meal_details,price_details)
                    json_handler.add_order(order_id, order,meal_details,price_details)
                    json_handler.insert_order_into_database(order_id)
                    logging.info(f"Inserted order {order_id} into database.")
                    self.driver.back()
                    self.driver.execute_script("document.body.style.zoom='50%'")
                    # Optionally, wait for the page to load
                    self.driver.implicitly_wait(5)  # Adjust the wait time as needed
                    sleep(10)
                except Exception as e:
                    logging.error(f"Error processing order {order_id}: {traceback.format_exc()}")
            else:
                continue
        json_handler.close_database()

if __name__ == "__main__":
    # json_handler = JsonDataHandler('orders.json')
    url="https://partner-centre.just-eat.co.uk/orders-and-invoices/order-history"
    driver_manager = WebDriverManager(url)

    db_config = {
        "host": "87.117.234.167",
        "user": "py_isb",
        "password": "7iIG3.X/T(ObjTK8",
        "database": "py_justeat"  # Assuming you have a database to connect to
    }

    json_file_path = "orders.json"

    sleep(30)
    while(1):
        try:
            orders=driver_manager.get_orders()
            print(orders)
            # Define the target date (2024, 11, 11, 0, 0)
            # target_date = datetime(2024, 11, 11, 0, 0)
            # Get today's date (ignoring the time part) 
            today_date = datetime.now().date()

            # Filter orders where the date matches the target date
            filtered_orders = [order for order in orders if order['date'] == today_date]
            print("##################### filter orders ",today_date)
            # print(filtered_orders)
            logging.info(f"Checking for active orders...,{len(filtered_orders)}")
            if filtered_orders:
                json_handler = JsonDataHandler(json_file_path,db_config) 
                logging.info(f"Database connection and status {json_handler}")
                driver_manager.controller(filtered_orders,json_handler)
                sleep(5)
            driver_manager.driver.refresh()
            logging.info("Refreshed the page.")
            driver_manager.driver.execute_script("document.body.style.zoom='50%'")
            sleep(60*4)
        except Exception as e:
            logging.error(f"Unexpected error in main loop: {traceback.format_exc()}")
            print(e)
            continue