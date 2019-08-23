
from _datetime import datetime
name = input("Enter your name:")
age = int(input("Enter your age:"))

now = datetime.now()
current_year = now.year
year = str((current_year - age) + 100)

print(name + "you will be 100 in the year"+ year)