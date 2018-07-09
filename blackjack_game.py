from random import randint, shuffle


def hand_value(hand):
    '''int -> int
    >>> hand_value([2,3,8])
    13
    >>> hand_value([3,8,9])
    20
    >>> hand_value([2,7,8,1])
    18
    '''

    total = 0
    for card in hand:
        total = total + card
    return total


def blackjack():
    cards = []

    for _suit in range(4):
        for i in range(2, 11):
            cards.append(i)
        for _facecard in range(3):
            cards.append(10)
        cards.append(11)

    shuffle(cards)
    dealer = []
    player1 = []

    player1.append(cards.pop())
    dealer.append(cards.pop())
    player1.append(cards.pop())
    dealer.append(cards.pop())

    while True:
        print('Your hand:', player1, hand_value(player1))
        print('dealer top card:', dealer[0])
        choice = input('Would you like to hit or stay?').strip()
        if hand_value(player1) == 21 or hand_value(dealer):
            print('Blackjack')
            break
        if choice == 'hit':
            hand_value(player1) < hand_value(dealer)
            player1.append(cards.pop())

        elif choice == 'stay':
            break

        if sum(player1) > 21:
            print(' Player1 BUSTED')
            break

    while hand_value(player1) < 21 and hand_value(dealer) < 21:
        print(hand_value(player1))
        response = input('You ready?')
        if hand_value(dealer) == 21:
            print(Blackjack)
        if hand_value(dealer) <= 17:
            dealer.append(cards.pop())
        elif response == 'no':
            player1.append(cards.pop())

        if hand_value(dealer) > 21:
            print(' Dealer BUSSED')
            break

        elif response == 'yes':
            break

    if hand_value(player1) > 21:
        print('Dealer wins')

    if hand_value(dealer) > 21:
        print('Player1 wins')

    if hand_value(player1) > hand_value(dealer):
        print('Player wins')

    if hand_value(dealer) > hand_value(player1):
        print('Dealer wins')


def main():
    blackjack()


if __name__ == '__main__':
    main()
