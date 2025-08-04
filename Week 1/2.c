#include <stdio.h>
int largest(int arr[], int n) {
    int mx = arr[0];
    for (int i = 0; i < n; i++) {
        if (mx < arr[i])
            mx = arr[i];
    }
    return mx;
}
int main() {
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);
    int arr[n];
    // Taking array elements from user
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    // Finding and printing the largest element
    int result = largest(arr, n);
    printf("The largest element is: %d\n", result);
    return 0;
}
