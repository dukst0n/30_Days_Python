#1. Déclaration de l'âge comme variable entière
nombre1 = 35
age = int(nombre1)

#2. Déclaration de la taille comme variable flottante
nombre2 = 1.75
taille = float(nombre2)

#3. Déclaration d'une variable qui stocke un nombre complexe
nombre3 = 3 + 2j 
complexe = complex(nombre3)
# Affichage des variables (facultatif, pour vérification)
print(f"Votre âge : {age} ans")
print(f"Votre taille : {taille} mètres")
print(f"Nombre complexe : {complexe}")
print()

#4. Script pour calculer l'aire d'un triangle
    #aire = (base x hauteur)/2 

data1 = input("Entrez la base du triangle : ")
base = float(data1)
data2 = input("Entrez la hauteur du triangle : ")
hauteur = float(data2)

    # Calculer l'aire
aire = 0.5 * base * hauteur

print(f"\nL'aire du triangle est : {aire}")
print()

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

cote1 = input("Entrez la longueur du côté a : ")
cote_a = float(cote1)
cote2 = input("Entrez la longueur du côté b : ")
cote_b = float(cote2)
cote3 = input("Entrez la longueur du côté c : ")
cote_c = float(cote3)

# le périmètre
perimetre = cote_a + cote_b + cote_c

print(f"Le périmètre du triangle est : {perimetre}")
print()

#6. Calcul de l'aire et du périmètre d'un rectangle

longueur = input("Entrez la longueur du rectangle : ")
L = float(longueur)
largeur = input("Entrez la largeur du rectangle : ")
l = float(largeur)

aire = L * l
perimetre = 2 * (L + l)

print(f"\nL'aire du rectangle est : {aire}")
print(f"\nLe périmètre du rectangle est : {perimetre}")
print()

#7. Calcul de l'aire et de la circonférence d'un cercle

import math
pi = 3.14
rayon = input("Entrez le rayon du cercle : ")
r = float(rayon)

aire = pi * r * r
circonference = 2 * pi * r

print(f"\nL'aire du cercle est : {aire}")
print(f"\nLa circonférence du cercle est : {circonference}")
print()

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# RESOLUTION DE FONCTION DU TYPE Y = AX²+BX+C

import math

A=input("Entrez le premier nombre a : ")
a=float(A)
B=input("Entrez le premier nombre b : ")
b=float(B)
C=input("Entrez le premier nombre c : ")
c=float(C)

d  = ((b * b)-(4 * a * c))

if d<0:
    print(f"\nLa fonction Y={a}X² + {b}X + {c} n'est pas résolvable")
    print(f"\nS = Ensemble vide")
    print()
elif d==0:
    print(f"\nLa fonction Y={a}X² + {b}X + {c} a une double solution : ")
    y  = float(-(b)/(2*a))
    print(f"\nS = {y}")
    print()
else :
    print(f"\nLa fonction Y={a}X² + {b}X + {c}  a deux solution y1 et y2")
    y1 = float(-(b)-(math.sqrt(d))/(2 * a))
    y2 = float(-(b)+(math.sqrt(d))/(2 * a))
    print(f"\ny1 = ({y1})")
    print(f"\ny2 = ({y2})")
    print(f"\nS = ({y1}, {y2})")
    print()

#12. Longueur de 'python' et 'dragon' et comparaison fausse

long_python = len('python')
long_dragon = len('dragon')

print(f"Longueur de 'python' : {long_python}")
print(f"Longueur de 'dragon' : {long_dragon}")

comparison = (long_python == long_dragon)

print(f"\nEst-ce que la longueur de 'python' est égale à la longueur de 'dragon' ? {comparison}")
print()

#13. Vérifier si 'on' est trouvé dans les deux chaînes

check_python = 'on' in 'python'
check_dragon = 'on' in 'dragon'

sortie = check_python and check_dragon

print(f"\n'on' est-il dans 'python' ? {check_python}")
print(f"\n'on' est-il dans 'dragon' ? {check_dragon}")
print(f"\n'on' est-il dans 'python' & 'dragon' ? {sortie}")
print()

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

heure = input("Entrez le nombre d'heures travaillées : ")
h = float(heure)

taux_horaire = input("Entrez le taux par heure (€ ou autre devise) : ")
th = float(taux_horaire)

salaire = taux_horaire * heure

print(f"\nLe salaire de la personne est : {salaire:.2f} (en tenant compte de 2 décimales)")
print()

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

annee = input("Entrez le nombre d'années : ")
ans = float(annee)

    # données prises en compte
    # jours_par_an = 365       
    # heures_par_jour = 24
    # minutes_par_heure = 60
    # secondes_par_minute = 60

secondes = annee * 365 * 24 * 60 * 60

print(f"\nVous avez vécu pendant {annee} an(s) soit {secondes:,.0f} secondes.")
print()

#23. Écrivez un script Python qui affiche le tableau suivant
    # 1 1 1 1 1 1 2 1 2 4
    # 8 3 1 3 9 27 4 1 4 1
    # 6 64 5 1 5 25 125

for i in range(1, 6):
    n_power_0 = 1
    n_power_1 = i
    n_power_2 = i ** 2
    n_power_3 = i ** 3

    if i == 1:
        print(f"{i} {n_power_0} {n_power_1} {n_power_2} {n_power_3}")
        print("2 1 2 4")
    elif i == 3:
        print(f"{i} {n_power_0} {n_power_1} {n_power_2} {n_power_3}")
    elif i == 4:
        print(f"{i} {n_power_0} {n_power_1} {n_power_2} {n_power_3}")
    elif i == 5:
        print(f"{i} {n_power_0} {n_power_1} {n_power_2} {n_power_3}")

print("1 1 1 1 1")
print("2 1 2 4")
print("8 3 1 3 9 27")
print("4 1 4 1")
print("6 64 5 1 5 25 125")