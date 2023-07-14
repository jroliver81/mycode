""" Personal Project, My favorite movie quotes"""

#question = list
#"question" & “answer” = dictionary
# this is three dictionaries

from PIL import Image
import crayons
import random
questions = [
        {"question": 'Name the movie this quote is from, " All my life I had to fight!"', "answer": "The Color Purple"},
        {"question": 'Name the movie this quote is from, " Im tired of this, Grandpa...Well thats too d*mn bad!"', "answer": 'Holes'},
        {"question": 'Name the movie this quote is from, " You been tripping every since I met you."', "answer": "Money Talks"},
        {"question": 'Name the movie this quote is from, " Ms.Hughes, what page fifteen on?"', "answer": "The Wood"},
        {"question": 'Name the movie this quote is from, " Forty Dolllaaarrss..Squeeze my tiny self up in this *smacks lips* Cute"', "answer": "Baby boy"},
        {"question": 'Name the movie this quote is from, " Yall aint never got two things that match.Either yall got Kool Aid, no sugar..."', "answer": "Friday"}
              ]


def main():
    print(f'{crayons.yellow("Want to play a game?", bold=True)}')
    print(f'{crayons.yellow("I will give you a quote from a movie and you name that movie!", bold=True)}')
    print(f'{crayons.yellow("Make sure you know the", bold=True)} {crayons.magenta("EXACT", bold=True)} {crayons.yellow("name of the movie title!", bold=True)}')
    print(f'{crayons.yellow("Type", bold=True)} {crayons.magenta("DONE", bold=True)} {crayons.yellow("to quit at any time.", bold=True)}')
    print(f'{crayons.green("Good Luck!", bold=True)}')
    print(f'{crayons.magenta("**********************************")}')

    print("What should I call you?")
    you = input()
    print("Heyy,", you + "!")
    print(f'{crayons.magenta("***********************************")}')

    score = 0
    image = Image.open(".jpg")

    for i in range(6):
        question = random.choice(questions)
        print(f"{crayons.cyan(question['question'])}")
        user_answer = input()

        if user_answer.lower() == 'done':
            break

        if user_answer.lower() == question["answer"].lower():
            print(f"{crayons.blue('Whew!')} You had me worried for a second!")
            score += 1
            questions.remove(question)

        else:
            print(f"{crayons.red('Boooo', bold=True)}"
                  f"{crayons.red(' tomatoes tomatoes!')} The movie is {crayons.cyan(question['answer'])}")
            score -= 0
            questions.remove(question)
    if score == 6:
        print(f'\n{crayons.yellow("See! I knew I liked you for a reason! Your score is", bold=True)} {score}/{len(questions)}.')
    if score < 6:
        print(f'\n{crayons.yellow("Sucks to be you, upgrade your watch list! Your score is", bold=True)} {score}/{len(questions)}.')
if __name__ == "__main__":
    main()
