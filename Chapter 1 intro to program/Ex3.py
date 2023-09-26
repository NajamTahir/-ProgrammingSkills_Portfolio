"""
Chapter 1 Ex 3
Write a Python program to display the current date and time.
"""
import datetime
c_datetime = datetime.datetime.now()
f_datetime = c_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", f_datetime)