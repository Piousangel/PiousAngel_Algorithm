#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    struct NODE *next;
    int data;
} node;

int main(){

    node *head = malloc(sizeof(node)); //머리노드 생성, 머리노드는 데이터를 저장하지않음

    node *node1 = malloc(sizeof(node));
    head -> next = node1;
    node1 -> data = 10;

    node *node2 = malloc(sizeof(node));
    node1 -> next = node2;
    node2 -> data = 20;
    node2 -> next = NULL;

    node *curr = head -> next;

    while(curr != NULL){
        printf("%d\n", curr->data);
        curr = curr->next;
    }

    free(node2);
    free(node1);
    free(head);

    return 0;
}