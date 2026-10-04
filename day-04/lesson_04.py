# ==========================================
# DAY 4 - DICT, TUPLE, SET
# ==========================================


# ==========================================
# 1. DICT - SŁOWNIKI
# ==========================================

# Dict przechowuje dane jako:
# klucz: wartość

car = {
    "brand": "Mercedes",
    "model": "W210",
    "year": 1998
}

# Pobieranie wartości
print(car["model"])

# Zmiana wartości
car["year"] = 2001

# Dodawanie nowej pary
car["engine"] = "OM606"

# Usuwanie
del car["engine"]

print(car)


# ------------------------------------------
# .get()
# ------------------------------------------

# [] może spowodować KeyError, jeśli klucza nie ma.
# .get() zwróci None zamiast błędu.

engine = car.get("engine")
print(engine)

# Możemy podać wartość domyślną:

color = car.get("color", "Brak informacji o kolorze")
print(color)


# ------------------------------------------
# Sprawdzanie, czy klucz istnieje
# ------------------------------------------

if "model" in car:
    print("Klucz model istnieje.")


# ------------------------------------------
# .keys(), .values(), .items()
# ------------------------------------------

user = {
    "name": "Alan",
    "age": 27,
    "premium": True
}

# Same klucze
for key in user.keys():
    print(key)

# Same wartości
for value in user.values():
    print(value)

# Klucz + wartość
for key, value in user.items():
    print(f"{key}: {value}")


# ------------------------------------------
# Zagnieżdżony dict
# ------------------------------------------

user = {
    "name": "Alan",
    "age": 27,
    "address": {
        "city": "Białystok",
        "country": "Polska"
    }
}

print(user["address"]["city"])
print(user["address"]["country"])


# ------------------------------------------
# Lista słowników
# ------------------------------------------

users = [
    {"name": "Alan", "age": 27},
    {"name": "Kamil", "age": 30},
    {"name": "Ola", "age": 24}
]

print(users[1]["age"])

for user in users:
    print(user["name"])


# ------------------------------------------
# Szukanie w liście słowników
# ------------------------------------------

def find_user(users, searched_name):
    for user in users:
        if user["name"] == searched_name:
            return user

    # Dopiero po sprawdzeniu wszystkich użytkowników
    return None


result = find_user(users, "Kamil")
print(result)


# ------------------------------------------
# len(dict)
# ------------------------------------------

car = {
    "brand": "Mercedes",
    "model": "W210",
    "year": 1998,
    "engine": "OM606"
}

# Liczba par klucz: wartość
print(len(car))


# ------------------------------------------
# Bool w słowniku
# ------------------------------------------

product = {
    "name": "Laptop",
    "price": 4500,
    "available": True
}

if product["available"]:
    print(f"{product['name']} jest dostępny.")


# ------------------------------------------
# .get() + if
# ------------------------------------------

user = {
    "name": "Alan",
    "age": 27,
    "admin": True
}

if user.get("admin"):
    print(f"{user['name']} jest administratorem.")
else:
    print(f"{user['name']} nie jest administratorem.")


# ==========================================
# 2. TUPLE - KROTKA
# ==========================================

# Tuple zapisujemy za pomocą ()
# Jest podobny do listy, ale nie możemy zmieniać jego elementów.

car = ("Mercedes", "W210", 1998)

print(car)
print(car[0])
print(car[1])
print(car[2])


# Tego NIE możemy zrobić:
#
# car[1] = "W211"
#
# TypeError - tuple jest niemutowalny.


# ------------------------------------------
# Rozpakowywanie tuple
# ------------------------------------------

person = ("Alan", 27, "Białystok")

name, age, city = person

print(name)
print(age)
print(city)


# ------------------------------------------
# Tuple z jednym elementem
# ------------------------------------------

# Przecinek jest tutaj bardzo ważny.

engine = ("OM606",)

print(engine)
print(type(engine))


# Bez przecinka byłby to zwykły string:

engine = ("OM606")

print(type(engine))


# ------------------------------------------
# Pętla po tuple
# ------------------------------------------

models = ("W210", "W211", "W212", "W213")

for model in models:
    print(f"Model: {model}")


# ------------------------------------------
# Funkcja zwracająca wiele wartości
# ------------------------------------------

dog = {
    "name": "Duke",
    "age": 2,
    "breed": "Pitbull"
}


def get_dog(dog):
    return dog["name"], dog["breed"]


name, breed = get_dog(dog)

print(name)
print(breed)


# ==========================================
# 3. SET - ZBIÓR
# ==========================================

