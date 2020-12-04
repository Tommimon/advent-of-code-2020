//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 04/12/20.
//
//Piccola modifica al file, ho inserito un a capo all'ultima riga
#include <stdio.h>
#include <math.h>
#include <string.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_4/AoC/AoC/input.txt"
#define DIM 25

//Funz DAY4_1, cerca due val che sommati facciano 2020 e moltiplicali tra loro
int DAY4_1(void);
//Funz DAY1_2, cerca tre val che sommati facciano 2020 e moltiplicali tra loro
int DAY4_2(void);

int main() {
    int result;
    
    result = DAY4_2();
    printf("\nIl risultato è: %d\n", result);
    
    return 0;
}

int DAY4_1(){
    char temp[DIM];
    int countField;
    int countPass;
    int c;
    int valid;
    char charLet;
    
    FILE* pFile;
    pFile = fopen(NOMEFILE, "r");
    
    c = 0;
    valid = 0;
    countPass = 0;
    countField = 0;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if((charLet=='\n')||(charLet==' ')){
            if(charLet=='\n') valid++;
            temp[c] = '\0';
            if('b'==temp[0]) countField++;
            if('i'==temp[0]) countField++;
            if('e'==temp[0]) countField++;
            if('h'==temp[0]) countField++;
            if('p'==temp[0]) countField++;
            printf("%s ", temp);
            c = 0;
        }else{
            temp[c] = charLet;
            valid = 0;
            c++;
        }
        if(valid == 2){
            if(countField==7){
                countPass++;
            }
            c = 0;
            valid = 0;
            countField = 0;
            printf("\n\n");
        }
    }
    if(countField==7){
        countPass++;
    }
    return countPass;
}

int DAY4_2(){
    char temp[DIM];
    int countField;
    int countPass;
    char charLet;
    int valid;
    int num;
    int c;
    int i;
    int control;
    char campione[4];
    
    FILE* pFile;
    pFile = fopen(NOMEFILE, "r");
    
    c = 0;
    num = 0;
    valid = 0;
    countPass = 0;
    countField = 0;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if((charLet=='\n')||(charLet==' ')){
            if(charLet=='\n') valid++;
            temp[c] = '\0';
            //Controllo su Birth Year
            if('b'==temp[0]){
                num = 0;
                for(i=7; i>3; i--){
                    num = num + (temp[i]-'0')*(pow(10, (7-i)));
                }
                if((num>=1920)&&(num<=2002)) countField++;
            }
            //Controllo su Issue Year
            if('i'==temp[0]){
                num = 0;
                for(i=7; i>3; i--){
                    num = num + (temp[i]-'0')*(pow(10, (7-i)));
                }
                if((num>=2010)&&(num<=2020)) countField++;
            }
            if('e'==temp[0]){
                //Controllo su Expiration Year
                if('y'==temp[1]){
                    num = 0;
                    for(i=7; i>3; i--){
                        num = num + (temp[i]-'0')*(pow(10, (7-i)));
                    }
                    if((num>=2020)&&(num<=2030)) countField++;
                }else{
                    //Controllo su Eye Color
                    for(i=4; i<=6; i++){
                        campione[i-4] = temp[i];
                    }
                    campione[3] = '\0';
                    if(strcmp("amb\0",campione)==0) countField++;
                    else if(strcmp("blu\0",campione)==0) countField++;
                    else if(strcmp("brn\0",campione)==0) countField++;
                    else if(strcmp("gry\0",campione)==0) countField++;
                    else if(strcmp("grn\0",campione)==0) countField++;
                    else if(strcmp("hzl\0",campione)==0) countField++;
                    else if(strcmp("oth\0",campione)==0) countField++;
                }
            }
            if('h'==temp[0]){
                //Controllo su Height
                if('g'==temp[1]){
                    if(temp[c-1]=='n'){
                        num = 0;
                        for(i=c-3; i>3; i--){
                            num = num + (temp[i]-'0')*(pow(10.0, (c-i-3)));
                        }
                        if((num>=59)&&(num<=76)) countField++;
                    }else if(temp[c-1]=='m'){
                        if(temp[c-1]=='m'){
                            num = 0;
                            for(i=c-3; i>3; i--){
                                num = num + (temp[i]-'0')*(pow(10.0, (c-i-3)));
                            }
                            if((num>=150)&&(num<=193)) countField++;
                        }
                    }
                }else{
                    //Controllo su Hair Color
                    if(('#'==temp[4])&&('\0'==temp[11])){
                        control = 0;
                        for(i=5; i<=10; i++){
                            if(((temp[i]>='0')&&(temp[i]<='9'))||((temp[i]>='a')&&(temp[i]<='f'))){
                                control++;
                            }
                        }
                        if(control==6)countField++;
                    }
                }
                
            }
            //Controllo su Passport ID
            if('p'==temp[0]){
                control = 0;
                for(i=4; i<13; i++){
                    if((temp[i]<'0')||(temp[i]>'9')) control++;
                }
                if(('\0'==temp[13])&&(control==0)){
                    countField++;
                }
            }
            printf("%s ", temp);
            c = 0;
        }else{
            temp[c] = charLet;
            valid = 0;
            c++;
        }
        if(valid == 2){
            if(countField==7){
                countPass++;
            }
            c = 0;
            valid = 0;
            countField = 0;
            printf(" \n\n");
        }
    }
    if(countField==7){
        countPass++;
    }
    return countPass;
}
