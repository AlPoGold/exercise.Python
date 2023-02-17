from itertools import permutations

numbers = [1, 2, 3, 4, 5, 6]
new_list = list(permutations(numbers, 6))
for a, b, c, d, e, f in new_list:
    if (a*10+b)**c == (d*10+e)**f:
        print(a, b, c, d, e, f)
