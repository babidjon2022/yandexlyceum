import itertools
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(str(input()))
print(*map(lambda x: f'{x[0]} {x[1]}', itertools.product(itertools.chain(range(2, 11),
      iter(['валет', 'дама', 'король', 'туз'])), suits)), sep='\n')
