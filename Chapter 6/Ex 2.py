"""
Chapter 6 Ex 1
A movie theater charges different ticket prices depending
on a person’s age. If a person is under the age of 3, 
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they 
are over age 12, the ticket is $15. Write a loop in which 
you ask users their age, and then tell them the cost of their movie ticket
"""
while True:
    age_str = input("Please enter your age (or 'quit' to exit): ")
    if age_str.lower() == 'quit':
        break
    try:
        age = int(age_str)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"Your movie ticket will cost ${ticket_price}.")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")
print("Thank you for using the ticket pricing system!")
