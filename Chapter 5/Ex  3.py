"""
Chapter 5 Ex 3
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""
# Create a glossary with programming terms and their meanings
programming_glossary = {
    'variable': 'A container for storing data in a program.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code until a condition is met.',
    'algorithm': 'A step-by-step procedure or set of instructions for solving a specific problem.',
    'conditional': 'A control structure that allows you to execute code selectively based on a condition.',
    'list': 'A collection of items that can be of different data types and is mutable.',
    'dictionary': 'A collection of key-value pairs that allows fast look-up based on keys.',
    'module': 'A file containing Python code, which can be imported and reused in other programs.',
    'exception': 'An event that occurs during the execution of a program that disrupts the normal flow of instructions.',
    'string': 'A sequence of characters, typically used for text representation.'
}
# Print each word and its meaning with a blank line in between
for word, meaning in programming_glossary.items():
    print(word + ':')
    print(meaning + '\n')
