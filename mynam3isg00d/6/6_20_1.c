//This wasn't too bad. Although the code is.
//Part 1

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
    str[strlen(str)-1] = '\0';
    if(strcmp(foundInGroup, "#############################") == 0) {
        strcpy(foundInGroup, str);
    } else {
        for(int i=0;str[i]!='\0' && str[i]!='\n';i++) {
            if(strchr(foundInGroup, str[i]) == NULL) {
                char append[2];
                append[0] = str[i]; append[1] = '\0';
                strcat(foundInGroup, append);
            }
        }
    }
}

//This is useless but for sake of clarity;
void endGroup() {
    gCounter += strlen(foundInGroup);
    strcpy(foundInGroup, "#############################");
}