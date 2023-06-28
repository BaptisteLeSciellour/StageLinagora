import pandas as pd
from openpyxl import Workbook

def main():
    tableau = []
    listeA = [12, 34]
    listeB = [13, 44]
    compteurs = 0
    dejavu = [listeA, listeB]
    with open("conver.txt", "r") as f:
        for s in f:
            s = s.split(',')
            test(dejavu, s, compteurs)
            print("//////////////////////////////////////////////////")
    for i in dejavu:
        tableau = i
        mot = "operation" + str(tableau[0]) + "complete.xlsx" # donne le nom du tableur
        tableau.pop(0)
        print(tableau)
        df = pd.DataFrame(tableau)  # Créez un DataFrame à partir du tableau complet
        df.to_excel(mot, index=False, header=False, engine='openpyxl')  # Écrivez le DataFrame dans le fichier Excel


def test(dejavu, s, compteur):
    index = 0
    while index < len(dejavu):
        w = dejavu[index]
        print("entre : ", w[0])
        if w[0] == s[13]: # ici pour changer la condition par le 13
            w.append(s)
            return 1
        index += 1
    compteur += 1
    ListeC = [s[13], s] # de même qu'ici
    dejavu.append(ListeC)

if __name__ == "__main__":
    main()
