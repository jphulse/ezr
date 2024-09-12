import sys,random

from ezr import the, DATA, SYM, COL, NUM, csv, dot, stats

def guess(N, d) :
    some = random.choices(d.rows, k=N)
    return d.clone().adds(some).chebyshevs().rows


def experiment(data) :
    somes = []
    for N in [20, 30, 40 , 50]:
        dNs = stats.SOME(text=f"dumb,{N}")
        somes += [dNs]
        sNs = stats.SOME(text=f"smart,{N}")
        somes += [sNs]
        d = DATA.new().csv(data)
        dumb = [guess(N,d) for _ in range(20)]
        dumb = [d.chebyshev(lst[0]) for lst in dumb]
        dNs += dumb
        the.last = N
        smart = [d.shuffle().activeLearning() for _ in range(20)]
        smart = [d.chebyshev(lst[0]) for lst in smart]
        sNs += smart 
    stats.report(somes)

