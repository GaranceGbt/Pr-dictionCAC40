# En-tete ---------------------------------------------------------------------
# # Author: Gabaut Garance 
# # Date: septemblre - octobre 2022
# # module : algorthmique - M. Gambo Magagi
# # tite : Crawler - La récuperation des données


# Packages --------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup # peremt de travailler et recolter les données sur une page Web
import pandas as pd # permet de manipuler des dataframes
import time # permet l'usage des dates et heures 


#  Partie 1 -------------------------------------------------------------------
# fonction qui parcours toutes les pages du site et les stock dans une liste
# en entrée : 
# en sortie : links - un vecteur 2*1 contenants les deux urls


def get_all_pages():
    links = [] 
    for i in range(1,3):  
        link= f"https://www.boursorama.com/bourse/actions/cotations/page-{i}?quotation_az_filter%5Bmarket%5D=1rPCAC&quotation_az_filter%5Bletter%5D=&quotation_az_filter%5Bfilter%5D=&pagination_617167101="
        links.append(link)  
    print(links)
    return links


# dans notre cas, les donnees du CAC 40 sont repartis sur deux pages
# avec 27 entreprises sur la premiere page, 13 sur la seconde



# Partie 2 ----------------------------------------------------------------------
# extrait le nom des entreprises 
# en entrée : lien(s) de notre/nos page(s) Web
# en sortie : un veceur name contenant les noms des entreprises du CAC 40


def name_compagnies(links) :
    
    for i in range(2): 
        #Boucle permettant de parcourir les deux pages de donnees du CAC40
        soup = BeautifulSoup(requests.get(links[i]).text, 'html.parser')
 
        if i==0: #1er page
            name0 = soup.find_all("div",{"o-pack__item u-ellipsis u-color-cerulean"})
            for k in range(len(name0)):
                name0[k]=name0[k].get_text(strip=True)
                
        else: #2eme page
            name1 = soup.find_all("div",{"o-pack__item u-ellipsis u-color-cerulean"})
            for k in range(len(name1)):
                name1[k]=name1[k].get_text(strip=True)
                
    #On regroupe tous les noms en concervant bien l'ordre (page 1 en premier puis la 2)
    name=name0+name1    
    return name



# extrait les données de la bourse
# en entrée : lien(s) de notre/nos page(s) Web
# en sortie : vecteur contenant les données fraichement recoltés

def datas_compagnies(links) :
    
    for i in range(2):
        #Boucle permettant de parcourir les 2 pages de donnees du CAC 40
        soup = BeautifulSoup(requests.get(links[i]).text, 'html.parser')
             
        # Les x premieres donnees ne concernent pas les entreprises du CAC40 
        # mais d'autres informations presentes sur la page
        # nous les retirons donc       
        if i==0:
            last0 = soup.find_all("span",{"c-instrument c-instrument--last"})
            x=len(last0)-27 #on determine le nombre de donnees qui ne nous concernent pas (donnees totale - nombre de d'entreprises)
            del last0[0:x] # les donnees inutiles sont au debut du vecteur, on les supprime simplement
            for j in range(len(last0)):
                last0[j]=last0[j].get_text(strip=True)

        else: 
            last1 = soup.find_all("span",{"c-instrument c-instrument--last"})
            x=len(last1)-13 #on determine le nombre de donnees qui ne nous concernent pas 
            del last1[0:x] # les donnees inutiles sont au debut du vecteur, on les supprime simplement
            for j in range(len(last1)):
                last1[j]=last1[j].get_text(strip=True)
                
    last=last0+last1 # On concatène les deux vecteurs, pour en avoir plus qu'un avec toutes le données
    return (last)



# #  Partie 3 --------------------------------------------------------------------
# # Recolter les donnees a intervalles de temps reguliers, le tout au sien d'une seule 
# # et unique data frame 



#en entree: date d'arret a ecrire de la facon suivante: "DD/MM/YYYY"
#           heure d arret a ecrire de la facon suivante: "%H:%M"
#           intervalle de temps entre chaue recolte en seconde
#           le titre que vous souhaitez donner a votre dataframe, elle s'enregistrera sous ce nom sur votre terminale
#en sortie: la table avec l'entierté des données recoltées

def collect_datas(stopDate, stopHour, interval, title):
    
    links=get_all_pages()  #on recolte les deux liens 
    name=name_compagnies(links) #on stocks les noms des entreprises
    AllDatas=pd.DataFrame(columns = name) # On commence par crée notre data frame avec les noms des entreprises
    currentDate= time.strftime("%d/%m/%Y") 
    currentHour = time.strftime("%H:%M") 
    IndexHour=[] 
    i=0
    
    while (currentDate <= stopDate)  : 
        if (currentHour <= stopHour): 
            if ((0<=int(time.strftime("%H"))<=9) or ("17:30"<=time.strftime("%H:%M")<="23:00") or ((time.strftime("%A") in ["Sunday"] ))):
               time.sleep(60) 
    
            else :  
                
                datasTime=datas_compagnies(links) # fonction qui recolte les données
                    
                hour = time.strftime("%H:%M:%S") 
                IndexHour.append(hour)
                AllDatas.loc[i] = datasTime  
                i+=1  
                time.sleep(interval) 
    
        currentHour = time.strftime("%H:%M") 
        currentDate= time.strftime("%d/%m/%Y")
        
    # enregtistre les donnees sur notre ordinateur
    AllDatas.index=IndexHour
    AllDatas.to_csv(f'{title}.csv', index=True , sep =";") 
    return(AllDatas)

# #  Partie 4 -----------------------------------------------------------------
# Utilisation du crawler

links=get_all_pages()  
name="entrerUnTitre"
date="05/11/2022"
hour="17:30"
interval=300
Datas=collect_datas(date, hour, interval, name)




