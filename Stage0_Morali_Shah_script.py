#!/usr/bin/env python
# coding: utf-8

# In[7]:


Name = "Morali Shah"
email = "shahmorali@gmail.com"
slackname = "@morali"
biostack = "Drug Development"
twitter = "@monica"


# In[8]:


def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
str1 = slackname
str2 = twitter

print(hammingDist(str1, str2))


# In[9]:


print(f"{Name}, {email}, {slackname}, {biostack}, {twitter}, {hammingDist(str1, str2)}")


# In[ ]:


