points=0
print("Welcome")

easy = input("1+2=" )

if easy == "3":
    print("Correct!")
    points += 1

medium = input("15*5=" )

if medium == "75":
    print("Correct again!")
    points += 2

hard = input("2^10=" )

if hard == "1024":
    print("Very good!")
    points += 3

print("Are you ready?")

impossible = input("-42+29=" )

if impossible == "-13":
    print("Congratulations!")
    points += 4
    print("You win!")
print(points)

if points == 10:
    print("Highscore achieved!")
    print("But you got the boring ending.")

if points > 0 and points < 10:
    print("You did fine.")
    print("You got the regular ending.")

if points == 0:
    print("Are you okay?")
    while True:
        check = input("Type YES to prove you are a human (case sensitive)" )
        if check == "YES":
            print("Due to an error try this.")
            retry = input("How many people are there on earth? (To the nearest billion)" )
            if retry == "8000000000" or retry == "8 billion" or retry == "8,000,000,000":
                print("You have confirmed.")
                print("Welcome to the money clicker game!")
                money = 0
                click = input("Type click to gain $1")
                if click == "click":
                    money += 1
                    print(money)
                    upgrade = input("Type up to spend 10 dollars to upgrade clicking power")
                    if upgrade == "up" and money > 9:
                        money -= 10    
                    if upgrade == "up" and money < 10:
                        print("Insufficient funds. Please try again later once you meet the requirements.")
                        print("You have reached the end of the calculator game. Thank you for playing!")
                        print("You got the good ending!")    
                break
            else:
                continue
        if check == "yes" or check == "Yes" or check == "YEs" or check == "yEs" or check == "yES" or check == "yeS":
            print("Make sure ALL letters are capitalized!")
            continue
        if check == "NO" or check == "no" or check == "No" or check == "nO":
            print("Our AI has detected that you are likely a robot. As a result, your IP has been banned from this site indefinitely. If you believe you were falsely banned, contact our support team at support@calculatorgame.com, or call us at 1-800-123-1575")
            print("You got the rebellious ending.")
            break
        



