import math

x = "foo"
y = "foo"


def search(lst, T):
    L = 0
    R = len(lst) - 1
    while L < R:
        m = math.floor((L + R) / 2)
        L, R = update_interval(lst, m, T, L, R)
    if lst[L] == T:
        return L
    return -1


def update_interval(lst, m, T, L, R):
    if lst[m] <= T:
        L = m + 1
    else:
        R = m - 1
    return L, R


def search_fix(lst, T):
    L = 0
    R = len(lst) - 1
    while L < R:
        m = math.floor((L + R) / 2)
        if lst[L] == T:
            return L
        L, R = update_interval(lst, m, T, L, R)
    if lst[L] == T:
        return L
    return -1
