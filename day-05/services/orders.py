from .prices import calculate_price
from utils.calculations import DISCOUNT

def calculate_order_total(price, quantity):
    return calculate_price(price, quantity)

def calculate_discounted_total(price, quantity):
    total = calculate_price(price, quantity)
    return total - (total * DISCOUNT)