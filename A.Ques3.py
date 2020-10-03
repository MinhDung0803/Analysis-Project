#!/usr/bin/env python
# coding: utf-8

# In[1]:


#INTRODUCTION: In analytic report project, I got the data of almost 5000 movies and there are three question I need to answer.
# 1. What areas(region of the movie) has the most influence on revenue ?
# 2. How is the movie's revenue and averege score affected by its genre ?
# 3. What influence does release date have on revenue ?


# In[2]:


import pandas as pd


# In[3]:


originaldata = pd.read_csv("tmdb_5000_movies.csv")
originaldata.head(5)


# In[4]:


# Above is a original data with many features which describes for each movies. For example: butget, genres, production_counties,
# revenue, id, original_tittle, etc.


# In[5]:


# Now I am going to answer the last question:
# 3. What influence does release date have on revenue ?
# To deal with this question. I have created a new data(choosing only two related features to this question: release_date
# and revenue), the others feature havwe been deleted. The data was renamed "Ques3.xlsx"
# Now I am going to load this data and do some neccessary taks on this data to answer this question.


# In[6]:


data = pd.read_excel("Ques3.xlsx")


# In[7]:


data.head()


# In[ ]:


#DESCRIBING THE DATA:I show the data above. It includes release_date of the movies and revenue information.
#Now, I am going to take the month information in release_date of each movie and put them in a new column beside revenue column.


# In[22]:


a = []
for i in range(len(data.release_date)):
    b = data.release_date[i]
    c = b.month
    if c > 0:
        a.append(int(c))
    else:
        a.append("none")


# In[23]:


data["month"] = a


# In[24]:


data.head()


# In[25]:


print(data.month.value_counts())


# In[26]:


# Now I am going to select the revenue of each month.


# In[38]:


month1 = []
month2 = []
month3 = []
month4 = []
month5 = []
month6 = []
month7 = []
month8 = []
month9 = []
month10 = []
month11 = []
month12 = []

for i in range(len(data.month)):
    if data.month[i] == 1:
        if data.revenue[i] != 0:
            month1.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 2:
        if data.revenue[i] != 0:
            month2.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 3:
        if data.revenue[i] != 0:
            month3.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 4:
        if data.revenue[i] != 0:
            month4.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 5:
        if data.revenue[i] != 0:
            month5.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 6:
        if data.revenue[i] != 0:
            month6.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 7:
        if data.revenue[i] != 0:
            month7.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 8:
        if data.revenue[i] != 0:
            month8.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 9:
        if data.revenue[i] != 0:
            month9.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 10:
        if data.revenue[i] != 0:
            month10.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 11:
        if data.revenue[i] != 0:
            month11.append(data.revenue[i])
        else:
            pass
    else:
        pass
for i in range(len(data.month)):
    if data.month[i] == 12:
        if data.revenue[i] != 0:
            month12.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[39]:


print(len(month1))
print(len(month2))
print(len(month3))
print(len(month4))
print(len(month5))
print(len(month6))
print(len(month7))
print(len(month8))
print(len(month9))
print(len(month10))
print(len(month11))
print(len(month12))


# In[36]:


# At this time, we can see that 12 months also have enough revenue information to be taken as sample on hypothesis testing.
# So, I am going to use all 12 months to answer this third question. But now, I need to choose randomly 200 revenue value
# for each month as samples.


# In[52]:


import random


# In[53]:


month1data = random.choices(month1, k=200)
month2data = random.choices(month2, k=200)
month3data = random.choices(month3, k=200)
month4data = random.choices(month4, k=200)
month5data = random.choices(month5, k=200)
month6data = random.choices(month6, k=200)
month7data = random.choices(month7, k=200)
month8data = random.choices(month8, k=200)
month9data = random.choices(month9, k=200)
month10data = random.choices(month10, k=200)
month11data = random.choices(month11, k=200)
month12data = random.choices(month12, k=200)


# In[55]:


#VISUALIZATION: Now I am going to plot these data.


# In[56]:


import matplotlib.pyplot as plt


# In[57]:


plt.plot(month1data)


# In[58]:


plt.plot(month2data)


# In[59]:


plt.plot(month3data)


# In[60]:


plt.plot(month4data)


# In[61]:


plt.plot(month5data)


# In[62]:


plt.plot(month6data)


# In[63]:


plt.plot(month7data)


# In[64]:


plt.plot(month8data)


# In[65]:


plt.plot(month9data)


# In[66]:


plt.plot(month10data)


# In[67]:


plt.plot(month11data)


# In[68]:


plt.plot(month12data)


# In[69]:


# Based on their figure, we can see that each month has the diffrence on revenue value. To find out which genres has the
# biggest average revenue value. Now I am going to calculate the average revenue for each month.


# In[70]:


def average(lst):
    return sum(lst)/len(lst)


# In[71]:


print("Average revenue of month1",average(month1data))
print("Average revenue of month2",average(month2data))
print("Average revenue of month3",average(month3data))
print("Average revenue of month4",average(month4data))
print("Average revenue of month5",average(month5data))
print("Average revenue of month6",average(month6data))
print("Average revenue of month7",average(month7data))
print("Average revenue of month8",average(month8data))
print("Average revenue of month9",average(month9data))
print("Average revenue of month10",average(month10data))
print("Average revenue of month11",average(month11data))
print("Average revenue of month12",average(month12data))


# In[72]:


# After calculated the revenue value for each month, we can easily see the movies that was released at June will have the
# biggest revenue. In the other sight, all the movies have been resealed at the begining of Summer(May, June, July).


# In[73]:


# ANALYSIS: We have to two hyphothesises:
# H0: All the movies was released at the difference months that have the same revenue.
# H1: All the movies was released at the difference months that have the difference revenue.
# And I am going to apply ANOVA-oneway to test these hyphothesises.


# In[74]:


from scipy.stats import f_oneway


# In[76]:


# We can get F(theory) = 1.79 by using FINV(0.05,11,2388) formular in excel with k = 12, n = 200 and p = 0.05
# Next, we are going to find F(statistics) by apply one-way ANOVA on month1data, month2data, month3data, month4data, month5data,
# month6data, month7data, month8data, month9data, month10data, month11data, month12data.


# In[77]:


f_oneway(month1data, month2data, month3data, month4data, month5data,month6data, month7data, month8data, month9data, month10data, month11data, month12data)


# In[78]:


#CONCLUSION: So, we can see that F(theory) = 1.79  < F(statistics) = 20.93 with pvalue = 4.53x10^(-41), 
# We are going to reject H0 and accept H1.
# We can make the conclusion that "All the movies was released at the difference months that have the difference revenue." 
# has the most influence on revenue.


# In[ ]:




