    # Entrez des nombres pour les opérations
p = input("Entrez le premier nombre entier différent de 0 : ")
q = input("Entrez le second nombre entier différent de 0 : ")

    # OPERATIONS
x = int(p)
y = int(q)
    # Addition
a = x + y
    # Soustraction normale
b = float(x - y)
    # Soustraction normalisée (Différence entre x et y)
if x > y :
    c = x - y
else :
    c = y - x
    # Multiplication
d = x * y
    # Division
e = x / y
    # Modulo 1
f = x % y
    # Modulo 2
g = y % x
    # Exponentielle 1
h = x ** y
    # Exponentielle 2
i = y ** x
    # Floor Divion Operation 1
j = x // y
    # Floor Divion Operation 2
k = y // x

    # SORTIES
print (f"x =  {x}")
print (f"y =  {y}")
print (f"Addition {x} + {y} = {a}")
print (f"Soustraction normale {x} - {y} = {b}")
print (f"Différence entre {x} et {y} = {c}")
print (f"Multiplication {x} * {y} = {d}")
print (f"Division {x} / {y} = {e}")
print (f"Modulo {x} % {y} = {f}")
print (f"Modulo {y} % {x} = {g}")
print (f"Exponentielle {x} ** {y} = {h}")
print (f"Exponentielle {y} ** {x} = {i}")
print (f"Floor Divion Operation {x} // {y} = {j}")
print (f"Floor Divion Operation {y} // {x} = {k}")