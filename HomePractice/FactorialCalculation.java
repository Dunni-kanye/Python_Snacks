import java.util.Scanner;

public class FactorialCalculation {
   public static void main(String[] args) {

    Scanner input = new Scanner(System.in);
	
	System.out.print("Enter a number:");
	int number = input.nextInt();

	long factorial = 1;

	for (int count = 1; count <= number; count++) {
		factorial *= count;

	}
	


	System.out.println("Factorial of " + number + " is: " + factorial);




   }


}