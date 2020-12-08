#include <stdio.h>
#include <string.h>

#define INPUT "input.txt"
#define MAX 654

typedef struct{
    char op[4];
    int value;
    int seen;
}operation;

void input(operation* array, int limit);
//void stampa (operation array[], int limit);

int main (){
    operation array[MAX];
    input(array, MAX);
    //stampa(array, MAX);
    return 0;
}

/*void stampa (operation array[], int limit){
    int i;
    for (i=0; i<limit; i++){
        printf("%s %d\n", array[i].op, array[i].value);
    }
}
*/

void input(operation* array, int limit){
    int i, error = 0;
    FILE * input;
    input = fopen(INPUT, "r");
    while (i<limit && error != EOF){
        fscanf(input, "%s %d", array[i].op, &array[i].value);
        error = fgetc(input);
        i++;
    }
    if (i != limit && error != EOF)
        printf("an error may have occured\n");
}