import sys,random, os

from ezr import the, DATA, csv
import stats


def guess(N, d) :
    some = random.choices(d.rows, k=N)
    return d.clone().adds(some).chebyshevs().rows

def makeDumb(N, d):
    dumb = [guess(N,d) for _ in range(N)]
    dumb = [d.chebyshev(lst[0]) for lst in dumb]
    return dumb

def makeSmart(N, d):
    smart = [d.shuffle().activeLearning() for _ in range(N)]
    smart = [d.chebyshev(lst[0]) for lst in smart]
    return smart

def asIs(data):
    d = DATA().adds(csv(data))
    b4 = [d.chebyshev(row) for row in d.rows]
    return [stats.SOME(b4,f"asIs,{len(d.rows)}")]

def experiment(data) :
    somes = []
    for N in [20, 30, 40 , 50]:
        
        the.last = N
        d = DATA().adds(csv(data))
        dumb = makeDumb(N,d)
        smart = makeSmart(N, d)
        dNs = stats.SOME(dumb, txt=f"dumb,{N}")
        
        sNs = stats.SOME(smart, txt=f"smart,{N}")

        somes += [dNs] 
        somes += [sNs]
    somes += asIs(data)
    print(somes)
    stats.report(somes)

print (sys.argv)
[(experiment(arg)) for arg in sys.argv if arg[-4:] == ".csv"]
