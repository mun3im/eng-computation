"""
Handling Imperfect Engineering Data - Using finally for Cleanup
"""

f = None
try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error reading file!")
finally:
    print("Closing file...")
    if f is not None:
        f.close()
