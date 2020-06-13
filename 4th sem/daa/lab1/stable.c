#include<stdio.h>
int check_rank(int rank[50][50],int i,int k,int w){
	if(rank[w][k]>rank[w][i])
		return 1;
	else 
		return 0;
	
}

int stable_match(int man[50][50],int woman[50][50],int rank[50][50],int n){
	int wife[50],husband[50],count[50],i,j;
	for(i=0;i<=n;i++){
		wife[i]= -1;
		husband[i]= -1;
		count[i]=0;
	}
	
		for(i=0;i<=n;i++){
			if (husband[i]== -1 && count[i]<=n){
				for(j=0;j<=n;j++){
					int w=man[i][j];
					if (wife[w]== -1){
						wife[w]=i;
						husband[i]=w;
						count[i]+=1;
					}
					
					else if(check_rank(rank,i,wife[w],w)){
						int m=wife[w];
						wife[w]=i;
						husband[i]=w;
						husband[m]= -1;
						count[i]+=1;
						
					}
				}
				
			}
				
		}
	
	
	for(i=0;i<=n;i++){
		printf("%d ",husband[i]);
	}
}

void main(){
	int n,i,j,r,rank[50][50],man[50][50],woman[50][50];
	printf("Enter the no. \n");
	scanf("%d",&n);
	printf("Enter man's preference \n");
	for(i=0;i<n;i++){
		printf("man %d-",i);
		for(j=0;j<n;j++){
			
			scanf("%d",&man[i][j]);
		}
		printf("\n");
	}
	printf("Enter women's preference \n");
	for(i=0;i<n;i++){
		printf("woman %d-",i);
		for(j=0;j<n;j++){
			
			scanf("%d",&woman[i][j]);
		}
		printf("\n");
	}
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			r=woman[i][j];
			rank[i][r]=j;
			
		}
	}
	/*for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("%d",rank[i][j]);
		}
	}*/
	stable_match(man,woman,rank,n-1);
	
}
