#!/usr/bin/env python3

import ft_filter


nombres = [1, 2, 3, 4, 5, 6]


def est_pair(x):
    return x % 2 == 0


resultat = filter(est_pair, nombres)
ft_resultat = ft_filter.ft_filter(est_pair, nombres)

print(list(resultat))
print(list(ft_resultat))
