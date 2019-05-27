#include<iostream>
#include<vector>
using namespace std;
int main(){
   long int n;
    cin>>n;
    vector<int>a;
    long int sum=0,k=0;
    for(long int i=0;i<n;i++){
        long int t;
        cin>>t;
        a.push_back(t);
    }
        int f=0;
    for(long int i=0;i<n;i++){
        if(a[i]>=0){
            sum+=a[i];
            k++;
            f++;
        }
    }
    if(f==0){
        for(long int i=0;i<n;i++){
            for(long int j=i+1;j<n;j++){
                if(a[i]<a[j]){
                    long int t;
                    t=a[j];
                    a[j]=a[i];
                    a[i]=t;
                }
            }
        }
        k=1;
        cout<<a[0]<<" "<<k<<"\n";
    }
    else{
    cout<<sum<<" "<<k<<"\n";
    }
    return 0;
}