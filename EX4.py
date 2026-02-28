num1 = float(input("Premier nombre : "))
num2 = float(input("Deuxième nombre : "))

print("\nChoisissez l'opération :")
print("1 : Addition")
print("2 : Soustraction")
print("3 : Multiplication")
print("4 : Division")


choix = input("Votre choix : ")

if choix == "1":
    resultat = num1 + num2
    print(f"Résultat : {resultat}")

elif choix == "2":
    resultat = num1 - num2
    print(f"Résultat : {resultat}")

elif choix == "3":
    resultat = num1 * num2
    print(f"Résultat : {resultat}")

elif choix == "4":

    if num2 != 0:
        resultat = num1 / num2
        print(f"Résultat : {resultat}")
    else:
        print("Erreur : division par zéro impossible.")

else:
    print("Choix invalide.")