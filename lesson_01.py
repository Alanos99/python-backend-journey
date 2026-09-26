name = input("Jak masz na imię?")
age = int(input("Ile masz lat?"))
ticket = int(input("Ile biletów chcesz kupić?"))

if age < 18:
    print("Przysługuje Ci zniżka uczniowska")
elif age < 65:
    print("Płacisz normalnie")
else:
    print("Zniżka seniora")

print(f"Cześć {name}!")
print(f"Kupujesz {ticket} bilety")
print(f"Cena przed rabatem: {ticket * 40}") 


