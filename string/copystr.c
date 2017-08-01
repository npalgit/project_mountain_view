// microsoft online techincal screen. implement or fix copy string function
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *copyString(char* a)
{
    char *f;
    f = (char*)malloc((strlen(a)+1)*sizeof(char));
    char *f_start;
    f_start = f;

    while (*a != 0)
    {
        *f = *a;
        f++;
        a++;
    }
    *f ='\0';
    return f_start;
}

int main()
{
    char * s;
    s = copyString("hellobg");
    printf("%s\n", s);
    return 0;
}
