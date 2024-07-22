import java.util.Scanner;
public class MultiplicationTable{
public static void main(String[]args) {
Scanner input = new Scanner(System.in);

	int number;
	int product;
	int count;
	
	System.out.print("Enter a number:");
	number= input.nextInt();
	for( count = 1; count <= 12; count++) {
	
		product = number * count;
	System.out.println( number + " * " + count + " = " + product);
	 

		
	}


	


   }



  }