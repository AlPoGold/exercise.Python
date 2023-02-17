# Расставить цифры 1, 2, 3, 4, 5, 6 так, чтобы равенство AB^C=DE^F соблюдалось
numbers = [1, 2, 3, 4, 5, 6]
for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                for e in numbers:
                    for f in numbers:
                        if (a*10+b)**c == (d*10+e)**f:
                            list_numbers = [a,b,c,d,e,f]
                            if len(set(list_numbers)) == 6:
                                print(a, b, c, d, e, f)