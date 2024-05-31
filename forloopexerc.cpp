#include<iostream>
using namespace std;
int main()
{
    int i,sum=0;
    for(i=1;1<=15;i++)
    {
        if(i%2 != 0)
        {
            sum=sum+i;
        }
    }
    cout<<"sum of odd no.s from 1-15 is :"<<sum<<endl;
    return 0;
}