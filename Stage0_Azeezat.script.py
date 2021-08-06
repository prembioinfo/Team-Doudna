List = [ "Azeezat Osikoya,  oluwatobiosikoya1@gmail.com , @Azeezat ,Drug Designing,@Azeeza2,"]

def Hamming_distance(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

str1 = "@Azeezat"
str2 = "@Azeeza2"

print (*List,Hamming_distance(str1, str2) )
