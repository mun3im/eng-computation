"""
Numbers, Variables and Units - Collections: Holding Several Values
Subsection: Other Useful List Methods
"""

# Joining list elements into a single string
words = ["apple", "banana", "cherry"]
sentence = ' '.join(words)
print(sentence)  # Output: 'apple banana cherry'

# Counting occurrences of a string
words = ["apple", "banana", "apple"]
count_apples = words.count("apple")
print(count_apples)  # Output: 2

# Finding the index of a string
index_of_banana = words.index("banana")
print(index_of_banana)  # Output: 1
