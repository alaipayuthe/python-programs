"""
Write a Python function total_seconds that takes three parameters hours, minutes and seconds and returns the total number of seconds for hours, minutes and seconds. Hours to seconds template --- Hours to seconds solution
"""

def total_seconds(hours, minutes, seconds):
    return ((hours * 60 * 60) + (minutes * 60) + seconds)

print("5 hrs 35 minutes 53 seconds = " + str(total_seconds(5, 35, 53)) + " seconds")
