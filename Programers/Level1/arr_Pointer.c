#include <stdio.h>

// 배열을 인자로 받는 방법 -> 배열의 주소값을 포인터로 받아서 진행
// c언어는 객체지향 x 절차적이라서 첨에 함수 프로토타입 선언해야 뒤에 작성할 수 있다.
void add_number(int *parr);

int main() {
    int arr[3];
   
    for(int i = 0; i < 3; i++) {
        scanf("%d", &arr[i]);
    }
    add_number(arr);
    printf("배열의 각 원소 : %d, %d, %d", arr[0], arr[1], arr[2]);
    return 0;
}

void add_number(int *parr) {
    for(int i=0; i < 3; i++){
        parr[i]++;
    }
}