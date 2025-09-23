import math
import random
import re
import time
import tkinter as tk

Nombre = input("Combien de participants ?\n> ")
regexp = re.compile('[a-zA-Z]+') #Regex qui cherche toutes les lettres (minuscules et majuscules) dans une châine


def Nb_Participants(Nb): #-----# Définition du nombre de participants ainsi que leurs noms #-----#
	count = 0
	Participants = []
	
	while(count < int(Nb)):
		Participants.append(input("Nom du participant\n>"))
		count = count + 1

	return(Participants)

def Randomizer(List): #-----# Fonction tirant les joueurs au hasard #-----#	
	return random.choice(List)	#Voir si la fontion ne prend pas juste le premier élément de la liste
	
def Relance_Ronde(List):
	
	Check = True
	cp = 0
	Nb_Ronde = 1
	List_Rondes = []
	regexp = re.compile('[a-z]+') #Regexp qui cherche les chaînes de caractères 
	
	if(Nb_Ronde > 1):
		while(cp < len(List)):
			if(regexp.search(str(List)) == regexp.search(str(List_Rondes[cp]))):
				Check = False
				break
				
	return (Check)	

def Blanc(Dico, String): #-----# Fonction de détection de l'obtention des blancs #-----#
	Liste_Verif = Dico
	Verif, Counter = False, 0
	
	return(Verif)




def Ronde(): #-----# Fonction principale #-----#
	
	
	#-----# Déclaration des variables #-----#	
	Joueur_Blanc, Rep = "", ""
	ronde = True	
	Matchs = False
	Nb_ronde = 1
	count, cp = 0, 0
	Match1, Match2, Liste_Matchs = [], [], []
	Score_Joueurs, Blanc = {}, {}
	Liste_Participants = Nb_Participants(Nombre)
	Verif_Match = {}
	
	
	#-----# Création de la grille des scores et de la grille d'obtention des blancs #-----#
	while(cp < len(Liste_Participants)):
		regexp2 = regexp.search(str(Liste_Participants[cp]))
		Score_Joueurs.update({str(regexp2.group()):0})
		Blanc.update({str(regexp2.group()):0})
		cp = cp + 1
	
	cp = 0
	
	#-----# Boucle principale des rondes #-----# 
	while(ronde == True):			
		print("Numero de la ronde : " + str(Nb_ronde))
		if(Nb_ronde > 1):
			print(Liste_Participants)
		#-----# Détermination des matchs #-----# 
		while(count < 2):
			Match1.append(random.choice(Liste_Participants))
			Match2.append(random.choice(Liste_Participants))
			count = count + 1
		
		#-----# Vérification des matchs #-----# --> faire vérif avec dictionnaire (faire comme un switch)
		if(Match1[0] == Match1[1] or Match2[0] == Match2[1] or Match1[0] == Match2[0] or Match1[0] == Match2[1] or Match2[0] == Match1[1] or Match1[1] == Match2[1]):     
			while(Matchs == False):
				print("Erreur de dispatch, relance de la ronde")
				if(Match1[0] == Match1[1] or Match2[0] == Match2[1] or Match1[0] == Match2[0] or Match1[0] == Match2[1] or Match2[0] == Match1[1] or Match1[1] == Match2[1]): 
					count = 0
					Match1, Match2 = [], []
					while(count < 2):                                                                    
						Match1.append(random.choices(Liste_Participants))
						Match2.append(random.choices(Liste_Participants))
						count = count + 1
				else:
					Matchs = True	

		count = count + 1
	
		#------------------------------------------#
		
		print("Liste des matchs\n" + str(Match1) + '\n' + str(Match2) + '\n')
		print("Résultat de la ronde : \n")
		
		Result = input("Match 1 : ")
		Score_Joueurs[Result] = Score_Joueurs[Result] + 1
		
		Result = input("Match 2 : ")
		Score_Joueurs[Result] = Score_Joueurs[Result] + 1
		
		Liste_Matchs.append(Match1)
		Liste_Matchs.append(Match2)
		print(Score_Joueurs)
		print(Blanc)
		
		#-----# Déclaration d'une autre ronde et remise au propre de la liste des participants #-----#	
		Rep = input("Declarer une autre ronde ?\n-> ")
		if(Rep == 'n' or Rep == 'N'):
			ronde = False
			
		else:
			Nb_ronde = Nb_ronde + 1
			Liste_Matchs.append(Match1)
			Liste_Matchs.append(Match2)
			Match1, Match2 = [], []
			count, cp = 0, 0
			Matchs = False
			
Ronde()