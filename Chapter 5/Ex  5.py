"""
Chapter 5 Ex 5
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""
# Create a list of dictionaries representing different pets
pets = [
    {
        'kind': 'Dog',
        'owner': 'Alice'
    },
    {
        'kind': 'Cat',
        'owner': 'Bob'
    },
    {
        'kind': 'Parrot',
        'owner': 'Charlie'
    }
]
# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()  # Blank line to separate pet information