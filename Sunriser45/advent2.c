#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAXLUNGH 50
#define LUNGHFILE 1000
//commento

int main()
{	
	int primo, secondo, match, password=0, cont=0;
	char confronto, stringa[MAXLUNGH];

		
	while (cont<1000)
	{

		scanf("%d-%d %c: %s",&primo, &secondo, &confronto, stringa);

		match=0;
		

	

		
		if(stringa[primo-1]!=stringa[secondo-1])
		{
			if(stringa[primo-1]==confronto||stringa[secondo-1]==confronto)
			{
				password++;
			}

		}

		cont++;

	}
printf("Il numero di password è %d", password);
		
		





}