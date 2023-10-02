// c中函数传值是值传递，可以直接在函数中利用形参，从而减少局部变量
int power(int base, int n)
{
    int p;
    for (p = 1; n > 0; --n)
    {
        p = p * base;
    }
    return p;
}