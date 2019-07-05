def highest_card(first, second, trump_suit):
    order = "6, 7, 8, 9, 10, J, Q, K, A".split(', ')
    first_value, first_suit = first[0:-1], first[-1]
    second_value, second_suit = second[0:-1], second[-1]

    if first_suit == second_suit:
        if order.index(first_value) > order.index(second_value):
            return 'First'
        else:
            return 'Second'
    else:
        if first_suit == trump_suit:
            return 'First'
        elif second_suit == trump_suit:
            return 'Second'
        else:
            return 'Error'


first_card, second_card = input().split()
trump = input()

print(highest_card(first_card, second_card, trump))


