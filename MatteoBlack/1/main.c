//
//  main.c
//  AoC
//
//  Created by Matteo Negro on 01/12/20.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NOMEFILE "/Users/matteoblack/Desktop/AoC/AoC_1/AoC/input.txt"
#define ANNO 2020

typedef struct EL{
    int Numero;
    struct EL* pNext;
}NumeroList;

typedef NumeroList* ListaNum;

//Funz Lettura File
ListaNum LetturaFile(void);
//Stampa Lista
void StampaLista(ListaNum pListaStamp);
//Funz DAY1_1, cerca due val che sommati facciano 2020 e moltiplicali tra loro
int DAY1_1(ListaNum pLista);
//Funz DAY1_2, cerca tre val che sommati facciano 2020 e moltiplicali tra loro
int DAY1_2(ListaNum pLista);

int main() {
    ListaNum pListaFile;
    int result;
    
    pListaFile = LetturaFile();
    StampaLista(pListaFile);
    result = DAY1_2(pListaFile);
    printf("\nIl risultato è: %d\n", result);
    
    return 0;
}

ListaNum LetturaFile(){
    ListaNum pLista;
    ListaNum pNuovoElem;
    ListaNum pPrec;
    int val;
    int c;
    
    FILE* pFile;
    pPrec = NULL;
    pLista = NULL;
    
    pFile = fopen(NOMEFILE, "r");
    if(pFile == NULL){
        printf("Errore in APERTURA");
    }else{
        c = 0;
        
        //Fai la ptima lettura
        fscanf(pFile, "%d", &val);
        pLista = malloc(sizeof(NumeroList));
        pLista->Numero = val;
        pNuovoElem = malloc(sizeof(NumeroList));
        pLista->pNext = pNuovoElem;

        //Ciclo lettura del File
        while((fscanf(pFile, "%d", &val))!=EOF){
            pNuovoElem->Numero = val;
            pNuovoElem->pNext = malloc(sizeof(NumeroList));
            pPrec = pNuovoElem;
            pNuovoElem = pNuovoElem->pNext;
        }
        //Segno la fine della lista e cancello elemento in più
        pPrec->pNext = NULL;
        free(pNuovoElem);
    }
    fclose(pFile);
    return pLista;
}

void StampaLista(ListaNum pListaStamp){
    ListaNum pCurr;
    pCurr = pListaStamp;
    int c = 1;
    printf("\nLista Num: \n\n");
    while(pCurr!=NULL){
        printf("%d- ",c);
        printf("%d\n", pCurr->Numero);
        pCurr = pCurr->pNext;
        c++;
    }
}

int DAY1_1(ListaNum pLista){
    int day1;
    int sum;
    int END;
    int in;
    int ext;
    ListaNum pCurrEXT;
    ListaNum pCurrIN;
    
    day1 = 0;
    ext = 1;
    END = 0;
    pCurrEXT = pLista;

    while((pCurrEXT!=NULL)&&(END == 0)){
        in = 1;
        pCurrIN = pLista;
        while((pCurrIN!=NULL)&&(END == 0)){
            if(in==ext) break;
            sum = (pCurrEXT->Numero) + (pCurrIN->Numero);
            if(sum == ANNO){
                printf("%d.%d - SUM = %d + %d = %d\n", ext, in, pCurrEXT->Numero,pCurrIN->Numero, sum);
                day1 = (pCurrEXT->Numero) * (pCurrIN->Numero);
                END = 1;
                break;
            }
            pCurrIN = pCurrIN->pNext;
            in++;
        }
        pCurrEXT = pCurrEXT->pNext;
        ext++;
    }
    return day1;
}

int DAY1_2(ListaNum pLista){
    int day1;
    int sum;
    int END;
    int in;
    int ext;
    int mid;
    ListaNum pCurrEXT;
    ListaNum pCurrIN;
    ListaNum pCurrMID;
    
    day1 = 0;
    ext = 1;
    END = 0;
    pCurrEXT = pLista;

    while((pCurrEXT!=NULL)&&(END == 0)){
        mid = 1;
        pCurrMID = pLista;
        while((pCurrMID!=NULL)&&(END == 0)){
            in = 1;
            if(in==ext) break;
            pCurrIN = pLista;
            while((pCurrIN!=NULL)&&(END == 0)){
                if((in==mid)||(ext==mid)) break;
                sum = (pCurrEXT->Numero) + (pCurrIN->Numero) + (pCurrMID->Numero);
                if(sum == ANNO){
                    printf("%d.%d.%d - SUM = %d + %d + %d = %d\n", ext, mid, in, pCurrEXT->Numero, pCurrIN->Numero, pCurrMID->Numero, sum);
                    day1 = (pCurrEXT->Numero) * (pCurrIN->Numero) * (pCurrMID->Numero);
                    END = 1;
                    break;
                }
                pCurrIN = pCurrIN->pNext;
                in++;
            }
            pCurrMID = pCurrMID->pNext;
            mid++;
        }
        pCurrEXT = pCurrEXT->pNext;
        ext++;
    }
    return day1;
}
