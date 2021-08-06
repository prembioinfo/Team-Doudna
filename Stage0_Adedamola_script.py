#!/usr/local/bin/python3
name: str = "Akintokun Adedamola"
email: str = "olaakintokun@gmail.com"
slack_username: str = "@Adedamola"
biostack = "Drug Development"

twitter_handle = "@Durosopee"

def hammingDist(str1, str2):
    i = 0
    count = 0
    while(i < len(str1)):
        if(str1[i] != str2[i]):
         count += 1
        i += 1
    return count
# Driver code 
str1 = "Adedamola"
str2 = "Durosopee"
# function call
print(f"{name}, {email}, {slack_username}, {biostack}, {twitter_handle}, {hammingDist(str1, str2)}")
