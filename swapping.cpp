#include<conio.h>
#include<stdio.h>

void swapp(int *x,int *y){
    int temp;
    temp = *y;
    *y = *x;
    *x = temp;
}

int main(){
    int x=5;
    int y=8;
    /*  x=x+y;
        y=x-y;
        x=x-y;*/

    /* int temp;
       temp; = y;
       y = x;
       x = temp;*/

     /*   x=x*y;
        y=x/y;
        x=x/y; */

    x = x^y;
    y = x^y;
    x = x^y;
    /*int *a,*b;
    a = &x;
    b = &y;
    swapp(&x,&y)*/;
    printf("%d, %d",x,y);
    return 0;
}

