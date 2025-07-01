#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Welcome to my first game!')  #print() will simply output whatever is in the parenthesis. string values are inside quotation marks
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")

health = 10

if age >= 18:                                              #if the user is 18 or older, they will be told theyre old enough
    print("You are old enough to play!")
    wants_to_play = input("The goal of this game is to escape the forest you're stranded in. Do you want to play? ").lower() #.lower() converts input to lowercase to match if statement
    if wants_to_play == "yes":                            
        print("Let's play!")
        print("You are starting with a health of", health)
        
        left_or_right = input("First choice... Left or Right? (left/right) ").lower()  #input() allows user to type and enter their answer
        
        if left_or_right == "left":
            ans = input("Nice, you've reached a hidden waterfall... Do you take this chance to hydrate or turn around? (hydrate/turn) ").lower()
            
            if ans == "hydrate":
                print("You took the time to replenish... Uh oh, you're feeling a little sick. You got poisoned and lost 5 health")
                health -= 5    #health -= 5 is the same as --> health = health - 5
                
                ans = input("A large tree is right by you, do you want to rest under the tree until you feel better? (yes/no)")
                if ans == "yes":
                    print("The tree provided a great shade in the extreme heat! But you didn't realize you were resting under a beehive, and you got attacked by a swarm of bees. You lose.")
                elif ans == "no":
                    print("You continue on the path. The poisoning made you weak, but the extreme heat is making you even weaker. You lost 5 health.")
                    health -= 5

                    if health <= 0:                               #This if/else statement informs user if they still have health left
                        print("You lost all health. You lose..." )  #If they don't have health left, they can't continue the game
                    else:
                        print("You stil have health left, keep going!")
                        
            elif ans == "turn":
                ans = input("You're now being stalked by an eery figure. Do you run for your life or confront the figure? (run/confront) ")
                
                if ans == "confront":
                    print("Better luck next time, your bare hands were not enough to fight off the mysterious figure. You lost the fight and this game...")

                elif ans == "run":
                    print("You lost the figure... Then tripped and fell hard. You lost 5 health.")
                    health -=5
                    
                    if health <=0:
                        print("You lost all health. You lose...")
                    else:
                        print("You still have health left, keep going!")
                        ans = input("As you limp off, you notice smoke rising from the trees on your left. Ahead, there is also what looks like a lake. Do you follow the smoke or the lake? (smoke/lake) ").lower()
                        
                        if ans == "smoke":
                            print("Perfect timing! You followed the smoke and caught a group of campers preparing to leave and offered to give you a ride outta here! You win!")
                        elif ans == "lake":
                            print("Did we mention the forest is in Florida... The alligators got to you as you let your guard down for a second... You lose.")



        if left_or_right == "right":
            ans = input("You've walked up to a small cottage with an open door. Do you go in or keep straight? (in/straight) ").lower()
            if ans == "in":
                print("You are welcomed by a sweet family, but their dog isn't fond of you. You got bit and lost 5 health.")
                health -= 5
                if health <= 0:
                    print("You lost all health. You lose...")
                else:
                    print("You still have health left, keep going!")
                
                ans = input("The family is now weary of you. Do you try to explain your situation or quickly leave? (explain/leave) ")
                if ans == "explain":
                    print("The family was very understanding.. or so you thought. However, they refuse to let you out and block all chances of escaping. You lose...")
                elif ans == "leave":
                    print("The family was insulted by your hastiness. They let the dogs out to chase you. You could not beat the 3 dogs. You lose...")
                
                

            if ans == "straight":
                print("You kept straight, and now you've stumbled upon an abandoned car.")
                ans = input("Would you like to explore the car or keep straight? (car/straight) ")
                
                if ans == "car":
                    print("Getaway car! You found the keys and a map of the forest inside! You win and are now able to escape the forest!")
                
                elif ans == "straight":
                    print("Watch your step! You accidently fell inside an old well and got stuck. You lose...")
                

                
            


    
    else:
        print("Cya...")   #The message if user answers no to whether or not they want to play
else:
    print("You are not old enough to play...")  #the message if user is younger than 18


# In[ ]:




