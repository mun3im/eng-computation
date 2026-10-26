"""
Numbers, Variables and Units - Collections: Holding Several Values
Subsection: Adding Elements to a List
Source: chapters/chapter3.tex, line 263
"""

# Adding a single string using append
words = ["apple", "banana"]
words.append("cherry")
print(words)  # Output: ['apple', 'banana', 'cherry']

# Extending the list with another list of strings
words.extend(["date", "fig"])
print(words)  # Output: ['apple', 'banana', 'cherry', 'date', 'fig']

# Inserting a string at a specific position
words.insert(1, "grape")
print(words)  # Output: ['apple', 'grape', 'banana', 'cherry', 'date', 'fig']
