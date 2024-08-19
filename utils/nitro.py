# Coded by 7b3087 


bleu = "\33[0;34m"
cyan = "\033[1;36m"
violet = "\033[0;35m"
vert = "\033[0;32m"
orange = "\033[0;33m"
rose = "\033[1;31m"
bleu_foncé = "\033[1;34m"
blanc = "\033[1;37m"
gris = "\033[1;30m"
rouge = "\033[1;39m"


import time
import random
import string
import requests
import random
import colorama
                                                            
num = input("Combien de nitro voulez vous générer ? ")

f = open("Nitro Codes .txt", "w", encoding='utf-8')

print(gris, 'Téléchargement des paquets...')
print(" ")
print(" ####- - - - - - 40 Pourcents...")
time.sleep(2)
print(" ######## - - 80 Pourcents...")
time.sleep(4)
print(vert, "Paquets Téléchargés !")
time.sleep(2)
print(bleu, "Génération des codes en cours...")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

with open("Nitro codes .txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(vert, " VALIDE | {} ".format(line.strip("\n")))
            break
        else:
            print(rouge," INVALIDE | {} ".format(line.strip("\n")))

input("Fin de la génération !")
input("7b3087 <3")
input("A bientot !")