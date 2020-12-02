#include <stdio.h>
#define DIM 1000
int firstPart();
int secondPart();


int main()
{

printf(" prima parte = %d\n",firstPart());
printf("seconda parte = %d\n ", secondPart());

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
    fclose(fp);
    return result;
}
int secondPart()
{
    FILE *fp;
    fp = fopen("input.txt","r");
    int n1;
    int n2;
    char c;
    char string[20];
    int result = 0;

    while (fscanf(fp, "%d-%d %c: %s",&n1,&n2,&c,string ) != EOF)
    {
        printf("%d-%d %c: %s \n", n1,n2,c,string);
        if((string[n1-1]== c && string[n2-1] != c) ||  (string[n1-1]!= c && string[n2-1] == c)) result++; //it's just a dumbass xor

    }
    fclose(fp);

    return result;


}