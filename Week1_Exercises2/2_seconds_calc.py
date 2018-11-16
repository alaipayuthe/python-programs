"""
Given a template that pre-defines three variables hours, minutes and seconds, write an assignment statement that updates the variable total_seconds to have a value corresponding to the total number of seconds for hours, minutes and seconds.
"""

# Total seconds calculator
hours   = 10
minutes = 55
seconds = 4

total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

print("Total seconds = " + str(total_seconds) + " seconds")

