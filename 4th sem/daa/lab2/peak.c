#include<stdio.h>

int peak(int arr[],int low,int high){
	if(low>high)
		return ;
	int mid=(low+high)/2;
	/*if(mid==(high+1)/2){
		return arr[mid];
				
	}*/
	if (arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]){
		return(arr[mid]) ;
	}
	
	if (arr[mid]>arr[mid-1] && arr[mid]<arr[mid+1]){
		return(peak(arr,mid+1,high));
	}
	else
		return(peak(arr,low,mid-1));
	
}


void main(){
	int arr[100],n,i;
	printf("enter no. \n");
	scanf("%d",&n);
	printf("Enter elements \n");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	printf("The peak element is:%d",peak(arr,0,n-1));
	
}
