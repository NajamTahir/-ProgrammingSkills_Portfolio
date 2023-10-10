"""
Chapter 7 Ex 4
Modify the make_shirt() function so that shirts are large by default with
a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a 
different message.
"""
def make_shirt():
    size = input("Enter the shirt size (e.g., Small, Medium, Large): ")
    message = input("Enter the message for the shirt: ")
    if size.lower() not in ["small", "medium", "large"]:
        print("Invalid shirt size. Defaulting to Large.")
    if not message:
        message = "I love Python"
    print(f"Shirt size: {size}, Message: {message}")
# Create a large shirt with the default message
make_shirt()
# Create a medium shirt with the default message
make_shirt()
# Create a custom-sized shirt with a different message
make_shirt()