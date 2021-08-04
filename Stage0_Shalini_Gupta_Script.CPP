#include<iostream.h>
#include<conio.h>
int hamdist(char* str1, char* str2)
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
clrscr();
char* Name = "Shalini";
char* Email_id = "shalinigupta0299@gmail.com";
char* Slack_Username = "@Shalini";
char* Biostack = "Data analytics and Vaccine informatics";
char* Twitter_Handle = "@Shashaa";
cout<<"Name: "<<Name<<"\n";
cout<<"Email Id: "<<Email_id<<"\n";
cout<<"Slack_Username: "<<Slack_Username<<"\n";
cout<<"Biostack: "<<Biostack<<"\n";
cout<<"Twitter_Handle: "<<Twitter_Handle<<"\n";
cout<<"Hamming Distance: "<<hamdist(Slack_Username,Twitter_Handle);
getch();
}
