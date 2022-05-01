#include <stdio.h>

void swap(int **dp1, int **dp2){
    int *temp;
    temp = *dp1;
    *dp1 = *dp2;
    *dp2 = temp;
}

int main(){

    int num1 = 10;
    int num2 = 20;
    int *ptr1;
    int *ptr2;

    ptr1 = &num1;
    ptr2 = &num2;

    printf("%d %d\n", *ptr1, *ptr2);
    swap(&ptr1, &ptr2);
    printf("%d %d\n", *ptr1, *ptr2);

    return 0;
}