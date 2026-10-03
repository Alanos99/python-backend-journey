def show_message():
    print("Uczę się Pythona!")
show_message()

def show_car(car):
    print(f"Mój samochód to {car}.")
show_car("Mercedes")


def show_dog(dog, age):
    print(f"Mój pies to {dog} i ma {age} lata.")
show_dog("Cane Corso", 4)


def calculate_salary(hourly_rate, hours):
    salary = hourly_rate * hours
    print(f"Wynagrodzenie: {salary} zł")
calculate_salary(50, 8)


def calculate_total(price, quantity):
    total = price * quantity
    return total
total = calculate_total(25, 4)
print(total):


def calculate_salary(hourly_rate, hours):
    salary = hourly_rate * hours
    return salary
salary = calculate_salary(50, 8)
tax = salary * 0.2
print(f"Wypłata: {salary} zł, Podatek:{tax} zł")


def check_salary(salary):
    if salary >= 5000:
        return "Dobra wypłata"
    else:
        return "Słaba wypłata"
result = check_salary(6000)
print(result)


def calculate_discount(price, discount):
    return price * discount
result = calculate_discount(200, 0.20)
print(result)


def check_score(score):
    if score >= 90:
        return "Świetny wynik"
    elif score >= 65:
        return "Dobry wynik"
    else:
        return "Słaby wynik"
result = check_score(75)
print(result)


def show_dogs(dogs):
    for dog in dogs:
        print(dog)
show_dogs(["Cane Corso", "Owczarek niemiecki", "Golden Retriever"])


def count_dogs(dogs):
    return len(dogs)
dog_count = count_dogs(["Cane Corso", "Owczarek niemiecki", "Golden Retriever"])
print(f"Liczba psów: {dog_count}")


def find_dogs(dogs):
    for dog in dogs:
        if dog == "Rottweiler":
            return "Znaleziono Rottweilera!"
print(f"Znaleziono {dogs}!")

def find_car(cars):
    for car in cars:
        if car == "Mercedes":
            return  "Znaleziono Mercedesa!"

cars = ["Audi", "BMW", "Mercedes", "Toyota"]
result = find_car(cars)
print(result)


def find_product(products):
    for product in products:
        if product == "Monitor":
            return "Znaleziono monitor!"

products = ["Laptop", "Telefon", "Monitor", "Klawiatura"]
result = find_product(products)
print(result)


def find_user(users, searched_user):
    for user in users:
        if users == "Alan":
            return "Znaleziono Alan!"

users = ["Adam", "Kasia", "Alan", "Marek"]
result = find_user(users, "Alan")
print(result)


def find_product(products, searched_product):
    for product in products:
        if product == searched_product
            return "Znaleziono produkt!"

products = ["Laptop", "Monitor", "Telefon", "Myszka"]
result = find_product(products, "Telefon")
print(result)        


def find_city(cities, searched_city):
    for city in cities:
        if city == searched_city
        return "Znaleziono miasto!"

cities = ["Warszawa", "Kraków", "Białystok", "Gdańsk"]
result = find_city(cities, "Białystok")
print(result)


def find_animal(animals, searched_animal)
    for animal in animals:
        if animal == searched_animal
        return "Znaleziono zwierzę!"

animals = ["Kot", "Pies", "Koń", "Królik"]
result = find_animal(animals, "Koń")
print(result)


def find_car(cars, searched_car)
    for car in cars:
        return "Znaleziono samochód"
    if car in searched_car == "Volvo":
        return "Nie znaleziono samochodu?"

cars = ["BMW", "Audi", "Mercedes", "Toyota"]
result = find_car(cars, "Volvo")
print(result)

def find_dog(dogs, searched_dog):
    for dog in dogs:
        if dogs == searched_dog
        return "Znaleziono psa!"
    return "Nie znaleziono psa!"

dogs = ["Labrador", "Beagle", "Rottweiler", "Husky"]
result = find_dog(dogs, "Maltańczyk")
print(result)


def find_games(games, searched_game):
    for game in games:
        if game == searched_game:
            return "Znaleziono grę!"
    return "Nie znaleziono gry!"

games = ["GTA", "Minecraft", "Cyberpunk", "Wiedźmin"]
result = find_games(games, "Skyrim")
print(result)


def show_language(language="Python")
    return (f"Uczę się {language}")

print(show_language(Java))


def create_account(username, account_type="Standard"):
    return f"Konto: {username}, typ: {account_type}"

print(create_account("Alan", account_type))
print(create_account("Kasia", "Premium"))


def find_car(cars, searched_car):
    for car in cars:
        if car == searched_car:
            return car

cars = ["BMW", "Mercedes", "Audi"]
result = find_car(cars, "Volvo")
if result is None:
    print("Nie znaleziono samochodu.")
else:
    print(f"Znaleziono samochód: {result}")

def is_product_available(stock)
    for product in stock:
        if product > 0:
            return True
    return False

result = is_product_available([5])
print(result)


def calculate_price(price, quantity):
    total = price * quantity
    return total

result = calculate_price(25, 4)
print(result)

def calculate_total(price, quantity):
    return price * quantity
total = calculate_total(50, 4)

def calculate_discount(total):
    return total * 0.10
print(total)
print(calculate_discount(total))


def calculate_salary(hourly_rate, hours):
    salary = hourly_rate * hours
    tax = salary * 0.20
    return salary, tax
salary, tax = calculate_salary(50, 40)
print(f"Salary: {salary}, Tax: {tax}")

