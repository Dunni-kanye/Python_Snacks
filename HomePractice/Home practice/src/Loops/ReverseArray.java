package Loops;

import java.util.Arrays;

public class ReverseArray {
    public static void reverseArray(int[] numbers) {
        int length = numbers.length;
        for (int i = 0; i < length / 2; i++) {
            int temp = numbers[i];
            numbers[i] = numbers[length - i - 1];
            numbers[length - i - 1] = temp;
        }
    }
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        reverseArray(numbers);
        System.out.println(Arrays.toString(numbers));
    }
}
