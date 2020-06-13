#include<stdio.h>
int max(int a,int b,int c){
	int max=0;
	max=a>b?(a>c?a:c):(b>c?b:c);
	return max;
}
int cross_sum(int arr[],int l,int m,int h){
	int l_sum=0,sum=0,i,r_sum=0;
	for(i=m;i>=l;i--){
		sum=sum+arr[i];
		if(sum>l_sum){
			l_sum=sum;
		}
	}
	sum=0;
	for(i=m+1;i<=h;i++){
		sum=sum+arr[i];
		if(sum>r_sum){
			r_sum=sum;
		}
	}
	return l_sum+r_sum;
	
}
int max_sum(int arr[ ],int l,int h){
	if(l==h){
		return arr[l];
	}
	int m=(l+h)/2;
	return max(max_sum(arr,l,m),max_sum(arr,m+1,h),cross_sum(arr,l,m,h));
}

void main(){
	int arr[100],i,n,s;
	printf("Enter size:  \n");
	scanf("%d",&n);
	printf("Enter array elements \n");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	s=max_sum(arr,0,n-1);
	printf("Max sum is %d \n",s);
}
