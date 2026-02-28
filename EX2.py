contacts = []
choix = ""

while choix != "3":

    print("\n--- MENU ---")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom du contact : ")

       
        if nom != "":
            contacts.append(nom)
            print(f"Contact ajouté : {nom}")
        else:
            print("Nom invalide.")

    elif choix == "2":

        if len(contacts) == 0:
            print("Aucun contact enregistré.")
        else:
            print("\nListe des contacts :")
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact}")

    elif choix == "3":
        print("Fin du programme.")

    else:
        print("Choix invalide.")