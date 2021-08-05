#!/usr/bin/env python
# coding: utf-8

# In[1]:


List = ["Name = Morali Shah",
        "email = shahmorali@gmail.com",
        "slackname = @morali",
        "biostack = Drug Development"]
print (*List, sep = "\n")


# In[ ]:


def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
str1 = "Monica"
str2 = "morali"

print(hammingDist(str1, str2))


print(f"{List}, {hammingDist(str1, str2)}")


# In[ ]:


