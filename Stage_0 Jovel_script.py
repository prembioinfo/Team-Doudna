Name = "Jovel Varghese Jose"
Email = "jovelvarghesejose718@gmail.com"
Slack_username = "jovel"
Biostack = "Drug development"
Twitter_handle = "gravityboyjovel"

def Hamming_distance(str1, str2):
    i = 0
    count = 0
    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count
str1 = Slack_username
str2 = Twitter_handle
print(f"{Name}, {Email}, {Slack_username}, {Biostack}, {Twitter_handle }, {Hamming_distance(str1, str2)}")
