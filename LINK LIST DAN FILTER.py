#!/usr/bin/env python
# coding: utf-8

# In[6]:


def multiply(x) :
    return (x*x)
def add(x) :
    return (x+x)

funcs = [multiply, add]
for i in range(5): 
    value = list(map(lambda x: x(i), funcs))
    print (value)


# In[9]:


#List alfabet 
alfabet = 'a',  'b', 'c', 'e', 'i' 'k', 'o', 'z', 
# fungsi penyaring hurung vokal 
def filter_vocal (alfabet):
    vocal = ['a', 'i' 'u', 'e', 'o', ]
    if alfabet in vocal : 
        return True 
    else:
        return False 

vocal_terfilter = filter(filter_vocal ,alfabet)
print ('Huruf vocal yang tersaring adalah:' )
for vocal in vocal_terfilter:
    print(vocal)
    


# In[ ]:




