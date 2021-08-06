#include<iostream.h>
#include<conio.h>
int hamdist(char* str1, char* str2)
{
int i=0, count=0;
for(i=0,str1[i]!=0;i++)
{
if(str1[i]!=str2[i])
count++;
}
return count;
}
void main()
{
clrscr();
char* Name="Akanksha";
char* Email_id="gmsbin15.akanksha.kulkarni@gnkhalsa.edu.in";
char* Slack_Username="@Akanksha";
char* Biostack="drug design and genomics";
char* Twitter_handle="@Avynksha";
cout<<"Name: "<<Name<<"\n";
cout<<"Email_id: "<<Email_id<<"\n";
cout<<"Slack_Username: "<<Slack_Username<<"\n";
cout<<"Biostack: "<<Biostack<<"\n";
cout<<"Twitter_Handle: "<<Twitter_handle<<"\n";
cout<<"Hamming Distance: "<<hamdist(Slack_Username, Twitter_handle);
getch();
}
