questionlist=["[null]","1","2","3","4","5"]
print("*********************************")
print("           C  EXAM               ")
print("*********************************")
score=0
print("1-What is the function that output text to the screen")
print("A)print()                       B)output()           ")
print("C)printf()                      D)outputf()          ")
answer1 = 0
while answer1 != 1:
    answer1 = input("Do you want to answer? (Y) or (N) ")
    if answer1 == "Y" or answer1 == "y":
        answer2 = 0
        while answer2 != 1:
            answer2 = input("Your answer: ")
            if answer2 == "C" or answer2 == "c":
                score = score + 1
                print("Your answer is correct.")
                answer2 = 1
                questionlist.pop(1)
                questionlist.insert(1,"")
            elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                score = score - 1
                print("Your answer was incorrect.Correct answer is 'C'")
                answer2 = 1
                questionlist.pop(1)
                questionlist.insert(1, "")
            else:
                print("Wrong letter.Be sure that you enter the correct letter and try again!")
        answer1 = 1
    elif answer1 == "N" or answer1 == "n":
        print("You skipped the question.You can try again when you finished the exam.")
        answer1 = 1
    else:
          print("Wrong letter.Be sure that you enter the correct letter and try again!")
print("2-What is the function that gets information from the user?")
print("A)scanf()                       B)input()         ")
print("C)scan()                        D)inputf()        ")
answer1 = 0
while answer1 != 1:
    answer1 = input("Do you want to answer? (Y) or (N) ")
    if answer1 == "Y" or answer1 == "y":
        answer2 = 0
        while answer2 != 1:
               answer2 = input("Your answer: ")
               if answer2 == "A" or answer2 == "a":
                score = score + 1
                print("Your answer is correct.")
                questionlist.pop(2)
                questionlist.insert(2, "")
                answer2 = 1
               elif answer2 == "C" or answer2 == "c" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                 score = score - 1
                 print("Your answer was incorrect.Correct answer is 'A'")
                 questionlist.pop(2)
                 questionlist.insert(2, "")
                 answer2 = 1
               else:
                 print("Wrong letter.Be sure that you enter the correct letter and try again!")
               answer1 = 1
    elif answer1 == "N" or answer1 == "n":
        print("You skipped the question.You can try again when you finished the exam.")
        answer1 = 1
    else:
        print("Wrong letter.Be sure that you enter the correct letter and try again!")
print("3-What is the most necessary function?")
print("A)main                      B)def           ")
print("C)void                      D)while         ")
answer1 = 0
while answer1 != 1:
     answer1 = input("Do you want to answer? (Y) or (N) ")
     if answer1 == "Y" or answer1 == "y":
        answer2 = 0
        while answer2 != 1:
            answer2 = input("Your answer: ")
            if answer2 == "A" or answer2 == "a":
                score = score + 1
                print("Your answer is correct.")
                questionlist.pop(3)
                questionlist.insert(3, "")
                answer2 = 1
            elif answer2 == "C" or answer2 == "c" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                score = score - 1
                print("Your answer was incorrect.Correct answer is 'A'")
                questionlist.pop(3)
                questionlist.insert(3, "")
                answer2 = 1
            else:
                print("Wrong letter.Be sure that you enter the correct letter and try again!")
        answer1 = 1
     elif answer1 == "N" or answer1 == "n":
         print("You skipped the question.You can try again when you finished the exam.")
         answer1 = 1
     else:
        print("Wrong letter.Be sure that you enter the correct letter and try again!")
print("4-What is the variable that stores single characters?")
print("A)double                   B)float           ")
print("C)int                      D)char            ")
answer1 = 0
while answer1 != 1:
    answer1 = input("Do you want to answer? (Y) or (N) ")
    if answer1 == "Y" or answer1 == "y":
        answer2 = 0
        while answer2 != 1:
            answer2 = input("Your answer: ")
            if answer2 == "D" or answer2 == "d":
                score = score + 1
                print("Your answer is correct.")
                questionlist.pop(4)
                questionlist.insert(4, "")
                answer2 = 1
                answer1=1
            elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "c" or answer2 == "C":
                score = score - 1
                print("Your answer was incorrect.Correct answer is 'D'")
                questionlist.pop(4)
                questionlist.insert(4, "")
                answer2 = 1
                answer1=1
            else:
                print("Wrong letter.Be sure that you enter the correct letter and try again!")
    elif answer1=="N" or answer1=="n":
        print("You skipped the question.You can try again when you finished the exam.")
        answer1 = 1
    else:
        print("Wrong letter.Be sure that you enter the correct letter and try again!")
