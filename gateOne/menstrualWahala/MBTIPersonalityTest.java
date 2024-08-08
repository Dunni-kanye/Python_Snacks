 import java.util.Scanner;

public class MBTIPersonalityTest {

	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
				
			System.out.print("How's your awareness?");
			System.out.print("Answer the following questions to see what taking the MBTI personality test might help you learn");

				
			System.out.print("To take the personality test select ("A" or "B") based on how well each statement describes you");
			System.out.print("What is your name:");
			String name = input.nextString();
			
			 System.out.print("Type CONTINUE to start:"); 
			 String start = input.nextLine().trim().toUpperCase();
		
		String[] questions = {

			"You find it takes effort to introduce yourself to other people. (A) Yes, (B) No",
                        "You consider yourself more practical than creative. (A) Yes, (B) No",
                        "Winning a debate matters less to you than making sure no one gets upset. (A) Yes, (B) No",
                        "You get energized going to social events that involve many interactions. (A) Yes, (B) No",
                        "You often spend time exploring unrealistic yet intriguing ideas. (A) Yes, (B) No",
			"Your travel plans are usually well thught out. (A) Yes, (B) No",
			" It is more important to you to make sure your work is finished on time. (A) Yes, (B) No",
			"You find it difficult to understand people who are very emotional.(A) Yes, (B) No",
			"You frequently and easily express your feelings and emotions. (A) Yes, (B) No",
			"You like to have a to-do list for your daily activities. (A) Yes, (B) No",
			"You prefer to relax alone or with a few close friends rather than in a large group. (A) Yes, (B) No",
			"You often rely on your intuition rather than on careful analysis. (A) Yes, (B) No",
			"You often think about what you should have said in a conversation long after it has taken place. (A) Yes, (B) No",
			"Your decisions are based more on feelings than on analysis of the situation. (A) Yes, (B) No",
			"You usually prefer to get your revenge rather than forgive. (A) Yes, (B) No",
			"You prefer to keep your options open and be spontaneous. (A) Yes (B) No",
			"You often think about humankind and its destiny. (A) Yes (B) No",
			"You believe the best decision is one that can be easily changed. (A) Yes, (B) No",
			"You often contemplate the reasons for human existence. (A) Yes, (B) No",
			"You think that considering the logical sequence of a process is more important than its emotional impact. (A) Yes, (B) No",

			};



			int extrovert = 0, introvert = 0;
        		int sensing = 0, intuitive = 0;
       		        int thinking = 0, feeling = 0;
       		        int judging = 0, perceiving = 0;
			 for (String question : questions) {
            		String answer = "";
	
            while (!answer.equals("A") && !answer.equals("B")) {
                System.out.println(question);
		 answer = input.nextLine().trim().toUpperCase();
                if (!answer.equals("A") && !answer.equals("B")) {
                    System.out.println("Please answer with 'A' or 'B' only.");
                }
		  }


		 switch(answer) {
                case "A":
		    if (question.contains("introduce yourself") || question.contains("energized going to social events") || question.contains("to-do list")) {
                        extrovert++;
                    } else if (question.contains("practical than creative") || question.contains("exploring unrealistic yet intriguing ideas") || question.contains("open and spontaneous") || question.contains("contemplate the reasons for human existence")) {
                        sensing++;
                    } else if (question.contains("Winning a debate") || question.contains("difficult to understand people who are very emotional") || question.contains("think about what you should have said")) {
                        thinking++;
                    } else {
                        judging++;
                    }
                    break;
                   
                case "B":
			 if (question.contains("introduce yourself") || question.contains("energized going to social events") || question.contains("to-do list")) {
                        introvert++;
                    } else if (question.contains("practical than creative") || question.contains("exploring unrealistic yet intriguing ideas") || question.contains("open and spontaneous") || question.contains("contemplate the reasons for human existence")) {
                        intuitive++;
                    } else if (question.contains("Winning a debate") || question.contains("difficult to understand people who are very emotional") || question.contains("think about what you should have said")) {
                        feeling++;
                    } else {
                        perceiving++;
                    }
                    break;
            }
        }
                    
                   String personalityType = "";
        personalityType += (extrovert > introvert) ? "E" : "I";
        personalityType += (sensing > intuitive) ? "S" : "N";
        personalityType += (thinking > feeling) ? "T" : "F";
        personalityType += (judging > perceiving) ? "J" : "P";


        System.out.println("Your MBTI personality type is: " + personalityType);





  }



}