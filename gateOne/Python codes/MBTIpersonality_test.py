
print("How's your awareness?")
print("Answer the following questions to see what taking the MBTI personality test might help you learn")

				
print("To take the personality test select A or B based on how well each statement describes you")
			

name = input("What is your name:")
			
start = input("Type CONTINUE to start:") 

questions = [
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
       					 ]

extrovert == 0, introvert == 0
sensing == 0, intuitive == 0
thinking == 0, feeling == 0
judging == 0, perceiving == 0
for answer in iterable:
	print(question)
answer = ""
while answer not in ["A", "B"]:
	answer = input("Please enter A or B: ")
	match answer:
       		case "A":
			if(question.startsWith("1.") or question.startsWith("5.") or question.startsWith("9.") or question.startsWith("13.") or question.startsWith("17.")):
				extrovert+= 1

			elif (question.startsWith("2.") or question.startsWith("6.") or 
				question.startsWith("10.") or question.startsWith(  "14.") or
				 question.startsWith("18.")):

                       		 sensing++
			elif (question.startsWith("3.") or question.startsWith("7.") or
				 question.startsWith("11.") or question.startsWith("15.") or 
				 question.startsWith("19.")):
                       	 	thinking++
			elif:
                   	 judging++
                   	 break

		case "B":
                    if (question.startsWith("1.") or question.startsWith("5.") or
			 question.startsWith("9.") or question.startsWith("13.") or 
			question.startsWith("17.")):
                        introvert++;

                    elif (question.startsWith("2.") or question.startsWith("6.") or 
				question.startsWith("10.") or question.startsWith("14.") or
				 question.startsWith("18.")):
                        intuitive++

                    elif (question.startsWith("3.") or question.startsWith("7.") or 
				question.startsWith("11.") or question.startsWith("15.") or
				 question.startsWith("19.")):
                        feeling++

                    else
                        perceiving++
                    
                    break
             		
print("""
	 E -means extrovert
	I- means introvert
	J - means judging
	 S - means sensing
	 F - means feelings
	P - means perceiving
 	T - means thinking
	N - means intuitive
	""")
					  
personalityType = ""
personalityType += (extrovert > introvert) ? "E" : "I"
personalityType += (sensing > intuitive) ? "S" : "N"
personalityType += (thinking > feeling) ? "T" : "F"
personalityType += (judging > perceiving) ? "J" : "P" 

print(f"{"Your MBTI personality result is:"} {personalityType}")

