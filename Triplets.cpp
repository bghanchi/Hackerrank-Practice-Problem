#include<iostream>
using namespace std;
int main(){
    long  long int a[3],b[3];
    long long int alice=0,bob=0;
    for(long long int i=0;i<3;i++){
        cin>>a[i];
    }
    for(long long int i=0;i<3;i++){
        cin>>b[i];
    }

    for(long long int i=0;i<3;i++){
        if(a[i]>b[i]){
            alice++;
        }
        else if(b[i]>a[i]){
            bob++;
        }
    }

    cout<<alice<<" "<<bob<<"\n";
return 0;
}