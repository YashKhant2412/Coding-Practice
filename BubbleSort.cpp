#include<iostream>
using namespace std;

int main(){
    int arr[6];
    for(int i=0;i<6;i++){
        cin>>arr[i];
    }

    for(int i=0;i<5;i++){
        for(int j=0;j<6-i;j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        } 
    }

    for(int i=0;i<6;i++){
        cout<<arr[i]<<" ";
    }
}