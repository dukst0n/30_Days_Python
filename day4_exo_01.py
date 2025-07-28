# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
concatenated_string_1 = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(f"1. Concatenated string 1: '{concatenated_string_1}'")
print()

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str_coding = 'Coding'
str_for = 'For'
str_all = 'All'
concatenated_string_2 = str_coding + ' ' + str_for + ' ' + str_all
print(f"2. Concatenated string 2: '{concatenated_string_2}'")
print()

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(f"3. Company variable declared: '{company}'")
print()

# 4. Print the variable company using print().
print(f"4. Printing company variable: '{company}'")
print()

# 5. Print the length of the company string using len() method and print().
company_length = len(company)
print(f"5. Length of company string: {company_length}")
print()

# 6. Change all the characters to uppercase letters using upper() method.
company_upper = company.upper()
print(f"6. Company string in uppercase: '{company_upper}'")
print()

# 7. Change all the characters to lowercase letters using lower() method.
company_lower = company.lower()
print(f"7. Company string in lowercase: '{company_lower}'")
print()

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(f"8. Formatting 'Coding For All':")
print(f"   - capitalize(): '{company.capitalize()}'")
print(f"   - title(): '{company.title()}'")
print(f"   - swapcase(): '{company.swapcase()}'")
print()

# 9. Cut(slice) out the first word of Coding For All string.
sliced_string = company[company.find(' ') + 1:]
print(f"9. String after cutting out the first word: '{sliced_string}'")
print()

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
contains_coding_in_operator = "Coding" in company
contains_coding_find = company.find("Coding") != -1
contains_coding_index = True
try:
    company.index("Coding") #
except ValueError:
    contains_coding_index = False

print(f"10. Does '{company}' contain 'Coding'?")
print(f"    - Using 'in' operator: {contains_coding_in_operator}")
print(f"    - Using find() method: {contains_coding_find}")
print(f"    - Using index() method (checking for error): {contains_coding_index}")
print()


# 11. Replace the word coding in the string 'Coding For All' to Python.
replaced_string_1 = company.replace("Coding", "Python")
print(f"11. Replacing 'Coding' with 'Python': '{replaced_string_1}'")
print()

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
original_string_for_replace = "Python for Everyone"
replaced_string_2 = original_string_for_replace.replace("Everyone", "All")
print(f"12. Changing 'Python for Everyone' to 'Python for All': '{replaced_string_2}'")
print()

# 13. Split the string 'Coding For All' using space as the separator (split()).
split_company = company.split(' ')
print(f"13. Splitting '{company}' by space: {split_company}")
print()

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies_string.split(',')

split_companies_cleaned = [c.strip() for c in split_companies]
print(f"14. Splitting '{companies_string}' by comma: {split_companies_cleaned}")
print()

# 15. What is the character at index 0 in the string Coding For All.
char_at_0 = company[0]
print(f"15. Character at index 0 in '{company}': '{char_at_0}'")
print()

# 16. What is the last index of the string Coding For All.
last_index = len(company) - 1
print(f"16. Last index of '{company}': {last_index}")
print()

# 17. What character is at index 10 in "Coding For All" string.
char_at_10 = company[10]
print(f"17. Character at index 10 in '{company}': '{char_at_10}'")
print()

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
name_py = 'Python For Everyone'
acronym_py = ''.join([word[0].upper() for word in name_py.split()])
print(f"18. Acronym for '{name_py}': '{acronym_py}'")
print()

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_cfa = ''.join([word[0].upper() for word in company.split()])
print(f"19. Acronym for '{company}': '{acronym_cfa}'")
print()

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
index_c = company.index('C')
print(f"20. First occurrence of 'C' in '{company}': {index_c}")
print()

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
index_f = company.index('F')
print(f"21. First occurrence of 'F' in '{company}': {index_f}")
print()

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
long_string = "Coding For All People"
rfind_l = long_string.rfind('l')
print(f"22. Last occurrence of 'l' in '{long_string}': {rfind_l}")
print()
