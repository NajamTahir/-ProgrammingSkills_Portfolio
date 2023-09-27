"""
Chapter 3 Ex 5
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
•Start with your program from Exercise 3-4. 
Add a print() call at the end of your program 
stating the name of the guest who can’t make it.
•Modify your list, replacing the name of the 
guest who can’t make it with the name of the new person you are inviting.
•Print a second set of invitation messages, 
one for each person who is still in your list.
"""
guests = ["Maaz","Danyal","Ahmed","Amir"]
print("Dinner Invitation:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us at my place for evening!")
guest_cant_make_it = guests.pop(1)
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")
new_guest = "Ibrahim"
guests.append(new_guest)
print("Updated Dinner Invitation:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us at my place for evening!")