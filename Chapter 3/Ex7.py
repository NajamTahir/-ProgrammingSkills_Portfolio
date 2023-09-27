"""
Chapter 3 Ex 7
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""
places_to_visit = ["Azerbaijan","Saudi Arabia","Norway","America","Iran"]
print("Original Order:")
print(places_to_visit)
print("\nAlphabetical Order (sorted()):")
print(sorted(places_to_visit))
print("\nOriginal Order (after sorted()):")
print(places_to_visit)
print("\nReverse Alphabetical Order (sorted()):")
print(sorted(places_to_visit, reverse=True))
print("\nOriginal Order (after sorted() with reverse=True):")
print(places_to_visit)
places_to_visit.reverse()
print("\nReversed Order:")
print(places_to_visit)
places_to_visit.reverse()
print("\nOriginal Order (after reverse() twice):")
print(places_to_visit)
places_to_visit.sort()
print("\nAlphabetical Order (sort()):")
print(places_to_visit)
places_to_visit.sort(reverse=True)
print("\nReverse Alphabetical Order (sort(reverse=True)):")
print(places_to_visit)