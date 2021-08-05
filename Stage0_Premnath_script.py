Name = "Premnath"
Email = "batchaamadan17@gmail.com"
SLACK_USERNAME = "@Premnath"
Biostack = "Drug Development"
Twitter_handle = "@Batchaa1"

def Hamming_distance(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

str1 = SLACK_USERNAME
str2 = Twitter_handle


print(f"Name: {Name}, Email-ID: {Email}, Slack_username: {SLACK_USERNAME}, Biostack: {Biostack}, Twitter handle: {Twitter_handle}, Hamming_distance: {Hamming_distance(str1, str2)}")
