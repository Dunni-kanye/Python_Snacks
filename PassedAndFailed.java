import java.util.Scanner;
public class PassedAndFailed {
public static void main(String[]args){

   Scanner input = new Scanner(System.in);

	int noOfStudentsPassed = 0;
	int noOfStudentsFailed = 0;
	
	for (int count = 1; count <= 15; count++){

	System.out.print("Enter fifteen scores:");
	int score = input.nextInt();

	
	if (score >= 45){
	noOfStudentsPassed++;
	  }
	
	else{
	noOfStudentsFailed++;
	}

	  }

	System.out.println("Passed is " + noOfStudentsPassed);
	System.out.println("Failed is " + noOfStudentsFailed);

   }

}