#include<iostream>
using namespace std;
int main()
{
    int money=0,partner_age=0;
    cout<<"enter money available:"<<endl;
    cin>>money;
    if(money>=1000)
    {
            cout<<"enter partner age:"<<endl;
            cin>>partner_age;
            if(partner_age>=18)
            {
                cout<<"let's have some wine bebbe!!"<<endl;
            }
            else
            {
                cout<<"let's have coffee:"<<endl;
            }
    }
    return 0;
}