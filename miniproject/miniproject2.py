#question = list
#"question" & “answer” = dictionary
# this is three dictionaries

import random
questions = [
        {"question": 'Name the movie this quote is from, "All my life I had to fight!"', "answer": "The Color Purple"},
        {"question": 'Name the movie this quote is from, " Im tired of this, Grandpa...Well thats too d*mn bad!"', "answer": 'Holes'},
        {"question": 'Name the movie this quote is from, " You been tripping every since I met you."', "answer": "Money Talks"}
              ]

def main():
    print("let's play a game!")
    print("I will give you a quote from a movie and you name that movie!")
    print("Type 'done' to quit at any time.")
    print("Good Luck!")

    print("What should I call you?")
    you = input()
    print("Heyy,", you + "!")

    score = 0
#    retry = false
    for i in range(3):
        question = random.choice(questions)
        print(question["question"])
        user_answer = input()

        if user_answer.lower() == 'done':
            break

        if user_answer.lower() == question["answer"].lower():
            print("Whew! You had me worried for a second!")
            score += 1
 #           retry = true
            questions.remove(question)

        elif user_answer.lower() != question["answer"].lower():
            print("You won a knuckle sandwich! Try again lol")
  #          retry = false
   #     if retry:
    #        user_answer.lower() != question["answer"].lower():
     #       pass

        else:
            print(f"Boooo tomatoes tomatoes! The movie is {question['answer']}.")

    if score > 0:
        print(f"\nThats a wrap folks! Your score is {score}/{len(questions)}.")

if __name__ == "__main__":
    main()
