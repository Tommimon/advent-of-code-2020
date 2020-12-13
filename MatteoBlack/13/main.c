//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 13/12/20.
//
//Piccola modifica al file, metto la virgola alla fine!!
#include <stdio.h>
#include <math.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_13/AoC/AoC/input.c"
#define LUNG 86 //prova: 8; input: 86;
#define MAX 10
#define MAXMAX 10003400
#define TIP 100000000000000  //input: 100000000000000

int readFile(int list[LUNG]);
void stampaList(int list[LUNG]);
int DAY13_1(int TimeStamp, int list[LUNG]);
long long int DAY13_2(int list[LUNG]); //Fallisce miseramente con l'input
long long int DAY13_2_BIS(int list[LUNG]); //Fallisce miseramente con l'input
long long int DAY13_2_BIS_BIS(int list[LUNG]); //Funziona con l'input

int main() {
    int TimeStamp;
    int list[LUNG];
    
    TimeStamp = readFile(list);
    
    printf("Il numero è: %lld\n", DAY13_2_BIS_BIS(list));
    
    return 0;
}

int DAY13_1(int TimeStamp, int list[LUNG]){
    int result;
    int num;
    int min;
    int ID;
    
    result = 0;
    min = MAXMAX;
    for(int c=0; c<LUNG; c++){
        if(list[c]!=-1){
            num = list[c];
            while(num<=TimeStamp){
                num = num + list[c];
            }
            if(min>num){
                min = num;
                ID = c;
            }
        }
    }
    result = (min-TimeStamp)*list[ID];
    return result;
}

long long int DAY13_2(int list[LUNG]){
    long long int result;
    long long int num1;
    long long int num2;
    long long int numJ;

    int end;
    int ripeti;
    
    end = 0;
    num1 = 0;
    num2 = 0;
    ripeti = 0;
    for(int i=0; (i<LUNG)&&(end==0); i++){
        if(list[i]!=-1){
            for(int c=i+1; (c<LUNG)&&(end==0); c++){
                if(list[c]!=-1){
                    //BARO...
                    num1 = (TIP/list[i]) * list[i];
                    num2 = (TIP/list[c]) * list[c];
                    while(num2!=num1+(c-i)){
                        num1 = num1 + list[i];
                        while(num2<num1+(c-i)){
                            num2 = num2 +  list[c];
                        }
                    }
                    while(end==0){
                        ripeti = 0;
                        for(int j=c+1; (ripeti==0)&&(j<LUNG); j++){
                            if(list[j]!=-1){
                                numJ = num1 + j;
                                if((numJ % list[j])!=0){
                                    ripeti = 1;
                                }
                            }
                        }
                        if(ripeti==0){
                            end = 1;
                        }
                        else{
                            num1 = num1 + (list[i] * list[c]);
                            ripeti = 0;
                        }
                    }
                }
            }
        }
    }
    result = num1;
    return result;
}

long long int DAY13_2_BIS(int list[LUNG]){
    long long int result;
    int control;
    int max;
    int end;
    int ID;
    
    max = 0;
    for(int i=0; i<LUNG; i++){
        if(list[i]!=-1){
            if(max<list[i]){
                max = list[i];
                ID = i;
            }
        }
    }
    
    end = 0;
    result = ((TIP/max) * (max));
    while(end==0){
        control = 0;
        for(int i=0; (i<LUNG)&&(control==0); i++){
            if(list[i]!=-1){
                if(((result + (i-ID)) % (list[i]))!=0){
                    control++;
                    break;
                }
            }
        }
        if(control==0) end = 1;
        else{
            result = result + max;
        }
    }
    return (result-ID);
}

long long int DAY13_2_BIS_BIS(int list[LUNG]){
    int block;
    int max1;
    int max2;
    int ID1;
    int ID2;
    int end;
    int control;
    long long int num1;
    long long int num2;
    
    max1 = 0;
    max2 = 0;
    for(int i=0; i<LUNG; i++){
        block = 0;
        for(int c=2; (c<list[i])&&(block==0); c++){
            if(list[i] % c == 0){
                block = 1;
            }
        }
        if(block==0){
            if(max1<list[i]){
                max2 = max1;
                ID2 = ID1;
                max1 = list[i];
                ID1 = i;
            }else if(max2<list[i]){
                max2 = list[i];
                ID2 = i;
            }
        }
    }
    num1 = (TIP/max1) * max1;
    num2 = (TIP/max2) * max2;
    while(num2!=num1+(ID2-ID1)){
        num1 = num1 + max1;
        while(num2<num1+(ID2-ID1)){
            num2 = num2 +  max2;
        }
    }
    end = 0;
    while(end==0){
        control = 0;
        for(int i=0; (i<LUNG)&&(control==0); i++){
            if(list[i]!=-1){
                if(((num1 + (i-ID1)) % (list[i]))!=0){
                    control++;
                    break;
                }
            }
        }
        if(control==0) end = 1;
        else{
            num1 = num1 + (max1 * max2);
        }
    }
    return (num1-ID1);
}


int readFile(int list[LUNG]){
    int num;
    int count;
    int index;
    int check;
    int ordine;
    int contrNum;
    int TimeStamp;
    char val[MAX];
    char charLet;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    fscanf(pFile, "%d\n", &TimeStamp);
    count = 0;
    index = 0;
    ordine = -1;
    contrNum = 0;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if((','==charLet)&&(contrNum==1)){
            check = 0;
            num = 0;
            for(int c=(index-1); c>=(index-ordine)-1; c--){
                num = num + (val[ordine-check]-'0')*(pow(10, check));
                check++;
            }
            list[count] = num;
            count++;
            contrNum = 0;
            ordine = -1;
        }else if('x'==charLet){
            list[count] = -1;
            count++;
        }else if((charLet>='0')&&(charLet<='9')){
            val[ordine+1] = charLet;
            ordine++;
            contrNum = 1;
        }
        index++;
    }
    return TimeStamp;
}

void stampaList(int list[LUNG]){
    for(int c=0; c<LUNG; c++){
        printf(" %d -", list[c]);
    }
}
