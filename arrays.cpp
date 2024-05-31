#include<iostream>
using namespace std;
int main()
{
    //int roll_no[60];//definition
    //extern int a[]; declaration
    int roll_no[100]={},sum=0;
    for(int i=0;i<=99;i++)
    {
        roll_no[i]=sizeof(char);
        cout<<roll_no[i];
        for (int j = 0; j <= 99; j++)
        {
            sum=sum + roll_no[j];
        }
        
    }
    cout<<sum<<endl;
    cout<<roll_no[2]<<endl;
    return 0;

}