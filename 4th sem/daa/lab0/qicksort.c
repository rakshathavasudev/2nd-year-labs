#include<stdio.h>

void swap(int* a,int* b){
	int t;
	t=*a;
	*a=*b;
	*b=t;
}

int partition(int a[],int low,int high){
	k=low-1;
	for(j=low;j<high;j++){
	int pivot,k,j;
	pivot=a[high];
		if (a[j]<=pivot){
			k=k+1;
			swap(&a[k],&a[j]);
				
		}
	
	}
	swap(&a[k+1],&a[high]);
	return k+1;	
	
}

void quick(int a[],int low,int high){
	int pi;
	if (low<high){
		pi=partition(a,low,high);
		
		quick(a,low,pi-1);
		quick(a,pi+1,high);
	}
	
}

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

