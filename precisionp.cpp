#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    long long int n;
    cin>>n;
    long long int a[n];
    long long int pos=0,neg=0,zero=0;
    for(long long int i=0;i<n;i++){
           cin>>a[i];
    }
    for(int i=0;i<n;i++){
        if(a[i]>0){
            pos++;
        }
        else if(a[i]<0){
            neg++;
        }
        else{
            zero++;
        }
    }
    long double pos1,neg1,zero1;
    pos1=double(pos)/n;
    neg1=double(neg)/n;
    zero1=double(zero)/n;
    cout<<setprecision(3)<<pos1<<"\n";
    cout<<neg1<<"\n";
    cout<<zero1<<"\n";

return 0;
}  