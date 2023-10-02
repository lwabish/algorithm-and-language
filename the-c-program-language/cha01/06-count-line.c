#include <stdio.h>

int main()
{
    int c, nl;
    nl = 0;
    while ((c = getchar()) != EOF)
    {
        // '' 和 ""不一样
        if (c == '\n')
        {
            // 两种写法都有
            // nl++;
            ++nl;
        }
    }
    printf("Number of lines: %d\n", nl);
}