//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 06/12/20.
//
//piccola modifica al File metto un a capo a fine File
#include <stdio.h>
#include <string.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_6/AoC/AoC/input.c"
#define DIM 100 //0-25 lettere + \0

//Funz DAY6_1,
long int DAY6_1(void);
//Funz DAY6_2,
long int DAY6_2(void);

int main() {
    long int result;
    
    result = DAY6_2();
    printf("\nIl risultato è: %ld\n", result);
    
    return 0;
}

long int DAY6_1(){
    char campioni[DIM];
    char charLet;
    long int sum;
    int valid;
    int c;
    int i;
        
    FILE* pFile;
    pFile = fopen(NOMEFILE, "r");
    
    if(pFile==NULL) printf("Errore");
    
    sum = 0;
    valid = 0;
    c = 0;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet=='\n'){
            valid++;
        }else{
            i = 0;
            if(c==0){
                campioni[c] = charLet;
                campioni[c+1] = '\0';
            }else{
                while((campioni[i]!='\0')&&(charLet!=campioni[i])){
                    i++;
                }
                if(campioni[i]=='\0'){
                    campioni[i] = charLet;
                    campioni[i+1] = '\0';
                }
            }
            valid = 0;
            c++;
        }
        if(valid == 2){
            sum = sum + strlen(campioni);
            c = 0;
            campioni[c] = '\0';
            valid = 0;
        }
    }
    sum = sum + strlen(campioni);
    return sum;
}

long int DAY6_2(){
    char campioni[DIM];
    char temp[DIM];
    char charLet;
    long int sum;
    int valid;
    int first;
    int control;
    int c;
    int i;
    int j;
        
    FILE* pFile;
    pFile = fopen(NOMEFILE, "r");
    
    sum = 0;
    valid = 0;
    c = 0;
    first = 1;
    campioni[0] = '\0';
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet=='\n'){
            i = 0;
            if(first==1){
                while(temp[i]!='\0'){
                    campioni[i] = temp[i];
                    i++;
                }
                campioni[i] = '\0';
            }else{
                while((valid==0)&&(campioni[i]!='\0')){
                    j = 0;
                    control = 0;
                    while(temp[j]!='\0'){
                        if(campioni[i]==temp[j]){
                            control = 1;
                        }
                        j++;
                    }
                    if(control==0){
                        j = i;
                        while(campioni[j]!='\0'){
                            campioni[j] = campioni[j+1];
                            j++;
                        }
                        i--;
                    }
                    i++;
                }
            }
            temp[0] = '\0';
            first = 0;
            valid++;
        }else{
            i = 0;
            if(c==0){
                temp[c] = charLet;
                temp[c+1] = '\0';
            }else{
                while((temp[i]!='\0')&&(charLet!=temp[i])){
                    i++;
                }
                if(temp[i]=='\0'){
                    temp[i] = charLet;
                    temp[i+1] = '\0';
                }
            }
            valid = 0;
            c++;
        }
        if(valid == 2){
            sum = sum + strlen(campioni);
            c = 0;
            campioni[c] = '\0';
            valid = 0;
            first = 1;
        }
    }
    sum = sum + strlen(campioni);
    return sum;
}

