
// i'm deeply embarassed by this code
// if you're conducting a search for hiring a cs engineer and you have stumbled upon this code, please, don't give me a job, i don't deserve it

/*new commit: cleaned up a little, still not a perfect solution but way better than that bodgy-ass looking code
also i removed any reference to the 44th president of the united states of america hitting on bisexual girls

*/
#include <stdio.h>
int main()
{
    FILE *fp;
    fp = fopen("input.txt","r");
    //firstPart(fp);
   
   char row[31];
    int index[5]={0,0,0,0,0};
    int xIncrement[5] = {1,3,5,7,1};
    int check = 1; // if check == -1 skip that bitch-ass row
    int indexCap;
    int result = 1;
    
    int nOfTrees[5] = {0,0,0,0,0};
    
    while(fscanf(fp, "%s",row)!= EOF)
    {
        for(int i = 0; i<5;i++)
        {
            if (index[i] >30 ) index[i] =  index[i]- 31;
        }
        
        if (check == 1)
        { 
            indexCap =5;
            check = -1;  
        }
        else
        {
            indexCap=4;
            check = 1;
        }
        
            for(int i =0; i<indexCap;i++)
            {
                if(row[index[i]] == '#') 
                {
                    nOfTrees[i]++;
                }
            }
            for (int j = 0;j<indexCap;j++)
            {
                index[j] = index[j]+ xIncrement[j];
            }

    } 

    for (int i = 0;i<5;i++)
    {
        result = result*nOfTrees[i];
    }
    
    printf("first part %d \n", nOfTrees[1]);
    printf("second part %d \n", result);
    fclose(fp);

}