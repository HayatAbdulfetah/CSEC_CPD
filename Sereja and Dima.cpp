#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++) {
        cin>>arr[i];
    }
    int left=0,right=n-1;
    bool turn=true;//first player
    int player1=0,player2=0;
    while(left<=right) {
        int value=0;
        if(arr[left]>=arr[right]) {
            value=arr[left];
            left++;
        }
        else {
            value=arr[right];
            right--;
        }
        if(turn)
            player1+=value;
        else player2+=value;
        turn= not turn;

    }
    cout<<player1<<" "<<player2<<"\n";
    return 0;
}
