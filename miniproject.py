#!/usr/bin/env python3

"""
Let's guess some movie quotes! 
I will give you a quote and you name the movie. 
Good Luck!

"""
round = 0           
while True:        
    round = round + 1     
    print('Name the movie this quote is from, "All my life I had to fight!"')
    answer = input("Your guess--> ")    
    if answer == 'The Color Purple': 
        print('Whew! You had me worried for a second! lol')
        break             
    elif round == 3:    
        print('Congrats! You won a knuckle sandwich!. Try again!')
        break             
    else:               
                print("You won a knuckle sandwich! Try again lol")
