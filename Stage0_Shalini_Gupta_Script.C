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
    printf("Name: %s\n",name);
    printf("Email Id: %s\n",email);
    printf("Slack Username: %s\n",slack);
    printf("Biostack: %s\n",biostack);
    printf("Twitter Handle: %s\n",twitter);
    printf("Hamming Distance: %d\n",hamdist(slack,twitter));
    getch();
}
