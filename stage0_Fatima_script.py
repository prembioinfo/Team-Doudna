Name = "Fatima Iftikhar"
Email = "fatimaiftikhar177@gmail.com"
Slack_handle = "@Fatimaiftikhar"
Biostack = "Vaccine informatics"
Twitter_handle = "@Fatima_scigeek"

str1 = "@Fatimaiftikhar"
str2 = "@Fatima_scigeek"


def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
         count += 1
    return count

print(Name, Email, Slack_handle, Biostack, Twitter_handle, hamming_distance(str1, str2), sep=",")

