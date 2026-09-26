# ==========================================
# PYTHON BACKEND JOURNEY — DAY 1
# Python Fundamentals
# ==========================================


# ------------------------------------------
# 1. PRINT — wyświetlanie informacji
# ------------------------------------------

print("Hello World")
print("Uczę się Pythona")


# ------------------------------------------
# 2. ZMIENNE
# ------------------------------------------

name = "Alan"
age = 27
height = 1.94

print(name)
print(age)
print(height)


# ------------------------------------------
# 3. PODSTAWOWE TYPY DANYCH
# ------------------------------------------

# str   = tekst
text = "Alan"

# int   = liczba całkowita
number = 27

# float = liczba dziesiętna
height = 1.94

# bool  = True albo False
has_ticket = True
is_banned = False


# ------------------------------------------
# 4. DZIAŁANIA MATEMATYCZNE
# ------------------------------------------

a = 10
b = 5

print(a + b)   # dodawanie
print(a - b)   # odejmowanie
print(a * b)   # mnożenie
print(a / b)   # dzielenie


# ------------------------------------------
# 5. INPUT — pobieranie danych od użytkownika
# ------------------------------------------

name = input("Jak masz na imię?")

# input() zawsze zwraca tekst (str)

age = int(input("Ile masz lat?"))

# int() zamienia tekst na liczbę całkowitą


# ------------------------------------------
# 6. F-STRING
# ------------------------------------------

print(f"Cześć {name}!")
print(f"Masz {age} lat.")
print(f"Za 10 lat będziesz mieć {age + 10} lat.")


# ------------------------------------------
# 7. IF / ELIF / ELSE
# ------------------------------------------

if age < 18:
    print("Jesteś niepełnoletni")
elif age == 18:
    print("Masz dokładnie 18 lat")
else:
    print("Jesteś pełnoletni")


# ------------------------------------------
# 8. = VS ==
# ------------------------------------------

# =  przypisuje wartość

age = 27

# == sprawdza, czy wartości są równe

if age == 27:
    print("Wiek wynosi 27")


# ------------------------------------------
# 9. AND / OR / NOT
# ------------------------------------------

has_ticket = True
is_vip = False
is_banned = False

# AND — wszystkie warunki muszą być prawdziwe

if age >= 18 and has_ticket:
    print("Masz 18 lat lub więcej i masz bilet")


# OR — wystarczy jeden prawdziwy warunek

if has_ticket or is_vip:
    print("Masz bilet albo jesteś VIP-em")


# NOT — odwraca True / False

if not is_banned:
    print("Nie masz bana")


# Możemy łączyć warunki:

if age >= 18 and (has_ticket or is_vip) and not is_banned:
    print("Możesz wejść")


# ==========================================
# MINI PROJEKT — KALKULATOR CENY BILETU
# ==========================================

name = input("Jak masz na imię?")
age = int(input("Ile masz lat?"))
ticket = int(input("Ile biletów chcesz kupić?"))

print(f"Cześć {name}!")
print(f"Kupujesz {ticket} bilety.")
print(f"Cena przed rabatem: {ticket * 40} zł.")

if age < 18:
    print("Przysługuje Ci zniżka uczniowska")
elif age < 65:
    print("Płacisz normalnie")
else:
    print("Przysługuje Ci zniżka seniora")


