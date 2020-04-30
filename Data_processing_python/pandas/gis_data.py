#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas
thefts=pandas.read_excel("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\thefts_and_pop.xls",sheet_name=0)
pop=pandas.read_excel("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\thefts_and_pop.xls",sheet_name=1)

thefts.head()

pop.head()

thefts["key"]=thefts["State"]+thefts["County"]
thefts["key"]=thefts["key"].str.lower()
pop["key"]=pop["State"]+pop["County"]
pop["key"]=pop["key"].str.lower()

thefts.head()

pop.head()

thefts_pop=pandas.merge(left=thefts, right=pop , left_on="key", right_on="key", how="inner")
thefts_pop.head()
thefts_pop.shape

thefts_pop["Thefts per 10000"]=thefts_pop["Motor vehicle thefts"]*(10000/thefts_pop[2014])
thefts_pop.head()

get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

thefts_pop["Thefts per 10000"].plot()

thefts_pop.iloc[thefts_pop["Thefts per 10000"].idxmax()]

thefts_pop.to_excel("C:\\Users\\hkacker\\Documents\\Python_Scripts\\input\\output.xls", index=None)

