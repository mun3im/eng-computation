"""
Numbers, Variables and Units - Collections: Holding Several Values
Subsection: Removing Elements from a List
"""

# Removing a string by value
words = ["apple", "banana", "cherry"]
words.remove("banana")
print(words)  # Output: ['apple', 'cherry']

# Removing by index using pop
removed_word = words.pop(1)
print(removed_word)  # Output: 'cherry'
print(words)  # Output: ['apple']

# Using del to remove by index
del words[0]
print(words)  # Output: []
