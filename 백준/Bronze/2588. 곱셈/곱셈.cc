#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int a,b;
    scanf("%d %d",&a, &b);
    
    int r1 = a*(b%10); 
    printf("%d\n",r1);
    int r2 = a*(b/10%10); 
    printf("%d\n",r2);
    int r3 = a*(b/100); 
    printf("%d\n",r3);
    int result = r1+(r2*10)+(r3*100); 
    printf("%d\n",result);
 
 
}
