
a = 2
b = 2
pro = a * b

print("The product of the numbers is", pro)

if pro > 5:
    print("This is high")
elif pro < 5:
    print("It's fair")
else:
    print("It's exactly 5")

from datetime import datetime
DOB = 1989
current_year = datetime.now().year
Age = current_year - DOB

print("The age is", Age)
