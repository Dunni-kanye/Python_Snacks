/**import java.util.Scanner
public class RotateArray {cs
    public int [] rotate(int[] number, int count) {
        
        count = count % number.length;

        reverse(number, 0, nums.length - 1);
        reverse(number, 0, count - 1);
        reverse(number, count, number.length - 1);
    	}
    }

    public static void main(String[] args) {
        int[] number = {1, 2, 3, 4, 5, 6, 7};
        int count = 3;
         rotate(number, count);
        System.out.println("Rotated Array: " + Arrays.toString(number));


	}**/
 
import java.util.Arrays;

public class SortArray {

    public void sortEvenOdd(int[] number) {
        int[] temp = new int[number.length];
        int evenIndex = 0;
        int oddIndex = number.length - 1;

        for (int i = 0; i < number.length; i++) {
            if (number[i] % 2 == 0) {
                temp[evenIndex] = number[i];
                evenIndex++;
            } else {
                temp[oddIndex] = number[i];
                oddIndex--;
            }
        }

       
        for (int i = 0; i < number.length; i++) {
            number[i] = temp[i];
        }
    }

    public static void main(String[] args) {
        SortArray index = new SortArray();
        int[] number = {2, 1, 4, 3, 6, 5};
        index.sortEvenOdd(number);
        System.out.println("Sorted Array: " + Arrays.toString(number));
    }
}
