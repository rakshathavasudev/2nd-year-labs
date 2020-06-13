#include<stdio.h>
void findavgwt(int n,int bt[],int wt[]){
	wt[0]=0;
	int i;
	for(i=1;i<n;i++){
		wt[i]=wt[i-1]+bt[i-1];
	}
}
void findavgtt(int n,int bt[],int wt[],int tt[]){
	int i;
	for(i=0;i<n;i++){
		tt[i]=wt[i]+bt[i];
	}
}
void findalltime(int n,int bt[])
{
	int wt[100],tt[100],totalwt=0,totaltt=0,i;
	float avgwt,avgtt;
	findavgwt(n,bt,wt);
	findavgtt(n,bt,wt,tt);
	
	for(i=0;i<n;i++){
		totalwt=totalwt+wt[i];
		totaltt=totaltt+tt[i];
	
	}
	printf("Process   BT   WT   TT \n");
	for(i=0;i<n;i++){
		printf("%d         %2d   %2d   %2d \n",i+1,bt[i],wt[i],tt[i]);
	}
	avgwt=(float)totalwt/(float)n;
	avgtt=(float)totaltt/(float)n;
	printf("Average waiting time: %f \n",avgwt);
	printf("Average turn-around time: %f \n",avgtt);
}

int main()
{

	int n=5;
	int bt[]={10,29,3,7,12};
	findalltime(n,bt);
	return 0;
	
}
