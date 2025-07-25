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

# Categorize based on age
if age < 18:
    print("You are a minor.")
elif age <= 40:
    print("You are an adult.")
else:
    print("You are middle-aged.")
