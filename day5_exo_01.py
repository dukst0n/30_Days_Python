# Exercises: Level 1

# 1. Declare an empty list
empty_list = []
print(f"1. Empty list: {empty_list}")

# 2. Declare a list with more than 5 items
my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"2. List with more than 5 items: {my_list}")

# 3. Find the length of your list
list_length = len(my_list)
print(f"3. Length of my_list: {list_length}")

# 4. Get the first item, the middle item and the last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2] # Integer division for middle index
last_item = my_list[-1]
print(f"4. First item: {first_item}, Middle item: {middle_item}, Last item: {last_item}")

# 5. Declare a list called mixed_data_types, put your (name, age, height, marital status, address)
mixed_data_types = ["Alice", 28, 1.65, "Single", "123 Python Lane"]
print(f"5. Mixed data types list: {mixed_data_types}")

# 6. Declare a list variable named it_companies and assign initial values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(f"6. IT Companies list: {it_companies}")

# 7. Print the list using print()
print(f"7. Printing IT Companies list: {it_companies}")

# 8. Print the number of companies in the list
num_companies = len(it_companies)
print(f"8. Number of companies: {num_companies}")

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f"9. First company: {first_company}, Middle company: {middle_company}, Last company: {last_company}")

# 10. Print the list after modifying one of the companies
# Let's modify 'Facebook' to 'Meta'
it_companies[0] = "Meta"
print(f"10. IT Companies list after modifying one: {it_companies}")

# 11. Add an IT company to it_companies
it_companies.append("Netflix")
print(f"11. IT Companies list after adding 'Netflix': {it_companies}")

# 12. Insert an IT company in the middle of the companies list
middle_index_it = len(it_companies) // 2
it_companies.insert(middle_index_it, "Salesforce")
print(f"12. IT Companies list after inserting 'Salesforce' in the middle: {it_companies}")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
# Let's change 'Google' to 'GOOGLE'
if "Google" in it_companies:
    google_index = it_companies.index("Google")
    it_companies[google_index] = it_companies[google_index].upper()
print(f"13. IT Companies list after changing 'Google' to uppercase: {it_companies}")

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(f"14. Joined IT Companies: '{joined_companies}'")

# 15. Check if a certain company exists in the it_companies list.
company_to_check = "Apple"
exists = company_to_check in it_companies
print(f"15. Does '{company_to_check}' exist in the list? {exists}")

# 16. Sort the list using sort() method
it_companies.sort()
print(f"16. IT Companies list after sorting: {it_companies}")

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(f"17. IT Companies list after reversing (descending order): {it_companies}")

# 18. Slice out the first 3 companies from the list
# This means showing the list *without* the first 3.
sliced_first_3 = it_companies[3:]
print(f"18. IT Companies list after slicing out the first 3: {sliced_first_3}")

# To demonstrate the original list is unchanged by slicing, we'll re-initialize for next steps
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon", "Netflix", "Salesforce"] # Re-initialize for accurate slicing

# 19. Slice out the last 3 companies from the list
sliced_last_3 = it_companies[:-3]
print(f"19. IT Companies list after slicing out the last 3: {sliced_last_3}")

# 20. Slice out the middle IT company or companies from the list
# Re-initialize for accurate slicing
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon", "Netflix", "Salesforce"]
mid_idx = len(it_companies) // 2
if len(it_companies) % 2 == 1: # Odd number of elements, slice out one middle
    sliced_middle = it_companies[:mid_idx] + it_companies[mid_idx + 1:]
else: # Even number of elements, slice out two middle
    sliced_middle = it_companies[:mid_idx - 1] + it_companies[mid_idx + 1:] # Adjust based on how many to remove
print(f"20. IT Companies list after slicing out the middle company(ies): {sliced_middle}")

# Re-initialize it_companies for removal operations to ensure consistent starting state
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 21. Remove the first IT company from the list
removed_first = it_companies.pop(0) # Removes and returns the item at index 0
print(f"21. Removed first company: '{removed_first}'. List now: {it_companies}")

# 22. Remove the middle IT company or companies from the list
# Re-initialize for accurate removal
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
mid_idx_remove = len(it_companies) // 2
if len(it_companies) % 2 == 1:
    removed_middle = it_companies.pop(mid_idx_remove)
    print(f"22. Removed middle company: '{removed_middle}'. List now: {it_companies}")
else:
    # For even, remove the two middle ones. Remove the higher index first to avoid shifting issues.
    removed_mid2 = it_companies.pop(mid_idx_remove)
    removed_mid1 = it_companies.pop(mid_idx_remove - 1)
    print(f"22. Removed middle companies: '{removed_mid1}', '{removed_mid2}'. List now: {it_companies}")

# Re-initialize for accurate removal
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 23. Remove the last IT company from the list
removed_last = it_companies.pop() # Removes and returns the last item
print(f"23. Removed last company: '{removed_last}'. List now: {it_companies}")

# 24. Remove all IT companies from the list
it_companies.clear()
print(f"24. IT Companies list after removing all companies: {it_companies}")

# 25. Destroy the IT companies list
# Re-initialize for destruction
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies
try:
    print(f"25. Attempting to print destroyed list: {it_companies}")
except NameError as e:
    print(f"    Error: {e} - The 'it_companies' list has been destroyed.")

print("\n--- List Joining and Manipulation ---")

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(f"26. Joined front_end and back_end lists: {joined_list}")

# 27. After joining the lists in question 26. Copy the joined list and assign it to a
#     variable full_stack, then insert Python and SQL after Redux.
full_stack = joined_list[:] # Create a shallow copy
# Find the index of 'Redux'
redux_index = full_stack.index('Redux')
# Insert 'Python' and 'SQL' after 'Redux'
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL') # +2 because Python shifted the index
print(f"27. Full stack list after adding Python and SQL: {full_stack}")
