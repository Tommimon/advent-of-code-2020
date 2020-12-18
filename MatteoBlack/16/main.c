//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 16/12/20.
//

#include <stdio.h>
#define NOME_RULES "/Users/matteoblack/Desktop/AoC/AoC_16/AoC/AoC/rules.txt"
#define NOME_NEARBY "/Users/matteoblack/Desktop/AoC/AoC_16/AoC/AoC/nearby.txt"
#define NOME_TICKET "/Users/matteoblack/Desktop/AoC/AoC_16/AoC/AoC/ticket.txt"
#define ROW_RULES 20
#define NOT_VALID 51 //Da funz 1 51
#define DIM_VALID 190
#define ROW_NEARBY 241


typedef struct{
    int colonna;
    int min1;
    int min2;
    int max1;
    int max2;
} Rules;

void readRules(Rules list[ROW_RULES]);
long int DAY16_1(Rules list[ROW_RULES]);
long long int DAY16_2(Rules list[ROW_RULES]);

int main(){
    Rules list[ROW_RULES];
    readRules(list);
    
    printf("num: %lld\n", DAY16_2(list));
    
    return 0;
}

long int DAY16_1(Rules list[ROW_RULES]){
    long int sum;
    int num;
    int valid;
    int check;
    FILE* pFile;

    sum = 0;
    valid = 0;
    pFile = fopen(NOME_NEARBY, "r");
    while(fscanf(pFile, "%d,", &num)!=EOF){
        check = 0;
        for(int i=0; i<ROW_RULES; i++){
            if(((list[i].min1<=num)&&(list[i].max1>=num))||((list[i].min2<=num)&&(list[i].max2>=num))) check = 1;
        }
        if(check==0){
            sum = sum + num;
            valid++;
        }
    }
    printf("Inizializza Array a: %d", valid);
    return sum;
}

long long int DAY16_2(Rules list[ROW_RULES]){
    long long int prod;
    int j;
    int num;
    int find;
    int check;
    int count;
    int search;
    int CheckRules;
    int campi[ROW_RULES];
    int myTicket[ROW_RULES];
    int NotValidNum[NOT_VALID];
    int valid[DIM_VALID][ROW_RULES];
    FILE* pFile;
    FILE* pFileTick;
    
    //mi salvo i val che non vanno
    j = 0;
    check = 0;
    pFile = fopen(NOME_NEARBY, "r");
    while(fscanf(pFile, "%d,", &num)!=EOF){
        check = 0;
        for(int i=0; i<ROW_RULES; i++){
            if(((list[i].min1<=num)&&(list[i].max1>=num))||((list[i].min2<=num)&&(list[i].max2>=num))) check = 1;
        }
        if(check==0){
            NotValidNum[j] = num;
            j++;
        }
    }
    //mi creo una mat dei  val che vanno
    j = 0;
    count = 0;
    CheckRules = 0;
    pFile = fopen(NOME_NEARBY, "r");
    while(fscanf(pFile, "%d,", &num)!=EOF){
        if(count==ROW_RULES){
            if(CheckRules==0) j++;
            count = 0;
            CheckRules = 0;
        }
        for(int i=0; i<NOT_VALID; i++){
            if(num==NotValidNum[i]) CheckRules = 1;
        }
        valid[j][count] = num;
        count++;
        
    }
    //conrollo regole vanno bene per la colonna c
    pFileTick = fopen(NOME_TICKET, "r");
    j = 0;
    find = 0;
    while(fscanf(pFileTick, "%d,", &num)!=EOF){
        myTicket[j] = num;
        j++;
    }
    
    for(int i=0; i<ROW_RULES; i++) campi[i] = 0;
    
    for(int j=0; j<ROW_RULES; j++){
        find = 0;
        for(int c=0; (c<ROW_RULES); c++){
            find = 0;
            for(int r=0; (r<DIM_VALID); r++){
                if(((list[j].min1<=valid[r][c])&&(list[j].max1>=valid[r][c]))||((list[j].min2<=valid[r][c])&&(list[j].max2>=valid[r][c]))){
                    find++;
                }
            }
            if(find==DIM_VALID){
                campi[c]++;
            }
        }
    }
    //scorro i campi e vedo quali
    for(int i=0; i<ROW_RULES; i++) list[i].colonna = -1;
    
    search = 1;
    while(search!=(ROW_RULES+1)){
        for(int i=0; i<ROW_RULES; i++){
            if(campi[i]==search){
                for(int j=0; j<ROW_RULES; j++){
                    find = 0;
                    for(int r=0; (r<DIM_VALID); r++){
                        if(((list[j].min1<=valid[r][i])&&(list[j].max1>=valid[r][i]))||((list[j].min2<=valid[r][i])&&(list[j].max2>=valid[r][i]))){
                            find++;
                        }
                    }
                    if(find==DIM_VALID){
                        if(list[j].colonna==-1){
                            list[j].colonna = i;
                        }
                    }
                    
                }
                search++;
            }
        }
    }
    //calcolo il prod
    prod = 1;
    for(int i=0; i<6; i++) prod = prod * myTicket[list[i].colonna];
    return prod;
}

void readRules(Rules list[ROW_RULES]){
    int c;
    char charLet;
    FILE* pFile;
    
    c = 0;
    pFile = fopen(NOME_RULES, "r");
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet==':'){
            fscanf(pFile, " %d-%d or %d-%d",  &(list[c].min1), &(list[c].max1), &(list[c].min2), &(list[c].max2));
            c++;
        }
    }
}
