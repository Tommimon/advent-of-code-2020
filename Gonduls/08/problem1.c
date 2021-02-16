#include <stdio.h>
#include <string.h>
//I'm sorry for the lack of comments, I couldn't bother. But I can briefly explain the program here:
//input -> main -> result. Result just executes the three rules in a recursive manner,
//always passing the next rule and with that deciding what happens next
#define INPUT "./Gonduls/8/input.txt"
#define MAX 654

typedef struct{
    char op[4];
    int value;
    int seen;
}operation;

void input(operation* array);
int result(operation array[], int accumulator);

int main (){;
    operation array[MAX];
    input(array);
    printf ("%d\n", result(array, 0));
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