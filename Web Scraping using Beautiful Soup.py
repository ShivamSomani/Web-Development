
# coding: utf-8

# In[1]:


# Application 7
import requests
from bs4 import BeautifulSoup


# In[2]:


r = requests.get("https://pythonhow.com/example.html")
c =r.content


# In[3]:


c  # it prints the source code


# In[4]:


soup = BeautifulSoup(c, "html.parser")


# In[7]:


all =soup.find_all("div",{"class": "cities"}) #


# In[8]:


all


# In[13]:


all[0].find_all("h2")[0].text   #beautiful soup supports indexing 


# In[11]:


for item in all:
    print (item.find_all("p")[0].text)

