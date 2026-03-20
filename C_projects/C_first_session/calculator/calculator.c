#include <stdio.h>
#include <stdlib.h>

int main() {
    int first_number, second_number;
    printf("Enter first number: ");
    scanf("%d", &first_number);
    printf("Enter second number: ");
    scanf("%d", &second_number);

    int sum = second_number + first_number;

    if (sum <= 5) {
        printf("Sum = %d\n", sum);
    }
    else {
        printf("I`m lazy calculator and I can`t give you sum more than 5");
    }

    return 0;
}