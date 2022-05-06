#include <stdio.h>

int main(void){

    int n = 5;
    int m = 10;
    int **arr = malloc(sizeof(int *)*n);

    for(int i = 0; i < n ; i++){
        arr[i] = malloc(sizeof(int) * m);

    }

    return 0;

}