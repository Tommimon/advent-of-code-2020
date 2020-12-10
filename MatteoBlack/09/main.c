//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 09/12/20.
//

#include <stdio.h>

#define PREAMBLE 25
#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_9/AoC/AoC/input.c"
#define DIM 1000 //prova: 20; input: 1000

void readFILE(int listNUM[DIM]);
int DAY9_1(int listNUM[DIM]);
int DAY9_2(int listNUM[DIM], int val);

int main() {
    int listNum[DIM];
    int input;
    
    readFILE(listNum);
    input = DAY9_1(listNum);
    printf("\nIl valore è: %d\n", DAY9_2(listNum, input));
    
    return 0;
}

int DAY9_1(int listNUM[DIM]){
    int numCheck;
    int control;
    int count;
    int stop;
    
    numCheck = 0;
    stop = 0;
    count = PREAMBLE;
    while((stop==0)&&(count<DIM)){
        numCheck = listNUM[count];
        control = 0;
        for(int i=count-PREAMBLE; i<(count-1); i++){
            for(int c=i+1; c<count; c++){
                if(numCheck == (listNUM[i]+listNUM[c])){
                    control = 1;
                }
            }
        }
        count++;
        if(control==0) stop = 1;
    }
    return numCheck;
}

int DAY9_2(int listNUM[DIM], int val){
    int stop;
    int count;
    int index;
    int check;
    int sum;
    int end;
    int indMin;
    int indMax;
    int min;
    int max;
    
    end = 0;
    sum = 0;
    stop = 0;
    count = 0;
    indMin = 0;
    indMax = 0;
    min = val;
    max = 0;
    while((end==0)&&(count<DIM)){
        index = count;
        check = val;
        stop = 0;
        while((stop==0)&&(count<DIM)){
            check = check - listNUM[index];
            if(check<0) stop = 1;
            else if(check==0){
                for(int i=count; i<=index; i++){
                    if(listNUM[i]<min){
                        min = listNUM[i];
                        indMin = i;
                    }if(listNUM[i]>max){
                        max = listNUM[i];
                        indMax = i;
                    }
                }
                sum = listNUM[indMin] + listNUM[indMax];
                end = 1;
                stop = 1;
            }
            index++;
        }
        count++;
    }
    return sum;
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
