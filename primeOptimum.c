#include<conio.h>
#include<stdio.h>

int main(){
  int inp;
  inp = scanf("%d",inp);
  int flag = 0;

  for(int i=2;i<inp;i++){
    if(inp%i==0){
        flag = 1;
        break;
    }

  }
  if(flag==1)
    printf("Not Prime");
  else
    printf("Prime");

  return 0;
}
