
import java.util.Scanner;

public class MortgageCalculator {  

public static void main(String[]args) {
Scanner input = new Scanner(System.in);

	System.out.print("Enter the principal amount:");
	int p = input.nextInt();

	System.out.print("Enter the annual interest rate:");
	int r = input.nextInt();

	System.out.print("Enter the duration in years:");
	int n = input.nextInt();

	p = principal_amount;
	r = annual_interest_rate / 100 /12; 
	n = duration_in_years * 12;

	int monthlyPayment = p * (r* (1+r)* n) / (((1+r)*n)-1);

	System.out.printf("%d%n",monthlyPayment);


	}

}


	
