#include<stdio.h>
#include<stdlib.h>

#define INPUT "input.txt"
#define MAX_LENGHT_STRING 12

typedef struct el{
    int value;
    struct el *next;
}card;

typedef card* pcard;


int conversion(char* string);
pcard last(pcard start);
void print_all(pcard start);
void init(pcard* player1, FILE* input);
int play(pcard* player1, pcard* player2);
void add(pcard* player, pcard to_add);
int count_points(pcard player);
int lenght(pcard player);

int main(int argc, char *argv[]){
    pcard me=NULL, crab=NULL;
    FILE* input= fopen(INPUT, "r");
    init(&me, input);
    init(&crab, input);
    fclose(input);
    printf("result = %d\n", play(&me, &crab));
    return 0;
}

int conversion(char* string){
    if(string[0]<'0' || string[0]>'9')
        return -1;
    if(conversion(string + 1)<0)
        return (string[0]-'0');
    else
        return ((string[0]-'0')*10 + conversion(string + 1));
}

pcard last(pcard start){
    pcard punt = start;
    if (start == NULL)
        return (NULL);
    while(punt->next != NULL)
        punt = punt->next;
    return(punt);
}

void print_all(pcard start){
    while(start != NULL){
        printf("%d\n", start->value);
        start = start->next;
    }
}

void init(pcard* player1, FILE* input){
    char string[MAX_LENGHT_STRING];
    pcard punt;
    int check = 0;

    // discard the sentence "Player" an then the sentence 1: or 2:, 
    // in player 2: player has already been read by previous init
    fscanf(input, "%s", string);
    fscanf(input, "%s", string);
    if(string[1] == ':')
        fscanf(input, "%s", string);

    // initialize the head of the list
    (*player1) = malloc(sizeof(card));
    (*player1)->value = conversion(string);
    (*player1)->next = NULL;

    // get all the remaining values
    punt = (*player1);
    fscanf(input, "%s", string);
    while(conversion(string)>0 && check != EOF){
        punt->next=malloc(sizeof(card));
        punt = punt->next;
        punt->value = conversion(string);
        punt->next = NULL;
        check = fscanf(input, "%s", string);
    }
}

int lenght(pcard player){
    int i = 0;
    while(player != NULL){
        i++;
        player = player->next;
    }
    return i;
}

int count_points(pcard player){
    int result = 0;
    int len = lenght(player);
    for (; len>0; len--){
        result += len*player->value;
        player = player->next;
    }
    return result;
}

int play(pcard* player1, pcard* player2){
    pcard punt;
    // using lenght 0 as False
    while(lenght(*player1) && lenght(*player2)){
        if((*player1)->value > (*player2)->value){
            punt = (*player1);
            (*player1) = punt->next;
            add(player1, punt);
            punt = (*player2);
            (*player2) = punt->next;
            add(player1, punt);
            continue;
        }
        punt = (*player2);
        (*player2) = punt->next;
        add(player2, punt);
        punt = (*player1);
        (*player1) = punt->next;
        add(player2, punt);
    }
    return(count_points(*player2) + count_points(*player1));
}

void add(pcard* player, pcard to_add){
    pcard punt;
    punt = last(*player);
    to_add->next = NULL;
    punt->next = to_add;
}