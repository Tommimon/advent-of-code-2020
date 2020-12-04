//This is what hell is made of [NSFL Warning]

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int flagCID = 0;
int gCounter = 0;

char list[8][4] = {
    "byr","iyr","eyr","hgt","hcl","ecl","pid","cid"
};

int validate(char fid[], char value[]) {

    int i, year, rv, height;
    char *indx1, *indx2;
    char elist[7][4] = {"amb","blu","brn","gry","grn","hzl","oth"};

    for(i=0;i<8;i++) {
        if(strcmp(fid, list[i]) == 0) break;
    }
    switch(i) {
        case 0:     //byr
            year = atoi(value);
            rv = ((year>=1920) && (year<=2002)) ? 1 : 0;
            return rv;
        case 1:     //iyr
            year = atoi(value);
            rv = ((year>=2010) && (year<=2020)) ? 1 : 0;
            return rv;
        case 2:     //eyr
            year = atoi(value);
            rv = ((year>=2020) && (year<=2030)) ? 1 : 0;
            return rv;
        case 3:     //hgt, the most convoluted i could make it
            if (((indx1 = strchr(value, 'c')) != NULL) != ((indx2 = strchr(value, 'i')) != NULL)) {
                if(indx2 != NULL) indx1 = indx2;
                char heightS[10];
                for(i=0;&value[i]!=indx1;i++) {
                    heightS[i] = value[i];
                }
                heightS[i] = '\0';
                height = atoi(heightS);
                if (*indx1 == 'c') {
                    rv = ((height>=150) &&  (height<=193)) ? 1 : 0;
                    return rv;
                } else if (*indx1 == 'i') {
                    rv = ((height>=59) &&  (height<=76)) ? 1 : 0;
                    return rv;
                }
            }
            return 0;
        case 4:     //hcl
            if(value[0] != '#') return 0;
            for(int i=1;i<7;i++) {
                if (!(((value[i]>=48) && (value[i]<=57)) || ((value[i]>=97) && (value[i]<=102)))) return 0;
            }
            return 1;
        case 5:     //ecl
            for(int i=0;i<7;i++) {
                if(strcmp(value, elist[i]) == 0) return 1;
            }
            return 0;
        case 6:     //pid
            for(int i=0;i<9;i++) {
                if(!((value[i]>=48) && (value[i]<=57))) return 0;
            }
            if(value[9] != '\0') return 0;
            return 1;
        case 7:     //cid
            flagCID = 1;
            return 1;
    }
}



int main() {
    
    int fieldCount = 0;
    //Open the file and variable declaration
    FILE *fp = fopen("input.txt", "r");

    //I suggest if you are faint of heart or a usual python programmer to not look beyond this point
    //Doing what I did to read a file is like driving through a kindergarden to reach a park down the road
    //This is the only way that I can read the ID and the value as separate strings, therefore
    //please excuse my killing spree

    //id is field id, val is the field value, c is used to determine wether or not there's a new passport
    char id[4], val[20], c;
    while(fscanf(fp, "%c%c%c:%s", &id[0], &id[1], &id[2], val) != EOF) {
        id[3]='\0';

        printf("%s: %s", id, val);
        
        //For output, [o] is correct, [x] is not
        int result = validate(id, val);
        if(result==1) printf("\t[O]\n");
        if(result==0) printf("\t[X]\n");
        fieldCount += result;

        //New passport check
        c = fgetc(fp);
        if(c == '\n') {
            c = fgetc(fp);
            if(c == '\n') {
                printf("\nFieldCount: %d, ", fieldCount);
                if (fieldCount == 8 || (fieldCount == 7 && flagCID == 0)) {
                    printf("passport is valid. Glory to Arstotzka\n\n");
                    gCounter++;
                } else {
                    printf("passport invalid. You are under arrest\n\n");
                }
                fieldCount = 0;
                flagCID = 0;

            } else {
                fseek(fp, -1L, SEEK_CUR);
            }
        }
    }
    
    printf("\nFieldCount: %d, ", fieldCount);
    if (fieldCount == 8 || (fieldCount == 7 && flagCID == 0)) {
        printf("passport is valid. Glory to Arstotzka\n\n");
        gCounter++;
    } else {
        printf("passport invalid. You are under arrest\n\n");
    }

    printf("\n-----------------------\nPassports valid: %d", gCounter);

    fclose(fp);
    return 0;
    
}