def calculate_order(price, quantity):
    total = calculate_price(price, quantity)
    shipping = calculate_shipping(total)
    return total, shipping
total, shipping = calculate_order(50, 3)
print(f"Total: {total}, Shipping: {shipping}")




def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total):
    if total >= 200:
        return total * 0.10
    else:
        return 0

def calculate_order(price, quantity):
    total = calculate_total(price, quantity)
    discount = calculate_discount(total)
    final_price = total - discount
    return total, discount, final_price

total, discount, final_price = calculate_order(50 ,5)
print(f"Total: {total}, Discount: {discount}, Final Price: {final_price}")



def is_premium_user(account_type):
    return account_type == "Premium"

def calculate_price(price, account_type):
    if is_premium_user(account_type):
        return price * 0.20
    return price

result = calculate_price(100, "Premium")
print(result)



def check_login(username, password):
    if username != "admin":
        return "Nieprawidłowy użytkownik"
    elif password != "python123":
        return "Nieprawidłowe hasło"
    else:
        return "Zalogowano pomyślnie"

print(check_login("admin", "python123"))


def check_order(stock, quantity):
    if quantity <= 0:
        return "Nieprawidłowa ilość w magazynie"

    if quantity > stock:
        return "Brak wystarczającej ilości w magazynie"

    return "Zamówienie możliwe"

print(check_order(10, 5))



def calculate_salary(hourly_rate: float, hours: int) -> float:
    return hourly_rate * hours


def calculate_sum(*args):
    total = 0
    for number in args:
        total = total + number
    return total

result = calculate_sum(10, 20, 30, 40)
print(result)


def show_user(**kwargs):

show_user(name="Alan", age=27, premium=True)
print("Wiadomości o użytkowniku:")


def calculate_discount(price):
    return price * 0.10

def use_calculation(function, price):
    use_calculation = function(price)
    result = use_calculation
    return result

print(use_calculation(calculate_discount, 200))


def calculate_bonus(salary):
    return salary * 0.20

def run_calculation(function, salary):
    result = function(salary)
    return result

print(run_calculation(calculate_bonus, 5000))


def calculate_product(price):

    def calculate_discount():
        return price * 0.20

    discount = calculate_discount()
    final_price = price - discount
    return final_price

print(calculate_product(200))

calculate_net = lambda salary: salary * 0.80
print(calculate_net(5000))


def calculate_order(price, quantity):
    if quantity <= 0:
        return "Nieprawidłowa ilość"
    total = price * quantity

    if total >= 500:
        total = total * 0.90
    return total    

print(calculate_order(100, 6))


def check_login(username, password, is_banned):
    if is_banned is True:
        return "Użytkownik zablokowany"
    elif username != "admin":
        return "Nieprawidłowy login"
    elif password != "python123":
        return "Nieprawidłowe hasło"
    else:
        return "Zalogowano pomyślnie"

print(check_login("admin", "python123", False))


def find_expensive_product(products):
    for product in products:
        if product >= 200:
            return f"Produkt kosztuje {product}"
    return "Nie znaleziono produktu"


products = [50, 120, 30, 250, 80]
print(find_expensive_product(products))


def calculate_total(price, quantity):


def calculate_total(price, quantity):
    total = price * quantity
    return total

def calculate_shipping(total):
    if total >= 200:
        return 0

    if total < 200:
        return 20

def calculate_final_price(price, quantity):
    total = calculate_total(price, quantity)
    shipping = calculate_shipping(total)
    final_price = total + shipping
    return final_price

print(calculate_final_price(50, 3))


def find_user(users, searched_user):
    if searched_user in users:
        return f"Użytkownik {searched_user} został znaleziony"
    else:
        return f"Użytkownik {searched_user} nie został znaleziony"

searched_user = "Ola"
result = find_user(users, searched_user)
if result is None:
    print("Użytkownik nie został znaleziony")
else:
    print(f"Użytkownik {searched_user} został znaleziony")


users = ["Alan", "Kamil", "Ola", "Bartek"]





cars = ["Mercedes", "BMW", "Audi", "Volvo"]

def find_car(cars, searched_car):
    for car in cars:
        if car == searched_car:
            return f"Samochód {searched_car} został znaleziony"
    
    return None

searched_car = "Audi"
result = find_car(cars, searched_car)
if result is None:
    print("Samochód nie został znaleziony")
else:
    print(f"Znaleziono samochód {searched_car}")


games = ["GTA", "Minecraft", "Witcher", "Cyberpunk"]

def find_game(games, searched_game):
    for game in games:
        if game == searched_game:
            return game
    return None

searched_game = "Witcher"
result = find_game(games, searched_game)
if result is None:
    print("Gra nie została znaleziona")
else:
    print(f"Znaleziono grę {result}")


dogs = ["Labrador", "Rottweiler", "Malinois", "Husky"]

def find_dog(dogs, searched_dog):
    for dog in dogs:
        if dog == searched_dog:
            return dog
    return None

searched_dog = "Malinois"
result = find_dog(dogs, searched_dog)
if result is None:
    print("Pies nie został znaleziony")
else:
    print(f"Znaleziono psa {result}")


def calculate_fee(amount): 
    if amount >= 1000:
        return amount * 0.02
    return 0

def withdraw(balance, amount):
    fee = calculate_fee(amount)
    if amount <= 0:
        return "Nieprawidłowa kwota"
    
    if amount + fee > balance:
        return "Brak środków"

    balance -= (amount + fee)
    return balance

print(withdraw(2000, 1000))