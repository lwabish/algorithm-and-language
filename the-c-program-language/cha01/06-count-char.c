#include <stdio.h>

int main()
{
    long nc;
    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("Number of characters: %ld\n", nc);
}