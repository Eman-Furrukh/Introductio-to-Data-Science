#!/usr/bin/env python
# coding: utf-8

# # Name: Eman Furrukh

# # Roll No: 21i-1726

# # ASSIGNMENT #7

# In[99]:


import pandas as pd
import numpy as np


# TASK 1: 

# In[100]:


df = pd.read_excel(r"C:\Users\DELL\Downloads\data.xlsx")
df


# In[101]:


#condition = {'<35000': 0, '>=35000': 1}
#df['>=35k'] = 0
#df['>=35k'] = df['Salary'].map(condition)
#df
df=pd.read_excel(r"C:\Users\DELL\Downloads\data.xlsx")
df['>=35k']=(df['Salary'] >= 35000).astype(int)
df


# TASK 2:

# In[102]:


#import libraries
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt


# In[103]:


df.head()


# In[104]:


#number of clusters
k = 10

# Select random observation as centroids
Centroids = (df.sample(n=k))
plt.scatter(df["SiteSpending"],df["SiteTime"],c='yellow')
plt.scatter(Centroids["SiteSpending"],Centroids["SiteTime"],c='red')
plt.xlabel('SiteSpending')
plt.ylabel('SiteTime')
plt.show()


# In[105]:


diff = 1
j=0

while(diff!=0):
    df2=df
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in df2.iterrows():
            d1=(row_c["SiteSpending"]-row_d["SiteSpending"])**2
            d2=(row_c["SiteTime"]-row_d["SiteTime"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        df[i]=ED
        i=i+1

    C=[]
    for index,row in df.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(k):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    df["Cluster"]=C
    Centroids_new = df.groupby(["Cluster"]).mean()[["SiteTime","SiteSpending"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['SiteTime'] - Centroids['SiteTime']).sum() + (Centroids_new['SiteSpending'] - Centroids['SiteSpending']).sum()
        print(diff.sum())
    Centroids = df.groupby(["Cluster"]).mean()[["SiteTime","SiteSpending"]]


# In[106]:


#cluster ka coloumn has been added previous line pe so:
d = df[['Cluster']]
d.head()


# In[107]:


color=['blue','green','yellow']
for k in range(3):
    data=df[df["Cluster"]==k+1]
    plt.scatter(data["SiteSpending"],data["SiteTime"],c=color[k])
plt.scatter(Centroids["SiteSpending"],Centroids["SiteTime"],c='red')
plt.xlabel('Site Spending')
plt.ylabel('Site Time')
plt.show()

