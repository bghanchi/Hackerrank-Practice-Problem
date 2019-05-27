#include<iostream>
#include<deque>
#include<vector>
using namespace std;
int main(){
    int t;
    cin>>t;
  deque<int>dq;
  deque<int>::iterator it;
  vector<int>v;
    while(t--){
        int n,t;
        cin>>n>>t;
         for(int i=0;i<n;i++){
             int t;
             cin>>t;
             dq.push_back(t);
         }
       
     for(int i=0;i<dq.size()-1;i++){
         for(int j=i;j<i+t;j++){
              v.push_back(dq[j]);
//                  cout<<v[0]<<" ";
              }
            for(int i1=0;i1<v.size();i1++){
                  for(int j1=i1+1;j1<v.size();j1++){
                      if(v[i1]>v[j1]){
                          int t1;
                          t1=v[j1];
                          v[j1]=v[i1];
                          v[i1]=t;
                      }
                    }
           }
            cout<<v[1]<<" ";
            v.clear();

             }
    }
     return 0;
    }

/*
                  for(int j1=i1+1;j<v.size();j++){
                      if(v[i1]<v[j1]){
                          int t1;
                          t1=v[j1];
                          v[j1]=v[i1];
                          v[i1]=t;
                      }


             for(int k=j+1;k<t;k++ ){
                 if(dq[j]<dq[k]){
                     int t1;
                     t1=dq[k];
                     dq[k]=dq[j];
                     dq[j]=t;
                 }
             }

*/
