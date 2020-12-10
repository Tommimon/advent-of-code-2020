//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 08/12/20.
//

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_8/AoC/AoC/input.c"
#define LUNG 20
#define ALT 654 //prova: 9, vera: 654

#include <stdio.h>
#include <math.h>
#include <string.h>

void leggiFILE(char list[ALT][LUNG]);
int DAY8_1(char list[ALT][LUNG]);
int DAY8_2(char list[ALT][LUNG]);

int main() {
    char list[ALT][LUNG];
    int NUM[ALT];
    int result;
    
    NUM[2] = 1;
    leggiFILE(list);
    result  = DAY8_2(list);
    printf("\nIl num è: %d\n", result);
    return 0;
}

int DAY8_1(char list[ALT][LUNG]){
    int sum;
    int row;
    int num;
    int stop;
    int segno;
    int NUM[ALT];
    int valid[ALT];
    
    for(int i=0; i<ALT; i++){
        valid[i] = 0;
    }
    
    segno = 1;
    row = 0;
    while(row<ALT){
        printf("%s\n", list[row]);
        num = 0;
        stop = 0;
        for(int i = 0; stop==0; i++){
            if(list[row][i]=='+'){
                segno = 1;
                stop = 1;
            }else if(list[row][i]=='-'){
                segno = -1;
                stop = 1;
            }
            if(stop==1){
                for(int c=(strlen(list[row])-1); (list[row][c]!='+')&&(list[row][c]!='-'); c--){
                    printf("\n-%d + %d*10^%d-", num, list[row][c]-'0', (strlen(list[row])-1-c));
                    num = num + (list[row][c]-'0')*(pow(10, (strlen(list[row])-1-c)));
                }
            }
            
        }
        NUM[row] = num * segno;
        row++;
    }
    
    sum = 0;
    stop = 0;
    row = 0;
    while(stop==0){
        if(valid[row]==0){
            valid[row] = 1;
            if(list[row][0]=='a'){
                //ACC
                sum = sum + NUM[row];
                row++;
            }else if(list[row][0]=='j'){
                //JUMP
                row = row + NUM[row];
            }else{
                //NOP
                row++;
            }
        }else{
            stop = 1;
        }
    }
    return sum;
}

int DAY8_2(char list[ALT][LUNG]){
    int sum;
    int row;
    int num;
    int stop;
    int segno;
    int first;
    int condizione;
    int NUM[ALT];
    int valid[ALT];
    int test[ALT];
    
    for(int i=0; i<ALT; i++){
        valid[i] = 0;
        test[i] = 0;
    }
    
    segno = 1;
    row = 0;
    while(row<ALT){
        num = 0;
        stop = 0;
        for(int i = 0; stop==0; i++){
            if(list[row][i]=='+'){
                segno = 1;
                stop = 1;
            }else if(list[row][i]=='-'){
                segno = -1;
                stop = 1;
            }
            if(stop==1){
                for(int c=(strlen(list[row])-1); (list[row][c]!='+')&&(list[row][c]!='-'); c--){
                    num = num + (list[row][c]-'0')*(pow(10, (strlen(list[row])-1-c)));
                }
            }
        }
        NUM[row] = num * segno;
        row++;
    }
    
    sum = 0;
    condizione = 0;
    while(condizione==0){
        first = 0;
        sum = 0;
        stop = 0;
        row = 0;
        
        for(int i=0; i<ALT; i++){
            valid[i] = 0;
        }
        
        while((stop==0)&&(row<ALT)){
            if(valid[row]==0){
                valid[row] = 1;
                if(list[row][0]=='a'){
                    //ACC
                    sum = sum + NUM[row];
                    row++;
                }else if(list[row][0]=='j'){
                    //JMP
                    if((first==0)&&(test[row]!=2)){
                        //TRASFORMO IN UNA NOP
                        first = 1;
                        test[row] = 2;
                        row++;
                    }else{
                        row = row + NUM[row];
                    }
                }else{
                    //NOP
                    if((first==0)&&(test[row]!=2)){
                        //TRASFORMO IN UNA JMP
                        first = 1;
                        test[row] = 2;
                        row = row + NUM[row];
                    }else{
                        row++;
                    }
                }
            }else{
                stop = 1;
            }
        }
        if(stop==0){
            condizione = 1;
        }
    }
    return sum;
}


void leggiFILE(char list[ALT][LUNG]){
    int row;
    int col;
    char charLet;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    row = 0;
    col = 0;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet=='\n'){
            list[row][col] = '\0';
            col = 0;
            row++;
        }else{
            list[row][col] = charLet;
            col++;
        }
    }
}
