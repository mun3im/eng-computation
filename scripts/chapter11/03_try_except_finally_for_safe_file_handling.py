"""
Handling Imperfect Engineering Data - Writing Robust Code
Subsection: Using finally for Cleanup
Listing: try/except/finally for safe file handling
"""

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
    try:
        f.close()
    except:
        pass
