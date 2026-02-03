'''Q.1) Write a Python program to count the even, odd numbers in a given array of integers using 
Lambda. '''

'''evenl=0
oddl=0
list1=[x for x in range (1,26)]
even = lambda s : s%2==0
for i in list1:
    if even(i):
        evenl=evenl+1
        
    else:
        oddl=oddl+1
print(evenl,oddl)'''

'''Q.2) Write a Python program to find palindromes in a given list of strings using Lambda. '''

'''words = ["nitin", "madam", "apple", "level", "python"]

palin = lambda s: s == s[::-1]

palindromes = list(filter(palin, words))

print("Palindromes:", palindromes)

print([w for w in words if palin(w)])'''

'''Q.3) Solve the following pattern using one loop only:  accept no. of rows from user. 
1 
121 
12321 
1234321'''

'''Q.4) Write a Python program to convert a byte string to a list of integers.    
Sample Input: 
“hello” 
Sample Output: 
[104, 101, 108, 108, 111]'''

'''str1 = "hello"

byte_str = bytes(str1, encoding="utf-8")
list1 = list(byte_str)

print(list1)'''
