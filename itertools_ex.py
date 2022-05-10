from itertools import permutations as P, combinations as C
lists = list(range(1, 41))

print(len(list(P(lists, 2))))
print(len(list(C(lists, 3))))