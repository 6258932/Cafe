choix = [("Starbucks", 1.2, 8),
         ("Cafe_local", 0.5, 7),
         ("Pete's_Coffee", 1.8, 9),
         ("Dunkin_Donuts", 0.8, 6)
         ]


def meilleur_cafe(choix):
    for n in range(0, len(choix)):
        meilleur_gout = 10
        rating = choix[n][2]

        if rating == meilleur_gout:
            return rating
        meilleur_gout -= 1
        if meilleur_gout == rating:
            return rating

    return "Aucun, veulez rechercher d'autre option"


def mieux_portefeuille(choix):
    for n in range(0, len(choix)):
        moins_gas = 0
        km = choix[n][1]
        if km == moins_gas:
            return km
        moins_gas += 0.5
        if moins_gas == km:
            return km

    return "Aucun, veulez rechercher d'autre option"

# fonctionne pas pourra jamais trouver identique
def le_mieux(resultat1, resultat2):
    for n in range(0, len(choix)):
        km = choix[n][1]
        name = choix[n][0]
        rating = choix[n][2]

        if resultat2 == km and resultat1 == rating:
            return name
        resultat1 -= 1
        resultat2 += 0.5
        if resultat2 == km and resultat1 == rating:
            return name


resultat = meilleur_cafe(choix)
resultat2 = mieux_portefeuille(choix)
resultat_final = le_mieux(resultat, resultat2)
print(f"Le meilleur café est {resultat}")
print(f"Le mieux pour le portefeuille est {resultat2}")
print(f"Le mieux pour le mieux {resultat_final}")
