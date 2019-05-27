#include<iostream>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a,a+n-1);
   int count=0,k=0;
   for(int i=n-1;i>=0;i--){
       for(int j=i;j>=0;j--){
           if(a[i]==a[j]){
            cout<<a[j]<<" ";
               count++;
           }
           else{
               i=j+1;
               k++;
               break;
           }
       }
       if(k==2){
           break;
       }
   }

   cout<<count<<" ";

return 0;    
}