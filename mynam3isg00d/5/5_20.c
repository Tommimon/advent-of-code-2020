//Result after spending a good 15 minutes on a sorting algorithm that is now gone

#include<stdio.h>
#define DIM 837 //magic of word editor

int findID(char str[], int lrm, int hrm, int lcm, int hcm);
int arrayID[DIM]; 
void sortArray(int arr[], int rep);

int main() {

    char strg[11];
    int max, i;
    max = i = 0;
    FILE *fp = fopen("input.txt", "r");
    while(fscanf(fp, "%s", strg) != EOF) {
        arrayID[i] = findID(strg, 0, 127, 0, 7);
        if (arrayID[i] > max) max = arrayID[i];
        i++; 
    }

    int flagFound = 0;
    for(i=0;i<DIM;i++) {
        if(arrayID[i] != max) {
            for(int j=0;j<DIM;j++) {
                if (arrayID[i]+1 == arrayID[j]) {
                    flagFound = 1;
                    break;
                }
            }
            if (flagFound == 0) break;
            flagFound = 0;
        }
    }
    printf("Missing seat: %d\n", arrayID[i]+1);
    printf("Max ID: %d", max);

    fclose(fp);
    return 0;
}

int findID(char str[], int lrm, int hrm, int lcm, int hcm) {
    if (*str == '\0') return((lrm*8)+lcm);
    if (*str == 'B') lrm = lrm + ((hrm - lrm)/2 + 1);
    if (*str == 'F') hrm = hrm - ((hrm - lrm)/2 + 1);
    if (*str == 'R') lcm = lcm + ((hcm - lcm)/2 + 1);
    if (*str == 'L') hcm = hcm - ((hcm - lcm)/2 + 1);
    findID(str+1, lrm, hrm, lcm, hcm);
}