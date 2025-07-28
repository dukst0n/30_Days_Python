# 1. Operations on the ages list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f"Original ages list: {ages}")

ages.sort()
print(f"Sorted ages list: {ages}")

min_age = ages[0] 
max_age = ages[-1] 

print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

ages.append(min_age)
ages.append(max_age)
ages.sort() 
print(f"Ages list after adding min/max and re-sorting: {ages}")

n = len(ages)
if n % 2 == 1:
    median_age = ages[n // 2]
else:
    mid1 = ages[n // 2 - 1]
    mid2 = ages[n // 2]
    median_age = (mid1 + mid2) / 2
print(f"Median age: {median_age}")

sum_ages = sum(ages)
average_age = sum_ages / n
print(f"Average age: {average_age:.2f}")

age_range = max_age - min_age
print(f"Range of ages: {age_range}")

diff_min_avg = abs(min_age - average_age)
diff_max_avg = abs(max_age - average_age)
print(f"|Min - Average|: {diff_min_avg:.2f}")
print(f"|Max - Average|: {diff_max_avg:.2f}")
if diff_min_avg < diff_max_avg:
    print("Absolute difference (min - average) is less than (max - average).")
elif diff_min_avg > diff_max_avg:
    print("Absolute difference (min - average) is greater than (max - average).")
else:
    print("Absolute differences (min - average) and (max - average) are equal.")

print("\n--- Country List Operations ---")

# 1. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(f"Original countries list: {countries}")

num_countries = len(countries)
middle_index = num_countries // 2

if num_countries % 2 == 1:
    middle_countries = [countries[middle_index]]
else:
    middle_countries = [countries[middle_index - 1], countries[middle_index]]

print(f"Middle country(ies): {middle_countries}")

# 2. Divide the countries list into two equal lists if it is even if not one more country
first_half_end_index = (num_countries + 1) // 2 
first_half_countries = countries[:first_half_end_index]
second_half_countries = countries[first_half_end_index:]

print(f"First half of countries: {first_half_countries}")
print(f"Second half of countries: {second_half_countries}")

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
country1, country2, country3, *scandic_countries = countries

print(f"Unpacked country 1: {country1}")
print(f"Unpacked country 2: {country2}")
print(f"Unpacked country 3: {country3}")
print(f"Scandic countries (rest): {scandic_countries}")
print()