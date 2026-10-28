"""
Decisions and Repetition - Loops
Subsection: Loops as Summation Operators (
"""

total_sum = 0           # The running total, starts at 0 -- this
                        # corresponds to "nothing added yet"

for i in range(1, 6):   # i takes the values 1, 2, 3, 4, 5
                        # (range(1, 6) stops *before* 6, matching
                        # the upper limit "5" in the sum)
    total_sum += i      # Accumulate: total_sum = total_sum + i

print(total_sum)        # Output: 15
