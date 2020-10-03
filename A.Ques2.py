#!/usr/bin/env python
# coding: utf-8

# In[1]:


#INTRODUCTION: In analytic report project, I got the data of almost 5000 movies and there are three question I need to answer.
# 1. What areas(region of the movie) has the most influence on revenue ?
# 2. How is the movie's revenue and average score affected by its genre ?
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


# Now I am going to answer the second question:
# 2. How is the movie's revenue and average score affected by its genre ?
# To deal with this question. I have created a new data(choosing three features: genre, average, revenue), the others
# feature havwe been deleted. The data was renamed "Ques2.xlsx"
# Now I am going to load this data and do some neccessary taks on this data to answer this question.


# In[116]:


# Firstly, I am going to answer this question: How is the movie's revenue affected by its genre ?


# In[117]:


data = pd.read_excel("Ques2.xlsx")


# In[118]:


data.head()


# In[119]:


#DESCRIBING THE DATA:I show the data above. It includes genres, vote_average and revenue information.


# In[132]:


import json


# In[133]:


a = []


# In[134]:


a = []
for i in range(len(data.genres)):
    b = json.loads(data.genres[i])
    if b:
        e = b[0]["name"]
        a.append(e)
    else:
        a.append("none")


# In[135]:


data["datagenres"] = a


# In[136]:


data.head()


# In[137]:


print(data.datagenres.value_counts())


# In[138]:


# There are many type of movies that have been showed above, we can see that in this data there are also some types that just
# have several samples, less than the other type so many. So we have to ignore them and choose what types have over 100 sample.
# They are 10 type of movies: Drama, Comedy, Action, Adventure, Horror, Crime, Thriller, Animation, Fantasy, Romance.


# In[139]:


# Now I am going to select the revenue of each type of movie.


# In[178]:


Drama = []
Comedy= [] 
Action= [] 
Adventure= [] 
Horror= [] 
Crime= []
Thriller= [] 
Animation= [] 
Fantasy= [] 
Romance= []

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Drama":
        if data.revenue[i] != 0:
            Drama.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Comedy":
        if data.revenue[i] != 0:
            Comedy.append(data.revenue[i])
        else:
            pass
    else:
        pass
    
for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Action":
        if data.revenue[i] != 0:
            Action.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Adventure":
        if data.revenue[i] != 0:
            Adventure.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Horror":
        if data.revenue[i] != 0:
            Horror.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Crime":
        if data.revenue[i] != 0:
            Crime.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Thriller":
        if data.revenue[i] != 0:
            Thriller.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Animation":
        if data.revenue[i] != 0:
            Animation.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.datagenres)):
    if data.datagenres[i] == "Fantasy":
        if data.revenue[i] != 0:
            Fantasy.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[180]:


print(len(Drama))
print(len(Comedy))
print(len(Action))
print(len(Adventure))
print(len(Horror))
print(len(Crime))
print(len(Thriller))
print(len(Animation))


# In[181]:


# After I collected all the revenue values of each movies's type. There are some zero values on revenue so I decided to delete
# all of that zero value. After colecting revenue data, we can see that only eight genres have over 100 revenue sample:
# Drama, Comedy, Action, Adventure, Horror, Crime, Thriller, Animation
# Now I am going to choose 100 sample of each genres above randomly as main sample data.


# In[182]:


import random


# In[183]:


Dramadata = random.choices(Drama, k=100)
Comedydata = random.choices(Comedy, k=100)
Actiondata = random.choices(Action, k=100)
Adventuredata = random.choices(Adventure, k=100)
Horrordata = random.choices(Horror, k=100)
Crimedata = random.choices(Crime, k=100)
Thrillerdata = random.choices(Thriller, k=100)
Animationdata = random.choices(Animation, k=100)


# In[187]:


#VISUALIZATION: Now I am going to plot these data.


# In[188]:


import matplotlib.pyplot as plt


# In[189]:


plt.plot(Dramadata)


# In[190]:


plt.plot(Comedydata)


# In[191]:


plt.plot(Actiondata)


# In[193]:


plt.plot(Adventuredata)


# In[194]:


plt.plot(Horrordata)


# In[195]:


plt.plot(Crimedata)


# In[196]:


plt.plot(Thrillerdata)


# In[197]:


plt.plot(Animationdata)


# In[198]:


# Based on their figure, we can see that each genres has the diffrence on revenue value. To find out which genres has the
# biggest average revenue value. Now I am going to calculate the average revenue for each genres.


# In[199]:


def average(lst):
    return sum(lst)/len(lst)


# In[200]:


print("Average revenue of Drama",average(Dramadata))
print("Average revenue of Comedy",average(Comedydata))
print("Average revenue of Action",average(Actiondata))
print("Average revenue of Adventure",average(Adventuredata))
print("Average revenue of Horror",average(Horrordata))
print("Average revenue of Crime",average(Crimedata))
print("Average revenue of Thriller",average(Thrillerdata))
print("Average revenue of Animation",average(Animationdata))


# In[201]:


# Based on above average value of each genre, we can see that Animation movies has the biggest revenue value.


# In[202]:


#ANALYSIS: We have to two hyphothesises:
# H0: All the genres have the same revenue values
# H1: These genres have differense revenue values


# In[203]:


from scipy.stats import f_oneway


# In[204]:


#We can get F(theory) = 2.02 by using FINV(0.05,7,793) formular in excel with k = 8, n = 100 and p = 0.05
# Next, we are going to find F(statistics) by apply one-way ANOVA on Dramadata, Comedydata, Actiondata, 
# Adventuredata, Horrordata, Crimedata, Thrillerdata, Animationdata


