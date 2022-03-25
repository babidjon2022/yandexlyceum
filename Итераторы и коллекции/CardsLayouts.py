from itertools import chain, product, combinations

suits = 'валет', 'дама', 'король', 'туз'
all_cards = tuple(
    product(chain(range(10, 11), range(2, 10), suits),
            ('бубен', 'пик', 'треф', 'червей')))
hearts = tuple(filter(lambda x: x[1] == 'червей', all_cards))
more10 = tuple(filter(lambda x: x[0] in suits, all_cards))
deck = list(map(lambda x: list(x), combinations(all_cards, 3)))
deck1 = list()
for i in range(len(deck)):
    if any(map(lambda x: x in hearts, deck[i])) and any(
            map(lambda x: x in more10, deck[i])):
        deck1.append(
            list(map(lambda x: ' '.join((str(x[0]), str(x[1]))), deck[i])))
deck1 = list(map(lambda x: ', '.join(x), deck1))
print(*deck1, sep='\n')
