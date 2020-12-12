//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 12/12/20.
//

#include <stdio.h>
#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_11/AoC/AoC/input.c"
#define ALT 93 //prova: 10; input: 93
#define LARG 90 //prova: 10; prova: 90

void readFile(int map[ALT][LARG]);
void printMAP(int map[ALT][LARG]);
void copyMAT(int map1[ALT][LARG], int map2[ALT][LARG]);
int checkMAT(int map1[ALT][LARG], int map2[ALT][LARG]);
int DAY11_1(int map[ALT][LARG]);
int DAY11_2(int map[ALT][LARG]);

int main(){
    int map[ALT][LARG];
    
    readFile(map);
    
    printf("\nIl num di posti occupati è: %d\n", DAY11_2(map));
    
    return 0;
}

int DAY11_1(int map[ALT][LARG]){
    int result;
    int change;
    int countPosti;
    int matLav[ALT][LARG];
    
    for(int r=0; r<ALT; r++){
        for(int c=0; c<LARG; c++){
            if(map[r][c]==0) map[r][c] = 1;
        }
    }
    change = 1;
    while(change==1){
        //Li libero...(1 = occupato)
        change = 0;
        copyMAT(matLav, map);
        for(int r=0; r<ALT; r++){
            for(int c=0; c<LARG; c++){
                countPosti = 0;
                if(map[r][c]==1){
                    if((countPosti<4)&&(r-1>=0)&&(matLav[r-1][c]==1)) countPosti++;
                    if((countPosti<4)&&(r-1>=0)&&(c+1<LARG)&&(matLav[r-1][c+1]==1)) countPosti++;
                    if((countPosti<4)&&(c+1<LARG)&&(matLav[r][c+1]==1)) countPosti++;
                    if((countPosti<4)&&(r+1<ALT)&&(c+1<LARG)&&(matLav[r+1][c+1]==1)) countPosti++;
                    if((countPosti<4)&&(r+1<ALT)&&(matLav[r+1][c]==1)) countPosti++;
                    if((countPosti<4)&&(r+1<ALT)&&(c-1>=0)&&(matLav[r+1][c-1]==1)) countPosti++;
                    if((countPosti<4)&&(c-1>=0)&&(matLav[r][c-1]==1)) countPosti++;
                    if((countPosti<4)&&(r-1>=0)&&(c-1>=0)&&(matLav[r-1][c-1]==1)) countPosti++;
                    
                    if(countPosti==4){
                        map[r][c] = 0;
                    }
                }
            }
        }
        //Li occupo...
        copyMAT(matLav, map);
        for(int r=0; r<ALT; r++){
            for(int c=0; c<LARG; c++){
                countPosti = 0;
                if(map[r][c]==0){
                    if((r-1>=0)&&(matLav[r-1][c]==1)) countPosti++;
                    if((r-1>=0)&&(c+1<LARG)&&(matLav[r-1][c+1]==1)) countPosti++;
                    if((c+1<LARG)&&(matLav[r][c+1]==1)) countPosti++;
                    if((r+1<ALT)&&(c+1<LARG)&&(matLav[r+1][c+1]==1)) countPosti++;
                    if((r+1<ALT)&&(matLav[r+1][c]==1)) countPosti++;
                    if((r+1<ALT)&&(c-1>=0)&&(matLav[r+1][c-1]==1)) countPosti++;
                    if((c-1>=0)&&(matLav[r][c-1]==1)) countPosti++;
                    if((r-1>=0)&&(c-1>=0)&&(matLav[r-1][c-1]==1)) countPosti++;
                    
                    if(countPosti==0){
                        map[r][c] = 1;
                    }
                }
            }
        }
        change = checkMAT(matLav, map);
    }
    //FINE WHILE
    result = 0;
    for(int r=0; r<ALT; r++){
        for(int c=0; c<LARG; c++){
            if(map[r][c]==1) result++;
        }
    }
    
    return result;
}

