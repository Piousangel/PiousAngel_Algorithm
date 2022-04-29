#include <stdio.h>

int main() {
    int a, b;
    int arr[3][4] = { 0, };       // 2차원 배열의 요소를 모두 0으로 초기화
    scanf("%d %d", &a, &b);
    // printf("%d", a+b);

    int col = sizeof(arr[0]) / sizeof(int);    
    int row = sizeof(arr) / sizeof(arr[0]);
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            printf("%d ", arr[i][j]);
        }
        printf(" \n");
    }
    return 0;
}