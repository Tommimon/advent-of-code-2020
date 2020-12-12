//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 12/12/20.
//

#include <stdio.h>
#include <string.h>
#include <math.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_12/AoC/AoC/input.c"
#define LUNG 772 //prova: 5; input: 772
#define DIM 10 //prova: 5; input: 10

void readFile(char istr[LUNG][DIM]);
int DAY12_1(char istr[LUNG][DIM]);
int DAY12_2(char istr[LUNG][DIM]);

int main(int argc, const char * argv[]) {
    char istr[LUNG][DIM];
    
    readFile(istr);
    printf("Il numero è: %d\n", DAY12_2(istr));
    
    return 0;
}

int DAY12_1(char istr[LUNG][DIM]){
    int sum;
    int num;
    int posX;
    int posY;
    int dir;
    
    sum = 0;
    posX = 0;
    posY = 0;
    dir = 90; //est
    for(int r=0; r<LUNG; r++){
        num = 0;
        for(int c=(strlen(istr[r])-1); (istr[r][c]>='0')&&(istr[r][c]<='9') ; c--){
            num = num + (istr[r][c]-'0')*(pow(10, (strlen(istr[r])-1-c)));
        }
        switch (istr[r][0]) {
            case 'N': {
                posY = posY + num;
                break;
            }
            case 'S': {
                posY = posY - num;
                break;
            }
            case 'E': {
                posX = posX + num;
                break;
            }
            case 'W': {
                posX = posX - num;
                break;
            }
            case 'L': {
                dir = dir - num;
                if(dir<0) dir = dir + 360;
                break;
            }
            case 'R': {
                dir = dir + num;
                if(dir>=360) dir = dir - 360;
                break;
            }
            case 'F': {
                if(dir==90) posX = posX + num;
                else if(dir==180) posY = posY - num;
                else if(dir==270) posX = posX - num;
                else if(dir==0) posY = posY + num;
                break;
            }
                
        }
    }
    //fabs -> valore assoluto
    sum = fabs(posX) + fabs(posY);
    return sum;
}

int DAY12_2(char istr[LUNG][DIM]){
    int sum;
    int num;
    int temp;
    int posX;
    int posY;
    int posWayX;
    int posWayY;

    posWayX = 10;
    posWayY = 1;
    sum = 0;
    posX = 0;
    posY = 0;
    for(int r=0; r<LUNG; r++){
        num = 0;
        for(int c=(strlen(istr[r])-1); (istr[r][c]>='0')&&(istr[r][c]<='9') ; c--){
            num = num + (istr[r][c]-'0')*(pow(10, (strlen(istr[r])-1-c)));
        }
        switch (istr[r][0]) {
            case 'N': {
                posWayY = posWayY + num;
                break;
            }
            case 'S': {
                posWayY = posWayY - num;
                break;
            }
            case 'E': {
                posWayX = posWayX + num;
                break;
            }
            case 'W': {
                posWayX = posWayX - num;
                break;
            }
            case 'L': {
                if(num==90){
                    temp = posWayX;
                    posWayX = -1 * posWayY;
                    posWayY = temp;
                }
                else if(num==180){
                    posWayX = -1 * posWayX;
                    posWayY = -1 * posWayY;
                }
                else if(num==270){
                    temp = posWayX;
                    posWayX = posWayY;
                    posWayY = -1 * temp;
                }
                else if((num==0)||(num==360)){
                    //nulla
                }
                break;
            }
            case 'R': {
                if(num==90){
                    temp = posWayX;
                    posWayX = posWayY;
                    posWayY = -1 * temp;
                }
                else if(num==180){
                    posWayX = -1 * posWayX;
                    posWayY = -1 * posWayY;
                }
                else if(num==270){
                    temp = posWayX;
                    posWayX = -1 * posWayY;
                    posWayY = temp;
                }
                else if((num==0)||(num==360)){
                    //nulla
                }
                break;
            }
            case 'F': {
                posY = posY + num * posWayY;
                posX = posX + num * posWayX;
                break;
            }
                
        }
    }
    //fabs -> valore assoluto
    sum = fabs(posX) + fabs(posY);
    return sum;
}

void readFile(char istr[LUNG][DIM]){
    char charLet;
    int c;
    int r;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    r = 0;
    c = 0;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet=='\n'){
            istr[r][c] = '\0';
            r++;
            c = 0;
        }else{
            istr[r][c] = charLet;
            c++;
        }
    }
}
