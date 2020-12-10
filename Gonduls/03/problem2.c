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
    int i=0;
    int columns[5];
    long int trees[5];
    for (i=0; i<5; i ++){
        columns[i]=0;
        trees[i]=0;
    }
    init();
    for (rows=0;rows<HIGHT; rows++){
        if(matrix[rows][columns[0]] == '#')
            trees[0]++;
        if(matrix[rows][columns[1]] == '#')
            trees[1]++;
        if(matrix[rows][columns[2]] == '#')
            trees[2]++;
        if(matrix[rows][columns[3]] == '#')
            trees[3]++;
        if((rows+2)%2==0){
            if (matrix[rows][columns[4]] == '#')
                trees[4]++;
            columns[4] += 1;
        }
        
        columns[0] += 1;
        columns[1] += 3;
        columns[2] += 5;
        columns[3] += 7;
        for (i=0; i<5; i ++){
            if (columns[i] >= LENGHT)
                columns[i] -= LENGHT;
        }
        
    }
    printf("Trees 0: %ld\n", trees[0]);
    printf("Trees 1: %ld\n", trees[1]);
    printf("Trees 2: %ld\n", trees[2]);
    printf("Trees 3: %ld\n", trees[3]);
    printf("Trees 4: %ld\n", trees[4]);
    printf("Trees: %ld\n", trees[0]*trees[1]*trees[2]*trees[3]*trees[4]);
    return 0;
}