//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 05/12/20.
//

#include <stdio.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_5/AoC/AoC/input.txt"
#define COL 7 //0-7
#define ROW 127 //0-127
#define DIMCODE 11 //per mettere il \0 (0-10)


//Funz DAY5_1
int DAY5_1(void);
//Funz DAY5_2
int DAY5_2(int mat[ROW+1][COL+1]);
//Creo Matrice
void InizMat(int mat[ROW+1][COL+1]);

int main() {
    int result;
    int posti[ROW+1][COL+1];
    
    InizMat(posti);
    result = DAY5_2(posti);
    printf("\nIl risultato è: %d\n", result);
    
    return 0;
}

int DAY5_1(){
    int maxID;
    int colIN;
    int colFIN;
    int rowIN;
    int rowFIN;
    int tempID;
    int c;
    char cod[DIMCODE];
    char campione;
    FILE* pFile;
    
    maxID = 0;
    pFile = fopen(NOMEFILE, "r");
    while((fscanf(pFile, "%s", cod))!=EOF){
        c = 1;
        colIN = 0;
        rowIN = 0;
        colFIN = COL;
        rowFIN = ROW;
        campione = cod[0];
        while(campione!='\0'){
            if(campione=='F'){
                rowFIN = rowFIN-(((rowFIN - rowIN)/2)+1);
            }else if(campione=='B'){
                rowIN = rowIN + (((rowFIN - rowIN)/2)+1);
            }else if(campione=='R'){
                colIN = colIN + (((colFIN - colIN)/2)+1);
            }else if(campione=='L'){
                colFIN = colFIN - (((colFIN - colIN)/2)+1);
            }
            campione = cod[c];
            c++;
        }
        tempID = rowIN * 8 + colIN;
        if(tempID>maxID){
            maxID = tempID;
        }
    }
    fclose(pFile);
    return maxID;
}

int DAY5_2(int mat[ROW+1][COL+1]){
    int myID;
    int colIN;
    int colFIN;
    int rowIN;
    int rowFIN;
    int row;
    int col;
    int c;
    char cod[DIMCODE];
    char campione;
    FILE* pFile;

    myID = 0;
    pFile = fopen(NOMEFILE, "r");
    while((fscanf(pFile, "%s", cod))!=EOF){
        c = 1;
        colIN = 0;
        rowIN = 0;
        colFIN = COL;
        rowFIN = ROW;
        campione = cod[0];
        while(campione!='\0'){
            if(campione=='F'){
                rowFIN = rowFIN-(((rowFIN - rowIN)/2)+1);
            }else if(campione=='B'){
                rowIN = rowIN + (((rowFIN - rowIN)/2)+1);
            }else if(campione=='R'){
                colIN = colIN + (((colFIN - colIN)/2)+1);
            }else if(campione=='L'){
                colFIN = colFIN - (((colFIN - colIN)/2)+1);
            }
            campione = cod[c];
            c++;
            mat[rowFIN][colFIN] = 1;
        }
    }
    for(row=0; row<ROW; row++){
        for(col=0; col<COL; col++){
            printf("%d ", mat[row][col]);
            if(mat[row][col]==0){
                if((mat[row-1][col]==1)&&(mat[row+1][col]==1)){
                    myID = row * 8 + col;
                }
            }
        }
        printf("\n");
    }
    fclose(pFile);
    return myID;
    
}

void InizMat(int mat[ROW+1][COL+1]){
    int row;
    int col;
    for(row=0; row<=ROW; row++){
        
        for(col=0; col<=COL; col++){
            mat[row][col] = 0;
//            printf("%d ", mat[row][col]);
        }
//        printf("\n");
    }
}

