#include <stdio.h>
#define IN 1
#define OUT 0

int main()
{
    int c, nl, nw, nc, state;
    state = OUT;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF)
    {
        // 遇到字符就++
        ++nc;
        // 如果遇到的字符是换行符，行数++
        if (c == '\n')
            ++nl;

        // 如果遇到了以下特殊字符，转换一次状态
        if (c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        // 如果是普通字符，且状态表明单词换了，那么计数，重置状态
        else if (state == OUT)
        {
            state = IN;
            ++nw;
        }
    }
    printf("%d %d %d\n", nl, nw, nc);
}