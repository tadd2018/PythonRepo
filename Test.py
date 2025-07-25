# This script calculates the age of a person based on their date of birth (DOB).
from datetime import datetime

# Ask user to enter DOB in YYYY-MM-DD format
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert the input string to a datetime object
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Get today's date
today = datetime.today()

# Calculate age
age = today.year - dob.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your age is:", age)
