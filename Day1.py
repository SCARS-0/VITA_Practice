#Q.1) Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first = input("Enter First Name: ")
last = input("Enter Last Name: ")
print(f"{last} {first}")

#Q.2) Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module.   

import calendar
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
print(calendar.month(year, month))

#Q.3)  Write a Python program to calculate number of days between two dates.[ use datetime module ] 
#Sample dates : (2014, 7, 2), (2014, 7, 11)   
#Expected output : 9 days   

from datetime import date
y1, m1, d1 = map(int, input("Enter first date (YYYY,MM,DD): ").split(","))
date1 = date(y1, m1, d1)
y2, m2, d2 = map(int, input("Enter first date (YYYY,MM,DD): ").split(","))
date2 = date(y2, m2, d2)

diff = abs((date2 - date1).days)

print("Number of days:", diff, "days")

#Q.4)  Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter Character: ")
vowel=['A','E','I','O','U']
if(letter.upper() in vowel ):
        print("Letter is vowel")
else:
        print("Not a vowel")