# In[205]:


f_oneway(Dramadata, Comedydata, Actiondata, Adventuredata, Horrordata, Crimedata, Thrillerdata, Animationdata)


# In[263]:


#CONCLUSION: So, we can see that F(theory) = 2.02  < F(statistics) = 28.55 with pvalue = 3.56x10^(-35), 
# We are going to reject H0 and accept H1.
# We can make the conclusion that "These genres have differense revenue" and "Animation movies" 
# has the most influence on revenue.


# In[209]:


# Lastly, I am going to answer this question: How is the movie's revenue affected by its avarage score ?


# In[210]:


# There are 10 levels of average score for each movies, from 1 to 10. Now I am going to collect the revenue value based on
# these level


# In[234]:


level10 = []
level9 = []
level8 = []
level7 = []
level6 = []
level5 = []
level4 = []
level3 = []
level2 = []
level1 = []
level0 = []

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=10:
        if data.revenue[i] != 0:
            level10.append(data.revenue[i])
        else:
            pass
    else:
        pass
    
for i in range(len(data.vote_average)):
    if data.vote_average[i] >=9 and data.vote_average[i] <10:
        if data.revenue[i] != 0:
            level9.append(data.revenue[i])
        else:
            pass
    else:
        pass
    
for i in range(len(data.vote_average)):
    if data.vote_average[i] >=8 and data.vote_average[i] <9:
        if data.revenue[i] != 0:
            level8.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=7 and data.vote_average[i] <8:
        if data.revenue[i] != 0:
            level7.append(data.revenue[i])
        else:
            pass
    else:
        pass
    
for i in range(len(data.vote_average)):
    if data.vote_average[i] >=6 and data.vote_average[i] <7:
        if data.revenue[i] != 0:
            level6.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=5 and data.vote_average[i] <6:
        if data.revenue[i] != 0:
            level5.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=4 and data.vote_average[i] <5:
        if data.revenue[i] != 0:
            level4.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=3 and data.vote_average[i] <4:
        if data.revenue[i] != 0:
            level3.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=2 and data.vote_average[i] <3:
        if data.revenue[i] != 0:
            level2.append(data.revenue[i])
        else:
            pass
    else:
        pass
    
for i in range(len(data.vote_average)):
    if data.vote_average[i] >=1 and data.vote_average[i] <2:
        if data.revenue[i] != 0:
            level1.append(data.revenue[i])
        else:
            pass
    else:
        pass

for i in range(len(data.vote_average)):
    if data.vote_average[i] >=0 and data.vote_average[i] <1:
        if data.revenue[i] != 0:
            level0.append(data.revenue[i])
        else:
            pass
    else:
        pass


# In[236]:


print("level10: ",len(level10))
print("level9: ",len(level9))
print("level8: ",len(level8))
print("level7: ",len(level7))
print("level6: ",len(level6))
print("level5: ",len(level5))
print("level4: ",len(level4))
print("level3: ",len(level3))
print("level2: ",len(level2))
print("level1: ",len(level1))
print("level0: ",len(level0))


# In[237]:


# After collecting all revenue based on their level, we can see that only levels 7, 6, 5, 4 have over 170 samples. The others
# has so few samples. So I will choose levels 7, 6, 5, 4 for analysis steps.
# # Now I am going to choose 170 sample of each areas above randomly.


# In[238]:


import random


# In[239]:


level7data = random.choices(level7, k=170)
level6data = random.choices(level6, k=170)
level5data = random.choices(level5, k=170)
level4data = random.choices(level4, k=170)


# In[240]:


#VISUALIZATION: Now I am going to plot these data.


# In[241]:


import matplotlib.pyplot as plt


# In[242]:


plt.plot(level7data)


# In[243]:


plt.plot(level6data)


# In[244]:


plt.plot(level5data)


# In[245]:


plt.plot(level4data)


# In[246]:


# Based on their figure, we can see that each score level has the diffrence on revenue value. To find out which score level 
# has the biggest average revenue value. Now I am going to calculate the average revenue for each score level.


# In[247]:


def average(lst):
    return sum(lst)/len(lst)


# In[248]:


print("Average revenue of level7data",average(level7data))
print("Average revenue of level6ata",average(level6data))
print("Average revenue of level5data",average(level5data))
print("Average revenue of level4data",average(level4data))


# In[249]:


# After calculated the revenue value for each score level, we can easily see that movies has the higher score will have the
# bigger revenue. And here, average score at 7 has ther biggest revenue and each score level also has the diffrence revenue
# value.


# In[255]:


# ANALYSIS: We have to two hyphothesises:
# H0: All the average score have the same revenue
# H1: These average scores have differense revenue
# And I am going to apply ANOVA-oneway to test these hyphothesises.


# In[256]:


from scipy.stats import f_oneway


# In[260]:


# We can get F(theory) = 2.61 by using FINV(0.05,3,677) formular in excel with k = 4, n = 170 and p = 0.05
# Next, we are going to find F(statistics) by apply one-way ANOVA on level7data, level6data, level5data, level4data


# In[261]:


f_oneway(level7data, level6data, level5data, level4data)


# In[262]:


#CONCLUSION: So, we can see that F(theory) = 2.61  < F(statistics) = 11.21 with pvalue = 3.4x10^(-7), 
# We are going to reject H0 and accept H1.
# We can make the conclusion that "These average scores have differense revenues" and "average score at 7" 
# has the most influence on revenue.


# In[ ]:




