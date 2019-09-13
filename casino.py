# -*-coding:Utf-8 -*
#!/usr/bin/python3.5
# ce programme est un jeu nommé z casino
#règle du jeu:Il s'agira d'un petit jeu de roulette très simplifié dans lequel vous pourrez miser une certaine somme et gagner ou perdre de l'argent (telle est la fortune, au casino !). Quand vous n'avez plus d'argent, vous avez perdu.

from random import randrange
from math import ceil

# variable globale
continuer=True
while continuer:# tant que l'utilisateur voudra rejouer le jeu

	print("saisissez un numéro compris entre 0 et 49")
	numero_saisi=input()
	numero_saisi=int(numero_saisi)
	while numero_saisi<0 or numero_saisi>49:
		numero_saisi=input("veuillez saisir un numero compris entre 0 et 49\n")
		try:
			numero_saisi=int(numero_saisi)
		except ValueError:
			print("veuillez saisir un nombre\n")
			continue
		if numero_saisi<0:
			print"le numero saisi est négatif\n"
		if numero_saisi>49:
			print"le numero saisi est superieur a 49\n"
	print"**************vous avez choisir:  ", numero_saisi, "*******************\n"
	somme_mise=0# je mets somme_mise a 0 pour pouvoir entrer dans la boucle
	while somme_mise<=0:
		somme_mise=input("combien souhaitez vous miser?\n")
		try:
			somme_mise=int(somme_mise)
		except ValueError:
		    print("veuillez saisir un entier \n")
		    continue
		if somme_mise<=0:
			print"la somme miseée ne peut etre inferieur ou egal a zero\n"
			
		
	print"******************vous avez miser ", somme_mise,"$ ***********************\n"
	numero_gagnant=randrange(50)
	print"********************le numero generé est:", numero_gagnant,"******************\n"
	if numero_gagnant==numero_saisi:
		gain=somme_mise*3
		gain=ceil(gain)
		print"bravo vous avez gagner : ", gain
	elif (numero_saisi%2==numero_gagnant%2):
		gain=somme_mise/2
		gain=ceil(gain)
		print"mince vous avez perdu la moitié de votre argent : ", gain
	else:
		print"dommage !vous avez perdu votre argent \n"
	quitter=raw_input("souhaiter vous quitter le jeu casison ou continuer a jouer(o/n)\n")
	# print(quitter)
	if quitter=="o" or quitter=="O":
		continuer=False
		print("==========================au revoir et a bientot!============================")


