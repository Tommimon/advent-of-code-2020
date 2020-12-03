
// i'm deeply embarassed by this code
// if you're conducting a search for hiring a cs engineer and you have stumbled upon this code, please, don't give me a job, i don't deserve it
#include <stdio.h>
int main()
{
    FILE *fp;
    fp = fopen("input.txt","r");
    //firstPart(fp);
   
   char row[31];
    int index[5]={0,0,0,0,0};
    int xIncrement[4] = {1,3,5,7};
    
    int nOfTrees[5] = {0,0,0,0,0};
    
    while(fscanf(fp, "%s",row)!= EOF)
    {
        for(int i = 0; i<4;i++)
        {
            if (index[i] >30 ) index[i] =  index[i]- 31;
        }
        for(int i =0; i<4;i++)
        {
            if(row[index[i]] == '#') 
            {
                nOfTrees[i]++;
            }
        }
        for (int j = 0;j<4;j++)
        {
            index[j] = index[j]+ xIncrement[j];
        }

    } 
    rewind(fp);
    int i = 0;
    int check = 1; // if check == -1 skip that bitch-ass row
    int obamaHittingBisexuals = 0;
    while(fscanf(fp,"%s",row) != EOF)
    {
       if (i>30) i = i -31;
        if (check == 1)
        {
            if(row[i] == '#') obamaHittingBisexuals++;
            i++;
            check = -1;

        }
        else if (check == -1)
        {
            check = 1;
        }
        
    }
    long ao = 1;
    for(int i =0; i<4;i++)
    {
         ao = ao * nOfTrees[i];
         printf("\n %d \n ", nOfTrees[i]);
    }
    ao = ao*obamaHittingBisexuals;
    printf(" valore %ld \n ", ao);
    fclose(fp);

}