import sys
sys.path.append("../")
from ordersystem.order_system import OrderSystem
from ordersystem.custom_exceptions import OrderIncompleteException, TooManyItemsException
import pytest

order = OrderSystem()
def test_failed_order():
    with pytest.raises(OrderIncompleteException) as e_info:
        order.get_order("Breakfast", "3")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Main and Side is missing"

def test_breakfast():
    assert order.get_order("Breakfast", "1,2,3") == "Eggs, Toast, Coffee"
    assert order.get_order("Breakfast", "1,2,3,3") == "Eggs, Toast, Coffee(2)"

def test_breakfast_toomany_excep():
    with pytest.raises(TooManyItemsException) as e_info:
        order.get_order("Breakfast", "1,1,2, 3")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Eggs cannot be ordered more than once" 

def test_lunch():
    assert order.get_order("Lunch", "1,2,3") == "Sandwich, Chips, Soda"
    assert order.get_order("Lunch", "1,2,2 ,3") == "Sandwich, Chips(2), Soda"

def test_lunch_toomany_excep():
    with pytest.raises(TooManyItemsException) as e_info:
        order.get_order("Lunch", "1,1,2, 3,3")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Sandwich and Soda cannot be ordered more than once"

def test_dinner():
    assert order.get_order("Dinner", "1,2,3,4") == "Steak, Potatoes, Water, Wine, Cake"
    assert order.get_order("Dinner", "1,2,4") == "Steak, Potatoes, Water, Cake"

def test_dinner_order_incomplete():
    with pytest.raises(OrderIncompleteException) as e_info:
        order.get_order("Dinner", "1,2,3")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Dessert is missing"

def test_dinner_toomany_excep():
    with pytest.raises(TooManyItemsException) as e_info:
        order.get_order("Dinner", "2,2,1,1,3,3,4")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Steak and Potatoes and Wine cannot be ordered more than once"

