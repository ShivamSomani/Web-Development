
# coding: utf-8

# In[1]:


#Reverse a NUMBER 3 methods

#1- Easiest method to reverse
a= 4567
s=0
while a:
  b= a%10
  s=(s*10)+b
  a=a//10
print(s)

#2- Using For Loop by converting the num into Str

reverse = ''
num1 = 3456
num=str(num1)
for i in range(len(num), 0, -1):
    reverse += num[i-1]
print(int(reverse))

# a = 4567
# b = str(a)
# s= ""
# for i in b:
#     s = str(i) +s 
# print (s)

#3- Using Math Pow function
import math

a= 4567
s=0
l=len(str(a))-1
while a:
  b= a%10
  s+= b*math.pow(10,l) #7*10^3=7000
  a=a//10
  l=l-1 
print(int(s))  #so that answer does not come in decimal


# In[5]:


# SUM OF DIGITS #EASY

def sum_digit():
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

# USING RECURSION
def sumdigits(number):
  if number == 0:  # base case
    return 0
  else:                       #recursive case
    return (number%10) + sumdigits(number//10)


# In[6]:


# Remove duplicate values from the List #without using set
a=[1,2,2,4,5,6,6]

seen=[]
for element in a:
    if element not in seen:
        seen.append(element)
print(seen)  #[1,2,4,5,6]


# In[7]:


# Print the DUPLICATES IN AN ARRAY
#1) Remove duplicate values from the List using COUNT
a=[1,2,2,4,5,6,6]
seen=set()
for element in a:
    if a.count(element)>1:
        seen.add(element)
print(seen) # 2,6


#2) Using two sets method
seq = [1,2,3,2,1,5,6,5,5,5]
seen = set()
seen_twice= set()

for x in seq:
    if x not in seen:#or seen_add(x):
        seen.add(x)
    else:    
        seen_twice.add(x)
print ( seen_twice ) #[1, 2, 5]


# In[26]:


#### DIFFICULT


# In[1]:


#String Comprehension

s= "AAAABBBBCCCCaabb"
i=1
l=len(s)
r=''
count=1

while i<l:
    if s[i]==s[i-1]:
        count+=1
    else:
        r=r+s[i-1]+ str(count)
        count=1
    i+=1
    
r=r+s[i-1]+ str(count) # This is done for calculating count of last word ie b here
print(r)  #A4B4C4a2b2


# In[8]:


#SUM OF DIGIT (removed from method as shown above)

n=4567
s = 0
while n > 0:
    s += n % 10
    n //= 10
print (s)


# In[10]:


#UNique characters in a string

s= "abcdea"

char= set()

for i in s:
    if i in char:
        print ("False")
else:
    char.add(s)
    
print ("True") # Will return true since s has 2a in it


# In[11]:


#Counting repeated characters in a string
s = "asldaksldkalskdla"
dict = {}
for letter in s:
 if letter not in dict.keys():
  dict[letter] = 1
 else:
  dict[letter] += 1

print (dict) # {'a': 4, 's': 3, 'l': 4, 'd': 3, 'k': 3}


# In[12]:


#Counting repeated characters in a string (2nd way)

import collections
letters = collections.Counter('google this ')
print(letters) #Counter({'g': 2, 'o': 2, ' ': 2, 'l': 1, 'e': 1, 't': 1, 'h': 1, 'i': 1, 's': 1})


# In[17]:


# # REVERSE SENTENCE WORD BYB WORD 2nd method

s='The dog ran'
s.split()
print(' '.join(w[::-1] for w in s.split())) #ehT god nar

# # REVERSE SENTENCE WORD BYB WORD 3rd method
txt= "a is this"
words = []
word = []

for char in txt:
    if char == ' ':
        words.append(''.join(word))
        word = []
    else:
        word.append(char)
words.append(''.join(word. ))

print( ' '.join(reversed(words))) # this is a


# REVERSE SENTENCE WORD BY WORD 4th method

sentence = 'This is a string to try'
answer = ''
temp = ''
for char in sentence:
    if char != ' ':
        temp += char
    else:
        answer = temp + ' ' + answer
        temp = ''
answer = temp + ' ' + answer
print (answer)


# In[18]:


#SORT array 0, 1, 2
a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(a)

lo = 0
hi = arr_size - 1
mid = 0
while mid <= hi:
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid],a[hi] = a[hi],a[mid] 
            hi = hi - 1
print(a)


# In[20]:


#Find the first non-repeated character in a LIST
word= [1,2,3,4,3,2,1,0]
count = {}
for c in word:
    if c not in count:
        count[c] = 0
    count[c] += 1
for c in word:
    if count[c] == 1:
        print (c)
        break


# In[22]:


#FInd MISSING NUMBER from a array which is not there in other array
import collections
def finder1(arr1,arr2):
    d= collections.defaultdict(int) 
    # Default dictinoary that takes integers
    # It does not throw key error, if key isn't in dict instead of 
    # throwing errors it adds the key
    
    for num in arr2:
        d[num]+=1
        
    for num in arr1:
        if d[num]==0:
            print (num)
            break
            
        else:
            d[num]-=1
            
            
arr1=[5,5,7,7]
arr2= [5,7,7]
finder1(arr1,arr2)



# In[23]:


#ARRAY PAIR SUM 
arr=[1,3,2,2]
k=4

seen= set()
output= set()

for num in arr:
    target= k - num
    
    if target not in seen:
        seen.add(num)
        
    else:
        #output.add((min(num, target), max (num, target)))
        output.add((num, target))
        
