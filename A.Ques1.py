#!/usr/bin/env python
# coding: utf-8

# In[68]:


#INTRODUCTION: In analytic report project, I got the data of almost 5000 movies and there are three question I need to answer.
# 1. What areas(region of the movie) has the most influence on revenue ?
# 2. How is the movie's revenue and averege score affected by its genre ?
# 3. What influence does release date have on revenue ?


# In[137]:


import pandas as pd


# In[138]:


originaldata = pd.read_csv("tmdb_5000_movies.csv")
originaldata.head(5)


# In[141]:


# Above is a original data with many features which describes for each movies. For example: butget, genres, production_counties,
# revenue, id, original_tittle, etc.


# In[142]:


# Now I am going to answer the first question:
# 1. What areas(region of the movie) has the most influence on revenue ?
# To deal with this question. I have created a new data(choosing only two related features to this question), the others
# feature havwe been deleted. The data was renamed "areas.xlsx"
# Now I am going to load this data and do some neccessary taks on this data to answer this question.


# In[143]:


data = pd.read_excel("areas.xlsx")


# In[144]:


data.head()


# In[ ]:


#DESCRIBING THE DATA:I show the data above. It includes production_countries and revenue information.


# In[151]:


data['areas'] = data.production_countries.apply(lambda x: x[17:19])


# In[152]:


data.head(10)


# In[182]:


print(data.areas.value_counts())


# In[ ]:


# There are many areas where the movies was made. In this data we have 71 countries. But there are many contries only have a few
# movies so I will only choose several countries that have over 170 movies in this data. There are 5 of them: US, GB, CA, DE, FR
# I will take all the revenue of these countries's movies into 5 lists.


# In[248]:


regionUS = []
regionGB = []
regionCA = []
regionDE = []
regionFR = []


# In[249]:


for i in range(len(data.areas)):
    if data.areas[i] == "US":
        if data.revenue[i] != 0:
            regionUS.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[250]:


for i in range(len(data.areas)):
    if data.areas[i] == "GB":
        if data.revenue[i] != 0:
            regionGB.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[251]:


for i in range(len(data.areas)):
    if data.areas[i] == "CA":
        if data.revenue[i] != 0:
            regionCA.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[252]:


for i in range(len(data.areas)):
    if data.areas[i] == "DE":
        if data.revenue[i] != 0:
            regionDE.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[253]:


for i in range(len(data.areas)):
    if data.areas[i] == "FR":
        if data.revenue[i] != 0:
            regionFR.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[254]:


print(len(regionUS))
print(len(regionGB))
print(len(regionCA))
print(len(regionDE))
print(len(regionFR))


# In[191]:


# Now I am going to choose 150 sample of each areas above randomly.


# In[192]:


import random


# In[265]:


dataUS = random.choices(regionUS, k=100)
dataGB = random.choices(regionGB, k=100)
dataCA = random.choices(regionCA, k=100)
dataDE = random.choices(regionDE, k=100)
dataFR = random.choices(regionFR, k=100)


# In[266]:


#VISUALIZATION: Now I am going to plot these data.


# In[267]:


import matplotlib.pyplot as plt


# In[268]:


plt.plot(dataUS)


# In[269]:


plt.plot(dataGB)


# In[270]:


plt.plot(dataCA)


# In[271]:


plt.plot(dataDE)


# In[272]:


plt.plot(dataFR)


# In[273]:


def average(lst):
    return sum(lst)/len(lst)


# In[274]:


print("Average revenue of US",average(dataUS))
print("Average revenue of GB",average(dataGB))
print("Average revenue of CA",average(dataCA))
print("Average revenue of DE",average(dataDE))
print("Average revenue of FR",average(dataFR))


# In[275]:


# We can see that GB has the biggest revenues on these sample.


# In[276]:


# We can see that each areas has difference revenue.


# In[277]:


#ANALYSIS: We have to two hyphothesises:
# H0: All the areas have the same revenue
# H1: These araes have differense revenue
# And I am going to apply ANOVA-oneway to test these hyphothesises.


# In[278]:


from scipy.stats import f_oneway


# In[282]:


#We can get F(theory) = 2.38 by using FINV(0.05,4,746) formular in excel with k = 5, n = 150 and p = 0.05
# Next, we are going to find F(statistics) by apply one-way ANOVA on dataUS, dataGB, dataCA, dataDE and dataFR


# In[283]:


f_oneway(dataUS,dataGB,dataCA,dataDE,dataFR)


# In[284]:


#CONCLUSION: So, we can see that F(theory) = 2.38  < F(statistics) = 3.77 with pvalue = 0.00488, 
# We are going to reject H0 and accept H1.
# We can make the conclusion that "These araes have differense revenue" and "GB(United Kingdom)" 
# has the most influence on revenue.


# In[ ]:




