#include <stdio.h>



int main(){

    int n;
    n = 9;
    int num;
    int arr[9] = {0,0,0,0,0,0,0,0,0};

    for(int i = 0; i < n; i++){
        scanf("%d", &num);
        arr[i] = num;

    }
    int max, idx;
    max = 0;
    idx = 0;
    for(int i = 0; i < n; i++){
        if (arr[i] > max) {
            max = arr[i];
            idx = i+1;
        }
    }
    printf("%d\n", max);
    printf("%d", idx);
    

    return 0;
}