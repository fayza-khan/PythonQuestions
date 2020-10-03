import math
import string
"""
Functions and Methods Homework
Complete the following questions:

Question 1:

Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as$$\frac{4}{3} πr^3$$

In [1]:
def vol(rad):
    pass
In [2]:
# Check
vol(2)
Out[2]:
33.49333333333333
"""


l = lambda r: (4/3)*math.pi*(r**3)
print(l(2))
print(l(30))



"""
Question 2:

Write a function that checks whether a number is in a given range (inclusive of high and low)

In [3]:
def ran_check(num,low,high):
    pass
In [4]:
# Check
ran_check(5,2,7)
5 is in the range between 2 and 7
If you only wanted to return a boolean:

In [5]:
def ran_bool(num,low,high):
    pass
In [6]:
ran_bool(3,1,10)
Out[6]:
True
"""


def ran_check(num, low, high):
    return num in range(low, high+1)


print(ran_check(13, 1, 10))



"""
Question 3:

Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!

In [7]:
def up_low(s):
    pass
In [8]:
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
No. of Upper case characters :  4
No. of Lower case Characters :  33
"""


def up_low(a):
    x = 0
    y = 0
    for i in a:
        if i.isupper():
            x += 1
        elif i.islower():
            y += 1
        else:
            pass
    print("No. of Upper case characters :", x, "\nNo. of Lower case Characters :", y)


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)




"""
Question 4:

Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
In [9]:
def unique_list(lst):
    pass
In [10]:
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
Out[10]:
[1, 2, 3, 4, 5]
"""


def unique_list(list_name):
    new_list = []
    for a in list_name:
        if a not in new_list:
            new_list.append(a)
    return new_list


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


"""
Question 5:

Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
In [11]:
def multiply(numbers):  
    pass
In [12]:
multiply([1,2,3,-4])
Out[12]:
-24
"""


def multiply(numbers):
    prod = 1
    for i in numbers:
        prod *= i
    return prod


print(multiply([1, 2, 3, -4]))


"""
Question 6:

Write a Python function that checks whether a passed in string is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

In [13]:
def palindrome(s):
    pass
In [14]:
palindrome('helleh')
Out[14]:
True
"""


def palindrome(s):
    return s[::] == s[::-1]


print(palindrome('helleh'))
print(palindrome('madam'))
print(palindrome('fayza'))
print(palindrome('palindrome'))


def is_pangram(str1, alphabet=string.ascii_lowercase):
    alpha_set = set(alphabet)
    return alpha_set <= set(str1.lower())


print(is_pangram('abcdefghijklmnopqrstuvwxyz'))
print(is_pangram('fayza is cool'))
print(is_pangram("The quick brown fox jumps over the lazy dog"))











