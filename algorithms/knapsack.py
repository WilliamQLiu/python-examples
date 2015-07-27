"""
    In a 0-1 Knapsack Problem, a knapsack can hold a specific weight and we
    have a series of objects to place in it.  Each object has a weight and a
    value ($).  Our goal is to utilize the space in the knapsack by maximizing the
    value of the objects placed in it.  You must place all of it or none.

    B = maximum weight
    n = number of items
    p = list of weights
    a = list of values

    p[i] = weight with value a[i]
"""

B = 100
n = 10
p = [10, 20, 15, 15, 20, 10, 10, 20, 10, 20]
a = [100, 200, 150, 150, 200, 100, 100, 200, 100, 200]

def solve_knapsack(B, n, p, a):

    m = [0]*(B+1)
    for j in range(n):
        for w in range(B,p[j]-1,-1):
            m[w] = max(m[w], m[w-p[j]] + a[j])

    return max(m)


if __name__ == '__main__':
    temp = solve_knapsack(B, n, p, a)
    print temp