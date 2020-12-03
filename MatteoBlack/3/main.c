//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 03/12/20.
//

#include <stdio.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_3/AoC/AoC/input.txt"
#define ALTEZZA 323 //prova: 11; input: 323
#define LARG 31    //prova: 11; input: 31
#define OSTACOLO '#'

//Funz DAY3_1, trova il percorso devo fare ALTEZZA + 1 passi, in larghezza equivale a spostarsi 3*passi + 1
int DAY3_1(int Mat[ALTEZZA][LARG]);
//Funz DAY3_2,
long int DAY3_2(int Mat[ALTEZZA][LARG]);
//Lettura FILE
void letturaFILE(char Mat[ALTEZZA][LARG+1], int MatFin[ALTEZZA][LARG], FILE* pFileElab);
//Stampa MAPPA
void stampaMAT(int Mat[ALTEZZA][LARG]);

int main() {
    long int result;
    char Map[ALTEZZA][LARG+1];
    int MapInt[ALTEZZA][LARG];
    FILE* pFile;
    
    pFile = NULL;
    letturaFILE(Map, MapInt, pFile);
    stampaMAT(MapInt);
    result = DAY3_2(MapInt);
    printf("\nIl num è: %ld\n", result);
    
    return 0;
}

void letturaFILE(char Mat[ALTEZZA][LARG+1], int MatFin[ALTEZZA][LARG], FILE* pFileElab){
    int row;
    int col;
    
    pFileElab = fopen(NOMEFILE, "r");
    
    if(pFileElab == NULL){
        printf("Errore in APERTURA");
    }else{
        row = 0;
        while(row<ALTEZZA){
            fscanf(pFileElab, "%s", &Mat[row][0]);
            col = 0;
            while(col<LARG){
                MatFin[row][col] = 0;
                if(OSTACOLO==Mat[row][col])
                {
                    MatFin[row][col]=1;
                }
                col++;
            }
            row++;
        }
    }
}

void stampaMAT(int Mat[ALTEZZA][LARG]){
    int row;
    int col;
    
    row = 0;
    printf("\n");
    while(row<ALTEZZA){
        col = 0;
        while(col<LARG){
            printf("%d", Mat[row][col]);
            col++;
        }
        printf("\n");
        row++;
    }
}

int DAY3_1(int Mat[ALTEZZA][LARG]){
    int counterAlberi;
    int row;
    int col;

    row = 0;
    col = 0;
    counterAlberi = 0;
    while(row<ALTEZZA-1){
        row++;
        col = col + 3;
        if(col>=LARG)
        {
            col = (col-(LARG-1))-1;
        }
        if(Mat[row][col]==1){
            counterAlberi++;
        }
    }
    return counterAlberi;
}

long int DAY3_2(int Mat[ALTEZZA][LARG]){
    int counterAlberi_1;
    int counterAlberi_2;
    int counterAlberi_3;
    int counterAlberi_4;
    int counterAlberi_5;
    int row;
    int col;
    long int result;
    
    //percorso 1
    row = 0;
    col = 0;
    counterAlberi_1 = 0;
    while(row<ALTEZZA-1){
        row++;
        col++;
        if(col>=LARG)
        {
            col = col - LARG;
        }
        if(Mat[row][col]==1){
            counterAlberi_1++;
        }
    }
    
    //percorso 2
    row = 0;
    col = 0;
    counterAlberi_2 = 0;
    while(row<ALTEZZA-1){
        row++;
        col = col + 3;
        if(col>=LARG)
        {
            col = col - LARG;
        }
        if(Mat[row][col]==1){
            counterAlberi_2++;
        }
    }
    
    //percorso 3
    row = 0;
    col = 0;
    counterAlberi_3 = 0;
    while(row<ALTEZZA-1){
        row++;
        col = col + 5;
        if(col>=LARG)
        {
            col = col - LARG;
        }
        if(Mat[row][col]==1){
            counterAlberi_3++;
        }
    }
    
    //percorso 4
    row = 0;
    col = 0;
    counterAlberi_4 = 0;
    while(row<ALTEZZA-1){
        row++;
        col = col + 7;
        if(col>=LARG)
        {
            col = col - LARG;
        }
        if(Mat[row][col]==1){
            counterAlberi_4++;
        }
    }
    
    //percorso 5
    row = 0;
    col = 0;
    counterAlberi_5 = 0;
    while(row<ALTEZZA){
        row = row + 2;
        if(row>=ALTEZZA) break;
        col++;
        if(col>=LARG)
        {
            col = col - LARG;
        }
        if(Mat[row][col]==1){
            counterAlberi_5++;
        }
    }
    
    result = counterAlberi_1 * counterAlberi_2 * counterAlberi_3 * counterAlberi_4 * counterAlberi_5;
    return result;
}
