import abc, os, json, logging
from collections import Counter

from ordersystem.custom_exceptions import UnknownItemException

class Menu:
    def __init__(self, meal):
        self.meal_menu = None
        self.complimentary_items = None
        self.meal = None
    
    @staticmethod
    def get_menu(meal):
        meal = meal.lower()
        logging.debug(f"Retrieving menu from environment for {meal}")
        menu = json.loads(os.getenv("MENU"))
        logging.debug(f"Retrieved menu from environment for meal {meal} /n /t {menu}")
        complimentary_items = json.loads(os.getenv("COMPLIMENTARY"))
        logging.debug(f"Retrieved complimentary menu from environment for {meal} /n /t {complimentary_items}")
        return menu[meal], complimentary_items[meal]
    
    def too_many_validation(self, order_list):
        message = None
        self.meal = self.meal.lower()
        logging.debug(f"Retrieving items that could only be ordered once from environment for {self.meal}")
        single_item_list = json.loads(os.getenv("SINGLE_ITEM"))[self.meal]
        logging.debug(f"Retrieved items that could only be ordered once from environment for {self.meal} \n \t {single_item_list}")
        for i in single_item_list:
            if order_list.count(i) > 1:
                if message is None:
                    message = f"{self.meal_menu[i]}"
                else:
                    message += f" and {self.meal_menu[i]}"
        logging.debug(f"Error Message for too many items: {message}")
        return message

    def aggregate(self, order_list):
        def aggregator(food_tuple):
            return self.meal_menu[food_tuple[0]] if food_tuple[1]< 2 else f"{self.meal_menu[food_tuple[0]]}({food_tuple[1]})"
        logging.info("Counting the list of items")
        counter_list = Counter(order_list)
        logging.debug(f"Breakdown of the order:{counter_list}")
        food_amount_list = [(item, amount) for item, amount in counter_list.items()]
        logging.debug(f"Food item and the number of times ordered tuple: \n \t {food_amount_list}")

        logging.info("Retrieving the meal category from environment variables")
        meal_category = json.loads(os.getenv("MEAL_CATEGORY_MAPPING"))
        logging.debug(f"Meal category mapping:{meal_category}")

        main = self.complimentary_items.get("main", "")
        side = self.complimentary_items.get("side", "")
        drink = self.complimentary_items.get("drink", "")
        dessert = self.complimentary_items.get("dessert", "")

        logging.debug(f"Complimentary items for the meal {self.meal} \n \t Main: {main} \n \t Side: {side} \n \t Drink: {drink} \n \t Dessert {dessert}")

        for k, v in food_amount_list:
            if k in self.meal_menu:
                logging.debug(f"Food Category: {k} Amount: {v}")
                if "main" in meal_category and k == meal_category["main"]:
                    main += aggregator((k,v)) if main == "" else main + ", " +  aggregator((k,v))
                elif "side" in meal_category and k == meal_category["side"]:
                    side += aggregator((k,v)) if side == "" else side + ", " +  aggregator((k,v))
                elif "drink" in meal_category and k == meal_category["drink"]:
                    drink = aggregator((k,v)) if drink == "" else drink + ", " +  aggregator((k,v))
                elif "dessert" in meal_category and k == meal_category["dessert"]:
                    dessert = aggregator((k,v)) if dessert == "" else dessert + ", " +  aggregator((k,v))
                else:
                    logging.info("Unknown Item")
                    raise UnknownItemException(k)
            elif k == "Water":
                if self.meal.lower() != "dinner":
                    drink += k
            else:
                logging.info("Unknown Item")
                raise UnknownItemException(k)
        
        logging.info("Formatting order")
        order = ""
        for i in [main, side, drink, dessert]:
            if i:
                order = order + i + " "
        order = order.strip().replace(" ", ", ")
        # if self.meal == "dinner":
        #     order = f"{main}, {side}, {drink}, {dessert}"
        #     logging.debug(f"Order: {order}")
        # else:
        #     order = f"{main}, {side}, {drink}"
        #     logging.debug(f"Order: {order}")
        return order

    @abc.abstractmethod
    def validate(self, order_list):
        return
    
    @abc.abstractmethod
    def get_food(self, order_list):
        return