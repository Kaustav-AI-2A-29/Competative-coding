#include <stdio.h>
#include <stdlib.h>

// Function to reverse the array
int* reverseArray(int a_count, int* a, int* result_count) {
    *result_count = a_count;

    int* reversed = malloc(a_count * sizeof(int));

    for (int i = 0; i < a_count; i++) {
        reversed[i] = a[a_count - 1 - i];
    }

    return reversed;
}

int main() {
    int arr_count;

    // Input: size of array
    printf("Enter number of elements: ");
    scanf("%d", &arr_count);

    int* arr = malloc(arr_count * sizeof(int));

    // Input: array elements
    printf("Enter %d integers:\n", arr_count);
    for (int i = 0; i < arr_count; i++) {
        scanf("%d", &arr[i]);
    }

    int res_count;
    int* res = reverseArray(arr_count, arr, &res_count);

    // Output: reversed array
    printf("Reversed array:\n");
    for (int i = 0; i < res_count; i++) {
        printf("%d ", res[i]);
    }
    printf("\n");

    // Free allocated memory
    free(arr);
    free(res);

    return 0;
}
