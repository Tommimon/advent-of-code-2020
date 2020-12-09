#include<stdio.h>

int main() {
    long long int arr[1000], i, *s, *e, *j, *k, f, res, m, M, c;
    FILE *fp = fopen("input.txt", "r");
    for(i=0;(fscanf(fp,"%lld",&arr[i])!=EOF);i++);
    for(s=arr,e=s+24;e!=arr+1000;s++,e++,f=0) { 
        for(j=s,k=s;j!=e;f=0,k++) {
            if(*j+*k==*(e+1) && j!=k) {f=1; break;}
            if(k==e) {j++;k=s-1;}
        }
        if(f==0) break;
    }
    res = *(e+1);
    printf("Part 1: %lld\n", res);
    for(s=j=arr,m=M=*s,c=0;c!=res;c+=*j,j++) {
        if(c>res) {s++;c=0;j=s;m=M=*s;}
        if(*j<m) m=*j;
        if(*j>M) M=*j;   
    }
    printf("Part 2: %lld", m+M);
    fclose(fp);
    return 0;
}