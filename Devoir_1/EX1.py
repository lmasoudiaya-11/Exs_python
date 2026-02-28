age = input("Entrez votre âge : ")
age = int(age)


if age >= 0 and age <= 12:
    print(f"Statut : Enfant")
elif age >= 13 and age <= 17:
    print(f"Statut : Adolescent")
elif age >= 18 and age <= 64:
    print(f"Statut : Adulte")
elif age >= 65:
    print(f"Statut : Senior")
else:
    print(f"Âge invalide")
