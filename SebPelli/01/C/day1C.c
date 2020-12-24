#include <stdio.h>
#include <stdlib.h>
#define DIM 200

int main() {
    int i, j, k;
    int exiter = 0; //I use this to exit the first cycle. Not a great programming practice
    int array[DIM+1];
    FILE *fp = fopen("/Users/sebastianpelli/Desktop/Advent/day2020.txt", "r");

    if (fp == NULL){
        printf("File couldn't be opened.\n");
        exit(1);
    }

    for (i = 0; i <= DIM; i++){
        fscanf(fp, "%d", &array[i]);
    }

    /*** PART ONE: ***/

    for(i = 0; i <= DIM; i++){
       if (exiter == 1)
           break;
        for (j = 0; j <= DIM; j++){
            if ((array[i]+array[j]) == 2020){
                printf("Solution is: %d\n", array[i] * array[j]);
                exiter = 1;
            }
        }
    }

    /*** PART TWO: ***/

    for(i = 0; i <=DIM; i++){
        for (j = 0; j <= DIM; j++){
            for (k = 0; k <= DIM; k++){
                if((array[i] + array[j] + array[k]) == 2020){
                    printf("Solution is: %d\n", array[i] * array[j] * array[k]);
                    return 0;
                }
            }
        }
    }

    return 0;
}
