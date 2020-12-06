//This wasn't too bad. Although the code is.
//Part 2

#include<stdio.h>
#include<string.h>

char foundInGroup[30] = "#############################";  //Bruteforcy eh? If you find a better way i'll gladly implement
int gCounter = 0;

void countLetters(char str[]);
void endGroup();                                        

int main() {
    char str[50];
    FILE *fp = fopen("input.txt", "r");
    
    while(fgets(str, 50, fp) != NULL) {
        if(*str=='\n') {
            endGroup();
        } else {
            countLetters(str);
        }
    }
    endGroup();
    printf("gCounter = %d", gCounter);

    fclose(fp);
    return 0;
}

void countLetters(char str[]) {
    if(strcmp(foundInGroup, "#############################") == 0) {
        strcpy(foundInGroup, str);
    } else {
        for(int i=0;foundInGroup[i]!='\0' && foundInGroup[i]!='\n';i++) {
            if(strchr(str, foundInGroup[i]) == NULL) foundInGroup[i] = '#';
        }
    }
}

void endGroup() {
    int res = 0;
    for(int i=0;foundInGroup[i]!='\0' && foundInGroup[i]!='\n';i++) {
        if(foundInGroup[i]!='#') res++;
    }
    gCounter += res;
    strcpy(foundInGroup, "#############################");
}