//for(range_declaration:range_expression)
#include<iostream>
using namespace std;
int main()
{
    int a[]={1,2,3,4,5};
    for(auto b:a)
    {
        cout<<b;
    }
    return 0;
}