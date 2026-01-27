'''1.	Write a Python function to check whether a string is a pangram or not. 
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''

####

'''def is_pangram(s):
    s = s.lower()
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in s:
            return False
    return True

print(is_pangram("zaman"))'''



'''3.	Solve the following pattern using one loop only:

1
121
12321
1234321'''

'''b="1234"
a=[x for x in b]
print(a)
for i in a:
    print(b[i],b[i+1],b[i])'''