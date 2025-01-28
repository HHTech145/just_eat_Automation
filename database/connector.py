import mysql.connector
from mysql.connector import Error
import json
from datetime import datetime
import traceback
class Database:
    def __init__(self, host="localhost", user="root", password="", port="",database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port=port
        self.connection = None
        self.connect()

    def connect(self):
        try:
            if self.database:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            else:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )
            if self.connection.is_connected():
                print("Connection successful!")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def create_database(self, db_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database '{db_name}' created successfully!")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()

    def initialize_database(self, db_name):
        try:
            self.connection.database = db_name
            print(f"Database '{db_name}' selected.")
        except Error as e:
            print(f"Error selecting database: {e}")

    def create_tables(self):
        try:
            cursor = self.connection.cursor()

            # Table for order details
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    order_id VARCHAR(50) PRIMARY KEY,  -- Increased size to accommodate larger IDs
                    date DATE,
                    time TIME,
                    payment_type VARCHAR(50),
                    service_type VARCHAR(50),
                    status VARCHAR(50),
                    delivery_price VARCHAR(50),
                    order_price DECIMAL(10, 2)
                );
            """)

            # Table for meals in an order
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_meals (
                    meal_id INT AUTO_INCREMENT PRIMARY KEY,
                    order_id VARCHAR(15),
                    meal_name VARCHAR(255),
                    price DECIMAL(10, 2),
                    quantity INT,
                    description TEXT,
                    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
                );
            """)

            # Table for customizations
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS meal_customizations (
                    customization_id INT AUTO_INCREMENT PRIMARY KEY,
                    meal_id INT,
                    customization_name VARCHAR(255),
                    customization_price DECIMAL(10, 2),
                    FOREIGN KEY (meal_id) REFERENCES order_meals(meal_id) ON DELETE CASCADE
                );
            """)

            # Table for price details of the order
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_price_details (
                    price_detail_id INT AUTO_INCREMENT PRIMARY KEY,
                    order_id VARCHAR(15) NOT NULL,
                    service_fee DECIMAL(10, 2),
                    delivery_fee DECIMAL(10, 2),
                    total DECIMAL(10, 2),
                    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
                    UNIQUE (order_id)  -- Ensures that order_id is unique
                );
            """)

            self.connection.commit()
            print("Tables created successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()
        finally:
            cursor.close()

    def insert_update_orders(self, order_details):
        try:
            cursor = self.connection.cursor()

            sql = """
                INSERT INTO orders (
                    order_id, date, time, payment_type, service_type, status,
                    delivery_price, order_price
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    date = VALUES(date),
                    time = VALUES(time),
                    payment_type = VALUES(payment_type),
                    service_type = VALUES(service_type),
                    status = VALUES(status),
                    delivery_price = VALUES(delivery_price),
                    order_price = VALUES(order_price)
            """

            # Prepare values
            values = (
                order_details["order_id"],
                order_details["date"],
                order_details["time"],
                order_details["payment_type"],
                order_details["service_type"],
                order_details["status"],
                order_details["delivery_price"].replace("£", "").replace("delivery fees", "").strip(),  # Sanitize input
                float(order_details["order_price"].replace("£", ""))  # Remove currency symbol and convert to float
            )

            cursor.execute(sql, values)
            self.connection.commit()
            print("Order details inserted or updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error in orders insertion: {err}")

        finally:
            cursor.close()

    def insert_update_order_price_details(self, order_id, order_price_details):
        try:
            cursor = self.connection.cursor()

            sql = """
                INSERT INTO order_price_details (order_id, service_fee, delivery_fee, total)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    service_fee = VALUES(service_fee),
                    delivery_fee = VALUES(delivery_fee),
                    total = VALUES(total)
            """

            # Extract and sanitize values
            values = (
                order_id,
                float(order_price_details["service_fee"].replace("£", "").strip()),
                float(order_price_details["delivery_fee"].replace("£", "").strip()),
                float(order_price_details["total"].replace("£", "").strip())
            )

            cursor.execute(sql, values)
            self.connection.commit()
            print("Order price details inserted/updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error in price details insertion: {err}")
            self.connection.rollback()  # Rollback in case of error

        finally:
            cursor.close()



    # def insert_update_order_price_details(self, order_id, order_price_details):
    #     try:
    #         cursor = self.connection.cursor()

    #         # Iterate over each price detail in order_price_details JSON array
    #         for detail in order_price_details:
    #             description = detail['description']
    #             amount = detail['amount']
                
    #             # Insert or update each entry in the order_price_details table
    #             sql = """
    #                 INSERT INTO order_price_details (order_id, description, amount)
    #                 VALUES (%s, %s, %s)
    #                 ON DUPLICATE KEY UPDATE
    #                     amount = VALUES(amount)
    #             """
    #             cursor.execute(sql, (order_id, description, amount))

    #         # Commit the transaction after all inserts/updates
    #         self.connection.commit()
    #         print("Order price details inserted/updated successfully.")
        
    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")
    #         self.connection.rollback()  # Rollback on error
        
    #     finally:
    #         cursor.close()

    def check_order_id(self, order_id):
        try:
            cursor = self.connection.cursor()

            # Check if the order_id already exists in the orders table
            cursor.execute("SELECT COUNT(*) FROM orders WHERE order_id = %s", (order_id,))
            exists = cursor.fetchone()[0] > 0

            if exists:
                print(f"Order ID {order_id} already exists. Skipping insertion.")
                return True  # Order ID exists
            else:
                return False  # Order ID does not exist

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return False  # Safeguard to prevent crashes if something goes wrong

        except Exception as e:
            print(f"Unexpected error: {traceback.format_exc()}")
            return False

        finally:
            cursor.close()



    def insert_order_meals_with_customizations(self, order_id, order_meal_details):
        try:
            cursor = self.connection.cursor()

            # Check if the order_id already exists in the order_meals table
            cursor.execute("SELECT COUNT(*) FROM order_meals WHERE order_id = %s", (order_id,))
            if cursor.fetchone()[0] > 0:
                print(f"Order ID {order_id} already exists. Skipping insertion.")
                return  # Exit the function to prevent duplicate insertions

            # Track unique combinations of meal name and customizations for this order
            added_meals = set()

            for meal in order_meal_details:
                meal_name = meal['meal_name']
                meal_price = meal['meal_price']
                quantity = int(meal['quantity'])
                # quantity = int(''.join(filter(str.isdigit, meal['quantity'])))  # Extract numeric part
                description = meal['description']

                # Generate a unique key for meal and customizations
                customizations_key = meal_name + "_" + "_".join(
                    f"{c['customization']}" for c in meal.get('customizations', [])
                )

                # Even if this meal + customization combination is seen before, insert it
                # Process each meal regardless of duplicates for same order_id
                meal_sql = """
                    INSERT INTO order_meals (order_id, meal_name, price, quantity, description)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(meal_sql, (order_id, meal_name, meal_price, quantity, description))
                meal_id = cursor.lastrowid  # Get the inserted meal_id

                # Process customizations for each meal
                for customization in meal.get('customizations', []):
                    customization_name = customization['customization']
                    price = customization['price']

                    # Check if this specific customization already exists for this meal
                    cursor.execute("""
                        SELECT customization_id FROM meal_customizations
                        WHERE meal_id = %s AND customization_name = %s
                    """, (meal_id, customization_name))
                    customization_record = cursor.fetchone()

                    if customization_record:
                        # Update customization if it exists
                        customization_id = customization_record[0]
                        cursor.execute("""
                            UPDATE meal_customizations SET customization_price = %s
                            WHERE customization_id = %s
                        """, (price, customization_id))
                    else:
                        # Insert new customization if it doesn't exist
                        customization_sql = """
                            INSERT INTO meal_customizations (meal_id, customization_name, customization_price)
                            VALUES (%s, %s, %s)
                        """
                        cursor.execute(customization_sql, (meal_id, customization_name, price))

            # Commit the transaction after processing all meals and customizations
            self.connection.commit()
            print("Order meals and customizations inserted/updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

        finally:
            cursor.close()


        # def insert_order_meals_with_customizations(self, order_id, order_meal_details):
        #     try:
        #         cursor = self.connection.cursor()

        #         # Check if the order_id already exists in the order_meals table
        #         cursor.execute("SELECT COUNT(*) FROM order_meals WHERE order_id = %s", (order_id,))
        #         if cursor.fetchone()[0] > 0:
        #             print(f"Order ID {order_id} already exists. Skipping insertion.")
        #             return  # Exit the function to prevent duplicate insertions

        #         # Track unique combinations of meal name and customization for this order
        #         added_meals = set()

        #         for meal in order_meal_details:
        #             meal_name = meal['meal_name']
        #             meal_price = meal['meal_price']
        #             quantity = int(''.join(filter(str.isdigit, meal['quantity']))) 
        #             description= meal['description']
        #             # quantity = int(meal['quantity'])

        #             # Generate a unique key for meal and customizations
        #             customizations_key = meal_name + "_" + "_".join(
        #                 f"{c['customization']}" for c in meal.get('customizations', [])
        #             )

        #             if (order_id, customizations_key) not in added_meals:
        #                 # Insert the meal if this unique combination has not been added
        #                 meal_sql = """
        #                     INSERT INTO order_meals (order_id, meal_name, price, quantity,description)
        #                     VALUES (%s, %s, %s, %s,%s)
        #                 """
        #                 cursor.execute(meal_sql, (order_id, meal_name, meal_price, quantity,description))
        #                 meal_id = cursor.lastrowid

        #                 # Mark this unique meal + customization combination as added
        #                 added_meals.add((order_id, customizations_key))
        #             else:
        #                 # Fetch the meal_id for updating if it exists
        #                 cursor.execute("""
        #                     SELECT meal_id FROM order_meals
        #                     WHERE order_id = %s AND meal_name = %s
        #                 """, (order_id, meal_name))
        #                 meal_id = cursor.fetchone()[0]

        #             # Process customizations for each meal
        #             for customization in meal.get('customizations', []):
        #                 customization_name = customization['customization']
        #                 price = customization['price']

        #                 # Check if this specific customization already exists for this meal
        #                 cursor.execute("""
        #                     SELECT customization_id FROM meal_customizations
        #                     WHERE meal_id = %s AND customization_name = %s
        #                 """, (meal_id, customization_name))
        #                 customization_record = cursor.fetchone()

        #                 if customization_record:
        #                     # Update customization if it exists
        #                     customization_id = customization_record[0]
        #                     cursor.execute("""
        #                         UPDATE meal_customizations SET customization_price = %s
        #                         WHERE customization_id = %s
        #                     """, (price, customization_id))
        #                 else:
        #                     # Insert new customization if it doesn't exist
        #                     customization_sql = """
        #                         INSERT INTO meal_customizations (meal_id, customization_name, customization_price)
        #                         VALUES (%s, %s, %s)
        #                     """
        #                     cursor.execute(customization_sql, (meal_id, customization_name, price))

        #         self.connection.commit()
        #         print("Order meals and customizations inserted/updated successfully.")

        #     except mysql.connector.Error as err:
        #         print(f"Error: {err}")
        #         self.connection.rollback()

        #     finally:
        #         cursor.close()







    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed.")


if __name__ == "__main__":
    db = Database(host="87.117.234.167", user="py_isb", password="7iIG3.X/T(ObjTK8",port=80)
    db.create_database("test_just_eat")
    # Initialize the database (connect to it)
    db.initialize_database("test_just_eat")
    # Call the function to create tables
    db.create_tables()
    # Close the connection
    db.close()