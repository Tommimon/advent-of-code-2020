#include <stdio.h>
#include <stdlib.h>

#define LENGHT 31
#define HIGHT 323
#define INPUT "input.txt"

char matrix[HIGHT][LENGHT];
int rows;

void init(){
    FILE* input;
    input = fopen(INPUT, "r");
    
    for (rows=0;rows<HIGHT; rows++){
        fscanf(input,"%s",&(matrix[rows][0]));
    }
    fclose(input);
}

int main(){
    int result=0;
    int columns=0;
    init();
    for (rows=0;rows<HIGHT; rows++){
        if(matrix[rows][columns] == '#')
            result++;
        columns += 3;
        if (columns >= LENGHT)
            columns -= LENGHT;
    }
    printf("Trees: %d\n", result);
    return 0;
}