print("5-What is the format specifier that uses for integers?")
print("A)%s                        B)%lf            ")
print("C)%d                        D)%f            ")
answer1 = 0
while answer1 != 1:
    answer1 = input("Do you want to answer? (Y) or (N) ")
    if answer1 == "Y" or answer1 == "y":
        answer2 = 0
        while answer2 != 1:
            answer2 = input("Your answer: ")
            if answer2 == "C" or answer2 == "c":
                score = score + 1
                print("Your answer is correct.")
                questionlist.pop(5)
                questionlist.insert(5, "")
                answer2 = 1
            elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                score = score - 1
                print("Your answer was incorrect.Correct answer is 'C'")
                questionlist.pop(5)
                questionlist.insert(5, "")
                answer2 = 1
            else:
                 print("Wrong letter.Be sure that you enter the correct letter and try again!")
            answer1 = 1
    elif answer1 == "N" or answer1 == "n":
        print("You skipped the question.You can try again when you finished the exam.")
        answer1 = 1
    else:
        print("Wrong letter.Be sure that you enter the correct letter and try again!")
answer3 = 0
while answer3 != 1:
    answer3 = input("Do you want to answer the questions that you skipped?")
    if answer3 == "y" or answer3 == "Y":
        answer4 = "m"
        while answer4 != "k":
            answer4 = int(input("Which is the question that you want to answer?"))
            if answer4 == 1:
                if questionlist[1]!="":
                    answer4 = "k"
                    print("1-What is the function that output text to the screen")
                    print("A)print()                       B)output()           ")
                    print("C)printf()                      D)outputf()          ")
                    answer1 = 0
                    while answer1 != 1:
                        answer1 = input("Do you want to answer? (Y) or (N) ")
                        if answer1 == "Y" or answer1 == "y":
                            answer2 = 0
                            while answer2 != 1:
                                answer2 = input("Your answer: ")
                                if answer2 == "C" or answer2 == "c":
                                    score = score + 1
                                    print("Your answer is correct.")
                                    answer2 = 1
                                    questionlist.pop(1)
                                    questionlist.insert(1, "")
                                elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                                    score = score - 1
                                    print("Your answer was incorrect.Correct answer is 'C'")
                                    answer2 = 1
                                    questionlist.pop(1)
                                    questionlist.insert(1, "")
                                else:
                                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
                            answer1 = 1
                        elif answer1 == "N" or answer1 == "n":
                            print("You skipped the question.You can try again when you finished the exam.")
                            answer1 = 1
                        else:
                            print("Wrong letter.Be sure that you enter the correct letter and try again!")
                else:
                    print("You can not answer the question that you already answered.")
            if answer4 == 2:
                if questionlist[2]!="":
                    answer4 = "k"
                    print("2-What is the function that gets information from the user?")
                    print("A)scanf()                       B)input()         ")
                    print("C)scan()                        D)inputf()        ")
                    answer1 = 0
                    while answer1 != 1:
                        answer1 = input("Do you want to answer? (Y) or (N) ")
                        if answer1 == "Y" or answer1 == "y":
                            answer2 = 0
                            while answer2 != 1:
                                answer2 = input("Your answer: ")
                                if answer2 == "A" or answer2 == "a":
                                    score = score + 1
                                    print("Your answer is correct.")
                                    questionlist.pop(2)
                                    questionlist.insert(2, "")
                                    answer2 = 1
                                elif answer2 == "C" or answer2 == "c" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                                    score = score - 1
                                    print("Your answer was incorrect.Correct answer is 'A'")
                                    questionlist.pop(2)
                                    questionlist.insert(2, "")
                                    answer2 = 1
                                else:
                                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
                                answer1 = 1
                        elif answer1 == "N" or answer1 == "n":
                            print("You skipped the question.You can try again when you finished the exam.")
                            answer1 = 1
                        else:
                            print("Wrong letter.Be sure that you enter the correct letter and try again!")
                else:
                    print("You can not answer the question that you already answered.")
            if answer4 == 3:
                if questionlist[3]!="":
                    answer4 = "k"
                    print("3-What is the most necessary function?")
                    print("A)main                      B)def           ")
                    print("C)void                      D)while         ")
                    answer1 = 0
                    while answer1 != 1:
                        answer1 = input("Do you want to answer? (Y) or (N) ")
                        if answer1 == "Y" or answer1 == "y":
                            answer2 = 0
                            while answer2 != 1:
                                answer2 = input("Your answer: ")
                                if answer2 == "A" or answer2 == "a":
                                    score = score + 1
                                    print("Your answer is correct.")
                                    questionlist.pop(3)
                                    questionlist.insert(3, "")
                                    answer2 = 1
                                elif answer2 == "C" or answer2 == "c" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                                    score = score - 1
                                    print("Your answer was incorrect.Correct answer is 'A'")
                                    questionlist.pop(3)
                                    questionlist.insert(3, "")
                                    answer2 = 1
                                else:
                                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
                            answer1 = 1
                        elif answer1 == "N" or answer1 == "n":
                            print("You skipped the question.You can try again when you finished the exam.")
                            answer1 = 1
                        else:
                            print("Wrong letter.Be sure that you enter the correct letter and try again!")
                else:
                    print("You can not answer the question that you already answered.")
            if answer4 == 4:
                if questionlist[4]!="":
                    answer4 = "k"
                    print("4-What is the variable that stores single characters?")
                    print("A)double                   B)float           ")
                    print("C)int                      D)char            ")
                    answer1 = 0
                    while answer1 != 1:
                        answer1 = input("Do you want to answer? (Y) or (N) ")
                        if answer1 == "Y" or answer1 == "y":
                            answer2 = 0
                            while answer2 != 1:
                                answer2 = input("Your answer: ")
                                if answer2 == "D" or answer2 == "d":
                                    score = score + 1
                                    print("Your answer is correct.")
                                    questionlist.pop(4)
                                    questionlist.insert(4, "")
                                    answer2 = 1
                                elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "c" or answer2 == "C":
                                    score = score - 1
                                    print("Your answer was incorrect.Correct answer is 'D'")
                                    questionlist.pop(4)
                                    questionlist.insert(4, "")
                                    answer2 = 1
                                else:
                                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
                        elif answer1 == "N" or answer1 == "n":
                            print("You skipped the question.You can try again when you finished the exam.")
                            answer1 = 1
                        else:
                            print("Wrong letter.Be sure that you enter the correct letter and try again!")
                else:
                    print("You can not answer the question that you already answered.")
                    answer4 = "k"
            if answer4 == 5:
                if questionlist[5]!="":
                    answer4 = "k"
                    print("5-What is the format specifier that uses for integers?")
                    print("A)%s                        B)%lf            ")
                    print("C)%d                        D)%f            ")
                    answer1 = 0
                    while answer1 != 1:
                        answer1 = input("Do you want to answer? (Y) or (N) ")
                        if answer1 == "Y" or answer1 == "y":
                            answer2 = 0
                            while answer2 != 1:
                                answer2 = input("Your answer: ")
                                if answer2 == "C" or answer2 == "c":
                                    score = score + 1
                                    print("Your answer is correct.")
                                    questionlist.pop(5)
                                    questionlist.insert(5, "")
                                    answer2 = 1
                                elif answer2 == "A" or answer2 == "a" or answer2 == "b" or answer2 == "B" or answer2 == "d" or answer2 == "D":
                                    score = score - 1
                                    print("Your answer was incorrect.Correct answer is 'C'")
                                    questionlist.pop(5)
                                    questionlist.insert(5, "")
                                    answer2 = 1
                                else:
                                    print("Wrong letter.Be sure that you enter the correct letter and try again!")
                                answer1 = 1
                        elif answer1 == "N" or answer1 == "n":
                            print("You skipped the question.You can try again when you finished the exam.")
                            answer1 = 1
                        else:
                            print("Wrong letter.Be sure that you enter the correct letter and try again!")
                else:
                    print("You can not answer the question that you already answered.")
    elif answer3 == "N" or "n":
        answer3 = 1
print("Your exam is done.Your total score:"+ str(score))