historique = []

while True:
    print(" CALCULATEUR DE TRAJET ")
    print("1 - Zemidjan")
    print("2 - Taxi")
    print("0 - Quitter")

    choix = input("Choisis ton moyen de transport : ")

    if choix == "0":
        print("Merci d'avoir utilisé le programme.")
        break

    if choix == "1":
        moyen = "Zemidjan"
        tarif_de_base = 150
        prix_par_km = 75
        majoration = 0.15

    elif choix == "2":
        moyen = "Taxi"
        tarif_de_base = 200
        prix_par_km = 100
        majoration = 0.25

    else:
        print("Choix invalide.")
        continue

    try:
        distance = float(input("Entrer la distance en km : "))

        heure = input("Entre l'heure du trajet (ex: 11:45) : ")

        heures, minutes = heure.split(":")
        heures = int(heures)
        minutes = int(minutes)

        if distance <= 0:
            print("La distance doit être supérieure à 0.")
            continue

        if heures < 0 or heures > 23 or minutes < 0 or minutes > 59:
            print("Heure est invalide.")
            continue

    except ValueError:
        print("Erreur : Verifier ce que vous avez entrer.")
        continue

    heure_decimal = heures + minutes / 60

    prix = tarif_de_base + (prix_par_km * distance)

    if (7 <= heure_decimal <= 8.75) or \
       (11.75 <= heure_decimal <= 13) or \
       (17 <= heure_decimal <= 19):

        heure_de_pointe = True
        prix = prix * (1 + majoration)

    else:
        heure_de_pointe = False

    prix_arrondi = round(prix / 25) * 25

    historique.append({
        "moyen": moyen,
        "distance": distance,
        "heure": heure,
        "pointe": heure_de_pointe,
        "prix": prix_arrondi
    })

    print(" RÉCAPITULATIF ")
    print("moyen :", moyen)
    print("Distance :", distance, "km")
    print("Heure :", heure)

    if heure_de_pointe:
        print("Heure de pointe : Oui")
    else:
        print("Heure de pointe : Non")

    print("Prix final :", prix_arrondi, "FCFA")

    encore = input("\nVeux-tu calculer un autre trajet ? (o/n) : ")

    if encore.lower() != "o":
        break


print(" HISTORIQUE DES TRAJETS ")

if len(historique) == 0:
    print("Aucun trajet enregistré.")
else:
    for i, trajet in enumerate(historique, 1):
        print("\nTrajet", i)
        print("moyen :", trajet["moyen"])
        print("Distance :", trajet["distance"], "km")
        print("Heure :", trajet["heure"])

        if trajet["pointe"]:
            print("Heure de pointe : Oui")
        else:
            print("Heure de pointe : Non")

        print("Prix :", trajet["prix"], "FCFA")

print("\nFin du programme.")