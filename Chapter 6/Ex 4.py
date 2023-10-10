"""
Chapter 6 Ex 4
Make a list called sandwich_orders and fill it with the names of various 
sandwiches. Then make an empty list called finished_sandwiches. Loop 
through the list of sandwich orders and print a message for each order,
such as I made your tuna sandwich. As each sandwich is made, move it to 
the list of finished sandwiches. After all the sandwiches have been made, 
print a message listing each sandwich that was made.
"""
# Create a list of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'club', 'vegetarian']
# Create an empty list for finished sandwiches
finished_sandwiches = []
# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order from the list  
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)