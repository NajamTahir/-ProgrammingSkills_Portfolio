"""
Chapter 7 Ex 3
Write a function called make_shirt() that accepts a size and the text 
of a message that should be printed on the shirt. The function should 
print a sentence summarizing the size of the shirt and the message printed 
on it. Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""
def make_shirt(size):
    message = input("Enter the message for the shirt: ")
    print(f"Shirt size: {size}, Message: {message}")
# Call the function using positional arguments to specify the size
size1 = input("Enter the shirt size (e.g., Small, Medium, Large): ")
make_shirt(size1)
# Call the function using keyword arguments to specify the size and message
size2 = input("Enter the shirt size (e.g., Small, Medium, Large): ")
message2 = input("Enter the message for the shirt: ")
make_shirt(size=size2, message=message2)
