print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")

text = "Sachin is greater"
print(text.lower())

if playing.lower() != "yes":
    quit()

print("okay! Let's play:)" )   
score = 0 

answer  = input("What does CPU for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")   

print("You got" + str(score) + "question correct!")  
print("You got" + str((score /4) * 100) + "%.")       