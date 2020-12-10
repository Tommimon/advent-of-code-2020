#include <stdio.h>
#include <stdlib.h>

#define MAXCHAR 200

int main()
{
	int addendo[MAXCHAR], somma, cont1, cont2, cont3;
	cont1=0;
	cont2=0;
	cont3=0;
	char line[MAXCHAR];	
	somma=0;
	
	FILE *fileinput =fopen("input.txt", "r");

	while (cont1<200&&somma!=2020)
	{

				fgets(line,100, fileinput);
				addendo[cont1]= atoi(line);
				cont1++;
				


	}

	cont1=0;

	while (cont1<200&&somma!=2020)
	{
			

			cont2=cont1;
		while (cont2<200&&somma!=2020)
		{	
			cont3=cont2;
			while(cont3<200&&somma!=2020)
			{
			somma=addendo[cont1]+addendo[cont2]+addendo[cont3];
			cont3++;
			}
			cont2++;

		}

		cont1++;


	}


	printf("Gli addendi sono %d,%d e %d eil loro prodotto %d", addendo[cont1-1], addendo[cont2-1], addendo[cont3-1], addendo[cont1-1]*addendo[cont2-1]*addendo[cont3-1]);
}