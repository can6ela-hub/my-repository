print ("-----welcome to the Cupcake Party!-----")
R = int(input("how many regular boxes are there?"))#8
S = int(input("how many small boxes are there?"))#3

totalCupcakes = R * 8 + S * 3

students = 28

leftover = totalCupcakes - students

answer = input("if you calculated those numbers you put in just now,and there are 28 students, how many are leftover?")

if leftover == int(answer):
   print("yes you are correct!") 
else:
    print("no you are not correct, the answer is",leftover)