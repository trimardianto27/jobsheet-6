#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Phyton program showing a use 
# lambda function 

# perfoming a addition of three number 
x1 = (lambda x, y, z: (x+y) * z)(1,2,3)
print (x1)

# function using a lambda function 
x2 = (lambda x, y, z: (x+y) if (z == 0) else (x * y)) (1,2,3)
print (x2)


# In[4]:


# phyton code to ilustrate cube of a number 
# showing difference between def() and lambda()
def cube(y): 
    return y*y*y; 

g= lambda x: x*x*x 
print(g(7))

print (cube(5))


# In[6]:


# phyton program performing 
# operation using def()
def fun(x, y, z):
    return x*y*z
a = 1
b = 2
c = 3

# logical jump
d = fun (a, b, c)
print(d)


# phyton program performing 
# operatin using lambda

d= (lambda x,y,z: x*y+z)(1,2,3)
print(d)


# In[8]:


def func(x):
    if x == 1:
        return "one"
    elif x == 2: 
        return "two"
    elif x == 3:
        return "three"
    else:
        return "ten"
num = func(3)
print(num)
 

# phyton program showing use 
# of lambda function 
num = (lambda x: "one" if x == 1 else("two" if x == 2
                       else ("three" if x == 3 else "ten")))(3)
print(num) 


# In[28]:


# phyton code to illustrate 
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 !=0 , li))
print(final_list)   


# In[17]:


# phyton code to ilustrate
# map() with lambda()
# to get double of a  list. 
li = [5, 7, 22, 97, 54 , 62 , 77 , 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)


# In[23]:


# phyton code to illustrate 
# reduce() with lambda()
# to get sum of a list 
from functools import reduce 
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)


# In[ ]:
                  




