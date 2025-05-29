import random

##first execise
# inputStr = input("verb: ")
# outputStr = f"I can {inputStr} better than you!"
# print(outputStr, (inputStr + " ") * 4 + inputStr, sep= "\n")


##Second exercise
# secret = random.randint(0,10)
# Answer = input("Can you guess the secret integer 0-10? ")
# while True:
#     try: 
#         user_number = int(Answer)
#         if user_number == secret:
#             print(f"Yes, the secret integer is: {secret}")
#         else:
#             print(f"No, the secret integer is: {secret}")
#         break
#     except ValueError:
#         input("Could not convert to an integer. Please try again: ")



#third execise
secret = random.randint(0,10)
Answer = input("Can you guess the secret integer 0-10? ")
while True:
    try: 
        user_number = int(Answer)
        if user_number == secret:
            print(f"Yes, the secret integer is: {secret}")
        elif user_number < secret:
            print(f"too low, the secret integer is: {secret}")
        elif user_number > secret:
            print(f"too high, the secret integer is: {secret}")
        break
    except ValueError:
        Answer = input("Could not convert to an integer. Please try again: ")