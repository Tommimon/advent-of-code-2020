#include <stdio.h>
#define DIM 1000
int firstPart();


int main()
{

printf("%d",firstPart());

}

// 1-13 r: gqdrspndrpsrjfjx

int firstPart()
{
    FILE *fp;
    fp = fopen("input.txt","r");
    int n1;
    int n2;
    char c;
    char string[20];
    int numberOfOccurences;
    int result = 0;

    while (fscanf(fp, "%d-%d %c: %s",&n1,&n2,&c,string ) != EOF)
    {
        numberOfOccurences = 0;
        //printf("%d-%d %c: %s \n", n1,n2,c,string); debug
        for (int i =0; string[i]!='\0';i++)
        {
            if(string[i] == c) numberOfOccurences++;
        }
        if(numberOfOccurences >= n1 && numberOfOccurences <= n2) result++;

    }
    return result;
}
