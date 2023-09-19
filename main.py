from random import randint

randomList = []
for i in range(20):
    randomList.append(randint(0, 5000))

exit = False
while not exit:
    print("MAIN MENU")
    print("1: Print Accounts")
    print("2: Deposit")
    print("3: Withdrawal")
    print("4: Count Under $2000")
    print("5: Generous Donor")
    print("6: Hacker Attack")
    print("7: Exit")
    choice = int(input(""))

    if(choice == 1):
        count = 0
        for i in randomList:
            print(f"Account {count}: ${i}")
            count+=1
    elif(choice == 2):
        print("DEPOSIT")
        account = int(input("Enter Account #:"))
        amt = int(input("Enter amount:"))
        print(f"Account {account} Previous Balance: {randomList[account]}")
        randomList[account] += amt
        print(f"Account {account} New Balance: {randomList[account]}")
    elif(choice == 3):
        print("WITHDRAWAL")
        account = int(input("Enter Account #:"))
        amt = int(input("Enter amount:"))
        if(amt <= randomList[account]):
            print(f"Account {account} Previous Balance: {randomList[account]}")
            randomList[account] -= amt
            print(f"Account {account} New Balance: {randomList[account]}")
        else:
            print("Sorry, insufficient funds.")
    elif(choice == 4):
        print("COUNT UNDER $2000")
        count = 0
        for i in range(len(randomList)):
            if(randomList[i] < 2000):
                count+=1
                print(f"Account {i}: ${randomList[i]}")
        print(f"Accounts with less than $2000: {count}")

    elif(choice == 5):
        print("GENEROUS DONOR")
        for i in range(len(randomList)):
            if(randomList[i] < 2000):
                print(f"Account {i} Previous Balance: {randomList[i]}")
                randomList[i] += 500
                print(f"Account {i} New Balance: {randomList[i]}")
    elif(choice == 6):
        print("Hacker Attack")
        tot = 0
        for i in range(len(randomList)):
            amt = (randomList[i] * 0.05)
            tot += amt
            randomList[i] -= amt
        print(f"Total stolen is: {tot}")
    else:
        exit = True
