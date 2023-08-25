#!/usr/bin/env python
# coding: utf-8

# In[213]:


#!pip install pyvis #for colab environment


# In[214]:


#data sci boilerplate
from pyvis.network import Network
import numpy as np
import pandas as pd
from os import path
from PIL import Image

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import figure
import networkx as nx


# In[215]:


df = pd.read_excel('data/4e1.xlsx') #excel file needs to be in a subdirectory named data
df.head()


# In[216]:


df.isnull().sum()


# In[217]:


df.columns


# In[218]:


len(df)


# In[219]:


df.loc[0,'1st Choice']


# In[220]:


pd.set_option('display.max_rows', 500)


# In[221]:


df = df.sort_values('Class Index No. ')


# In[222]:


df


# In[223]:


net=Network(directed=True,notebook=True)


# In[224]:


class_size = int(input('enter class size:'))


# In[225]:


for i in range(1,class_size+1):
  net.add_node(i, label=str(i))


# In[226]:


lst = ['1st Choice','2nd Choice','3rd Choice']
for i in range(len(df)):
  for elem in lst:
    net.add_edge(int(df.loc[i,'Class Index No. ']),int(df.loc[i,elem]))
  print('added', df.loc[i,'Full Name'],'1st:',df.loc[i,'1st Choice'],'2nd:',df.loc[i,'2nd Choice'],'3rd',df.loc[i,'3rd Choice'])


# In[227]:


net.show('4e1.html')

