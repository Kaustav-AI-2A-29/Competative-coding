#include <stdio.h>

int getSecondLargest(int *arr, int n) {
    int largest = -1, second_largest = -1;

    for (int i = 0; i < n; i++) {
        if (arr[i] > largest)
            largest = arr[i];
    }

    for (int i = 0; i < n; i++) {
        if (arr[i] != largest && arr[i] > second_largest)
            second_largest = arr[i];
    }

    return second_largest;
}

int main() {
    int n;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    int result = getSecondLargest(arr, n);
    printf("Second largest element: %d\n", result);

    return 0;
}
