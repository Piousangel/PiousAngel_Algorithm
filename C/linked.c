#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    
    struct Node *next;
    int data;
} node;

int main(){

    node *head = malloc(sizeof(node));

    node *node1 = malloc(sizeof(node));
    head -> next = node1;
    node1 -> data = 10;

    node *node2 = malloc(sizeof(node));
    node1 -> next = node2;
    node2 -> data = 20;

    node *curr = head -> next;
    while(curr != NULL){

        printf("%d\n", curr->data);
        curr = curr -> next;
    }
    free(head);
    free(node1);
    free(node2);
    
    return 0;
}