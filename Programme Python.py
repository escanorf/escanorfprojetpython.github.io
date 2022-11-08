import sys
##########Calculette basique##############


##a= input(" entre un nombre ")
##b= input(" entre un autre nombre ")
##print (f"le resulat du calcul de {a} et {b} est egal a {int(a) + int(b)}")



#######################Affichage utilsateur#######################

##for i in range(1,11):
##    print(f"utlilisateur {i}")



################ liste de courses ###########################

LISTE = []  

MENU = """Choisisez parmi les 5 options suivantes : 
1: AJouter un element a la liste
2: Retirer un element de la liste
3: afficcher la liste
4: vider la liste 
5: Quitter
 Votre choix : """
 
MENU_CHOICES = ["1" , "2" , "3" , "4" , "5"]
 
 
while True:
     user_choice = ""
     while user_choice not in MENU_CHOICES:
         user_choice = input (MENU)
         if user_choice not in MENU_CHOICES: 
            print("Veuiller choisir une option valide...")
     
     
if user_choice == "1": #Ajouter un element
            item = input ("entrer le nom d'un element à ajouter a la liste de courses:")
            LISTE.append (item)
            print(f"l'element {item} a bien ete ajoute a la lsite.")
            
elif user_choice =="2": #Retirer un element 
            item = input("entrer le nom d'un element à ajouter a la liste de courses:")
            if item in LISTE:
                LISTE.remove(item)
                print(f"l'element {item} a bien ete ajoute a la lsite.")
            else:
                print(f"l'element {item} a bien ete ajoute a la liste.")
     
elif user_choice =="3":#afficher la liste    
    if LISTE:
        print("Voici le contenu de votre liste:")
    for i, item in enumerate(LISTE):
        print(f"{i+1}. {item}")
    else:
        print("votre liste ne contient aucun element.")        
elif user_choice == "4": #Vider la liste
    LISTE.clear()
    print("la liste a ete videe de son contenu.")
elif user_choice == "5": #Quitter
    print("A bientot !")
    sys.exit()
    
    print("-" *50)
    