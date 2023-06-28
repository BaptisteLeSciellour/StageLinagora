import pandas as pd 

def main():
    tableau = []
    verif = False
    with open("conver.txt",'r') as f:
        for s in f:
            verif = False
            s=s.split(',')
            for i in range(0,len(tableau)):
                if(s[10]==tableau[i]): # c'est ici au niveau du chiffre qu'il faut changer, il faut mettre la valeur du tableau que vous souhaitez comparé
                    verif = True
            if (verif == False):
                tableau.append(s[10])

    print(tableau)
    df = pd.DataFrame(tableau)  # Créez un DataFrame à partir du tableau complet
    df.to_excel("listeTypedeTache.xlsx", index=False, header=False, engine='openpyxl')  # Écrivez le DataFrame dans le fichier Excel


if __name__ == "__main__":
    main()

