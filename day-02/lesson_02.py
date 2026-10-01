cars = ["Mercedes", "Toyota", "BMW", "Audi"]
cars.append("Porsche")
cars.remove("BMW")
cars[1] = "Ferrari"

for car in cars:
    print(f"Moim samochodem jest {car}")

for number in numbers:
    print(f"{number} * 2 = {number * 2}")

numbers = [5, 12, 7, 20, 3, 15]

for number in numbers:
    if number > 10:
        print(f"{number} jest większe niż 10")
    else:
        print("Numer jest mniejszy lub równy 10")

ages = [12, 18, 25, 15, 40]

for age in ages:
    if age >= 18:
        print(f"{age} - Pełnoletni")
    else:
        print(f"{age} - Niepełnoletni")

for number in range(2, 9):
    print(number)

for number in range(10, 21)
    print(number)
for number in range(0, 21, 5)

for number in range(1, 11, 1):
if number >=5:
    print(f"{number} jest większe lub równe 5")

while number <= 5:
    print(number)
    number = number + 1

while number <= 10:
    print(number)
    number = number + 2

number = 10
while number >= 5:
    print(number)
    number = number - 1

number = 3
while number <=8:
    print(number)
    number = number + 1

number = 15
while number >= 10:
    print(number)
    number = number - 1

number = 3
while number <= 18:
    print(number)
    number = number + 3

number = 20
while number >= 10:
    print(number)
    number = number - 2

number = 5
while number >= 30:
    print(number)
    number = number + 5

number = 40
while number >= 20:
    print(number)
    number = number - 5

number = 7
while number <= 42:
    print(number)
    number = number + 7

number = 100
while number >= 30:
    print(number)
    number = number - 10

number = 1
while number <= 100:
    print(number)
if number == 7:
    break
number = number + 1

number = 1
while number <= 30:
    print(number)
    if number == 8:
        break
    number = number + 1

number = 1
while number <= 12:
    number = number + 1
    if number == 7:
        continue
    print(number)

number = 0
while number <= 10:
    if number == 4:
        number = number + 1
        continue
    print(number)
    numer = number + 1

number = 0
while number <= 15:
    if number == 5 or number == 10:
        number = number + 1
        continue
    print(number)
    number = number + 1

number = 0
while number <= 20:
    if number == 7 or number == 12 or number == 16:
        number = number + 1
        continue
    print(number)
    number = number + 1

cars = ["Mercedes", "BMW", "Audi", "Toyota", "Porsche"]
for car in cars:
    if car == "Toyota":
        continue
    print(f"Moim samochodem jest {car}")

for car in cars:
    if car == "Toyota":
        print("Nie lubię Toyoty")
    else:
        print(f"Lubię {car}")

for car in cars:
    if car == "Toyota":
        break
    print(f"Moim samochodem jest {car}")

for number in range(1, 11, 1):
    if number == 5:
        continue
    print(number)

for number in range(1, 11, 1):
    if number == 3:
        continue
    if number == 8:
        break
    print(number)

for number in range(1, 11, 1):
    if number == 3:
        continue
    print(number)
    if number == 8:
        break

for number in range(1, 16, 1):
    if number == 4 or number == 7:
        continue
    print(number)
    if number == 12:
        break

for number in range(2, 21, 2):
    if number == 6 or number == 10:
        continue
    if number == 16:
        break
    print(number)

for cars in cars:
    if cars == "BMW":
        continue
    print(f"Samochód {cars}")
    if cars == "Porsche":
        break

for dog in dogs:
    if dog == "Mops" or dog == "Beagle":
        continue
    print(f"Rasa: {dog}")
    if dog == "Rottweiler":
        break

for price in prices:
    if price > 80:
        continue
    print(f"Cena: {price}")

for age in ages:
    if age < 18:
        continue
    print(f"Wiek: {age}")

for score in scores:
    if score < 40:
        continue
    print(f"Wynik: {score}")
    if score == 85:
        break

for order in orders:
    if order < 60:
        continue
    if order == 200:
        break
    print(f"Zamówienie: {order} zł")

for product in products:
    if product < 70:
        continue
    print(f"Cena produktu {product} zł")

    # ==================================================
# DAY 2 - PODSUMOWANIE
# ==================================================

# LISTY
# Lista przechowuje wiele wartości w jednej zmiennej.

cars = ["Mercedes", "BMW", "Audi"]

# Element listy pobieramy przez indeks.
# Indeksy zaczynają się od 0.

print(cars[0])  # Mercedes

# Dodawanie elementu:
cars.append("Porsche")

# Usuwanie elementu:
cars.remove("BMW")

# Zmiana elementu:
cars[0] = "Ferrari"


# ==================================================
# FOR
# ==================================================

# for przechodzi po elementach jeden po drugim.

for car in cars:
    print(car)

# car = aktualny element listy
# cars = cała lista


# ==================================================
# RANGE
# ==================================================

# range(start, stop, step)
# stop NIE jest wliczany.

for number in range(0, 11, 2):
    print(number)

# Wynik:
# 0 2 4 6 8 10


# ==================================================
# WHILE
# ==================================================

# while wykonuje kod tak długo,
# jak długo warunek jest True.

number = 1

while number <= 5:
    print(number)
    number = number + 1


# ==================================================
# CONTINUE
# ==================================================

# continue pomija resztę aktualnej iteracji
# i przechodzi do następnej.

for number in range(1, 6):
    if number == 3:
        continue

    print(number)

# Wynik:
# 1 2 4 5


# ==================================================
# BREAK
# ==================================================

# break kończy CAŁĄ pętlę.

for number in range(1, 10):
    if number == 5:
        break

    print(number)

# Wynik:
# 1 2 3 4


# ==================================================
# NAJWAŻNIEJSZA ZASADA DAY 2
# ==================================================

# Python wykonuje kod:
#
# 1. Od góry do dołu.
# 2. Linijka po linijce.
# 3. Pętla bierze jeden element.
# 4. Wykonuje kod dla tego elementu.
# 5. Potem bierze następny element.
#
# continue = następna iteracja
# break = koniec całej pętli


# ==================================================
# FINALNY PRZYKŁAD
# ==================================================

products = [25, 70, 120, 45, 200, 90, 300]

for product in products:
    if product < 70:
        continue

    print(f"Cena produktu: {product} zł")

    if product == 200:
        break


# ==================================================
# END OF DAY 2
# ==================================================