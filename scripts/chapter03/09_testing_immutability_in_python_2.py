"""
Numbers, Variables and Units - Testing Immutability in Python
"""

# A list is mutable: appending edits the object in place
readings = [26.5, 26.6]
before = id(readings)
readings += [26.7]              # the same operator as the tuple below
print(id(readings) == before)   # Output: True  -- same object

# A tuple is immutable: "adding" must create a new object
point = (2.5, 4.0)
before = id(point)
point += (1.0,)
print(id(point) == before)      # Output: False -- a different object
