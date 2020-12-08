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
int result(operation array[], int accumulator);

int main (){
    int accumulator=0;
    operation array[MAX];
    input(array, MAX);
    accumulator = result(array, accumulator);
    printf ("%d\n", accumulator);
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
        array[i].seen=0;
        error = fgetc(input);
        i++;
    }
    if (i != limit && error != EOF)
        printf("an error may have occured\n");
}

int result(operation array[], int accumulator){
    if(array->seen)
        return(accumulator);
    array->seen = 1;
    if(strcmp(array->op, "nop") == 0)
        return(result(array+1, accumulator));
    if(strcmp(array->op, "acc") == 0)
        return(result(array+1, accumulator + array->value));
    if(strcmp(array->op, "jmp") == 0)
        return(result(array+array->value, accumulator));
    printf("error, program closing\n");
    return 0;
}