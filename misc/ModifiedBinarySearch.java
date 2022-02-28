package com.company;

public class ModifiedBinarySearch {

    public static int modifiedBS(int[] arr, int start, int end, int ele) {

        while(start <= end) {
            int mid = start + (end - start)/2;

            if (ele == arr[mid]) {
                return mid;
            }
            if (mid - 1 >= start && arr[mid - 1] == ele) {
                return mid - 1;
            }

            if (mid + 1 <= end && arr[mid + 1] == ele) {
                return mid + 1;
            }
            if (ele < arr[mid]) {
                end = mid - 2;
            }
            if (ele > arr[mid]) {
                start = mid + 2;
            }
        }

        return -1;
    }
}
