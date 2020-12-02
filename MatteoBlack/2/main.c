//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 02/12/20.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_2/AoC/AoC/input.txt"
#define LUNGHEZZA 100

//Funz DAY2_1, legge quante volte compare una lettera
int DAY2_1(FILE* pFileElab);
//Funz DAY2_2, legge se la lettera compare una volat nelle pos
int DAY2_2(FILE* pFileElab);

int main() {
    int result;
    FILE* pFile;
    
    pFile = NULL;
    result = DAY2_2(pFile);
    printf("\nIl num di pwd è: %d\n", result);
    
    return 0;
}

int DAY2_1(FILE* pFileElab){
    int counterPwd;
    int countChar;
    int c;
    int min;
    int max;
    char campione;
    char pwd[LUNGHEZZA];
    
    counterPwd = 0;
    
    pFileElab = fopen(NOMEFILE, "r");
    if(pFileElab == NULL){
        printf("Errore in APERTURA");
    }else{
        //Fai lettura !!vincolata!! alla formattazione del file...
        while((fscanf(pFileElab, "%d-%d %c: %s", &min, &max, &campione, pwd))!=EOF){
            c = 0;
            countChar = 0;
            while(pwd[c]!='\0'){
                if(pwd[c]==campione){
                    countChar++;
                }
                c++;
            }
            if((countChar<=max)&&(countChar>=min)){
                counterPwd++;
            }
        }
    }
    fclose(pFileElab);
    return counterPwd;
}

int DAY2_2(FILE* pFileElab){
    int counterPwd;
    int c;
    int pos_1;
    int pos_2;
    int valid;
    char campione;
    char pwd[LUNGHEZZA];
    
    counterPwd = 0;
    
    pFileElab = fopen(NOMEFILE, "r");
    if(pFileElab == NULL){
        printf("Errore in APERTURA");
    }else{
        //Fai lettura vincolata alla formattazione del file...
        while((fscanf(pFileElab, "%d-%d %c: %s", &pos_1, &pos_2, &campione, pwd))!=EOF){
            c = 0;
            valid = 0;
            pos_1--;
            pos_2--;
            while(pwd[c]!='\0'){
                if((c==pos_1)||(c==pos_2)){
                    if(pwd[c]==campione){
                        valid++;
                    }
                }
                c++;
            }
            if(valid==1){
                counterPwd++;
            }
        }
    }
    fclose(pFileElab);
    return counterPwd;
}
