//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 07/12/20.
//

#include <stdio.h>
#include <string.h>
#include <math.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_7/AoC/AoC/input.c"
#define LUNG 150
#define ALT 594 //9 prova, 594 input
#define DIM 50
#define ALT_SEARCH 1000

int DAY7_1(char search[ALT_SEARCH][DIM], char rules[ALT][LUNG]);
int DAY7_2(char search[ALT_SEARCH][DIM], char rules[ALT][LUNG]);

void InizMat(char mat[ALT][LUNG]);
void StampaMat(char mat[ALT][LUNG]);
void CreaCamp(char camp[ALT_SEARCH][DIM], char color[DIM], int row);

int main() {
    char rules[ALT][LUNG];
    char campione[ALT_SEARCH][DIM];
    int result;
    
    CreaCamp(campione, "shinygold", 0);
    InizMat(rules);
    result = DAY7_2(campione, rules);
    printf("\nIl risultato è: %d\n", result);
    return 0;
}

int DAY7_1(char search[ALT_SEARCH][DIM], char rules[ALT][LUNG]){
    int div;
    int index;
    int colors;
    int row;
    int countCopy;
    int rowSearch;
    int count;
    char newSearch[DIM];
    int valid[ALT];
    
    for(index=0; index<ALT; index++){
        valid[index] = 0;
    }
    
    colors = 0;
    rowSearch = 0;
    count = 0;
    while(count<=rowSearch){
        for(row=0;row<ALT;row++){
            if((valid[row]==0)&&(NULL!=strstr(rules[row], search[count]))){
                div = 0;
                for(int i=0; search[count][i]!='\0';i++){
                    if(search[count][i]!=rules[row][i]) div++;
                }
                if(div!=0){
                    colors++;
                    valid[row] = 1;
                    //Condizione pietosa ma funzionale
                    countCopy = 0;
                    while((rules[row][countCopy]!='b')||(rules[row][countCopy+1]!='a')||(rules[row][countCopy+2]!='g')||(rules[row][countCopy+3]!='s')){
                        newSearch[countCopy] = rules[row][countCopy];
                        countCopy++;
                    }
                    newSearch[countCopy] = '\0';
                    CreaCamp(search, newSearch, ++rowSearch);
                }
            }
        }
        count++;
    }
    return colors;
}

int DAY7_2(char search[ALT_SEARCH][DIM], char rules[ALT][LUNG]){
    int div;
    int index;
    int sum;
    int row;
    int countCopy;
    int rowSearch;
    int count;
    int check;
    char newSearch[DIM];
    int num[ALT_SEARCH];
    
    for(index=0; index<ALT_SEARCH; index++){
        num[index] = 0;
    }
    
    sum = 0;
    rowSearch = 0;
    count = 0;
    num[0] = 1;
    while(count<=rowSearch){
        for(row=0;row<ALT;row++){
            if(NULL!=strstr(rules[row], search[count])){
                div = 0;
                for(int i=0; search[count][i]!='\0';i++){
                    if(search[count][i]!=rules[row][i]) div++;
                }
                if(div==0){
                    check = 0;
                    for(int i=0; rules[row][i]!='.';i++){
                        if((rules[row][i]>='1')&&(rules[row][i]<='9')){
                            rowSearch++;
                            num[rowSearch] = num[count] * (rules[row][i]-'0');
                            printf("-%d = %d * %d -\n", num[rowSearch], (rules[row][i]-'0'), num[count]);
                            //Condizione pietosa ma funzionale
                            countCopy = i;
                            while((rules[row][countCopy+1]!='b')||(rules[row][countCopy+2]!='a')||(rules[row][countCopy+3]!='g')){
                                newSearch[countCopy-i] = rules[row][countCopy+1];
                                countCopy++;
                            }
                            newSearch[countCopy-i] = '\0';
                            CreaCamp(search, newSearch, rowSearch);
                            check = 1;
                        }
                    }
                }
            }
        }
        sum = sum + num[count];
        count++;
    }
    sum--;
    return sum;
}

void CreaCamp(char camp[ALT_SEARCH][DIM], char color[DIM], int row){
    int c;
    c = 0;
    while(color[c]!='\0'){
        camp[row][c] = color[c];
        c++;
    }
    camp[row][c] = '\0';
}

void InizMat(char mat[ALT][LUNG]){
    int row;
    int col;

    char charLet;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    row = 0;
    col = 0;
    while((fscanf(pFile, "%c", &charLet))!=EOF){
        if(charLet==' '){
        }else if(charLet=='\n'){
            mat[row][col] = '\0';
            col = 0;
            row++;
        }else{
            mat[row][col] = charLet;
            col++;
        }
    }
}

void StampaMat(char mat[ALT][LUNG]){
    int row;
    printf("\n");
    for(row=0;row<ALT;row++){
        printf("%s\n", mat[row]);
    }
}
