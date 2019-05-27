#include<iostream>
#include <algorithm>
using namespace std;
int main(){
    long long  int n;
    cin>>n;
     long long int a[n];
    for(long long int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a,a+n);
   long long int count=0,k=0;
   for( long long int i=n-1;i>0;i--){
        if(a[i]==a[n-1]){
            count++;
        }
        else{
            break;
        }
          }
cout<<count<<" ";

return 0;    
}