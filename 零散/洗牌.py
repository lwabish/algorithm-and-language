import random
colors = ['♥️', '♦️', '♣️', '♠️']
nums = ['A',  2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


def generate_all_cards():
    cards = list()
    for i in colors:
        for j in nums:
            card_name = i + str(j)
            cards.append(card_name)
    cards += ['大王', '小王']
    return cards


def shuffle_card(n):
    cards = generate_all_cards()
    print(cards)
    shuffled_cards = list()
    for i in range(n):
        shuffled_cards.append(cards.pop(random.randint(0, n-i-1)))
    return shuffled_cards


shuffled_cards = shuffle_card(54)
print(shuffled_cards)
