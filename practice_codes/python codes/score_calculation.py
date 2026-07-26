student_name=input("enter your name: ")
score=int(input("enter your score: "))
if score<0 or score>100:
    print("invalid number. enter correct score between 0 to 100")
else:
    print("check your grade")


    if score>=90:
        print("grade A")
        print("Excellent Effort")
    elif score>=80:
        print("grade B")
        print("Good Effort")

    elif score>=70:
        print("grade C")
        print("You need to work hard")
    elif score>=60:
        print("grade D")
        print("Poor Performance")


    if score<60:
        print(f"{student_name},you have been FAILED try to work hard and do get pass in next subject")
    else:
        print(f"{student_name}, you have been PASSED Congratulations")

