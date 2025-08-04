#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isPalindrome(char s[]) {
    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    char s[100];

    printf("Enter a string: ");
    scanf("%s", s);  // Reads string until space or newline

    if (isPalindrome(s)) {
        printf("Yes, it is a palindrome.\n");
    } else {
        printf("No, it is not a palindrome.\n");
    }

    return 0;
}
