//Shortest c program I could get, WITHOUT CHEATING.
#include<stdio.h>

char input[10013];
long long int trees(int x,int y) {
    long long int p, rv, i; 
    rv = p = i = 0;
    while (p < 10013) {
        if (input[p] == '#') rv++; 
        i++;
        p = 31*i*y + (i*(x+31*y))%31;
    }
    return rv;
}
int main() {
    int i = 0;
    char c;
    FILE *fp = fopen("input.txt","r");
    while((c = fgetc(fp)) != EOF) {
        if(c != '\n') {
            input[i] = c; 
            i++;
        }
    }
    printf("Part 1: %lld\nPart 2: %lld", trees(3,1), trees(1,1)*trees(3,1)*trees(5,1)*trees(7,1)*trees(1,2));
}