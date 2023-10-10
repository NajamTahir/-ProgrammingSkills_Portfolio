"""
Chapter 4 Ex 3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
alien_color = str(input("Enter the color of the alien "))
if alien_color == 'green':
    print("Player earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Player earned 10 points for shooting the yellow alien.")
elif alien_color == 'red':
    print("Player earned 15 points for shooting the red alien.")
else:
    print("Player earned 0 points. Invalid alien color.")