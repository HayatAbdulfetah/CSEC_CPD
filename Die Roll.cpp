#include<iostream>
using namespace std;
int main() {
    int x,y,a,b=6;
    cin>>x>>y;
    a=7-max(x,y);
    for(int i=2; i<=6; i++) {
        if(a%i==0 && b%i==0) {
            a/=i;
            b/=i;
        }
    }
    cout<<a<<"/"<<b;
    return 0;
}
