#include <stdio.h>
#include <stdlib.h>

int main(void){

    int *list = malloc(3 * sizeof(int));

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    int *tmp = realloc(list, 4 * sizeof(int));
    // int *tmp = malloc(4 * sizeof(int));
    if(tmp == NULL){
        return 1;
    }
    tmp = list;
    tmp[3] = 4; 

    for(int i=0; i < 4; i++){
        printf("%i\n", tmp[i]);
    }

    // free(list)
    free(tmp);

    return 0;
}