int DAY11_2(int map[ALT][LARG]){
    int j;
    int i;
    int result;
    int change;
    int countPosti;
    int matLav[ALT][LARG];
    
    for(int r=0; r<ALT; r++){
        for(int c=0; c<LARG; c++){
            if(map[r][c]==0) map[r][c] = 1;
        }
    }
    change = 1;
    while(change==1){
        //Li libero...(1 = occupato)
        change = 0;
        copyMAT(matLav, map);
        for(int r=0; r<ALT; r++){
            for(int c=0; c<LARG; c++){
                countPosti = 0;
                if(map[r][c]==1){
                    //NORD
                    for(int i=r-1; (i>=0)&&(countPosti<5)&&(matLav[i][c]!=0); i--){
                        if(matLav[i][c]==1){
                            countPosti++;
                            break;
                        }
                    }
                    //NORD-EST
                    j = c + 1;
                    for(i=r-1; (j<LARG)&&(i>=0)&&(countPosti<5)&&(matLav[i][j]!=0); i--){
                        if(matLav[i][j]==1){
                            countPosti++;
                            break;
                        }
                        j++;
                    }
                    //EST
                    for(i=c+1; (i<LARG)&&(countPosti<5)&&(matLav[r][i]!=0); i++){
                        if(matLav[r][i]==1){
                            countPosti++;
                            break;
                        }
                    }
                    //SUD-EST
                    j = c + 1;
                    for(i=r+1; (j<LARG)&&(i<ALT)&&(countPosti<5)&&(matLav[i][j]!=0); i++){
                        if(matLav[i][j]==1){
                            countPosti++;
                            break;
                        }
                        j++;
                    }
                    //SUD
                    for(i=r+1; (i<ALT)&&(countPosti<5)&&(matLav[i][c]!=0); i++){
                        if(matLav[i][c]==1){
                            countPosti++;
                            break;
                        }
                    }
                    //SUD-OVEST
                    j = c - 1;
                    for(i=r+1; (j>=0)&&(i<ALT)&&(countPosti<5)&&(matLav[i][j]!=0); i++){
                        if(matLav[i][j]==1){
                            countPosti++;
                            break;
                        }
                        j--;
                    }
                    //OVEST
                    for(i=c-1; (i>=0)&&(countPosti<5)&&(matLav[r][i]!=0); i--){
                        if(matLav[r][i]==1){
                            countPosti++;
                            break;
                        }
                    }
                    //NORD-OVEST
                    j = c - 1;
                    for(i=r-1; (j>=0)&&(i>=0)&&(countPosti<5)&&(matLav[i][j]!=0); i--){
                        if(matLav[i][j]==1){
                            countPosti++;
                            break;
                        }
                        j--;
                    }
                    
                    if(countPosti==5){
                        map[r][c] = 0;
                    }
                }
            }
        }
        printMAP(map);
        printf("\n\n");
        //Li occupo...
        copyMAT(matLav, map);
        for(int r=0; r<ALT; r++){
            for(int c=0; c<LARG; c++){
                countPosti = 0;
                if(map[r][c]==0){
                    //NORD
                    for(i=r-1; (i>=0)&&(countPosti==0)&&(matLav[i][c]==-1); i--);
                    if((matLav[i][c]==1)&&(i>=0)&&(countPosti==0)){
                        countPosti++;
                    }
                    //NORD-EST
                    j = c + 1;
                    for(i=r-1; (j<LARG)&&(i>=0)&&(countPosti==0)&&(matLav[i][j]==-1); i--) j++;
                    if((matLav[i][j]==1)&&(i>=0)&&(j<LARG)&&(countPosti==0)){
                        countPosti++;
                    }
                    //EST
                    for(i=c+1; (i<LARG)&&(countPosti==0)&&(matLav[r][i]==-1); i++);
                    if((matLav[r][i]==1)&&(i<LARG)&&(countPosti==0)){
                        countPosti++;
                    }
                    //SUD-EST
                    j = c + 1;
                    for(i=r+1; (j<LARG)&&(i<ALT)&&(countPosti==0)&&(matLav[i][j]==-1); i++) j++;
                    if((matLav[i][j]==1)&&(i<ALT)&&(j<LARG)&&(countPosti==0)){
                        countPosti++;
                    }
                    //SUD
                    for(i=r+1; (i<ALT)&&(countPosti==0)&&(matLav[i][c]==-1); i++);
                    if((matLav[i][c]==1)&&(i<ALT)&&(countPosti==0)){
                        countPosti++;
                    }
                    //SUD-OVEST
                    j = c - 1;
                    for(i=r+1; (j>=0)&&(i<ALT)&&(countPosti==0)&&(matLav[i][j]==-1); i++) j--;
                    if((matLav[i][j]==1)&&(j>=0)&&(i<ALT)&&(countPosti==0)){
                        countPosti++;
                    }
                    //OVEST
                    for(i=c-1; (i>=0)&&(countPosti==0)&&(matLav[r][i]==-1);i--);
                    if((matLav[r][i]==1)&&(i>=0)&&(countPosti==0)){
                        countPosti++;
                    }
                    //NORD-OVEST
                    j = c - 1;
                    for(i=r-1; (j>=0)&&(i>=0)&&(countPosti==0)&&(matLav[i][j]==-1); i--) j--;
                    if((matLav[i][j]==1)&&(i>=0)&&(j>=0)&&(countPosti==0)){
                        countPosti++;
                    }
                        
                    if(countPosti==0){
                        map[r][c] = 1;
                    }
                }
            }
        }
        printMAP(map);
        printf("\n\n");
        change = checkMAT(matLav, map);
    }
    //FINE WHILE
    result = 0;
    for(int r=0; r<ALT; r++){
        for(int c=0; c<LARG; c++){
            if(map[r][c]==1) result++;
        }
    }
    
    return result;
}

void readFile(int map[ALT][LARG]){
    int c;
    int r;
    char charLet;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    r = 0;
    c = -1;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if('\n'==charLet){
            r++;
            c = -1;
        }else if('.'==charLet){
            c++;
            map[r][c] = -1;
        }else if('L'){
            c++;
            map[r][c] = 0;
        }
    }
}

void printMAP(int map[ALT][LARG]){
    for(int r=0; r<ALT; r++){
        for(int c=0; c<LARG; c++){
            printf("%d\t", map[r][c]);
        }
        printf("\n");
    }
}

void copyMAT(int map1[ALT][LARG], int map2[ALT][LARG]){
    for(int r=0; r<ALT; r++){
        for(int c=0; c<LARG; c++){
            map1[r][c] = map2[r][c];
        }
    }
}

int checkMAT(int map1[ALT][LARG], int map2[ALT][LARG]){
    int div;
    div = 0;
    for(int r=0; (div==0)&&(r<ALT); r++){
        for(int c=0; (div==0)&&(c<LARG); c++){
            if(map1[r][c]!=map2[r][c]){
                div = 1;
                break;
            }
        }
    }
    return div;
}
