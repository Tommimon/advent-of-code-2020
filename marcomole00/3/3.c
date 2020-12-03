#include <stdio.h>
#define OPEN '.'
#define TREE 
void firstPart();
int main()
{
    FILE *fp;
    fp = fopen("input.txt","r");
    firstPart(fp);
    fclose(fp);
}
void firstPart(FILE *fp)
{
    char row[31];
    int index=0;
    int nOfTrees=0;
    
    while(fscanf(fp, "%s",row)!= EOF)
    {
        if(index > 30) index = index - 31;
        if (row[index] == '#')
        { 
            nOfTrees++;
        }
        index = index +3;
    } 
    printf("number of trees = %d \n", nOfTrees);

}