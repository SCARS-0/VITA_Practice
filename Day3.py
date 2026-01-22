#Q.1) Write a code to Read a file and append lines to a list. 
'''lines_list = []

with open("C:\\Users\\Sherz\\OneDrive\\Desktop\\sample.txt", "r") as file:
    for line in file:
        lines_list.append(line.strip())

print(lines_list)'''


#Q.2) Write a code to catch an Exception in python?

'''try:
    x=1/1
    y=1/0
    print(x)
    print(y)
except ZeroDivisionError:
    print("Number cannot be divided by zero")'''


'''Q.3) Write a Python function that accepts a list containing strings and integers. 
Merge all string elements using # and add all integer elements. 
e.g.  
input list is  
['100', 'welcome', 'hi', '200', '300', 'bye', 'welldone', '500'] 
Output should be: 
welcome#hi#bye#welldone# 
1100 '''

'''list1 = []
n = int(input("List size: "))

for i in range(n):
    list1.append(input("Enter element: "))

string_list = []
sum_nums = 0

for item in list1:
    if item.isdigit():
        sum_nums += int(item)
    else:
        string_list.append(item)

merged_string = "#".join(string_list) + "#"

print("Merged String:", merged_string)
print("Sum:", sum_nums)'''


'''Q.4) Write a script to sort a dictionary based on its values and find the sum of middle two 
values 
input_dict = {"x": 5, "y": 15, "z": 25} 
Output:  
Sorted Dictionary: {'x': 5, 'y': 15, 'z': 25} 
Sum of middle two values: 15 + 5 = 20 
or 
input_dict = {"x": 5, "y": 15, "z": 25,"p":12} 
Output:  
Sorted Dictionary: {'x': 5, 'p': 12,'y': 15, 'z': 25} 
Sum of middle two values: 12 + 15 = 27'''

input_dict = {"x": 5, "y": 15, "z": 25, "p": 12}

# Sort dictionary by values
sorted_items = sorted(input_dict.items(), key=lambda x: x[1])
sorted_dict = dict(sorted_items)

print("Sorted Dictionary:", sorted_dict)

# Extract sorted values
values = list(sorted_dict.values())
n = len(values)

# Find sum of middle two values
if n >= 2:
    mid_sum = values[n//2 - 1] + values[n//2]
    print("Sum of middle two values:", mid_sum)
