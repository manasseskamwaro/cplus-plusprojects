#include<iostream>
using namespace std;
int main()
{
    //initialiation,termination condition,update
    //for(initialization;condition;update)
    int i=0,sum=0;
    for(i=1;i<=15;i++)
    {
        cout<<i<<endl;
        sum=sum+i;
    }
    cout<<sum<<endl;
    return 0;

}