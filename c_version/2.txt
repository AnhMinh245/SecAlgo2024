#include<stdio.h>
#include<math.h>
// chắc tùy máy vì máy mình làm đc 5 là căng, máy bạn mình làm đc tận 10
int main()
{
    int n,i,j,p,t,d;
    printf("\nNhap n: "); scanf("%d",&n);
    d=pow(10,n-1);
    n=pow(10,n)-1;
    int a[n];
    for(i=d;i<=n;i++)
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
    for(i=d;i<=n;i++)
    {
        if (a[i]==1)
        {
            printf("%d ",i);
        }
    }
    printf(")");
}
