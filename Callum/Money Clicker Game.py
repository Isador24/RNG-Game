print("Welcome to the money clicker game!")
print("Type 1 to click for money, or 2 to visit the shop!")
money = 0
cupgrade = "Lvl 0"
iupgrade = "Lvl 0"
run = True
while run == True:
    click = input("Choose an option.")
    if click == "1":
        if cupgrade == "Lvl 0":
            money += 1
        elif cupgrade == "Lvl 1":
            money += 2
        print("You have $" + str(money))
    if click == "2":
        print("Welcome to the shop!")
        option = input("Type 1 to view clicking power upgrades, 2 to view idle upgrades, and 3 to leave.")
        if option == "1":
            print("Clicking power is currently at " + cupgrade)
            option2 = input("Type 1 to upgrade clicking power for $10, or 2 to leave.")
            if option2 == "1" and money > 9:
                money -= 10
                cupgrade = "Lvl 1"
                print("Clicking power upgraded to " + cupgrade)
                option2 = "2"
            if option2 == "1" and money < 10:
                print("Insufficient funds. Please try again later once you meet the requirements.")
                option2 = "2"
            if option2 == "2":
                print("You have left clicking power upgrades.")
                option = "3"
        if option == "2":
            print("Idle upgrades are currently at " + iupgrade)
            option3 = input("Type 1 to upgrade idle upgrades for $10, or 2 to leave.")
            if option3 == "1" and money > 9:
                money -= 10
                iupgrade = "Lvl 1"
                print("Idle upgrades upgraded to " + iupgrade)
            if option3 == "1" and money < 10:
                print("Insufficient funds. Please try again later once you meet the requirements.")
                option3 = "2"
            if option3 == "2":
                print("You have left idle upgrades.")
                option = "3"
        if option == "3":
            print("You have left the shop.")
            continue