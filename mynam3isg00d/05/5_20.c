//-----------------WARNING-----------------------
//The following script only works in windows because I am too lazy to make it compatible for
//other (fairly unpopular) OS.

//Result after spending a good 15 minutes on a sorting algorithm that is now gone.

//Another 18 hours later and we also got feedback! The exe opens up a fairly simple
//ASCII visualisation of the boarding.

//PS: While I do realize now (thanks tommy boy) that the seat encoding is just 
//a convoluted binary notation, it's far too late to change it and furthermore
//i'm not really sure that a c implementation of the algorithm would be shorter than this.

#include<stdio.h>
#include<stdlib.h>
#include <windows.h>    //I'm sure there's a library that supports
                        //linux, but it's not really important to 
                        //support linux, let's be honest
                        
#define DIM 837 //magic of word editor

int findID(char str[], int lrm, int hrm, int lcm, int hcm);
int arrayID[DIM]; int coords[2];
char seats[8][128];
void printPlane();

int main() {

    char strg[11];
    int max, i;
    max = i = 0;

    //Inizialize Seats.
    for(int i=0;i<8;i++) {
        for(int j=0;j<128;j++) {
            seats[i][j] = '.';
        }
    }

    //read lines from file and into findID, also prints the plane.
    FILE *fp = fopen("input.txt", "r");
    while(fscanf(fp, "%s", strg) != EOF) {
        arrayID[i] = findID(strg, 0, 127, 0, 7);
        printPlane(coords);
        if (arrayID[i] > max) max = arrayID[i];
        i++; 
    }

    //What I find a rudimental way of finding the missing seat.
    int flagFound = 0;
    for(i=0;i<DIM;i++) {    
        if(arrayID[i] != max) {                     //key line, otherwise it just prints the max since
            for(int j=0;j<DIM;j++) {                //of course, the next one is missing.
                if (arrayID[i]+1 == arrayID[j]) {
                    flagFound = 1;
                    break;
                }
            }
            if (flagFound == 0) break;
            flagFound = 0;
        }
    }

    printf("\nMissing seat: %d\nMax ID: %d", arrayID[i]+1, max);

    system("pause");
    fclose(fp);
    return 0;
}

//Finds the ID...yes i didn't notice the binary.
int findID(char str[], int lrm, int hrm, int lcm, int hcm) {
    if (*str == '\0') {
        coords[0] = lrm;
        coords[1] = lcm;
        return((lrm*8)+lcm);
    }
    if (*str == 'B') lrm = lrm + ((hrm - lrm)/2 + 1);
    if (*str == 'F') hrm = hrm - ((hrm - lrm)/2 + 1);
    if (*str == 'R') lcm = lcm + ((hcm - lcm)/2 + 1);
    if (*str == 'L') hcm = hcm - ((hcm - lcm)/2 + 1);
    findID(str+1, lrm, hrm, lcm, hcm);
}

//prints the plane, it's fairly simple.
void printPlane(int coords[]) {
    system("cls");
    seats[coords[1]][coords[0]] = '#';

    for(int i=0;i<8;i++) {
        for(int j=0;j<128;j++) {
            if(j%32==0) printf(" ");
            printf("%c", seats[i][j]);
        }
        printf("\n");
        if(i == 1 || i == 5) printf("\n");
    }
    Sleep(5);
}