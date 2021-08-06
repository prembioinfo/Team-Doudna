#!/usr/local/bin/python3
name: str = "Adeniran Fadekemi"
email: str = "fadekeadeniran@yahoo.com"
slack_username: str = "@Morenike"
biostack = "Drug Development"
twitter_handle = "@dekemiii"
def hammingDist(str1, str2):
    i = 0
    count = 0
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
# Driver code 
str1 = "Morenike"
str2 = "Dekemiii"
# function call
print(f"{name}, {email}, {slack_username}, {biostack}, {twitter_handle}, {hammingDist(str1, str2)}")
