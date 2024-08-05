import java.util.Scanner;

public class PrimeChecker {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		System.out.print("Enter a number:");
		int number = input.nextInt();
		
		boolean prime = true;
		
		if (number <= 1) {
		prime = false;
		
		} else {
		  for (int count = 2; count <= Math.sqrt(number); count++) {
			if (number % count == 0) {
				prime = false;
				break;
			}
	
		    }

		}
		
		if (prime) {
		    System.out.println(number + " is a prime number");


		}else {
	 		
		   System.out.println(number + " is not a prime number.");

			}
		   }
		}


