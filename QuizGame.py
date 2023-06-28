print ("Hellow welcome to quiz game")
playing = input("Do you want to play play? ")
if playing.lower() != "yes":
    quit()
score=0
print("  ")
print ("okkay lets play the game:-")

answer = input("how many hour you are daily giving to your laptop? ")
if answer.lower() == "2hour":
     print("Correct")
     score+=1

else:
    print("Incorrect")

answer = input("how much do you scroll socialn media daily?  ")
if answer.lower() == "2hour":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What do you think is it important right now to waste to hours on daily basis?  ")
if answer.lower() == "well not":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what do you think where you would be after 2 or 3 years")
if answer.lower() == "on the way to great":
    print("Correct")
    score+=1
else:
    print("Incorrect")
print("you get " +str(score)+ " Correct answer" )
print("you get "+str((score/4)*100)+" percentage")

