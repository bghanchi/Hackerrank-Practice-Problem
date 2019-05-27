#include<iostream>
using namespace std;
long long int grade(long long int );

int main(){
    long long int n;
    cin>>n;
    long long int a[n];
    for(long long int i=0;i<n;i++){
        cin>>a[i];
    }

    for(long long int i=0;i<n;i++){
             a[i]=grade(a[i]);
    }

    for(long long int i=0;i<n;i++){
       cout<<a[i]<<"\n"; 
    }
return 0;    
}

long long int grade(long long int i){
             if(i%5>2 &  i>=38 ){
                 i=i+(5-i%5);   
                 
        }

     return i;      

}