#include <stdio.h>
#include <string.h>
//Like problem1, but tries, for every nop or jmp, swapping between the 2 and checking index
#define INPUT "./Gonduls/8/input.txt"
#define MAX 654

typedef struct{
    char op[4];
    int value;
    int seen;
}operation;

void input(operation* array);
int result(operation array[], int *accumulator, int index);
int try(operation array[]);
void stampa (operation array[]);

int main (){
    operation array[MAX];
    input(array);
    printf ("%d\n", try(array));
    return 0;
}

void input(operation* array){
    int i, error = 0;
    FILE * input;
    input = fopen(INPUT, "r");
    while (i<MAX && error != EOF){
        fscanf(input, "%s %d", array[i].op, &array[i].value);
        array[i].seen=0;
        error = fgetc(input);
        i++;
    }
    fclose(input);
    if (i != MAX && error != EOF)
        printf("an error may have occured\n");
}

int result(operation array[], int *accumulator, int index){
    if (index==MAX)
        return index;
    if((array+index)->seen)
        return(index);
    (array+index)->seen = 1;
    if(strcmp((array + index)->op, "nop") == 0)
        return(result(array, accumulator, index+1));
    if(strcmp((array + index)->op, "acc") == 0){
        *accumulator=*accumulator + (array + index)->value;
        return(result(array, accumulator, index +1));
    }
    if(strcmp((array + index)->op, "jmp") == 0){
        return(result(array, accumulator, index + (array+index)->value));
    }
    printf("error, program closing\n");
    return 0;
}

int try(operation array[]){
    int i, j;
    int accumulator;
    for (i=0; i<MAX; i++){
        accumulator=0;
        for (j=0; j<MAX; j++)
            (array+j)->seen=0;
        if(strcmp((array + i)->op, "nop") == 0){
            strcpy((array + i)->op, "jmp");
            if(result(array, &accumulator, 0) == MAX)
                return accumulator;
            strcpy((array + i)->op, "nop");
        }
        if(strcmp((array + i)->op, "jmp") == 0){
            strcpy((array + i)->op, "nop");
            if(result(array, &accumulator, 0) == MAX)
                return accumulator;
            strcpy((array + i)->op, "jmp");
        }
    }
    printf("Error occured, no nop or jmp eligeble\n");
    return 0;
}