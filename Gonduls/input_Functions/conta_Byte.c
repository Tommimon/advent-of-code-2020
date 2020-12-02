#include <stdio.h>
#define INPUT "/mnt/d/Pierluigi/programmazione/adventofcode/20/advent-of-code-2020/Gonduls/2/input.txt"

int main(){
    int c=1;
    int result=-1;
    FILE* input;
    input = fopen(INPUT, "r");

    while (c != EOF){
        c = fgetc(input);
        result ++;
    }
    fclose(input);
    printf("Numero totale di byte: %d\n", result);

    //for (c=0; c<256; c++){
    //    printf("Aschii #%d= %c", c, c);
    //    if (c=="\n")
    //        printf("\\n");
    //    printf("\n");
    //}
    return 0;
}