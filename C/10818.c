#include <stdio.h>

int main(){

    int n, num, min = 100001, max = -100001;

    scanf("%d", &n);
    
    for(int i= 1; i <= n; i++){
        scanf("%d", &num);
        if(num > max){
            max = num;
        }           
        if(num < min){
            min = num;
        }
    }
    printf("%d %d", min, max);
    return 0;
}