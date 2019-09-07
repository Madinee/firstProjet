# -*-coding:Utf-8 -*
#!/usr/bin/python3.5
# ce programme est un jeu nommé z casino
#règle du jeu:Il s'agira d'un petit jeu de roulette très simplifié dans lequel vous pourrez miser une certaine somme et gagner ou perdre de l'argent (telle est la fortune, au casino !). Quand vous n'avez plus d'argent, vous avez perdu.

from random import randrange
from math import ceil


print("saisissez un numéro compris entre 0 et 49")
numero_saisi=input()
numero_saisi=int(numero_saisi)
while numero_saisi<0 or numero_saisi>49:
	numero_saisi=input("veuillez saisir un numero compris entre 0 et 49\n")
	try:
		numero_saisi=int(numero_saisi)
		break
	except NameError:
		print("veuillez saisir une valeur entière\n")
		continue
	#except ValueError:
	   # print("veuillez saisir un entier \n")
		#continue
print("vous avez choisir:  ", numero_saisi)
while 1:
    try:
        somme_mise=input("combien souhaitez vous miser?\n")
        somme_mise=int(somme_mise)
        assert somme_mise>0
        break
    except NameError:
	    print("veuillez saisir une valeur entière\n")
	    continue
    except ValueError:
	    print("veuillez saisir un entier \n")
	    continue
	# except AssertionError:
	# 	print("veuillez saisir une valeur positive\n")
	# 	continue
print("vous avez miser ", somme_mise,"$\n")
numero_gagnant=randrange(50)
print("le numero generé est:\n ", numero_gagnant)
if numero_gagnant==numero_saisi:
	gain=somme_mise*3
	gain=ceil(gain)
	print("bravo vous avez gagner: ", gain)
elif (numero_saisi%2==numero_gagnant%2):
	gain=somme_mise/2
	gain=ceil(gain)
	print("mince vous ne gagner que la moité de votre  somme misée : ", gain)
else:
	print("vous avez perdu votre argent ")

print("au revoir et a bientot!")


