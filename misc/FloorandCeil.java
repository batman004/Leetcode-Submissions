package com.company;

public class FloorandCeil {

    public static int floorInSorted(int[] arr, int start, int end, int ele) {
        int res=-1;

        while (start <= end)
        {
            // find the mid-value in the search space
            int mid = start + (end - start) / 2;

            if (arr[mid] == ele) {
                return arr[mid];
            }

            else if (ele < arr[mid]) {
                end = mid - 1;
            }

            else {
                res = arr[mid];
                start = mid + 1;
            }
        }

        return res;


    }

    public static int ceilInSorted(int[] arr, int start, int end, int ele) {
        int res=-1;

        while (start <= end)
        {
            // find the mid-value in the search space
            int mid = start + (end - start) / 2;

            // edge case #1 max element in array < ele

            if(ele > arr[end]){
                return arr[end];
            }

            if (arr[mid] == ele) {
                return arr[mid];
            }

            else if (ele < arr[mid]) {
                res = arr[mid];
                end = mid - 1;
            }

            else {
                start = mid + 1;
            }
        }

        return res;


    }


    public static char ceilInAlphabets(char[] arr, int start, int end, char ele) {
        char res='#';

        while (start <= end)
        {
            // find the mid-value in the search space
            int mid = start + (end - start) / 2;

            if (Character.compare(arr[mid], ele) == 0) {
                start = mid + 1;
            }

            else if (Character.compare(arr[mid], ele) > 0) {
                res = arr[mid];
                end = mid - 1;
            }

            else {
                start = mid + 1;
            }
        }

        return res;


    }

}
