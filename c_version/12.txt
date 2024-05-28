#include<stdio.h>
#include<math.h>
// Bài này lừa đấy, chỉ có 1 dãy số thỏa mãn thôi nhé, klaim đi nếu bấm 10000 k ra nhiều
int main()
{
    int n,i,j,p,t,Tong,check,k;
    j=0;
    check=1;
    printf("\nNhap n: "); scanf("%d",&n);
    int a[n],b[n];
    for(i=2;i<=n;i++)
    {
        a[i]=1;
    }
        for (p=2;p<n;p++)
            {
                t= n/p;
                for (i=2;i<=t;i++)
                            a[p*i]=0;
            }
    printf("(");
    for(i=2;i<=n;i++)
    {
        if (a[i]==1)
        {
            b[j]=i;
            j++;
        }
    }
    for (i=0;i<j;i++) printf("%d ",b[i]);
    printf(")");
    for (i=0;i<j-4;i++)
    {
	
    Tong=b[i]+b[i+1]+b[i+2]+b[i+3];
    for (k=2;k<=sqrt(Tong);k++)
    	{
    		if (Tong%k==0) check = 0;
		}
		if (check==1)    printf("\n%d %d %d %d",b[i],b[i+1],b[i+2],b[i+3]);
}
}