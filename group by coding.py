#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import the pandas library
import pandas as pd 

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2, 4,1,2], 
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points': [876,789,863,673,741,812,756,788,694,701,804,690]} 
df = pd.DataFrame(ipl_data) 

print (df)


# In[9]:


#import the pandas library
import pandas as pd 

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2, 4,1,2], 
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points': [876,789,863,673,741,812,756,788,694,701,804,690]} 
df = pd.DataFrame(ipl_data) 

print (df.groupby ('Team'). groups)


# In[11]:


#import the pandas library
import pandas as pd 

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2, 4,1,2], 
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points': [876,789,863,673,741,812,756,788,694,701,804,690]} 
df = pd.DataFrame(ipl_data) 

print (df.groupby(['Team','Year']).groups)


# In[12]:


#import the pandas library
import pandas as pd 

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2, 4,1,2], 
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points': [876,789,863,673,741,812,756,788,694,701,804,690]} 
df = pd.DataFrame(ipl_data) 

grouped = df.groupby('Year')

for name,group in  grouped:
    print (name)
    print (group)
    
    


# In[15]:


#import the pandas library
import pandas as pd 

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2, 4,1,2], 
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points': [876,789,863,673,741,812,756,788,694,701,804,690]} 
df = pd.DataFrame(ipl_data) 

grouped = df.groupby('Year')
print (grouped.get_group(2014))
                     


# In[ ]:




