#question = list
#”question” & “answer” = dictionary
# this is three dictionaries

questions = [
        {"question": 'Name the movie this quote is from, "All my life I had to fight!"', "answer": "The Color Purple"},
        {"question": 'Name the movie this quote is from, " Im tired of this, Grandpa...Well thats too d*mn bad!"', "answer": 'Holes'},
        {"question": 'Name the movie this quote is from, " You been tripping every since I met you."', "answer": "Money Talks"}
              ]

def menu():
    print("let's play a game!")
    print("I will give you a quote from a movie and you name that movie!")
    print("Good Luck!")

print("What should I call you?")
you = input()
print("Heyy,", you + "!")

round = 0
answer = " "

for question in questions:
	print( " The game starts now!:" +question)
score = 0

while user_answer.lower() != question["answer"].lower() :
    print(f"Boooo tomatoes tomatoes! The movie is {question['answer']}.")
user_answer = input()


if user_answer.lower() == question["answer"].lower():
    print("Whew! You had me worried for a second!")
score += 1

else
    print("You won a knuckle sandwich! Try again lol")


print(f"\nThats a wrap folks! Your score is {score}/{len(questions)}.")

