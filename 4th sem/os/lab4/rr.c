#include<stdio.h>
#include <stdbool.h>
void findavgwt(int n,int bt[], int wt[], int quantum) 
{ 
    int rem_bt[n],i; 
    for(i = 0 ; i < n ; i++) 
        rem_bt[i] =  bt[i]; 
  
    int t = 0,j;  
    while (1) 
    { 
        bool done = true; 
        for (j= 0 ; j < n; j++) 
        { 
            if (rem_bt[j] > 0) 
            { 
                done = false; 
  
                if (rem_bt[j] > quantum) 
                { 
                    t += quantum; 

                    rem_bt[j] -= quantum; 
                } 
  
                else
                { 
                  
                    t = t + rem_bt[j]; 

                    wt[j] = t - bt[j]; 

                    rem_bt[j] = 0; 
                } 
            } 
        } 
        if (done == true) 
          break; 
    } 
} 
  
void findavgtt(int n,int bt[],int wt[],int tt[]){
	int i;
	for(i=0;i<n;i++){
		tt[i]=wt[i]+bt[i];
	}
}
void findalltime(int n,int bt[],int quantum)
{
	int wt[100],tt[100],totalwt=0,totaltt=0,i;
	float avgwt,avgtt;
	findavgwt(n,bt,wt,quantum);
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

	int n=5,quantum;
	printf("Enter the quantum \n");
	scanf("%d",&quantum);
	int bt[]={10,29,3,7,12};
	findalltime(n,bt,quantum);
	return 0;
	
}
