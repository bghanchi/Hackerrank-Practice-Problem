#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>v;
     int n;
     cin>>n;
     for(int i=0;i<n;i++){
        int a;
        cin>>a;
        v.push_back(a); 
     }

     for(int i=0;i<n;i++){
           for(int j=i+1;j<n;j++){
               if(v[i]>v[j]){
                   int t;
                   t=v[j];
                   v[j]=v[i];
                   v[i]=t;
               }
           }
     }

     for(int i=0;i<n;i++){
         cout<<v[i]<<" ";
     }
        return 0;
}