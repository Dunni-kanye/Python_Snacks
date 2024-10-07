import java.util.Scanner;
public class NumberPattern {
	public static void main(String... args){
	Scanner input = new Scanner(System.in);
	System.out.print("Enter the range: ");
	int number = input.nextInt();
		displayPattern(number);


	}
	public static void displayPattern(int row){

	for(int count = row; count >= 1; count--){
		for(int counter = 1; counter < count-1; counter++){
		
		System.out.print("  ");

		}
		
		for(int inner = 1; inner <=row- count + 1; inner++){
		System.out.print(inner + "  ");
	}


		System.out.println();
	}

	}
}