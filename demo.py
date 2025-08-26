import random
file = open("score.txt", "w")
print("Welcome to number guessing game:")
name = input("Enter your name:")
file.write(f"Player Name: {name}\n")

def feedback(random_number, userguess):
    difference = abs(random_number - userguess)
    if difference == 0:
        print("Congrats!You've guessed the correct number")
    elif difference > 40:
        print("Way off!")
    elif difference >= 20 and difference < 40:
        print("Still quite far")
    elif difference >= 10 and difference < 20:
        print("You're getting close")
    else:
        print("Almost there")

def hint(max, random_number):
    half = max / 2
    if random_number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    if random_number > half:
        print("Number is in upper half")
    else:
        print("Number is in lower half")

def gameplay(level):
    usedhints = 0
    usedattempts = 0  # <-- Added to track used attempts

    if level == 1:
        min = 1
        max = 50
        attempts = 12
        random_number = random.randint(min, max)
        print("Enter a number between 1 and 50:")
        for i in range(attempts):
            print(f"\nAttempt {i + 1}")
            user_input = input("Enter your guess or press 'H' for a hint: ").strip().lower()
            if user_input == 'h':
                usedhints += 1
                hint(max, random_number)
            else:
                userguess = int(user_input)
                usedattempts += 1
                if userguess == random_number:
                    print("Correct guess")
                    break
                else:
                    print("Incorrect guess")
                    feedback(random_number, userguess)
        else:
            print("You've used all your attempts. The correct number was", random_number)

        score = (attempts - usedattempts) * 10 - (usedhints * 5)
        print("Score:", score)
        file.write(f"Score: {score}\n")

    elif level == 2:
        min = 1
        max = 100
        attempts = 10
        random_number = random.randint(min, max)
        print("Enter a number between 1 and 100:")
        for i in range(attempts):
            print(f"\nAttempt {i + 1}")
            user_input = input("Enter your guess or press 'H' for a hint: ").strip().lower()
            if user_input == 'h':
                usedhints += 1
                hint(max, random_number)
            else:
                userguess = int(user_input)
                usedattempts += 1
                if userguess == random_number:
                    print("Correct guess")
                    break
                else:
                    print("Incorrect guess")
                    feedback(random_number, userguess)
        else:
            print("You've used all your attempts. The correct number was", random_number)

        score = (attempts - usedattempts) * 10 - (usedhints * 5)
        print("Score:", score)
        file.write(f"Score: {score}\n")

    elif level == 3:
        min = 1
        max = 200
        attempts = 8
        random_number = random.randint(min, max)
        print("Enter a number between 1 and 200:")
        for i in range(attempts):
            print(f"\nAttempt {i + 1}")
            user_input = input("Enter your guess or press 'H' for a hint: ").strip().lower()
            if user_input == 'h':
                usedhints += 1
                hint(max, random_number)
            else:
                userguess = int(user_input)
                usedattempts += 1
                if userguess == random_number:
                    print("Correct guess")
                    break
                else:
                    print("Incorrect guess")
                    print(random_number, userguess)
        else:
            print("You've used all your attempts. The correct number was", random_number)

        score = (attempts - usedattempts) * 10 - (usedhints * 5)
        print("Score:", score)
        file.write(f"Score: {score}\n")

print("Press 1 for level 1 : Easy")
print("Press 2 for level 2 : Medium")
print("Press 3 for level 3 : Hard")
level = int(input())
if level == 1:
    gameplay(1)
elif level == 2:
    gameplay(2)
else:
    gameplay(3)

file.write(f"Level: {level}\n")
file.close()


           








    
    
    
    



