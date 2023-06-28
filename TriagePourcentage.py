import pandas as pd
from openpyxl import Workbook

def main():
    sortie =[]
    with open("conver.txt", "r") as f:
       with open("listesocunique.txt","r") as r:
           tableau=[]
           for s in r :
               s=s.split(",")
               uneliste=[s[0],s[2]]
               tableau.append(uneliste)
       j=0
       verif = False
       for s in f : 
         j +=1
         verif = False
         s=s.split(',')
         for i in range(0,len(tableau)):
           if s[2]==tableau[i][0] and verif == False:
              if tableau[i][1]=="Yannick":
                sortie.append('Yannick RIVERA')
              if tableau[i][1]=="Nicolas":
                sortie.append('Nicolas CHRISTODOULOU')
              if tableau[i][1]=="":
                 sortie.append('Michel-Marie MAUDET')
              verif = True
         if verif==False : 
            sortie.append('Baptiste LE SCIELLOUR')
    
    print(len(sortie),"/",j)
    df = pd.DataFrame(sortie)  # Créez un DataFrame à partir du tableau complet
    df.to_excel("listeCommerciaux.xlsx", index=False, header=False, engine='openpyxl')  # Écrivez le DataFrame dans le fichier Excel

   



if __name__ == "__main__":
    main()
