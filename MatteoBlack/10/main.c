//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 10/12/20.
//

#include <stdio.h>
#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_10/AoC/AoC/input.c"
#define DIM 110 //prova: 11; prova1: 31; input: 110
#define MAX 10000

void readFILE(int listNUM[DIM]);
int searchSucc(int listNUM[DIM], int val);

int DAY10_1(int listNUM[DIM]);
long long int DAY10_2_BIS(int listNUM[DIM]);
int DAY10_2(int listNUM[DIM], int iniz);

int main() {
    int listNum[DIM];
    long long int input;
    
    readFILE(listNum);
    input = DAY10_2_BIS(listNum);
    printf("\nIl valore è: %lld\n", input);
    
    return 0;
}

int DAY10_1(int listNUM[DIM]){
    int count;
    int result;
    int oneJ;
    int threeJ;
    int find;
    int index;
    int block;
    
    //devo aggiungere uno al counte dei tre per ottenere il val max(per def)
    count = 0;
    result = 0;
    oneJ = 0;
    threeJ = 1;
    block = 0;
    while(count<DIM){
        if((listNUM[count]==1)&&(block==0)){
            oneJ++;
            block = 1;
        }
        else if((listNUM[count]==3)&&(block==0)){
            threeJ++;
            block = 1;
        }
        find = 0;
        index = 0;
        //check +1
        while((find==0)&&(index<DIM)){
            if((listNUM[count]+1)==listNUM[index]){
                oneJ++;
                find = 1;
            }
            index++;
        }
        index = 0;
        //check +3
        while((find==0)&&(index<DIM)){
            if((listNUM[count]+3)==listNUM[index]){
                threeJ++;
                find = 1;
            }
            index++;
        }
        count++;
    }
    result = oneJ * threeJ;
    return result;
}

int DAY10_2(int listNUM[DIM], int iniz){
    int path;
    int count;
    int listOrd[DIM+1];
    
    count = 0;
    for(int c=0; c!=(-1); c=searchSucc(listNUM, c)){
        listOrd[count] = c;
        count++;
    }
    
    path = 0;
    if(iniz==DIM){
        path = 1;
        return path;
    }
    if(((iniz+1)<=DIM)&&((listOrd[iniz]+1)==listOrd[iniz+1])){
        path = path + DAY10_2(listNUM, (iniz+1));
    }
    if(((iniz+1)<=DIM)&&((listOrd[iniz]+2)==listOrd[iniz+1])){
        path = path + DAY10_2(listNUM, (iniz+1));
    }
    if(((iniz+1)<=DIM)&&((listOrd[iniz]+3)==listOrd[iniz+1])){
        path = path + DAY10_2(listNUM, (iniz+1));
    }
    if(((iniz+2)<=DIM)&&((listOrd[iniz]+2)==listOrd[iniz+2])){
        path = path + DAY10_2(listNUM, (iniz+2));
    }
    if(((iniz+2)<=DIM)&&((listOrd[iniz]+3)==listOrd[iniz+2])){
        path = path + DAY10_2(listNUM, (iniz+2));
    }
    if(((iniz+3)<=DIM)&&((listOrd[iniz]+3)==listOrd[iniz+3])){
        path = path + DAY10_2(listNUM, (iniz+3));
    }
    return path;
}

long long int DAY10_2_BIS(int listNUM[DIM]){
    unsigned long long int path;
    int div;
    int count;
    int find;
    int blocco;
    int pathPrec;
    int listOrd[DIM+1];
    long long int contaOcc[DIM+1];

    count = 0;
    for(int c=0; c!=(-1); c=searchSucc(listNUM, c)){
        listOrd[count] = c;
        count++;
    }
    
    for(int c=0; c<=DIM; c++){
        contaOcc[c] = 0;
    }
    
    div = 0;
    path = 1;
    blocco = 0;
    pathPrec = 1;
    contaOcc[0] = 1;
    for(int c=0; c<=DIM; c++){
        find = 0;
        if(blocco<1) blocco = 1;
        //Check succ
        if(((c+1)<=DIM)&&(listOrd[c+1]==listOrd[c]+1)){
            find++;
            contaOcc[c+1] = contaOcc[c+1] + contaOcc[c];
        }else if(((c+1)<=DIM)&&(listOrd[c+1]==listOrd[c]+2)){
            find++;
            contaOcc[c+1] = contaOcc[c+1] + contaOcc[c];
        }else if(((c+1)<=DIM)&&(listOrd[c+1]==listOrd[c]+3)){
            find++;
            contaOcc[c+1] = contaOcc[c+1] + contaOcc[c];
        }
        //check su due avanti
        if(((c+2)<=DIM)&&(listOrd[c+2]==listOrd[c]+2)){
            find++;
            contaOcc[c+2] = contaOcc[c+2] + contaOcc[c];
        }else if(((c+2)<=DIM)&&(listOrd[c+2]==listOrd[c]+3)){
            find++;
            contaOcc[c+2] = contaOcc[c+2] + contaOcc[c];
        }
        //check su tre avanti
        if(((c+3)<=DIM)&&(listOrd[c+3]==listOrd[c]+3)){
            find++;
            contaOcc[c+3] = contaOcc[c+3] + contaOcc[c];
        }
        //condizioni
        if(find==3){
            if(blocco==1){
                path = path * find;
                blocco = 4;
            }else{
                path = path + 2 * contaOcc[c];
            }
        }else if(find==2){
            if(blocco==1){
                path = path * find;
                blocco = 3;
            }else{
                path = path + contaOcc[c];
            }
        }
        blocco--;
    }
    
    return path;
}

//Restituisce -1 se son lo trova...
int searchSucc(int listNUM[DIM], int val){
    int succ;
    
    succ = MAX;
    for(int c=0; c<DIM; c++){
        if(listNUM[c]>val){
            if(listNUM[c]<succ) succ = listNUM[c];
        }
    }
    if(succ==MAX) succ = -1;
    return succ;
}

void readFILE(int listNUM[DIM]){
    int count;
    
    FILE *pFile;
    
    pFile = fopen(NOMEFILE, "r");
    count = 0;
    while(fscanf(pFile, "%d", &listNUM[count])!=EOF){
        count++;
    }
}
