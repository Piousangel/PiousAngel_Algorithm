#include <stdio.h>

int add(int a, int b){
    return a+b;
}

int mul(int a, int b){
    return a*b;
}

int main(){

    int (*fp)(int, int);
    //int형 반환값과 int형 매개변수 두 개를 가지고 있는 add, mul 함수를 저장할 것이므로 함수 포인터를 선언할 때 반환값은 int로 지정하고, 
    //맨 뒤의 괄호 안에는 int를 두 개 넣어줍니다. 이때 매개변수의 자료형만 알려주면 되므로 매개변수의 이름은 지정하지 않아도 됩니다.

    fp = add;
    printf("%d\n", fp(10,20));

    fp = mul;
    printf("%d\n", fp(10,20));

    return 0;
}