//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 17/12/20.
//

#include <stdio.h>
#define Z 13 //13
#define W 13 //13
#define XY 20 //20
#define START_XYZ 6 //inzio pos (6,6) angolo alt sx
#define START_W 6 //6
#define DIM 8 //8
#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_17/AoC/AoC/input.txt"
#define ATTIVO '#'

void stampaMAT(int Mat[Z][XY][XY], int AngNO);
void stampaMAT_2(int Mat[W][Z][XY][XY], int AngNO);
void letturaFILE(int Mat[Z][XY][XY]);
void letturaFILE_2(int Mat[W][Z][XY][XY]);
void copyMAT(int Mat1[Z][XY][XY], int Mat2[Z][XY][XY]);
void copyMAT_2(int Mat1[W][Z][XY][XY], int Mat2[W][Z][XY][XY]);
int DAY17_1(int MatFin[Z][XY][XY]);
int DAY17_2(int MatFin[W][Z][XY][XY]);


int main() {
    int Mat[W][Z][XY][XY];
//    int MatProva[Z][XY][XY];
    
    letturaFILE_2(Mat);
//    letturaFILE(MatProva);
    
    printf("Il num: %d\n", DAY17_2(Mat));
//    printf("Il num: %d\n", DAY17_1(MatProva));
    
    return 0;
}

int DAY17_1(int MatFin[Z][XY][XY]){
    int Mat[Z][XY][XY];
    int active;
    int count;
    
    for(int g=0; g<6; g++){
        copyMAT(MatFin, Mat);
        for(int z=0; z<Z; z++){
            for(int y=0; y<XY; y++){
                for(int x=0; x<XY; x++){
                    count = 0;
                    if(Mat[z][y][x]==0){
                        //facciata sopra
                        if(((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[z-1][y-1][x-1]==1)) count++;
                        if(((z-1)>=0)&&((y-1)>=0)&&(Mat[z-1][y-1][x]==1)) count++;
                        if(((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z-1][y-1][x+1]==1)) count++;
                        if(((z-1)>=0)&&((x-1)>=0)&&(Mat[z-1][y][x-1]==1)) count++;
                        if(((z-1)>=0)&&(Mat[z-1][y][x]==1)) count++;
                        if(((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z-1][y][x+1]==1)) count++;
                        if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z-1][y+1][x-1]==1)) count++;
                        if(((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[z-1][y+1][x]==1)) count++;
                        if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z-1][y+1][x+1]==1)) count++;
                        //facciata sotto
                        if(((z+1)<=(XY-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[z+1][y-1][x-1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y-1)>=0)&&(Mat[z+1][y-1][x]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z+1][y-1][x+1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z+1][y][x-1]==1)) count++;
                        if(((z+1)<=(XY-1))&&(Mat[z+1][y][x]==1)) count++;
                        if(((z+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z+1][y][x+1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z+1][y+1][x-1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y+1)<=(XY-1))&&(Mat[z+1][y+1][x]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z+1][y+1][x+1]==1)) count++;
                        //foglio in mezzo
                        if(((y-1)>=0)&&((x-1)>=0)&&(Mat[z][y-1][x-1]==1)) count++;
                        if(((y-1)>=0)&&(Mat[z][y-1][x]==1)) count++;
                        if(((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z][y-1][x+1]==1)) count++;
                        if(((x-1)>=0)&&(Mat[z][y][x-1]==1)) count++;
                        if(((x+1)<=(XY-1))&&(Mat[z][y][x+1]==1)) count++;
                        if(((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z][y+1][x-1]==1)) count++;
                        if(((y+1)<=(XY-1))&&(Mat[z][y+1][x]==1)) count++;
                        if(((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z][y+1][x+1]==1)) count++;
                        
                        if(count==3) MatFin[z][y][x]=1;
                    }
                    else{
                        if(((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[z-1][y-1][x-1]==1)) count++;
                        if(((z-1)>=0)&&((y-1)>=0)&&(Mat[z-1][y-1][x]==1)) count++;
                        if(((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z-1][y-1][x+1]==1)) count++;
                        if(((z-1)>=0)&&((x-1)>=0)&&(Mat[z-1][y][x-1]==1)) count++;
                        if(((z-1)>=0)&&(Mat[z-1][y][x]==1)) count++;
                        if(((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z-1][y][x+1]==1)) count++;
                        if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z-1][y+1][x-1]==1)) count++;
                        if(((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[z-1][y+1][x]==1)) count++;
                        if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z-1][y+1][x+1]==1)) count++;
                        //facciata sotto
                        if(((z+1)<=(XY-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[z+1][y-1][x-1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y-1)>=0)&&(Mat[z+1][y-1][x]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z+1][y-1][x+1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z+1][y][x-1]==1)) count++;
                        if(((z+1)<=(XY-1))&&(Mat[z+1][y][x]==1)) count++;
                        if(((z+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z+1][y][x+1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z+1][y+1][x-1]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y+1)<=(XY-1))&&(Mat[z+1][y+1][x]==1)) count++;
                        if(((z+1)<=(XY-1))&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z+1][y+1][x+1]==1)) count++;
                        //foglio in mezzo
                        if(((y-1)>=0)&&((x-1)>=0)&&(Mat[z][y-1][x-1]==1)) count++;
                        if(((y-1)>=0)&&(Mat[z][y-1][x]==1)) count++;
                        if(((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[z][y-1][x+1]==1)) count++;
                        if(((x-1)>=0)&&(Mat[z][y][x-1]==1)) count++;
                        if(((x+1)<=(XY-1))&&(Mat[z][y][x+1]==1)) count++;
                        if(((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[z][y+1][x-1]==1)) count++;
                        if(((y+1)<=(XY-1))&&(Mat[z][y+1][x]==1)) count++;
                        if(((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[z][y+1][x+1]==1)) count++;
                        
                        if((count!=3)&&(count!=2)) MatFin[z][y][x]=0;
                    }
                }
            }
        }
    }
    
    active = 0;
    for(int z=0; z<Z; z++){
        for(int y=0; y<XY; y++){
            for(int x=0; x<XY; x++){
                if(MatFin[z][y][x]==1) active++;
            }
        }
    }
    
    return active;
}

