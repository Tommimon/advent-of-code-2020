//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 18/12/20.
//

#include <stdio.h>
#include <math.h>
#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_18/AoC/AoC/input.c"
#define LUNG 1000
#define MAX 1000
#define ALT 374

typedef struct{
    int tipo; //parentesi 1; operatore 2; numero: 0;
    char parentesi;
    char operatore;
    long long int num;
}Elemento;

typedef struct{
    Elemento El[MAX];
    int NumEle;
}Espress;

void readFile(char Espression[ALT][LUNG]);
void stampaFile(char Espression[ALT][LUNG], int i);
int calcola(char Espr[LUNG],int pos);
long long int ValutaEspressione(Espress *esp);
long long int Calcola(long long int Num1, long long int Num2, char op);
void Sostituisci(Espress *esp, int Posizione);
void Sostituisci_2(Espress *esp, int Posizione);
long long int ValutaEspressione(Espress *esp);
long long int DAY18(char Espression[ALT][LUNG],int pos);

int main(){
    char Espression[ALT][LUNG];
    readFile(Espression);
    
    printf("\nIl risultato è: %lld", DAY18(Espression, 0));
    
    return 0;
}

long long int DAY18(char Espr[ALT][LUNG],int pos){
    long long int sum;
    int c;
    int i;
    int NumTemp;
    int CloneC;
    Espress Espressione;

    sum = 0;
    for(int r=0; r<ALT; r++){
        stampaFile(Espr, r);
        Espressione.NumEle=0;
        //Ciclo per il passaggio dei valori dalla String temporanea alla Lista Squenziale Espressioen
        c=0;
        CloneC=0;
        while((Espr[r][c]!='\0')){
            //Controllo se l'elemento è una parentesi
            if(('('==Espr[r][c])||(')'==Espr[r][c])){
                if('('==Espr[r][c]){
                    Espressione.El[CloneC].tipo = 1;
                    Espressione.El[CloneC].parentesi = '(';
                    ++Espressione.NumEle;
                }
                else if(')'==Espr[r][c]){
                    Espressione.El[CloneC].tipo = 1;
                    Espressione.El[CloneC].parentesi = ')';
                    ++Espressione.NumEle;
                }
            }
            //Controllo se l'elemento è un operatore
            else if(('+'==Espr[r][c])||('*'==Espr[r][c])){
                if('+'==Espr[r][c]){
                    Espressione.El[CloneC].tipo = 2;
                    Espressione.El[CloneC].operatore = '+';
                    ++Espressione.NumEle;
                }else if('*'==Espr[r][c]){
                    Espressione.El[CloneC].tipo = 2;
                    Espressione.El[CloneC].operatore = '*';
                    ++Espressione.NumEle;
                }
            }
            //Controllo se l'elemento è un numero
            else if((Espr[r][c]>='0')&&(Espr[r][c]<='9')){
                i = 0;
                NumTemp = 0;
                //Ciclo per l'unione delle cifre nel numero
                while(((Espr[r][c+i]>='0')&&(Espr[r][c+i]<='9'))&&(Espr[r][c+i]!='\0')){
                    NumTemp = NumTemp*10+(Espr[r][c+i]-'0');
                    ++i;
                }
                --i;
                Espressione.El[CloneC].tipo = 0;
                Espressione.El[CloneC].num = NumTemp;
                ++Espressione.NumEle;
            }
            c = (c+i)+1;
            ++CloneC;
        }
        printf("\n--- %lld ---\n", ValutaEspressione(&Espressione));
        sum = sum + ValutaEspressione(&Espressione);
    }
    return sum;
}

void readFile(char Espression[ALT][LUNG]){
    int r;
    int c;
    char charLet;
    FILE* pFile;
    
    r = 0;
    c = 0;
    pFile =  fopen(NOMEFILE, "r");
    while(fscanf(pFile, "%c", &charLet)!=EOF){
        if(charLet==' '){
        }else if(charLet=='\n'){
            Espression[r][c] = '\0';
            r++;
            c = 0;
        }else{
            Espression[r][c] = charLet;
            c++;
        }
    }
}

void stampaFile(char Espression[ALT][LUNG], int i){
//    for(int i=0; i<ALT; i++){
        printf("%s\n", Espression[i]);
//    }
}

long long int ValutaEspressione(Espress *esp){
    int scorEspress;
    scorEspress = 0;
    while(esp->NumEle!=1){
        //MODIFICA A SECONDA SE PARTE DUE O UNO
        Sostituisci_2(esp, scorEspress);
    }
    return esp->El[0].num;
}

