#include <stdio.h>
void solution();

int main()
{

solution();
}

void solution()
{
    FILE *fp;
    fp = fopen("input.txt","r");
    int n1;
    int n2;
    char c;
    char string[20];
    int numberOfOccurences;
    int result1 = 0;
    int result2 = 0;

    while (fscanf(fp, "%d-%d %c: %s",&n1,&n2,&c,string ) != EOF)
    {
        numberOfOccurences = 0;
        //printf("%d-%d %c: %s \n", n1,n2,c,string); debug
        for (int i =0; string[i]!='\0';i++)
        {
            if(string[i] == c) numberOfOccurences++;
        }
        if(numberOfOccurences >= n1 && numberOfOccurences <= n2) result1++; // solution of the first part

        if((string[n1-1]== c && string[n2-1] != c) ||  (string[n1-1]!= c && string[n2-1] == c)) result2++; //it's just a dumbass xor(second part)
    }
    printf(" first part  = %d\n", result1);
    printf(" second part  = %d\n", result2);
    fclose(fp);
    return ;
}
