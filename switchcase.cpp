#include<iostream>
using namespace std;
int main()
{
    char ch;
    cout<<"enter your choice:"<<endl;
    cin>>ch;
    switch (ch)
    {
    case 'a':
        cout<<"I want to know my balance.";
        break;
    case 'A':
        cout<<"I want to pass a complaint.";
        break;
    case 'c':
        cout<<"I want to talk to the manager.";
        break;
    
    default:
        cout<<"enter valid choice.";
        break;
    }
    cout<<"\nout of switch case";
}