
a = 2
b = 5
pro = a * b

print("The product of the numbers is", pro)

if pro > 5:
    print("This is high")
elif pro < 5:
    print("It's fair")
else:
    print("It's exactly 5")

from datetime import datetime
DoB = 1989
current_year = datetime.now().year
Age = current_year - DoB

print("The age is", Age)
