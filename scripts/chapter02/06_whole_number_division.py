"""
Your First Python Programs - Whole-Number Division

Output as printed in the book:
    1 h 2 min 5 s
"""

duration = 3725              # seconds

hours = duration // 3600     # whole hours
remaining = duration % 3600  # seconds left over
minutes = remaining // 60
seconds = remaining % 60

print(hours, "h", minutes, "min", seconds, "s")
