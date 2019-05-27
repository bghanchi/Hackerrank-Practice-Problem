#include<iostream>
using namespace std;
int main(){
    long long int s,t;
    cin>>s>>t;
    long long int a,b;
    cin>>a>>b;
    long long int m,n;
    cin>>m>>n;
    long long int a1[m],b1[n];
    for(long long int i=0;i<m;i++){
        cin>>a1[i];
    }
    for(long long int i=0;i<n;i++){
        cin>>b1[i];
    }
    for(long long int i=0;i<m;i++){
        a1[i]=a+a1[i];
    }
     for(long long int i=0;i<n;i++){
        b1[i]=b+b1[i];
    }
    long long int apples=0,orages=0;
    for(long long int i=0;i<m;i++){
        if(a1[i]>=s & a1[i]<=t){
            apples++;
        }
    }
    for(long long int i=0;i<n;i++){
        if(b1[i]>=s & b1[i]<=t){
            orages++;
        }
    }              

     cout<<apples<<"\n"; 
     cout<<orages<<"\n"; 
return 0;
}