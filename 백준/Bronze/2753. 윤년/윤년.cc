#include <stdio.h>
int main(){
    int a,b;
    scanf("%d",&a);
    if(a%400==0){
       b=1;}
    else if(a%100==0){
        b=0;
    } else if(a%4==0){
        b=1;
    } else b=0;
    printf("%d\n",b);
return 0;
}