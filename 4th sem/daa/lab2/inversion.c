#include<stdio.h>

int split_inversion(int arr[],int low,int mid,int high){
	int i,j,k,c=0,temp[100];
	i=low;
	j=mid;
	k=low;
	while(i<=(mid-1) && j<=high){

		if (arr[i]<=arr[j])
			temp[k++]=arr[i++];
		else
		{
			temp[k++]=arr[j++];
			c=c+(mid-i);
		}
	}
	while(i<=mid-1){
		temp[k++]=arr[i++];
	}
	while(j<=high){
		temp[k++]=arr[j++];
	}
	for (i = low; i <= high; i++) 
        arr[i] = temp[i]; 
  
	return c;
	
}

int inversion(int arr[],int low,int high){
	int l=0,r=0,s=0;
	if(high>low){
	
		int mid=(low+high)/2;
		l=inversion(arr,low,mid);
		r=inversion(arr,mid+1,high);
		s=split_inversion(arr,low,mid+1,high);
}
	return l+r+s;
}

void main(){
	int arr[100],n,i;
	printf("enter no. \n");
	scanf("%d",&n);
	printf("Enter elements \n");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	printf("The no. of inversions is:%d",inversion(arr,0,n-1));
	
}
