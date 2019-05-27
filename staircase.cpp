#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int k=n;
    while(k){
        for(int i=1;i<=n+1;i++){
             if(i>k){
                 cout<<"#";
             }
             else{
                 cout<<' ';
             }
        }
        cout<<"\n";
        k--;
    }
}