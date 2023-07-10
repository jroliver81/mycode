#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Name the movie this qoute is from, "All my life I had to fight!"')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == 'The Color Purple': # logic to check if user gave correct answer
        print('Whew! You had me worried for a second! lol')
        break             # break statement escapes the while loop
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Congrats! You won a knuckle sandwich!. Try again!')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
                print("You won a knuckle sandwich! Try again lol")

#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer != "The Color Purple":
    round += 1     # increase the round counter by 1
    answer = input('Name the movie this qoute is form, "All my life I had to fight!": ')
    if answer == "The Color Purple": # logic to check if user gave correct answer
        print("Whew! You had me worried for a second!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the movie was The Color Purple, you should check it out!")
    else:                 # if answer was wrong
        print("You won a knuckle sandwich! Try again lol")

