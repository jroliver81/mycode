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

round = 0
answer = " "

for item in questions:
    while round < 3 and answer != item['answer']:
    round += 1     
    answer = input(item['question'])
    if answer == item['answer']:
        print("Whew! You had me worried for a second!")
    elif round == 3:    
        print(f"Sorry, the movie was {item['answer']}, you should check it out!")
    else:               
        print("You won a knuckle sandwich! Try again lol")
