#!/usr/bin/env python
# coding: utf-8

# # Financial Sample Project

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# In[3]:


df = pd.read_csv('Financial_Sample.csv')


# In[4]:


df.head(50)


# In[5]:


df['Date'] = pd.to_datetime(df['Date'])
df.head()


# In[6]:


imputer = SimpleImputer(strategy='constant')
df2 = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)


# In[7]:


df2.head()


# In[8]:


df3 = df2.groupby(['Country', 'Date'])[['Units Sold', 'Sale Price', 'Profit']].sum().reset_index()


# In[9]:


df3


# In[11]:


countries = df3['Country'].unique()
len(countries)


# In[12]:


for idx in range(len(countries)):
    c = df3[df3['Country']==countries[idx]].reset_index()
    plt.scatter(np.arange(0, len(c)), c['Units Sold'], color='cyan', label='Units Sold')
    plt.scatter(np.arange(0, len(c)), c['Sale Price'], color='yellow', label='Sale Price')
    plt.scatter(np.arange(0, len(c)), c['Profit'], color='green', label='Profit')
    plt.title(countries[idx])
    plt.xlabel('Data Points')
    plt.ylabel('Values')
    plt.legend()
    plt.show()


# In[13]:


df4 = df3.groupby(['Date'])[['Units Sold', 'Sale Price', 'Profit']].sum().reset_index()


# In[14]:


c = df4
plt.scatter(np.arange(0, len(c)), c['Units Sold'], color='cyan', label='Units Sold')
plt.scatter(np.arange(0, len(c)), c['Sale Price'], color='yellow', label='Sale Price')
plt.scatter(np.arange(0, len(c)), c['Profit'], color='green', label='Profit')
plt.title('Performance Trends in the "World" Dataset')
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.legend()
plt.show()


# In[ ]:




