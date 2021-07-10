#include<iostream>
using namespace std;

int main(){
    int arr[6];
    for(int i=0;i<6;i++){
        cin>>arr[i];
    }

    for(int i=0;i<5;i++){
        for(int j=i+1;j<6;j++){
            if(arr[j]<arr[i]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j]=temp;
            }
        }
    }

    for(int i=0;i<6;i++){
        cout<<arr[i]<<" ";
    }
}