#include <stdio.h>
#include <string.h>

char* reverseString(char* s) {
    int left = 0;
    int right = strlen(s) - 1;
    char temp;

    while (left < right) {
        temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }

    return s;
}

int main() {
    char s[100];

    printf("Enter the string: ");
    fgets(s, sizeof(s), stdin);

    // Remove newline character if present
    s[strcspn(s, "\n")] = '\0';

    reverseString(s);

    printf("Reversed string: %s\n", s);

    return 0;
}