void Sostituisci(Espress *esp, int Posizione){
    int countSpost;
    if(esp->El[Posizione].tipo==1){
        if(esp->El[Posizione].parentesi=='('){
            if((esp->El[Posizione+4].tipo==1)&&(esp->El[Posizione+4].parentesi==')')){
                esp->El[Posizione].tipo = 0;
                esp->El[Posizione].num = Calcola(esp->El[Posizione+1].num, esp->El[Posizione+3].num, esp->El[Posizione+2].operatore);
                for(countSpost=(Posizione+1); countSpost<esp->NumEle; countSpost++){
                    esp->El[countSpost]=esp->El[countSpost+4];
                }
                esp->NumEle = esp->NumEle-4;
            }else if((esp->El[Posizione+3].tipo==1)&&(esp->El[Posizione+3].parentesi=='(')){
                Sostituisci(esp, Posizione+3);
                ValutaEspressione(esp);
            }else if(esp->El[Posizione+3].tipo==0){
                esp->El[Posizione+1].num = Calcola(esp->El[Posizione+1].num, esp->El[Posizione+3].num, esp->El[Posizione+2].operatore);
                for(countSpost=(Posizione+2); countSpost<esp->NumEle; countSpost++){
                    esp->El[countSpost]=esp->El[countSpost+2];
                }
                esp->NumEle = esp->NumEle-2;
            }else{
                Sostituisci(esp, Posizione+1);
                ValutaEspressione(esp);
            }
        }
    }else if(esp->El[Posizione].tipo==0){
        if((esp->El[Posizione+2].tipo==1)&&(esp->El[Posizione+2].parentesi=='(')){
            Sostituisci(esp, Posizione+2);
            ValutaEspressione(esp);
        }else if(esp->El[Posizione+2].tipo==0){
            esp->El[Posizione].tipo = 0;
            esp->El[Posizione].num = Calcola(esp->El[Posizione].num, esp->El[Posizione+2].num, esp->El[Posizione+1].operatore);
            for(countSpost=(Posizione+1); countSpost<esp->NumEle; countSpost++){
                esp->El[countSpost]=esp->El[countSpost+2];
            }
            esp->NumEle = esp->NumEle-2;
        }
    }
}

void Sostituisci_2(Espress *esp, int Posizione){
    int check;
    int precedenza;
    int countSpost;
    if(esp->El[Posizione].tipo==1){
        if(esp->El[Posizione].parentesi=='('){
            if((esp->El[Posizione+4].tipo==1)&&(esp->El[Posizione+4].parentesi==')')){
                esp->El[Posizione].tipo = 0;
                esp->El[Posizione].num = Calcola(esp->El[Posizione+1].num, esp->El[Posizione+3].num, esp->El[Posizione+2].operatore);
                for(countSpost=(Posizione+1); countSpost<esp->NumEle; countSpost++){
                    esp->El[countSpost]=esp->El[countSpost+4];
                }
                esp->NumEle = esp->NumEle-4;
            }else if((esp->El[Posizione+3].tipo==1)&&(esp->El[Posizione+3].parentesi=='(')){
                Sostituisci_2(esp, Posizione+3);
                ValutaEspressione(esp);
            }else if(esp->El[Posizione+3].tipo==0){
                if((esp->El[Posizione+2].tipo==2)&&(esp->El[Posizione+2].operatore=='+')){
                    esp->El[Posizione+1].num = Calcola(esp->El[Posizione+1].num, esp->El[Posizione+3].num, esp->El[Posizione+2].operatore);
                    for(countSpost=(Posizione+2); countSpost<esp->NumEle; countSpost++){
                        esp->El[countSpost]=esp->El[countSpost+2];
                    }
                    esp->NumEle = esp->NumEle-2;
                }else if((esp->El[Posizione+2].tipo==2)&&(esp->El[Posizione+2].operatore=='*')){
                    check = 1;
                    for(int i=(Posizione+2); (esp->El[i].tipo==2)&&(check==1); i=i+2){
                        if(esp->El[i].operatore=='+') check = 0;
                        precedenza = i;
                    }
                    if(check==1){
                        esp->El[Posizione+1].num = Calcola(esp->El[Posizione+1].num, esp->El[Posizione+3].num, esp->El[Posizione+2].operatore);
                        for(countSpost=(Posizione+2); countSpost<esp->NumEle; countSpost++){
                            esp->El[countSpost]=esp->El[countSpost+2];
                        }
                        esp->NumEle = esp->NumEle-2;
                    }else{
                        Sostituisci_2(esp, precedenza-1);
                        ValutaEspressione(esp);
                    }
                }
            }else{
                Sostituisci_2(esp, Posizione+1);
                ValutaEspressione(esp);
            }
        }
    }else if(esp->El[Posizione].tipo==0){
        if((esp->El[Posizione+2].tipo==1)&&(esp->El[Posizione+2].parentesi=='(')){
            Sostituisci_2(esp, Posizione+2);
            ValutaEspressione(esp);
        }else if(esp->El[Posizione+2].tipo==0){
            if((esp->El[Posizione+1].tipo==2)&&(esp->El[Posizione+1].operatore=='+')){
                esp->El[Posizione].num = Calcola(esp->El[Posizione].num, esp->El[Posizione+2].num, esp->El[Posizione+1].operatore);
                for(countSpost=(Posizione+1); countSpost<esp->NumEle; countSpost++){
                    esp->El[countSpost]=esp->El[countSpost+2];
                }
                esp->NumEle = esp->NumEle-2;
            }else if((esp->El[Posizione+1].tipo==2)&&(esp->El[Posizione+1].operatore=='*')){
                check = 1;
                for(int i=(Posizione+1); (esp->El[i].tipo==2)&&(check==1); i=i+2){
                    if(esp->El[i].operatore=='+') check = 0;
                    precedenza = i;
                }
                if(check==1){
                    esp->El[Posizione].num = Calcola(esp->El[Posizione].num, esp->El[Posizione+2].num, esp->El[Posizione+1].operatore);
                    for(countSpost=(Posizione+1); countSpost<esp->NumEle; countSpost++){
                        esp->El[countSpost]=esp->El[countSpost+2];
                    }
                    esp->NumEle = esp->NumEle-2;
                }else{
                    Sostituisci_2(esp, precedenza-1);
                    ValutaEspressione(esp);
                }
            }
        }
    }
}

long long int Calcola(long long int Num1,long long int Num2, char op){
    long long int risultato;
    if(op=='+') risultato = Num1 + Num2;
    else if(op=='*') risultato = Num1 * Num2;
    
    return risultato;
}
