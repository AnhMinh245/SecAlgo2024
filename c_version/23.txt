#include <stdio.h>
#include <stdlib.h>

int kiem_tra_nguyen_to(int i)
{
    int x, n = i / 2;

    for(x=2; x<=n; x++)
    {
        if ((i % x) == 0)
            return 0;
    }

    return 1;
}

int main()
{
    int i,A,B;
    int sum = 0;
    printf("Nhap vao A: ");
    scanf("%d",&A);
    printf("Nhap vao B: ");
    scanf("%d",&B);
    printf("Cac so nguyen to trong Khoang [A,B] la: ");
    for( i = A; i <= B; i++)
    {
        if((kiem_tra_nguyen_to(i)) && (i!=1))
        {
            printf("%d\t", i);
            sum += i;
        }
        else
            sum = sum;
    }
    printf("\n");
    printf("Sum = %d", sum);
    printf("\n");
    if(kiem_tra_nguyen_to(sum))
        printf("YES"); //YES neu 'Sum' la so nguyen to
    else
        printf("NO");  //No neu 'Sum' khong la so nguyen to

}