# Set:
# - przechowuje unikalne wartości
# - nie przechowuje duplikatów
# - nie korzystamy z indeksów
# - nie zakładamy konkretnej kolejności


dogs = {
    "Labrador",
    "Husky",
    "Labrador",
    "Malinois",
    "Husky"
}

print(dogs)

# Mimo że wpisaliśmy 5 elementów,
# są tylko 3 unikalne.
print(len(dogs))


# ------------------------------------------
# .add()
# ------------------------------------------

cars = {"Mercedes", "BMW", "Audi"}

cars.add("Porsche")

print(cars)


# ------------------------------------------
# .remove()
# ------------------------------------------

dogs = {"Labrador", "Husky", "Malinois"}

dogs.remove("Husky")

print(dogs)

# UWAGA:
# remove() nieistniejącego elementu powoduje KeyError.


# ------------------------------------------
# .discard()
# ------------------------------------------

cars = {"Mercedes", "BMW", "Audi"}

# Nie powoduje błędu, nawet jeśli Porsche nie istnieje.
cars.discard("Porsche")

print(cars)


# ------------------------------------------
# Sprawdzanie elementu
# ------------------------------------------

allowed_roles = {"admin", "moderator", "editor"}

if "admin" in allowed_roles:
    print("Admin ma dostęp.")


# ------------------------------------------
# Lista -> set
# ------------------------------------------

dogs = [
    "Husky",
    "Labrador",
    "Husky",
    "Malinois",
    "Labrador",
    "Rottweiler"
]

# Usunięcie duplikatów
unique_dogs = set(dogs)

print(unique_dogs)
print(len(unique_dogs))


# ------------------------------------------
# Pusty set
# ------------------------------------------

# {} oznacza pusty DICT!
empty_dict = {}

# Pusty SET tworzymy tak:
skills = set()

skills.add("Python")
skills.add("SQL")
skills.add("Git")

print(skills)
print(type(skills))


# ------------------------------------------
# Pętla po set
# ------------------------------------------

skills = {"Python", "SQL", "Git"}

for skill in skills:
    print(f"Umiem: {skill}")


# ==========================================
# OPERACJE NA SETACH
# ==========================================

alan_skills = {"Python", "SQL", "Git", "FastAPI"}
job_skills = {"Python", "Git", "Docker", "PostgreSQL"}


# ------------------------------------------
# intersection()
# ------------------------------------------

# Co mają wspólnego?

common_skills = alan_skills.intersection(job_skills)

print("Wspólne:", common_skills)


# ------------------------------------------
# difference()
# ------------------------------------------

# A.difference(B)
# = co jest w A, czego NIE MA w B

# Czego wymaga praca, czego Alan nie ma?

missing_skills = job_skills.difference(alan_skills)

print("Brakujące:", missing_skills)


# ------------------------------------------
# union()
# ------------------------------------------

# Połączenie obu setów bez duplikatów.

all_skills = alan_skills.union(job_skills)

print("Wszystkie:", all_skills)


# ==========================================
# DICT + SET + TUPLE + FUNCTION
# ==========================================

candidate = {
    "name": "Alan",
    "skills": {"Python", "SQL", "Git", "FastAPI"}
}

job_skills = {
    "Python",
    "Git",
    "Docker",
    "PostgreSQL"
}


def analyze_candidate(candidate, job_skills):
    # Pobieramy set ze słownika.
    candidate_skills = candidate["skills"]

    # Co mają wspólnego?
    common_skills = candidate_skills.intersection(job_skills)

    # Czego wymaga praca, czego kandydat nie ma?
    missing_skills = job_skills.difference(candidate_skills)

    # Zwracamy dwie wartości.
    return common_skills, missing_skills


# Rozpakowanie dwóch zwróconych wartości.
common, missing = analyze_candidate(candidate, job_skills)

print("Wspólne umiejętności:", common)
print("Brakujące umiejętności:", missing)


# ==========================================
# ŚCIĄGA
# ==========================================

# LIST
# []
# uporządkowana, można zmieniać

# DICT
# {"key": "value"}
# dane jako klucz -> wartość

# TUPLE
# ()
# uporządkowany, ale nie można zmieniać elementów

# SET
# {"Python", "Git"}
# unikalne elementy, bez indeksowania


# SET - NAJWAŻNIEJSZE OPERACJE:
#
# A.intersection(B)
# -> co mają wspólnego
#
# A.union(B)
# -> wszystko z A i B bez duplikatów
#
# A.difference(B)
# -> co jest w A, czego nie ma w B
#
# Najkrócej:
#
# intersection = WSPÓLNE
# union        = WSZYSTKO
# difference   = A MINUS B