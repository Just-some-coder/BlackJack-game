import random #all the libraries that might be useful
import time

# ? dealer cheating (taking best of three crads)
# ? difficulty level based of dealer algorithm
# ? algorithm so that dealer choses to hit or stand basing on players hand

answer = "Y"
guiDelay = 1
print("Welcome to BlackJack")
cash = float(input("Enter the amount of money you have: "))
time.sleep(guiDelay)

def blackJack(money,bet):   # Main Blackjack Function
    isDoubleDown = False

    a = ["Ace","2","3","4","5","6","7","8","9","10","King","Queen","Jack"] # deck Creation
    b = ["Spades","Clubs","Hearts","Diamonds"]
    deck = []
    for i in b:
        for j in a:
            deck.append(j+" of "+i)

    print(f"You have {money} dollars")
    time.sleep(guiDelay)
    print("New Round Begins")
    time.sleep(guiDelay)
    print(f"Bet Made : {bet} dollars")
    time.sleep(guiDelay)

    money-=bet
    dealerHand = []
    playerHand = []
    dealerWorth = 0
    playerWorth = 0
    dealerHand.append("?")
    dealerHand.append(random.choice(deck)) # Two Cards are added to player and dealer is given a hidden card?
    playerHand.append(random.choice(deck))
    playerHand.append(random.choice(deck))

    print(f"The Dealer has hand : {dealerHand}")
    time.sleep(guiDelay)
    print(f"The player has hand : {playerHand}")

    dealerHand[0]=random.choice(deck) # The hidden dealer card is added

    worth = {"Ace" : 11,"King":10,"Queen":10,"Jack":10} #value of face cards

    for i in dealerHand:   #player and dealer hand are calculated to worth
        if (i.split(" ")[0]) in worth.keys():
            dealerWorth+=worth[i.split(" ")[0]]
        else:
            dealerWorth+=int(i.split(" ")[0])
    for i in playerHand:
        if (i.split(" ")[0]) in worth.keys():
            playerWorth+=worth[i.split(" ")[0]]
        else:
            playerWorth+=int(i.split(" ")[0])


    time.sleep(guiDelay)
    print(f"The player has value : {playerWorth}")
    time.sleep(guiDelay)
    move = input("Enter Your Next move: Hit , Double Down (DD) , Stand : ")


    while move.lower()=="hit" and playerWorth<21: # if player choses to add another card
        time.sleep(guiDelay)
        playerHand.extend([random.choice(deck)])
        time.sleep(guiDelay)
        print(f"Player Hand : {playerHand}")
        if ((playerHand[-1].split())[0]) in worth.keys():
            playerWorth+=worth[(playerHand[-1].split()[0])]
        else:
            playerWorth+=int(playerHand[-1].split()[0])
        print(f"Player Worth is {playerWorth}")
        if playerWorth>=21:
            continue
        time.sleep(guiDelay)
        move = input("Enter Your Next move: Hit , Double Down (DD) , Stand : ")

    else: 
        if playerWorth>21: # if player exceeds 21
            time.sleep(guiDelay)
            print("Bust")
            print("You lose the round")
            time.sleep(guiDelay)
            time.sleep(guiDelay)
            print(f"You now have {money} dollar(s)")
            return money
        if move.upper() == "DD": # if player choses to double down
            money-=bet
            isDoubleDown=True
            playerHand.extend([random.choice(deck)])
            time.sleep(guiDelay)
            print(f"Player Hand : {playerHand}")
            time.sleep(guiDelay)
            if ((playerHand[-1].split())[0]) in worth.keys():
                playerWorth+=worth[(playerHand[-1].split()[0])]
                print(f"Player Worth is {playerWorth}")
            else:
                playerWorth+=int(playerHand[-1].split()[0])
                print(f"Player Worth is {playerWorth}")
    
    time.sleep(guiDelay)
    print(f"The Dealer's Hand Now Revealed: {dealerHand}")
    time.sleep(guiDelay)
    print(f"The Dealer's Hand is worth: {dealerWorth}")

    #dealer taking 0-3 cards at random
    for i in range(random.randrange(0,2)):
        dealerHand.append(random.choice(deck))
        if ((dealerHand[-1].split())[0]) in worth.keys():
            dealerWorth+=worth[(dealerHand[-1].split()[0])]
        else:
            dealerWorth+=int(dealerHand[-1].split()[0])

        time.sleep(guiDelay)
        print(f"The Dealer Choses to draw a Card")
        time.sleep(guiDelay)
        print(f"Dealer drew a : {dealerHand[-1]}")
        time.sleep(guiDelay)
        print(f"Dealer's Hand :{dealerHand}")
        time.sleep(guiDelay)
        print(f"Dealer Worth: {dealerWorth}")
        time.sleep(guiDelay)
    print(f"Dealer choses to Stay with their hand")
    time.sleep(guiDelay)
    

    # the final winner is decided
    if (dealerWorth>playerWorth or dealerWorth==21 or playerWorth>21) and  not (dealerWorth>21):
        print("Dealer Wins With a Blackjack" if dealerWorth==21 else "Dealer wins")
        isDoubleDown = False
        return money
    elif dealerWorth == playerWorth and dealerWorth<=21:
        print("A Double BlackJack! The player wins " if dealerWorth==21 else "Its a Tie. The Player Wins")
        money+=(4*bet if isDoubleDown else 2*bet)
        time.sleep(guiDelay)
        print(f"You now have {money} dollar(s)")
        isDoubleDown = False
        return money

    else:
        print("Player Wins With a Blackjack" if playerWorth==21 else "Player wins")
        money+=(4*bet if isDoubleDown else 2*bet)
        time.sleep(guiDelay)
        print(f"You now have {money} dollar(s)")
        isDoubleDown = False
        return money


# make money update in the main()
while answer=="Y":
    risk = int(input("Enter The bet You would like to make: "))
    cash = blackJack(cash,risk)
    time.sleep(guiDelay)
    answer = (input("Another Round?(y/n): ")).upper()
else:
    time.sleep(guiDelay)
    print(f"Your final Amount is {cash}")
    time.sleep(guiDelay)
    if cash<0:
        print("Hopefully, you can pay that debt")
    else:
        print("Hope you had fun")
    time.sleep(guiDelay)
    print("Thanks for playing the game")