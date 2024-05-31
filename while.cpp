#include<iostream>
using namespace std;

int main()
{
    int i;
    cout<<"Enter number between 2 and 7:"<<endl;
    cin>>i;
    while(i>2 && i<7)
    {
        cout<<i<<endl;
        i++;
    }
}