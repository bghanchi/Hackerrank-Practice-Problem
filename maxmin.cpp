#include<iostream>
using namespace std;
int main(){
    long long int a[5];
    long long int array[5];
    for(long long int i=1;i<=5;i++){
        cin>>a[i];
    }
    long long int sum=0,max=0,mix=0,count=1,k=0;
    for(long long int i=1;i<=5;i++){
        sum=0;
      for(long long int j=1;j<=5;j++){
        if(j!=count){
            sum+=a[j];
        }
      }
        array[k]=sum;
        k++;
        count++; 

    }

    for(long long int i=0;i<5;i++){
        for(long long int j=i+1;j<5;j++){
            if(array[i]>array[j]){
                long long int t;
                t=array[j];
                array[j]=array[i];
                array[i]=t;
            }
        }
    }
    cout<<array[0]<<" "<<array[4]<<"\n";
}