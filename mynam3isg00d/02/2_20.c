//C, a language used in 2020, does not implicitly support boolean.

#include <stdio.h>

void passwordValidator(int min, int max, char car, char str[]);         //clear function names; no comments needed
void NEWpasswordValidator(int pos1, int pos2, char car, char str[]);
int globCounter1 = 0;
int globCounter2 = 0;

int main() {

    int min, max;
    char car, str[30];

    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp==NULL) return -1;

    while(fscanf(fp, "%d%*c%d %c%*c %s", &min, &max, &car, str) != EOF) {   //insane way of reading the input, but it do be one line
        passwordValidator(min, max, car, str);
        NEWpasswordValidator(min, max, car, str);
    }
    printf("\n***********************\n Valid passwords: %d\n nonono, ACTUAL Valid passwords: %d", globCounter1, globCounter2);
    fclose(fp);
    return 0;
}

void passwordValidator(int min, int max, char car, char str[]) {
    int counter = 0;
    for(int i=0;str[i]!='\0';i++) if(str[i] == car) counter++;
    if(counter <= max && counter >= min) {
        //printf("%s is valid\n", str);
        globCounter1++;
    }
    return;
}

void NEWpasswordValidator(int pos1, int pos2, char car, char str[]) {
    int isValid = -1;                                       //instead of using a boolean, which are not even supported in the
    if(str[pos1-1] == car) isValid = isValid * (-1);        //first place, decided to use an int. this turned out nice, since
    if(str[pos2-1] == car) isValid = isValid * (-1);        //i can just mult by -1 to check if both letters are present
    if (isValid > 0) {                                      //if an even number of letters are present (either 0 or 2, both of which we dont want)
        //printf("%s is valid\n", str);                     //isValid is set to -1, else, by mult only once by -1, it is set to 1 
        globCounter2++;                                     //(which means only one of the two letters is present)
    }
}