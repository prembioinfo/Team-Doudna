#!/usr/local/bin/python3
name: str = "Idowu Jinadu"
email: str = "neemahjinadu@gmail.com"
slack_username: str = "@Neemahj"
biostack = "Drug Development"
twitter_username = "@Aramide"
def hammingDist(str1, str2):
   i = 0
   count = 0
   while(i < len(str1)):
       if(str1[i] != str2[i]):
           count += 1
       i += 1
   return count
# Driver code
str1 = "@Neemahj"
str2 = "@Aramide"
# function call
print (name, email, slack_username, biostack, twitter_username, hammingDist (str1, str2))
