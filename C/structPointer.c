#include <stdio.h>
#include <stdlib.h>

typedef struct Data {
    char c1;
    int *numPtr;
} data;

int main(){

    int num1 = 10;
    data d1;
    data *d2 = malloc(sizeof(data));

    d1.numPtr = &num1;
    d2->numPtr = &num1;

    printf("%d\n", *d1.numPtr);
    printf("%d\n", *d2->numPtr);




    free(d2);
    return 0;
}