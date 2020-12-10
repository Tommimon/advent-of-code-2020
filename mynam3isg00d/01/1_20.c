//Brute force gang; no comments needed

#include <stdio.h>
#define DIM 200

int arr[DIM];
int input;
int output;

void solvePartOne();
void solvePartTwo();

int main() {

    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp==NULL) return -1;

    int i = 0;
    while(fscanf(fp, "%d", &arr[i]) != EOF) i++;

    solvePartOne();
    solvePartTwo();

    fclose(fp);
    return 0;

}

void solvePartTwo() {

    //THREE nested fors lol

    for(int stat1 = 0; stat1 < DIM; stat1++) {
        for(int stat2 = stat1+1; stat2 < DIM; stat2++) {
            for(int move = stat2+1; move < DIM; move++) {
                if(arr[stat1] + arr[stat2] + arr[move] == 2020) {
                    output = arr[stat1] * arr[stat2] * arr[move];
                    break;
                }
            }
        }
    }

    printf("Output2: %d\n", output);
}

void solvePartOne() {

    for(int stat = 0; stat < DIM; stat++) {
        for(int move = stat+1; move < DIM; move++) {
            if (arr[stat] + arr[move] == 2020) {
                output = arr[stat]*arr[move];
                break;
            }
        }
    }

    printf("Output1: %d\n", output);
}