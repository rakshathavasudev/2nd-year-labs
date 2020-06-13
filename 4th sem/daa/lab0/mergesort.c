#include<stdio.h>





















void print(int a[],int high){
	int i;
	for(i=0;i<high;i++){
		printf("%d",a[i]);
		printf("\n");
	}
}

void main()
{
	int n,a[100],i,temp;
	printf("Enter the no. of elements \n");
	scanf("%d",&n);
	printf("Enter the elements of array \n");
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	quick(a,0,n-1);
	print(a,n);
	
}

