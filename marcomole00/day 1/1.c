#include <stdio.h>
#define DIM 200 //i've just read the number of rows in the text editor...

int prima_parte();
int seconda_parte(); 
// the solutions are just brute force with two and three for loops nested, can't think of anything better in C rn

int main()
{
FILE *fp;
fp = fopen("input.txt","r");

int input[200];
int i=0;
while (fscanf(fp,"%d",&input[i]) != EOF)
{
    //printf("%d\n", input[i]);
    i++;
}
printf("prima %d", prima_parte(input));
printf("secondo %d", seconda_parte(input));

}

int prima_parte(int *input)
{
    for(int i = 0;i<DIM;i++)
    {
        for(int j = i; j<DIM;j++)
        {
            if((input[i] + input[j]) == 2020)
            {
                return input[i]* input[j];
            }
        }
    }


}

int seconda_parte(int *input)
{
    for(int i = 0;i<DIM;i++)
    {
        for(int j = i; j<DIM;j++)
        {
            for (int k=j; k<DIM;k++)
            {
                if (input[j]+input[i]+input[k] == 2020)
                return input[i]* input[j]*input[k];
            }
        }
    }


}