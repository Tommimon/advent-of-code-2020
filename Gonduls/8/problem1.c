#include <stdio.h>
#include <string.h>

#define INPUT "input.txt"
#define MAX 654

typedef struct{
    char op[4];
    int value;
}operation;

void input(operation* array, int limit);
void stampa (operation array[], int limit);

int main (){
    operation array[MAX];
    input(array, MAX);
    stampa(array, MAX);
    return 0;
}

void stampa (operation array[], int limit){
    int i;
    for (i=0; i<limit; i++){
        printf("")
    }
}