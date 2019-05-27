#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>v;
     int n;
     cin>>n;
     for(int i=1;i<=n;i++){
        int a;
        cin>>a;
        v.push_back(a); 
     }
 vector<int>::iterator it;
  int k;
  cin>>k;
 v.erase(v.begin()+k-1);
  int a,b;
  cin>>a>>b;
  
 v.erase(v.begin()+a-1,v.begin()+b-1);

  cout<<n-(b-a)-1<<"\n";   
 for( it = v.begin(); it != v.end(); it++){
     cout<<*it<<" ";
 }
        return 0;
}