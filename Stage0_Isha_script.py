#!/usr/bin/env python
# coding: utf-8

NAME , EMAIL , SLACKID , BIOSTACK , TWITTER = "Isha Barve" , "isha.barve0@gmail.com", "@Isha", "Drug Development", "@Isba"

def Hamming_distance(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

str1 = SLACKID
str2 = TWITTER

print(f"{NAME}, {EMAIL}, {SLACKID}, {BIOSTACK}, {TWITTER}, {Hamming_distance(str1, str2)}")

# In[ ]:




