import java.util.Scanner;

public class FibonacciSequence {
   public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

	System.out.print("Enter the number of terms: ");
	int n = input.nextInt();
	
	int firstTerm = 0;
	int secondTerm = 1;

	System.out.print("Fibonacci Sequence: " + firstTerm + ", " + secondTerm);

	for (int count = 3; count <= n; count++){
	int nextTerm = firstTerm + secondTerm;
	System.out.print(", " + nextTerm);
	firstTerm = secondTerm;
	secondTerm = nextTerm;


     }


}

	}


