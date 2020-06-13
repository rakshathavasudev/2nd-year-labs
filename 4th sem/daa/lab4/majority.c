#include<stdio.h>

int majority(int arr[],int low,int high){
	if (low==high){
		return arr[0];
		
	}
	if(high==(low+1)){
		if(arr[0]==arr[1])
			return arr[0];
		
		else
			return -1; 
	}
	int mid=(low+high)/2;
	int el1=majority(arr,low,mid);
	int el2=majority(arr,mid+1,high);
	
	if(el1==-1 && el2>=0)
		return el2;
		
	if(el2==-1 && el1>=0)
		return el1;
		
	if(el1==el2)
		return el1;
	else
		return -1;
			
}

void main(){
	int arr[100],n,i;
	printf("enter no. \n");
	scanf("%d",&n);
	printf("Enter elements \n");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	int c=majority(arr,0,n-1);
	if(c==-1)
		printf("no");
	else
		printf("yes");
	
}
