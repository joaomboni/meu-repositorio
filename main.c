#include <stdio.h>
#include <stdlib.h>

int main()
{
    float c, f;
    printf("Digite a temperatura em Celsius: ");
    scanf("%f", &c);

    f = (c*9/5)+32;

    printf("\nA temperatura em Fahrenheit e: %2.f", f);

    return 0;

}
