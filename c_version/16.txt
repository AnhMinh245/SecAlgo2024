#include <stdio.h>
#include <math.h>
// Nếu code nó không ra kết quả, hãy thử chép tay thay vì copy, mình làm được 
int main()
{
	int check,n,i,j,ra;
	
	
	printf("Nhap so n"); scanf("%d",&n);
	for(j=0;j<n;j++)
	{
	check=1;
	ra=rand();
	printf("%d",ra);
	for(i=2;i<sqrt(ra);i++)
		{
			if (ra%i==0) check =0;
		}
	if (check==1) printf(" Day la so nguyen to\n"); else printf(" Day khong phai la so nguyen to\n");
}

}
