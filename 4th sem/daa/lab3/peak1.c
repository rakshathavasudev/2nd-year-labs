#include<stdio.h>
void main(){
	int a[50],n,i,j,s,st,end,max=0;
	
	scanf("%d", &n);
	for (i = 0; i <n; ++i)
	{
	scanf("%d", &a[i]);	/* code */
	}

	for(i=0;i<n;i++){
		s=0;
		for(j=i;j<n;j++){
			s=s+a[j];
			if(max<s){
				max=s;
				 st=i;
				 end=j;
			}

		}

	}
	printf("%d\n",max);
	printf(" indices  %d %d", st,end);

}
