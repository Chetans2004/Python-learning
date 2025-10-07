# # random.random(): Returns a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).
# # random.randint(a, b): Returns a random integer N such that a <= N <= b.
# # random.randrange(start, stop, step): Returns a randomly selected element from range(start, stop, step).
# random.choice(sequence): Returns a random element from a non-empty sequence (e.g., list, tuple, string).
# random.shuffle(list): Shuffles the items of a list in place.

import random
# a=random.randint(1,100)
# print(a)

# a=random.randrange(1,9)
# print(a)


# l=[1,4,3,5,6]
# # print(random.choice(l))
# random.shuffle(l)
# print(l)

#TEAD AND TAILS
head_tail=random.randint(0,1)
print(head_tail)
if head_tail==1:
    print("Head")
else:
    print("Tail")

