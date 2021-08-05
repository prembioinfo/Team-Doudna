#include <stdio.h>
#include <conio.h>
int hamdist(char str1[], char str2[])
{
  int i=0, count=0;
  for(i=0;str1[i]!=0;i++)
  {
    if(str1[i]!=str2[i])
    count++;
  }
  return count;
}  
void main()
{
    char name[]="Shalini";
    char email[]="shalinigupta02992gmail.com";
    char slack[]="@Shalini";
    char biostack[]="Data analytics and Vaccine informatics";
    char twitter[]="@Shashaa";
    printf("%s,",name);
    printf("%s,",email);
    printf("%s,",slack);
    printf("%s,",biostack);
    printf("%s,",twitter);
    printf("%d,",hamdist(slack,twitter));
    getch();
}
