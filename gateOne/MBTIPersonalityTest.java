 import java.util.Scanner;

public class MBTIPersonalityTest {

	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
				
			System.out.println("How's your awareness?");
			System.out.println("Answer the following questions to see what taking the MBTI personality test might help you learn");

				
			System.out.println("To take the personality test select A or B based on how well each statement describes you");
			
			System.out.println("What is your name?");
			String name = input.nextLine();
			
			 System.out.println("Type CONTINUE to start:"); 
			 String start = input.nextLine().trim().toUpperCase();
		
			String[] questions = {
           		 "1. (A) Expend energy, enjoy groups (B) Conserve energy, enjoy one-on-one",
           		 "2. (A) Interpret literally (B) Look for meaning and possibilities",
           		 "3. (A) Logical, thinking, questioning (B) Empathetic, feeling, accommodating",
           		 "4. (A) Organized, orderly (B) Flexible, adaptable",
           		 "5. (A) More outgoing, think out loud (B) More reserved, think to yourself",
           		 "6. (A) Practical, realistic, experiential (B) Imaginative, innovative, theoretical",
           		 "7. (A) Candid, straight forward, frank (B) Tactful, kind, encouraging",
           		 "8. (A) Plan, schedule (B) Unplanned, spontaneous",
            		"9. (A) Seek many tasks, public activities, interaction with others (B) Seek private, solitary activities with quiet to concentrate",
           		 "10. (A) Standard, usual, conventional (B) Different, novel, unique",
            		"11. (A) Firm, tend to criticize, hold the line (B) Gentle, tend to appreciate, conciliate",
            		"12. (A) Regulated, structured (B) Easy-going, 'live' and let live",
            		"13. (A) External, communicative, express yourself (B) Internal, reticent, keep to yourself",
           		 "14. (A) Focus on here-and-now (B) Look to the future, global perspective, big picture",
           		 "15. (A) Tough-minded, just (B) Tender-hearted, merciful",
           		 "16. (A) Preparation, plan ahead (B) Go with the flow, adapt as you go",
           		 "17. (A) Active, initiate (B) Reflective, deliberate",
           		 "18. (A) Facts, things, what is (B) Ideas, dreams, what could be, philosophical",
            		"19. (A) Matter of fact, issue-oriented (B) Sensitive, people-oriented, compassionate",
            		"20. (A) Control, govern (B) Latitude, freedom"
       					 };

			int extrovert = 0, introvert = 0;
        		int sensing = 0, intuitive = 0;
       		        int thinking = 0, feeling = 0;
       		        int judging = 0, perceiving = 0;
			for (String question : questions) {
            			String answer = "";
				String A = "";
				String B = "";
				System.out.println(question);
		 		answer = input.nextLine();

			 	while (!answer.equals("A") && !answer.equals("B")) {
					System .out.println("Please answer with 'A' or 'B' only.");
					answer = input.nextLine();
				}
				
			switch (answer) {
                case "A":
                    if (question.contains("1.") || question.startsWith("5.") ||
			 question.startsWith("9.") || question.startsWith("13.") || 
			 question.startsWith("17.")) {

                        extrovert++;

                    } else if (question.startsWith("2.") || question.startsWith("6.") || 
				question.startsWith("10.") || question.startsWith("14.") ||
				 question.startsWith("18.")) {

                       		 sensing++;

                    } else if (question.startsWith("3.") || question.startsWith("7.") ||
				 question.startsWith("11.") || question.startsWith("15.") || 
				 question.startsWith("19.")) {
                        thinking++;

                    } else {
                        judging++;
                    }
                    break;

		case "B":
                    if (question.startsWith("1.") || question.startsWith("5.") ||
			 question.startsWith("9.") || question.startsWith("13.") || 
			question.startsWith("17.")) {
                        introvert++;

                    } else if (question.startsWith("2.") || question.startsWith("6.") || 
				question.startsWith("10.") || question.startsWith("14.") ||
				 question.startsWith("18.")) {
                        intuitive++;

                    } else if (question.startsWith("3.") || question.startsWith("7.") || 
				question.startsWith("11.") || question.startsWith("15.") ||
				 question.startsWith("19.")) {
                        feeling++;

                    } else {
                        perceiving++;
                    }
                    break;
            
        }
		}
             		
			System.out.println("""
					  E -means extrovert
					  I- means introvert
					  J - means judging
					  S - means sensing
					  F - means feelings
					  P - means perceiving
 					  T - means thinking
					  N - means intuitive
					  """);
					  
                    
                   String personalityType = "";
        personalityType += (extrovert > introvert) ? "E" : "I";
        personalityType += (sensing > intuitive) ? "S" : "N";
        personalityType += (thinking > feeling) ? "T" : "F";
        personalityType += (judging > perceiving) ? "J" : "P"; 


        System.out.println("Your MBTI personality type is: " + personalityType);





  }



}