#include <stdio.h>
// 函数原型
int power(int m, int n);

int power(int base, int n)
{
    int i, p;
    // 如果不赋初值，会怎么样？
    // 局部变量不赋初值，则其值是随机的垃圾值
    p = 1;
    for (i = 1; i <= n; i++)
        p = p * base;
    return p;
}

int main()
{
    int i;
    for (i = 1; i <= 10; i++)
        printf("%d\t%d\n", i, power(2, i));
    return 0;
}