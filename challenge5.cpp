#include<iostream>
#include<deque>
#include<vector>
using namespace std;
int main(){
    int t1;
    cin>>t1;
  deque<int>dq;
  deque<int>::iterator it;
  vector<int>v;
    while(t1--){
        int n,t;
        cin>>n>>t;
         for(int i=0;i<n;i++){
             int c;
             cin>>c;
             dq.push_back(c);
         }
      int j=0;
      while(t<=n){
          for(int i=j;i<t;i++){
              v.push_back(dq[i]);
          }
          for(int k=0;k<v.size();k++){
              for(int l=k+1;l<v.size();l++){
                  if(v[k]<v[l]){
                      int t2;
                      t2=v[l];
                      v[l]=v[k];
                      v[k]=t2;
                  }
              }
          }

          cout<<v[0]<<" ";
       t=t+1;
       j=j+1;
       v.clear();
      }
      cout<<"\n";
    dq.clear();
    } 
     return 0;
    }
