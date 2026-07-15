import random

print("-------------------- RPS Challenge ---------------------")
print("Rock. Paper. Scissors. Powered by Python, Driven by Fun!")
print("--------------------------------------------------------")
print("Quit Will end this War!!!")
ch=["rock","paper","scissor"]
win=0
los=0
tie=0
rnd=0
while True:
    print()
    ures=input("Your Choice : ")
    if ures.lower()=="quit":
        print("Thank you For Playing")
        break
    if ures not in ch:
        print("Invalid choice,Please Try again")
    cres=random.choice(ch)
    print("Computer's Choice: ",cres)
    if ures==cres:
        print("Draw")
        tie+=1
        rnd+=1
    elif (ures.lower()=="rock" and cres.lower=="paper") or (ures.lower()=="paper" and cres=="scissor") or (ures=="scissor" and cres=="paper"):
        print("You Win!!")
        rnd+=1
        win+=1
    else:
        print("Computer Wins!!")
        rnd+=1
        los+=1

print()
print("-------Game is Ended-------")
print("Total Rounds  :",rnd)
print("Win           :",win)
print("Loss          :",los)
print("Tie           :",tie)
        
