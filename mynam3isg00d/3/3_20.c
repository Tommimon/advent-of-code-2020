//I'm remaking it even shorter later, motherfuckers

#include<stdio.h>
#define DIMX 31
#define DIMY 323

char map[DIMY][DIMX];
int teamTrees(int xInc, int yInc);

int main() {

    FILE *fp;
    fp = fopen("input.txt", "r");

    int i = 0;
    while(fscanf(fp, "%s", map[i])!=EOF) i++;   //fscanf sucks for this, it doesn't even break the lines, but it works so who cares

    printf("1,1: %d\n", teamTrees(1, 1));
    printf("3,1 (part 1 solution): %d\n", teamTrees(3, 1));
    printf("5,1: %d\n", teamTrees(5, 1));
    printf("7,1: %d\n", teamTrees(7, 1));
    printf("1,2: %d\n", teamTrees(1, 2));

    long int res = teamTrees(1, 1) * teamTrees(3, 1) * teamTrees(5, 1) * teamTrees(7, 1) * teamTrees(1, 2);
    printf("--------\nFinal result: %ld", (long) res);  //this shit fucking works but how the FUCK do you print a long

    system("PAUSE");
    fclose(fp);
    return 0;
}

int teamTrees(int xInc, int yInc) {
    int x, y, gCounter;
    x = y = gCounter = 0;
    while(y<DIMY) {
        if(map[y][x] == '#') gCounter++;
        x += xInc;
        if(x>=DIMX) x-=DIMX;
        y += yInc;
    }
    return gCounter;
}
