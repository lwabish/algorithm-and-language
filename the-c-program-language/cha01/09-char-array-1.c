#include <stdio.h>
#define MAXLINE 1000

int max;
char line[MAXLINE];
char longest[MAXLINE];

// void省略也可以正常编译
int getline1();
void copy(void);

int getline1(void)
{
    int c, i;
    extern char line[];
    for (i = 0; i < MAXLINE - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
    {
        line[i] = c;
    }

    if (c == '\n')
    {
        line[i] = c;
        ++i;
    }
    return i;
}

void copy(void)
{
    int i;
    extern char line[], longest[];
    i = 0;
    while ((longest[i] = line[i]) != '\0')
    {
        ++i;
    }
}

int main(void)
{
    int len;
    extern char longest[];
    max = 0;
    while ((len = getline1()) > 0)
    {
        if (len > max)
        {
            copy();
            max = len;
        }
    }
    if (max > 0)
        printf("longest: %s", longest);
    return 0;
}