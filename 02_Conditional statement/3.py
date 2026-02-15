# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), E (below 60).
score = input("Enter your score: ")
score_in_int = int(score)
if(score_in_int>100): 
    print("Invalid")
    exit()
elif(score_in_int<60):print("E")
elif(score_in_int<70):print("D")
elif(score_in_int<80):print("C")
elif(score_in_int<90):print("B")
else:print("A")


