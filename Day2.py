'''
Q.1) Write a Python program to print all even numbers from a given list of numbers in the 
same order. Stop printing if any number that comes after 237 in the sequence is 
encountered. 
Sample  
numbers list :  
numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 237, 412, 566, 731, 210, 912, 216, 244, 896, 101, 867, 355, 430 ] 
expected output: 
386 462 418 344 236 566 978 328 162 758
'''

#Solution
'''
list1=[]
n = int(input("Length of list: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))

for x in list1:
    if x%2==0 :
        print(x,end=" ")
    elif x==237:
        break
    else:
        continue
'''

'''
Q.2) Write a python program to get the path and name of the file that is currently executing
'''

#Solution
'''
import os
print("File path:", os.path.abspath(__file__))
print("File name:", os.path.basename(__file__))
'''

'''
Q.3) pattern 
1 
212 
32123 
4321234 
543212345 
'''

#Solution
'''patternrange=int(input("Enter range of value"))

for i in range(1,patternrange+1):
    print()
    for j in range(1,i+1):
        if j == 1:
            print(j,end="")
        else:
            print(i,end="")'''
'''
Q.4) Write a code to accept a number & print its digits in words . 
Ex: 321
'''

#Solution
'''numdic={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
num = input("Enter number: ")

for i in num:
    print(numdic.get(int(i)))'''