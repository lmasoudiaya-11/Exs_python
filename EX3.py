mot_correct = "python123"
mot = ""

while mot != mot_correct:

    mot = input("Entrez le mot de passe : ")

    if mot != mot_correct:
        print("Mot de passe incorrect.")

print("Accès autorisé.")