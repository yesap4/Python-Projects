count = 0
def ques():
    ques1 = input("Are you above 18 years of age? (yes/no): ")
    if ques1.lower() == 'yes':
        ques2 = input("Do you have a valid ID proof? (yes/no): ")
        if ques2.lower() == 'yes':
            print("You are eligible to vote.")
        elif ques2.lower() == 'no':
            print("You need a valid ID proof to vote.")
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
    elif ques1.lower() == 'no':
        print("You are not eligible to vote.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")       
    global count
    count += 1
    if count < 3:
        ques()
    else:
        print("Thank you for using the voting eligibility checker.")
ques()
