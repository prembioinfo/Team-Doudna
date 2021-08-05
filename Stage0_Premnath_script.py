my_details = ["Name", "Email", "SLACK_USERNAME", "Biostack", "Twitter_handle"]
my_details[0] = "Premnath"
my_details[1] = "batchaamadan17@gmail.com"
my_details[2] = "@Premnath"
my_details[3] = "Drug Development"
my_details[4] = "@Batchaa1"

def Hamming_distance(string_1, string_2):
    i = 0
    count = 0

    while (i < len(string_1)):
        if (string_1[i] != string_2[i]):
            count += 1
        i += 1
    return count

string_1 = my_details[2]
string_2 = my_details[4]

Hamming_distance_between_strings = Hamming_distance(string_1, string_2)

print(my_details[0],my_details[1], my_details[2],my_details[3], my_details[4],Hamming_distance_between_strings, sep=', ')