print ('\n'.join(map(str, list(output)))) # (3,1) (2,2)  
print(len(output))  #=2


# In[24]:


# Sentence Reversal word by word
s= "This is a string"
spaces= [" "]
listt=[]
l=len(s)
i=0

while i<l:
    #if s[i] not in spaces:
        word_start=i
    
        while i< l and s[i] not in spaces:
            i+=1
        listt.append(s[word_start : i])
        i+=1

print(" ".join(reversed(listt))) #string a is This


# In[25]:


#Reverse a string in PYthon without using reversed
s = "Geeksforgeeks"

str = ""
for i in s:
    str = i + str
print (str)


# In[2]:


#  SLACK-QUESTIONS
#EX: Input "AABC32DE4P%@23Pu" output should be 32+4+23 = 59 
x="AAAAA223###10"
sum=0
num=''  # An empty string
for i in x:
    if i.isdigit():
        num = num+i
    else:
        if(num != ''):
            sum = sum+int(num)
            num=''
sum= sum+int(num)
print (sum)


# In[3]:


# Take a interger and replace 0 with 5
import  math
n = 12030
count = 0
result = n
while (n != 0):
    if (n % 10 == 0):
        result +=  5 * math.pow(10, count)

    n = n // 10
    count+=1

print(int(result))


######### Using regular expression
#import re

#a='10230'
#print(re.sub('0', '5', a))


# In[4]:


# INsertion Sort
a=[-6,-7, -4, 5, 2, 8]
for i in range(1,len(a)):
        currentvalue= a[i]
        
        while i>0 and a[i-1]>currentvalue:
            a[i]= a[i-1]
            i-=1
            
        a[i]=currentvalue
print(a)


# In[5]:


# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
#Arrange given numbers to form the biggest number | Set 1

# Python TWO Program to get the maximum possible integer from given array of integers...
'''So how do we go about it? The idea is to use any comparison based sorting algorithm. In the used sorting 
algorithm, instead of using the default comparison, write a comparison function myCompare() and use 
it to sort numbers. Given two numbers X and Y, how should myCompare() decide which number to put first – we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is larger, then X should come before Y in output, else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.
'''


# custom comparator to sort according
# to the ab, ba as mentioned in description
def comparator(a, b):
	ab = str(a)+str(b)
	ba = str(b)+str(a)
	return cmp(int(ba), int(ab))

# driver code 
a = [54, 546, 548, 60,]
sorted_array = sorted(a, cmp=comparator)
number = "".join([str(i) for i in sorted_array])
print(number)


# In[7]:


#https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
# Python3 program to print 
# given matrix in spiral form
def spiralPrint(m, n, a) :
    k = 0; l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
     
 
    while (k < m and l < n) :
         
        # Print the first row from
        # the remaining rows 
        for i in range(l, n) :
            print(a[k][i], end = " ")
             
        k += 1
 
        # Print the last column from
        # the remaining columns 
        for i in range(k, m) :
            print(a[i][n - 1], end = " ")
             
        n -= 1
 
        # Print the last row from
        # the remaining rows 
        if ( k < m) :
             
            for i in range(n - 1, (l - 1), -1) :
                print(a[m - 1][i], end = " ")
             
            m -= 1
         
        # Print the first column from
        # the remaining columns 
        if (l < n) :
            for i in range(m - 1, k - 1, -1) :
                print(a[i][l], end = " ")
             
            l += 1
 
# Driver Code
a = [ [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18] ]
       
R = 3; C = 6
spiralPrint(R, C, a)
 


# In[8]:


#https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
# Returns true if there is Pythagorean
# triplet in ar[0..n-1]
def isTriplet(ar, n):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Calculate square of array elements
                x = ar[i]*ar[i]
                y = ar[j]*ar[j]
                z = ar[k]*ar[k] 
                if (x == y + z or y == x + z or z == x + y):
                    return 1
    
    # If we reach here, no triplet found
    return 0
  
   
# Driver program to test above function 
ar = [3, 1, 4, 6, 5]
ar_size = len(ar)
 
if(isTriplet(ar, ar_size)):
    print("Yes")
else:
    print("No")
    
#Time Complexity of the above solution is O(n3).
  


# In[9]:


# Python program to reverse a  string with special characters- https://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
 
# Returns true if x is an aplhabatic character, false otherwise
def isAlphabet(x):
    return x.isalpha()
 
def reverse(string):
    LIST = toList(string)
 
    # Initialize left and right pointers
    r = len(LIST) - 1
    l = 0
 
    # Traverse LIST from both ends until 'l' and 'r'
    while l < r:
 
        # Ignore special characters
        if not isAlphabet(LIST[l]):
            l += 1
        elif not isAlphabet(LIST[r]):
            r -= 1
         
        # Both LIST[l] and LIST[r] are not special
        else: 
            LIST[l], LIST[r] = LIST[r],LIST[l]
            l += 1
            r -= 1
 
    return toString(LIST)
 
# Utility functions
def toList(string):
    List = []
    for i in string:
        List.append(i)
    return List
 
def toString(List):
    return ''.join(List)

 
# Driver code
string = "a!!!b.c.d,e'f,ghi"
print ("Input string: " + string)
string = reverse(string)
print ("Output string: " + string)
 
# This code is contributed by Bhavya Jain


# In[11]:


# https://www.geeksforgeeks.org/return-maximum-occurring-character-in-the-input-string/
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

def max_occur_string(str):
    count = {}
    max_count = 0

    for i in str:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

   
    print (max(count, key=count.get))
max_occur_string("CCCCABCDEABB")

