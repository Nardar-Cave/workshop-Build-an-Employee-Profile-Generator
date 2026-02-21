# Create a variable first_name which stores the string John and a variable last_name which stores the string Doe. 
# Then print first_name and last_name.

'''first_name, last_name = "John", "Doe"
print(first_name, last_name)'''

'''first_name = "John"
last_name = "Doe"
print(first_name)
print(last_name)'''

# Create a variable full_name by concatenating first_name and last_name. Then print full_name.

'''full_name = first_name + last_name
print(full_name)'''

#Update your full_name variable so it concatenates first_name, a space, and last_name.

'''full_name = first_name + ' ' + last_name
print(full_name)'''

# Next, create a variable address to store the employee's address. 
# Assign it the string 123 Main Street, and finally print address.

'''address = "123 Main Street"
print(address)'''

# Use the += operator to add the string , Apartment 4B to your address variable.

'''address += ", Apartment 4B"
print(address)'''

#Remove all the print() statements from your code.

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'

#Now create a variable named employee_age and assign it the integer 28.

employee_age = 28

# Now, you want to create a string that displays the employee's age.
# Start by creating a variable employee_info and assign it the result of concatenating:
# the full_name variable.
# a string consisting of the characters is preceded and followed by a space.

'''employee_info= full_name + " is "'''

# Now try to concatenate employee_age to the end of your employee_info string.
# Once you've done so, you'll see a TypeError in the terminal. In the next step, you'll work on fixing it.

'''employee_info= full_name + " is " + employee_age'''

# Update your employee_info assignment to convert employee_age to a string using str(employee_age).

'''employee_info = full_name + ' is ' + str(employee_age)'''

# Now complete the sentence by concatenating the string  years old to the end of employee_info. 
# Remember to include a space at the beginning of your string.
# Finally, print employee_info.

employee_info = full_name + ' is ' + str(employee_age) +  ' years old'
print(employee_info)

# Create a variable named experience_years and assign it the integer 5.
# Then, create a variable experience_info. 
# Assign it a string formed by concatenating 'Experience: ', the experience_years variable (converted to a string), and ' years'. 
# Print the result to the terminal.

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Create a variable employee_card and assign it an f-string that displays Employee: followed by a space and the value of the full_name variable.

'''employee_card = f"Employee: {full_name}"'''

# Update the employee_card assignment to include the employee's age. 
# The final string should look like this: Employee: [name] | Age: [age] with [name] replaced with the employee's name, and [age] replaced with the employee's age.

'''employee_card = f'Employee: {full_name} | Age: {employee_age}''''

# Create a variable named position with the value of the string Data Analyst and a variable named salary with the value of the integer 75000.
#Then, update your employee_card f-string to include the position and salary. 
# It should follow this exact format: Employee: [full_name] | Age: [employee_age] | Position: [position] | Salary: $[salary]. 
# Replace the placeholders with the corresponding variables.
# Finally, print employee_card to see the result.

salary = 75000
position = "Data Analyst"
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Define employee_code as 'DEV-2026-JD-001'. 
# After that, create a variable department and assign it the slice of employee_code from index 0 to 3. 
# Then print department to the terminal.

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

# Create a variable year_code and assign it the slice of employee_code from index 4 to 8. This will extract 2026.
# Then create a variable initials and assign it the slice of employee_code from index 9 to 11. This will extract JD.
# Finally, print both variables to the terminal.

year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)

# Create a variable named last_three. 
# Use negative indexing to extract the last three characters from employee_code (which represent the ID number). 
# Finally, print last_three to the terminal.

last_three = employee_code [-3:]
print(last_three)