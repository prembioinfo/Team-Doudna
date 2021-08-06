List = [ "Isha Barve,  isha.barve0@gmail.com , @Isha ,  Drug Designing,"]

def Hamming_distance(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

str1 = "@isha"
str2 = "@isba"

print (*List,Hamming_distance(str1, str2) )
