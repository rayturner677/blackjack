from random import randint, shuffle


def blackjack():
    cards = []

    for _suit in range(4):
        for i in range(2, 11):
            cards.append(i)
        for _facecard in range(3):
            cards.append(10)
    cards.append('Ace')

    shuffle(cards)
    dealer = []
    player1 = []

    player1.append(cards.pop())
    dealer.append(cards.pop())
    player1.append(cards.pop())
    dealer.append(cards.pop())

    while True:
        print('Your hand:', player1)
        print('dealer top card:', dealer[0])
        choice = input('Would you like to hit or stay?').strip()
        if choice == 'hit':
            sum(player1) < sum(dealer)
            print(sum(player1))
            player1.append(cards.pop())

        elif sum(player1) == 21:
            print('Blackjack')

        elif choice == 'stay':
            break

        else:
            if sum(player1) > 21:
                print('BUSSED')

    while sum(player1) < 22 and sum(dealer) < 22:
        print(sum(player1))
        response = input('Would the dealer like to hit or stay?').strip()
        if response == 'hit':
            player1.append(cards.pop())

        if sum(dealer) == 21:
            print('Blackjack')

        if sum(dealer) > 21:
            print('BUSSED')

        elif response == 'stay':
            break

    if sum(player1) > sum(dealer):
        print('Player wins')

    if sum(dealer) > sum(player1):
        print('dealer wins')


blackjack()