int DAY17_2(int MatFin[W][Z][XY][XY]){
    int Mat[W][Z][XY][XY];
    int active;
    int count;
    
    for(int g=0; g<6; g++){
        copyMAT_2(MatFin, Mat);
        for(int w=0; w<W; w++){
            for(int z=0; z<Z; z++){
                for(int y=0; y<XY; y++){
                    for(int x=0; x<XY; x++){
                        count = 0;
                        if(Mat[w][z][y][x]==0){
                            if(((w-1)>=0)&&((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z-1][y-1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y-1)>=0)&&(Mat[w-1][z-1][y-1][x]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z-1][y-1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w-1][z-1][y+1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w-1][z-1][y+1][x]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[w-1][z-1][y+1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z-1][y][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&(Mat[w-1][z-1][y][x]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z-1][y][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z+1][y-1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y-1)>=0)&&(Mat[w-1][z+1][y-1][x]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z+1][y-1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w-1][z+1][y+1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&(Mat[w-1][z+1][y+1][x]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w-1][z+1][y+1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((x-1)>=0)&&(Mat[w-1][z+1][y][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&(Mat[w-1][z+1][y][x]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((x+1)<=(XY-1))&&(Mat[w-1][z+1][y][x+1]==1)) count++;
                            if(((w-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z][y-1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((y-1)>=0)&&(Mat[w-1][z][y-1][x]==1)) count++;
                            if(((w-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z][y-1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w-1][z][y+1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w-1][z][y+1][x]==1)) count++;
                            if(((w-1)>=0)&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w-1][z][y+1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z][y][x-1]==1)) count++;
                            if(((w-1)>=0)&&(Mat[w-1][z][y][x]==1)) count++;
                            if(((w-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z][y][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z-1][y-1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y-1)>=0)&&(Mat[w+1][z-1][y-1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z-1][y-1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w+1][z-1][y+1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w+1][z-1][y+1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w+1][z-1][y+1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z-1][y][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&(Mat[w+1][z-1][y][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z-1][y][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z+1][y-1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y-1)>=0)&&(Mat[w+1][z+1][y-1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z+1][y-1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w+1][z+1][y+1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&(Mat[w+1][z+1][y+1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w+1][z+1][y+1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((x-1)>=0)&&(Mat[w+1][z+1][y][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&(Mat[w+1][z+1][y][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((x+1)<=(XY-1))&&(Mat[w+1][z+1][y][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z][y-1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y-1)>=0)&&(Mat[w+1][z][y-1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z][y-1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w+1][z][y+1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y+1)<=(XY-1))&&(Mat[w+1][z][y+1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w+1][z][y+1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((x-1)>=0)&&(Mat[w+1][z][y][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&(Mat[w+1][z][y][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((x+1)<=(XY-1))&&(Mat[w+1][z][y][x+1]==1)) count++;
                            if(((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w][z-1][y-1][x-1]==1)) count++;
                            if(((z-1)>=0)&&((y-1)>=0)&&(Mat[w][z-1][y-1][x]==1)) count++;
                            if(((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z-1][y-1][x+1]==1)) count++;
                            if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w][z-1][y+1][x-1]==1)) count++;
                            if(((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w][z-1][y+1][x]==1)) count++;
                            if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[w][z-1][y+1][x+1]==1)) count++;
                            if(((z-1)>=0)&&((x-1)>=0)&&(Mat[w][z-1][y][x-1]==1)) count++;
                            if(((z-1)>=0)&&(Mat[w][z-1][y][x]==1)) count++;
                            if(((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z-1][y][x+1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w][z+1][y-1][x-1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y-1)>=0)&&(Mat[w][z+1][y-1][x]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z+1][y-1][x+1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w][z+1][y+1][x-1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&(Mat[w][z+1][y+1][x]==1)) count++;
                            if(((z+1)<=(Z-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w][z+1][y+1][x+1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((x-1)>=0)&&(Mat[w][z+1][y][x-1]==1)) count++;
                            if(((z+1)<=(Z-1))&&(Mat[w][z+1][y][x]==1)) count++;
                            if(((z+1)<=(Z-1))&&((x+1)<=(XY-1))&&(Mat[w][z+1][y][x+1]==1)) count++;
                            if(((y-1)>=0)&&((x-1)>=0)&&(Mat[w][z][y-1][x-1]==1)) count++;
                            if(((y-1)>=0)&&(Mat[w][z][y-1][x]==1)) count++;
                            if(((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z][y-1][x+1]==1)) count++;
                            if(((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w][z][y+1][x-1]==1)) count++;
                            if(((y+1)<=(XY-1))&&(Mat[w][z][y+1][x]==1)) count++;
                            if(((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[w][z][y+1][x+1]==1)) count++;
                            if(((x-1)>=0)&&(Mat[w][z][y][x-1]==1)) count++;
                            if(((x+1)<=(XY-1))&&(Mat[w][z][y][x+1]==1)) count++;
                            
                            if(count==3) MatFin[w][z][y][x] = 1;
                        }
                        else{
                            if(((w-1)>=0)&&((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z-1][y-1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y-1)>=0)&&(Mat[w-1][z-1][y-1][x]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z-1][y-1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w-1][z-1][y+1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w-1][z-1][y+1][x]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[w-1][z-1][y+1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z-1][y][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&(Mat[w-1][z-1][y][x]==1)) count++;
                            if(((w-1)>=0)&&((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z-1][y][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z+1][y-1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y-1)>=0)&&(Mat[w-1][z+1][y-1][x]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z+1][y-1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w-1][z+1][y+1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&(Mat[w-1][z+1][y+1][x]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w-1][z+1][y+1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((x-1)>=0)&&(Mat[w-1][z+1][y][x-1]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&(Mat[w-1][z+1][y][x]==1)) count++;
                            if(((w-1)>=0)&&((z+1)<=(Z-1))&&((x+1)<=(XY-1))&&(Mat[w-1][z+1][y][x+1]==1)) count++;
                            if(((w-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z][y-1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((y-1)>=0)&&(Mat[w-1][z][y-1][x]==1)) count++;
                            if(((w-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z][y-1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w-1][z][y+1][x-1]==1)) count++;
                            if(((w-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w-1][z][y+1][x]==1)) count++;
                            if(((w-1)>=0)&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w-1][z][y+1][x+1]==1)) count++;
                            if(((w-1)>=0)&&((x-1)>=0)&&(Mat[w-1][z][y][x-1]==1)) count++;
                            if(((w-1)>=0)&&(Mat[w-1][z][y][x]==1)) count++;
                            if(((w-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w-1][z][y][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z-1][y-1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y-1)>=0)&&(Mat[w+1][z-1][y-1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z-1][y-1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w+1][z-1][y+1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w+1][z-1][y+1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w+1][z-1][y+1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z-1][y][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&(Mat[w+1][z-1][y][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z-1][y][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z+1][y-1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y-1)>=0)&&(Mat[w+1][z+1][y-1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z+1][y-1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w+1][z+1][y+1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&(Mat[w+1][z+1][y+1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w+1][z+1][y+1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((x-1)>=0)&&(Mat[w+1][z+1][y][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&(Mat[w+1][z+1][y][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((z+1)<=(Z-1))&&((x+1)<=(XY-1))&&(Mat[w+1][z+1][y][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w+1][z][y-1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y-1)>=0)&&(Mat[w+1][z][y-1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w+1][z][y-1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w+1][z][y+1][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&((y+1)<=(XY-1))&&(Mat[w+1][z][y+1][x]==1)) count++;
                            if(((w+1)<=(W-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w+1][z][y+1][x+1]==1)) count++;
                            if(((w+1)<=(W-1))&&((x-1)>=0)&&(Mat[w+1][z][y][x-1]==1)) count++;
                            if(((w+1)<=(W-1))&&(Mat[w+1][z][y][x]==1)) count++;
                            if(((w+1)<=(W-1))&&((x+1)<=(XY-1))&&(Mat[w+1][z][y][x+1]==1)) count++;
                            if(((z-1)>=0)&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w][z-1][y-1][x-1]==1)) count++;
                            if(((z-1)>=0)&&((y-1)>=0)&&(Mat[w][z-1][y-1][x]==1)) count++;
                            if(((z-1)>=0)&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z-1][y-1][x+1]==1)) count++;
                            if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w][z-1][y+1][x-1]==1)) count++;
                            if(((z-1)>=0)&&((y+1)<=(XY-1))&&(Mat[w][z-1][y+1][x]==1)) count++;
                            if(((z-1)>=0)&&((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[w][z-1][y+1][x+1]==1)) count++;
                            if(((z-1)>=0)&&((x-1)>=0)&&(Mat[w][z-1][y][x-1]==1)) count++;
                            if(((z-1)>=0)&&(Mat[w][z-1][y][x]==1)) count++;
                            if(((z-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z-1][y][x+1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y-1)>=0)&&((x-1)>=0)&&(Mat[w][z+1][y-1][x-1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y-1)>=0)&&(Mat[w][z+1][y-1][x]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z+1][y-1][x+1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w][z+1][y+1][x-1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((y+1)<=(XY-1))&&(Mat[w][z+1][y+1][x]==1)) count++;
                            if(((z+1)<=(Z-1))&&(((y+1)<=(XY-1)))&&((x+1)<=(XY-1))&&(Mat[w][z+1][y+1][x+1]==1)) count++;
                            if(((z+1)<=(Z-1))&&((x-1)>=0)&&(Mat[w][z+1][y][x-1]==1)) count++;
                            if(((z+1)<=(Z-1))&&(Mat[w][z+1][y][x]==1)) count++;
                            if(((z+1)<=(Z-1))&&((x+1)<=(XY-1))&&(Mat[w][z+1][y][x+1]==1)) count++;
                            if(((y-1)>=0)&&((x-1)>=0)&&(Mat[w][z][y-1][x-1]==1)) count++;
                            if(((y-1)>=0)&&(Mat[w][z][y-1][x]==1)) count++;
                            if(((y-1)>=0)&&((x+1)<=(XY-1))&&(Mat[w][z][y-1][x+1]==1)) count++;
                            if(((y+1)<=(XY-1))&&((x-1)>=0)&&(Mat[w][z][y+1][x-1]==1)) count++;
                            if(((y+1)<=(XY-1))&&(Mat[w][z][y+1][x]==1)) count++;
                            if(((y+1)<=(XY-1))&&((x+1)<=(XY-1))&&(Mat[w][z][y+1][x+1]==1)) count++;
                            if(((x-1)>=0)&&(Mat[w][z][y][x-1]==1)) count++;
                            if(((x+1)<=(XY-1))&&(Mat[w][z][y][x+1]==1)) count++;
                            
                            if((count!=3)&&(count!=2)) MatFin[w][z][y][x] = 0;
                        }
                    }
                }
            }
        }
    }
    
    active = 0;
    for(int w=0; w<W; w++){
        for(int z=0; z<Z; z++){
            for(int y=0; y<XY; y++){
                for(int x=0; x<XY; x++){
                    if(MatFin[w][z][y][x]==1) active++;
                }
            }
        }
    }
    return active;
}

void letturaFILE(int Mat[Z][XY][XY]){
    int r;
    int c;
    char charLet;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    
    for(int z=0; z<Z; z++){
        for(int y=0; y<XY; y++){
            for(int x=0; x<XY; x++){
                Mat[z][y][x] = 0;
            }
        }
    }
    
    r = START_XYZ;
    c = START_XYZ;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet=='\n'){
            c = START_XYZ-1;
            r++;
        }else if(charLet==ATTIVO){
            Mat[START_XYZ][r][c] = 1;
        }
        c++;
    }
}

void letturaFILE_2(int Mat[W][Z][XY][XY]){
    int r;
    int c;
    char charLet;
    FILE* pFile;
    
    pFile = fopen(NOMEFILE, "r");
    for(int w=0; w<W; w++){
        for(int z=0; z<Z; z++){
            for(int y=0; y<XY; y++){
                for(int x=0; x<XY; x++){
                    Mat[w][z][y][x] = 0;
                }
            }
        }
    }
    
    r = START_XYZ;
    c = START_XYZ;
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet=='\n'){
            c = START_XYZ-1;
            r++;
        }else if(charLet==ATTIVO){
            Mat[START_W][START_XYZ][r][c] = 1;
        }
        c++;
    }
}

void stampaMAT(int Mat[Z][XY][XY], int AngNO){
    for(int z=AngNO; z<Z; z++){
        printf("lv: %d\n------------\n", z);
        for(int y=AngNO; y<(XY); y++){
            for(int x=AngNO; x<(XY); x++){
                printf("%d\t", Mat[z][y][x]);
            }
            printf("\n");
        }
    }
    
}

void stampaMAT_2(int Mat[W][Z][XY][XY], int AngNO){
    for(int y=AngNO; y<(XY); y++){
        for(int x=AngNO; x<(XY); x++){
            printf("%d\t", Mat[6][6][y][x]);
        }
        printf("\n");
    }
}

//copia Mat1 in Mat2...
void copyMAT(int Mat1[Z][XY][XY], int Mat2[Z][XY][XY]){
    for(int z=0; z<Z; z++){
        for(int y=0; y<XY; y++){
            for(int x=0; x<XY; x++){
                Mat2[z][y][x] = Mat1[z][y][x];
            }
        }
    }
}

void copyMAT_2(int Mat1[W][Z][XY][XY], int Mat2[W][Z][XY][XY]){
    for(int w=0; w<W; w++){
        for(int z=0; z<Z; z++){
            for(int y=0; y<XY; y++){
                for(int x=0; x<XY; x++){
                    Mat2[w][z][y][x] = Mat1[w][z][y][x];
                }
            }
        }
    }
}
