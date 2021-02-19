#include<stdio.h>
#include<stdlib.h>

#define INPUT "input2.txt"
#define MAX_LENGHT_STRING 12

typedef struct el{
    int value;
    struct el *next;
}card;
typedef card* pcard;

typedef struct elem{
    pcard passage;
    struct elem *next;
}passages;


int conversion(char* string);
pcard last(pcard start);
void print_all(pcard start);
void init(pcard* player1, FILE* input);
int play(pcard* player1, pcard* player2);
void add(pcard* player, pcard to_add);
int count_points(pcard player);
int lenght(pcard player);
void copy(pcard *player, int cards, pcard** destination);
int confront(passages *done, pcard steps);
void empty(passages *steps);

int main(int argc, char *argv[]){
    int winner, result;
    pcard me=NULL, crab=NULL;
    FILE* input= fopen(INPUT, "r");
    init(&me, input);
    init(&crab, input);
    fclose(input);
    winner = play(&me, &crab);
    // Using 'winner' as bool: winner == 0 => I (player 1) won, else crab (player 2) won
    if(winner)
        result = count_points(crab);
    else
        result = count_points(me);
    printf("result = %d\n", result);
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
        printf("%d, ", start->value);
        start = start->next;
    }
    printf("\n");
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

void add(pcard* player, pcard to_add){
    pcard punt;
    punt = last(*player);
    to_add->next = NULL;
    punt->next = to_add;
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

//copies n(cards) cards starting from player
void copy(pcard *player, int cards, pcard** destination){
    pcard punt;
    int i;
    (**destination) = malloc(sizeof(card));
    (**destination)->value = (*player)->value;
    (**destination)->next = NULL;
    punt = (**destination);
    for (i = 0; i<cards - 1; i++){
        (*player) = (*player)->next;
        punt->next = malloc(sizeof(card));
        punt = punt->next;
        punt->value = (*player)->value;
        punt->next = NULL;
    }
}

// returns 1 if steps was found in done
int confront(passages *done, pcard steps){
    passages *ppunt, *end;
    pcard punt, punt_steps;
    ppunt = done;
    while(ppunt != NULL){

        // I need to remember the last element in list so that I can eventually add steps to done afterwards
        if(ppunt->next == NULL)
            end = ppunt;

        // Have to initialize both decks of cards that have to be confronted
        // ppunt changes, steps doesn't
        punt = (*ppunt).passage;
        punt_steps = steps;

        // If they have different lenghts there is no point in confronting them
        if(lenght(punt) == lenght(punt_steps)){
            while(punt!=NULL){
                if(punt->value != punt_steps->value)
                    break;
                punt = punt->next;
                punt_steps = punt_steps->next;
            }
            // If i've completed a whole cicle without braking, steps was found in done
            if(punt==NULL)
                return 1;
        }
        // ppunt changes every time so that I check all states of the deck
        ppunt = (*ppunt).next;
    }
    end->next = malloc(sizeof(passages));
    end = end->next;
    end->next = NULL;
    end->passage = steps;
    return 0;
}

void empty(passages *steps){
    passages *pppunt;
    pcard punt1, punt2;
    pppunt = steps;
    while (pppunt != NULL){
        punt1 = pppunt->passage;
        if(punt1 == NULL){
            continue;
        }
        punt2 = punt1->next;
        while(punt2 != NULL){
            free(punt1);
            punt1 = punt2;
            punt2 = punt1->next;
        }

        pppunt = steps->next;
        free(steps);
        steps = pppunt;
    }
}

// now a recursive function, return 0 = player1 won, return 1 = player2 won
int play(pcard* player1, pcard* player2){
    pcard punt;
    passages * pl1_moves, * pl2_moves;
    passages *cleanup;
    pcard *sub_pl1, *sub_pl2;
    int winner, subgame = 0;

    //I have to initialize passages with first state
    pl1_moves = malloc(sizeof(passages));
    pl1_moves->next = NULL;
    pl1_moves->passage = *player1;
    pl2_moves = malloc(sizeof(passages));
    pl2_moves->next = NULL;
    pl2_moves->passage = *player2;

    // using lenght 0 as False - if a player doesn't have any more cards he lost
    while(lenght(*player1) && lenght(*player2)){
        printf("Player 1:\n");
        print_all(*player1);
        printf("Player 2:\n");
        print_all(*player2);
        printf("\n");
        if((*player1)->value < lenght(*player1) && (*player2)->value < lenght(*player2)){
            copy(&((*player1)->next), (*player1)->value, &sub_pl1);
            copy(&((*player2)->next), (*player2)->value, &sub_pl2);
            // winner determins who gets the card
            winner = play(sub_pl1, sub_pl2);
            subgame = 1;
            // I have to cleanup all the mallocs created by copy
            cleanup = malloc(sizeof(passages));
            cleanup->passage = (*sub_pl1);
            cleanup->next = malloc(sizeof(passages));
            cleanup->next->next = NULL;
            cleanup->next->passage = (*sub_pl2);
            //empty(cleanup);
        }
        else if((*player1)->value > (*player2)->value)
            winner = 0;
        else
            winner = 1;
        printf("\t%d\n", winner);
        if (winner){
            punt = (*player2);
            (*player2) = punt->next;
            add(player2, punt);
            punt = (*player1);
            (*player1) = punt->next;
            add(player2, punt);
        }
        else{
            punt = (*player1);
            (*player1) = punt->next;
            add(player1, punt);
            punt = (*player2);
            (*player2) = punt->next;
            add(player1, punt);
        }
        // have to check if I've entered a loop and to keep updated passages, confront returns 1 if steps in done
        if ((confront(pl1_moves, *player1) && confront(pl2_moves, *player2) && subgame == 0)){
            printf("\tENDED\n");
            empty(pl1_moves);
            empty(pl2_moves);
            // If a loop occured player 1 automatically wins
            return(0);
        }
        subgame = 0;
    }
    empty(pl1_moves);
    empty(pl2_moves);
    if(lenght(*player1))
        return 0;
    return 1;
}

/*int play(pcard* player1, pcard* player2){
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
    return(0);
}
*/
