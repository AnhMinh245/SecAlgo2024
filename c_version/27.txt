#include<stdio.h>
#include<math.h>
int gcd(int a, int b)
{  int tmp;
   if(b>a)
    {
	tmp=a; 
	a=b;
	b=tmp;}
	while(b>0)
	{ int r=a%b;
	  a=b;
	  b=r; 
	 }
	 return a; 
 }
 
int kiemtratinhgnuyento(int m)
{ int k;
	if (m==0) return 0;
	if (m==1) return 0;
 for(k=2;k<m;k++)
  {  if(m%k==0)
       return 0; 
   } 
   return 1; 
 } 
int main()
{ int a, b;
  do 
  { printf("nhap vao so a : ");
    scanf("%d", &a);
	printf("nhap vao so b :");
	scanf("%d", &b); 
  }while(a<0||b>1000);
  int d; 
  int dem=0; 
  int i, j, k;
  for(i=a;i<b;i++)
     { for(j=a;j<b;j++)
	      { d=gcd(i,j); 
	        if(kiemtratinhgnuyento(d)==1) 
		      {
			  printf("[%d %d] %d ", i, j, d);
		        }
	}
	  } 
	   
 }
