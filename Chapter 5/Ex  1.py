"""
Chapter 5 Ex 1
Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""
person_info = {
    'first_name': str(input("Enter your first name ")),
    'last_name': str(input("Enter your last name ")),
    'age': int(input("Enter your age ")),
    'city': str(input("Where do you live "))
}
# Print each piece of information stored in the dictionary
print("First Name:", person_info['first_name'])
print("Last Name:", person_info['last_name'])
print("Age:", person_info['age'])
print("City:", person_info['city'])
