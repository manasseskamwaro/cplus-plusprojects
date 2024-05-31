//3 types-sequential,iteration,

#include<iostream>
using namespace std;

int main()
{
    //sequential
    /*int a=0,b=0,sum=0;
    cout<<"enter a & b:"<<endl;
    cin>>a>>b;
    sum=a+b;
    cout<<"sum="<<sum<<endl;
    return 0;*/
    //selection
    //if,if-else,else-if ladder,nested if,switch
    //iteration-repeating to a certain condition
    //for ,while,do while loops
    //if statement;
    /*int money=0;
    cout<<"Howmuch do you have?"<<endl;
    cin>>money;
    if(money>=1000)
        {
            cout<<"Coffee in starbucks!!"<<endl;
            cout<<"It was good"<<endl;
        }
    cout<<"Let's go home!!";*/
    //if-else statement
    int money=0;
    cout<<"Enter funds available:"<<endl;
    cin>>money;
    if (money>1000 && money<5000)
       {
        cout<<"Funds available:"<<money<<endl;
        cout<<"Coffee at starbucks is possible."<<endl;
        cout<<"Was nice!!"<<endl;
       }
    else if(money>=5000)
    {
        cout<<"Let's get out of town"<<endl;
        cout<<"Mi amore!!";
    }
    else
        {
            cout<<"Funds available:"<<money<<endl;
            cout<<"Coffee at home!!!!!!"<<endl;
        }
    cout<<"let's go home:"<<endl;

    return 0;
}
