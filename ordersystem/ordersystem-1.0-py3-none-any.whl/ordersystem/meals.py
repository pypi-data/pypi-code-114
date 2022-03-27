from ordersystem.menu import Menu
from ordersystem.custom_exceptions import TooManyItemsException, OrderIncompleteException
import os, json, logging

class Breakfast(Menu):
    def __init__(self):
        self.meal = "breakfast"

    def get_food(self, order_list):
        self.meal_menu, self.complimentary_items = Menu.get_menu(self.meal)
        logging.info("Validating Breakfast Order...")
        logging.debug(f"Validating Breakfast Order {order_list}")
        self.validate(order_list)
        logging.info("Getting order")
        return self.aggregate(order_list)
    
    def validate(self, order_list):
        too_many_message = self.too_many_validation(order_list)
        if too_many_message is not None:
            raise TooManyItemsException(too_many_message)
        return


class Lunch(Menu):
    def __init__(self):
        self.meal = "lunch"

    def get_food(self, order_list):
        self.meal_menu, self.complimentary_items = Menu.get_menu(self.meal)
        logging.info("Validating Lunch Order...")
        logging.debug(f"Validating Lunch Order {order_list}")
        self.validate(order_list)
        logging.info("Getting order")
        return self.aggregate(order_list)

    def validate(self, order_list):
        too_many_message = self.too_many_validation(order_list)
        if too_many_message is not None:
            raise TooManyItemsException(too_many_message)
        return

class Dinner(Menu):
    def __init__(self):
        self.meal = "dinner"

    def get_food(self, order_list):
        self.meal_menu, self.complimentary_items = Menu.get_menu(self.meal)
        logging.info("Validating Dinner Order...")
        logging.debug(f"Validating Dinner Order {order_list}")
        self.validate(order_list)
        logging.info("Getting order")
        return self.aggregate(order_list)

    def validate(self, order_list):
        meal_category = json.loads(os.getenv("MEAL_CATEGORY_MAPPING"))
        dessert = meal_category["dessert"]
        if dessert not in order_list:
            raise OrderIncompleteException("Dessert")
        too_many_message = self.too_many_validation(order_list)
        if too_many_message is not None:
            raise TooManyItemsException(too_many_message)
        
        return