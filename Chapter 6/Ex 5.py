"""
Chapter 6 Ex 5
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 
'pastrami' appears in the list at least three times. Add code near the 
beginning of your program to print a message saying the deli has run out 
of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end 
up in finished_sandwiches.
"""
# Create a list of sandwich orders with 'pastrami' appearing multiple times
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'club', 'pastrami', 'vegetarian', 'pastrami']
# Create an empty list for finished sandwiches
finished_sandwiches = []
# Print a message indicating that the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")
# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order from the list  
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)