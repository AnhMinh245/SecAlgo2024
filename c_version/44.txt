#include<stdio.h>
#include<math.h>
int main()
{
    int phantu,e,n,t,p,soto, sobe,trunggian;
    printf("\nNhap p: "); scanf("%d",&p);
    printf("Nhap so phan tu trong mang: "); scanf("%d",&phantu);
    int mang[phantu];
    printf("Nhap cac phan tu cua mang, hay de so nay va p co gcd bang mot nhe \n");
    label:
        for(e=0;e<phantu;e++)
        {
            printf("A[%d] = ",e); scanf("%d",&mang[e]);
            if(mang[e]>p)
            {
                soto=mang[e];sobe=p;
            }
            if(p>mang[e])
            {
                soto=p; sobe=mang[e];
            }
            if(p==mang[e])
                goto label;
            while(sobe>0)
            {
                trunggian=soto%sobe;
                soto=sobe;
                sobe=trunggian;
            } //gcd = soto
            if(soto!=1)
            {
                printf("\nHay nhap lai tu dau!\n");
                goto label;
            }
        }
        printf("mang A = (");
        for(e=0;e<phantu;e++)
            printf("  %d  ",mang[e]);
        printf(")");
        int mangB[phantu];
        for(e=0;e<phantu;e++)
        {
            //tinh nghich dao cua mang[e] va p
            int a,b,d,q,r,x,y,x1,x2,y1,y2;
            a=p; b=mang[e];
            x1=0;x2=1;y1=1;y2=0;
            while (b>0)
            {
                q=a/b;
                r=a-q*b;
                x=x2-q*x1;
                y=y2-q*y1;
                a=b; b=r; x2=x1; x1=x; y2=y1; y1=y;
            }
            d=a; x=x2; y=y2;
            mangB[e]=y;
        }
        printf("\nKet qua: (");
        for(e=0;e<phantu;e++)
        {
			if (mangB[e]<0) mangB[e]=mangB[e]+p;
            printf(" %d ",mangB[e]);
    	}
		printf(")");
}

