def MBTI_personality_test():
    print("How's your awareness?")
    print("Answer the following questions to see what taking the MBTI personality test might help you learn")

    print("To take the personality test, select A or B based on how well each statement describes you")
    name = input("What is your name?\n")
    start = input("Type CONTINUE to start:\n").strip().upper()

    if start != "CONTINUE":
        print("You did not type CONTINUE.")
        return

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
        "12. (A) Regulated, structured (B) Easy-going, 'live and let live'",
        "13. (A) External, communicative, express yourself (B) Internal, reticent, keep to yourself",
        "14. (A) Focus on here-and-now (B) Look to the future, global perspective, big picture",
        "15. (A) Tough-minded, just (B) Tender-hearted, merciful",
        "16. (A) Preparation, plan ahead (B) Go with the flow, adapt as you go",
        "17. (A) Active, initiate (B) Reflective, deliberate",
        "18. (A) Facts, things, what is (B) Ideas, dreams, what could be, philosophical",
        "19. (A) Matter of fact, issue-oriented (B) Sensitive, people-oriented, compassionate",
        "20. (A) Control, govern (B) Latitude, freedom"
    ]
    introvert = 0
    extrovert = 0
    sensing = 0
    thinking = 0
    judging = 0
    perceiving = 0
    intuitive = 0
    feeling = 0

    for question in questions:
        print(question)
        answer = input().strip().upper()

        while answer not in ["A", "B"]:
            print("Please answer with 'A' or 'B' only.")
            
        if answer == "A":
            if question.startswith("1.") or question.startswith("5.") or \
               question.startswith("9.") or question.startswith("13.") or \
               question.startswith("17."):
                extrovert += 1
            elif question.startswith("2.") or question.startswith("6.") or \
                 question.startswith("10.") or question.startswith("14.") or \
                 question.startswith("18."):
                sensing += 1
            elif question.startswith("3.") or question.startswith("7.") or \
                 question.startswith("11.") or question.startswith("15.") or \
                 question.startswith("19."):
                thinking += 1
            else:
                judging += 1
        elif answer == "B":
            if question.startswith("1.") or question.startswith("5.") or \
               question.startswith("9.") or question.startswith("13.") or \
               question.startswith("17."):
                introvert += 1
            elif question.startswith("2.") or question.startswith("6.") or \
                 question.startswith("10.") or question.startswith("14.") or \
                 question.startswith("18."):
                intuitive += 1
            elif question.startswith("3.") or question.startswith("7.") or \
                 question.startswith("11.") or question.startswith("15.") or \
                 question.startswith("19."):
                feeling += 1
            else:
                perceiving += 1

    print("""
        E - means extrovert
        I - means introvert
        J - means judging
        S - means sensing
        F - means feelings
        P - means perceiving
        T - means thinking
        N - means intuitive
    """)

    personality_type = ""
    personality_type += "E" if extrovert > introvert else "I"
    personality_type += "S" if sensing > intuitive else "N"
    personality_type += "T" if thinking > feeling else "F"
    personality_type += "J" if judging > perceiving else "P"

    print(f"Your MBTI personality result is: {personality_type}")

MBTI_personality_test()
