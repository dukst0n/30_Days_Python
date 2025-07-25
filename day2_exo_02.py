#1. Check the data type of all your variables using type() built-in function
my_integer = 35
my_float = 3.05
my_string = "washiu"
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}

print(type(my_integer))
print(type(my_float))
print(type(my_string))
print(type(my_list))
print(type(my_dict))

#2. Using the len() built-in function, find the length of your first name
first_name = "washiu"
length_of_first_name = len(first_name)
print(length_of_first_name)

#3. Compare the length of your first name and your last name
first_name = "Uk'iva"
last_name = "DAPAM"

len_first_name = len(first_name)
len_last_name = len(last_name)

print(f"La longueur du first name ({first_name}): {len_first_name}")
print(f"La longueur du last name ({last_name}): {len_last_name}")

if len_first_name > len_last_name:
    print("Le first_name est le plus long.")
elif len_first_name < len_last_name:
    print("Le last_name est le plus long.")
else:
    print("Les deux, first_name et last_name ont la même longueur.")

#4. Declare 5 as num_one and 4 as 
num_one = 5
num_two = 4

print(f"num_one: {num_one}")
print(f"num_two: {num_two}")
print()

#5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

print(f"Total: {total}")
print()

#6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

print(f"Difference: {diff}")
print()

#7. Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

print(f"Product: {product}")
print()

#8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

print(f"Division: {division}")
print()

#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

print(f"Remainder: {remainder}")
print()

#10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

print(f"Exponent: {exp}")
print()

#11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

print(f"Floor Division: {floor_division}")
print()

#12. The radius of a circle is 30 meters.
import math

    # i. Calculate the area of a circle and assign the value to a variable name of 
radius = 30
    # aire = r x r x pi ou r² x pi
area_of_circle = math.pi * radius**2 
print(f"i. Area of the circle with radius {radius}m: {area_of_circle:.2f} sq meters")
print()

    # ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    # périmetre = (r + r) x pi ou d x pi ou 2 x r x pi
circum_of_circle = 2 * math.pi * radius
print(f"ii. Circumference of the circle with radius {radius}m: {circum_of_circle:.2f} meters")
print()

    # iii. Take radius as user input and calculate the area.
rad = input("Enter your radius")
rayon = float(rad)
aire = rayon*rayon*math.pi
print(f"\nL'aire de votre rayon {rayon} est {aire} m²")
print()

#13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
your_age = int(age)

print(f"\nFirst Name: {first_name}")
print(f"\nLast Name: {last_name}")
print(f"\nCountry: {country}")
print(f"\nAge: {your_age}")
print()
