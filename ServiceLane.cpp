#include<iostream>
#include<algorithm>
using namespace std;
int main(){
   long long int n,t;
    cin>>n>>t;
    long long int a[n];
    for(long long int i=0;i<n;i++){
        cin>>a[i];
    }
 while(t--){
    long long int w1,w2;
     cin>>w1>>w2;
    long long int n1=w2-w1;
     long long int a1[n1],k=0;
     for(long long int i=w1;i<=w2;i++){
         a1[k]=a[i];
         k++;
     }
     sort(a1,a1+n1+1);
       cout<<a1[0]<<"\n";

  }
}


/*

*/