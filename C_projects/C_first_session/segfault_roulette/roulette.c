#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));

    char compliments_array[][100] = {
        "You`re seems to be so good",
        "Today is really a beautiful day",
        "You`re so gorgeous",
        "Thank you that you are here"
    };

    int length = sizeof(compliments_array) / sizeof(compliments_array[0]);
    int count = rand() % (length + 1);

    if (count < length) {
        printf("%s", compliments_array[count]);
    } else {
        printf("Sorry our crash was happen during segfault failure(");
        int *p = NULL;
        *p = 1;
    }
    return 0;
}