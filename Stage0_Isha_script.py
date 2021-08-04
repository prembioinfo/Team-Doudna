#!/usr/bin/env python
# coding: utf-8

NAME = "Isha Barve"
EMAIL = "isha.barve0@gmail.com"
SLACKID = "@Isha"
BIOSTACK = "Drug Development"
TWITTER = "@isba"

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

print(f"NAME:- {NAME}\nEMAIL-ID:- {EMAIL}\nSLACK ID:- {SLACKID}\nBIOSTACK:- {BIOSTACK}\nTWITTER HANDLE:- {TWITTER}\nHAMMING DISTANCE:- {Hamming_distance(str1, str2)}")

# In[ ]:




