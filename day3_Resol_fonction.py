import math

#FONVCTION DU TYPE y=ax²+bx+c

A=input("Entrez le premier nombre : ")
a=float(A)
B=input("Entrez le premier nombre : ")
b=float(B)
C=input("Entrez le premier nombre : ")
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
