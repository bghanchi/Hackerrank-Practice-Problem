#include<iostream>
#include<vector>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    vector<int>s;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int total=a[i]+a[j];
            if(total%k!=0){
                s.push_back(a[i]);
                s.push_back(a[j]);
            }

        }
    }

     
    for(int i=0;i<s.size();i++){
        for(int j=i+1;j<s.size();j++){
             cout<<s[i]<<" "<<s[j]<<"\n";
            if(s[i]==s[j]){
           s.erase(s.begin()+j);
            }
        }
    }


    for(int i=0;i<s.size();i++){
        cout<<s[i]<<" ";
    }
    return 0;
}
