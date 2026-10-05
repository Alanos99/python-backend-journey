from utils.messages import welcome_user
from services.orders import calculate_discounted_total, calculate_order_total
from utils.calculations import VAT

greeting = welcome_user("Alan")
order_total = calculate_order_total(50, 4)
discounted_total = calculate_discounted_total(50, 4)
vat_amount = order_total * VAT
print(greeting)
print(order_total)
print(discounted_total)
print(vat_amount)
