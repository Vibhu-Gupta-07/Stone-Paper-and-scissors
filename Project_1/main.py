import random
'''
1 for rock
-1 for paper
0 for sicsoor
'''

computer = random.choice([-1,0,1])

print("Want to play rock, paper, sicsoor")

print("r = rock\ns = sicsoor\np = paper")

youstr = input("Enter your choice between r/p/s: ")

if (youstr == "r" or youstr == "p" or youstr == "s"):
    
    youDict = {"r":1,"p":-1,"s":0}
    
    reverseDict = {1:"rock",-1:"paper",0:"sicsoor"}
    
    you = youDict[youstr]
    
    print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

    if(computer == you ):        
        print("Match draw")
       #another short method
    #elif((computer - you)== -1 or (computer - you)==2 ):
    #     print("you Win!")
    # else:
    #     print("you lose!")
        
    else:
        if(computer == -1 and you == 1):    # c = paper   y = rock   {-1 -(1)  = -2}
            print("You lose!")
        elif(computer == 0 and you == -1):           # c = sicsoor y = paper {0  -(-1)  = 1}
            print("you lose!")
        elif(computer == 1 and you == 0):          # c = rock y = sicsoor {1 - 0  = 1}
            print("you lose!")
        elif(computer == 1 and you == -1):         # c= rock y = paper {1 - (-1)  = 2}
            print("You Win!")
        elif(computer == -1 and you == 0):          # c = paper y = sicsoor {-1 - 0  = -1}
            print("you win!")
        elif(computer == 0 and you == 1):         # c = sicsoor  y = rock  {0 -(1)  = -1}
            print("You Win!")
        else:
            print("something went wrong")
            
else:
    print("incorrect input")

