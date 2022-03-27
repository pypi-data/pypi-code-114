from ordersystem.meals import Breakfast, Lunch, Dinner
import logging, os, json
from ordersystem.custom_exceptions import OrderIncompleteException

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=LOG_LEVEL)

class OrderSystem:
    def __init__(self):
        self.menu_mapping = {
            "breakfast": Breakfast(),
            "lunch" : Lunch(),
            "dinner" : Dinner()
        }

    def get_order(self, menu_type, order):
        order = order.replace(" ", "")
        order_list = order.split(",")
        logging.debug(f"Received order: {menu_type} List of items: {order_list}")
        meal_category = json.loads(os.getenv("MEAL_CATEGORY_MAPPING"))
        main = meal_category["main"]
        side = meal_category["side"]
        logging.info("Validating food")
        self.validate(order_list, main, side)
        logging.info("Done Validating")
        drink = meal_category["drink"]

        if drink not in order_list:
            logging.info("Drink is not included. Adding water...")
            order_list.append("Water")
        
        logging.info("Getting the menu")
        menu = self.menu_mapping[menu_type.lower()]

        logging.info(f"Getting the food for {menu}")
        return menu.get_food(order_list)

    def validate(self, order_list, main, side):
        logging.info(f"Validating {order_list}")
        logging.debug(f"Main Category is {main}. Side Category is {side}")
        
        if main not in order_list and side not in order_list:
            raise OrderIncompleteException("Main and Side")
        if main not in order_list:
            raise OrderIncompleteException("Main")
        if side not in order_list:
            raise OrderIncompleteException("Side")
        return