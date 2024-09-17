import sys,random

from ezr import the, DATA, csv
from contextlib import redirect_stdout
import stats

class EXP :
    runs = 0
    dumbNoDiff = 0
    smartNoDiff = 0
    smartLengthOff = 0
    dumbLengthOff = 0
    stop = False

#Returns a sorted list of N random rows based on chebyshev distance
# Used for making k guesses
def guess(N, d) :
    some = random.choices(d.rows, k=N)
    return d.clone().adds(some).chebyshevs().rows

# dumb guessing for random chance, experiment is to demonstrate whether this is equal to learning
def makeDumb(ex, N, d):
    dumb = [guess(N,d) for _ in range(20)]
    
    dumb = [d.chebyshev(lst[0]) for lst in dumb]
    # Save that we actually guessed different values at some point during guessing (low chance to fail)
    ex.dumbNoDiff += 0 if len(set(dumb)) > 1 else 1
    return dumb

# Makes smarter guesses using the active learning code and the naive bayes model that produces
def makeSmart(ex, d):
    smart = [d.shuffle().activeLearning() for _ in range(20)]
    
    smart = [d.chebyshev(lst[0]) for lst in smart]
    # Save case that the shuffle actually jiggled around the data and resulted in different answers
    ex.smartNoDiff += 0 if len(set(smart)) > 1 else 1
    return smart

# Test method for testing the chebyshev sorting 
def testCheby(d, rows) -> bool:
    min = d.chebyshev(rows[0])
    for row in rows:
        if d.chebyshev(row) < min:
            return False
    return True

# Baseline (mainly to satisfy scripting)
def asIs(data):
    d = DATA().adds(csv(data))
    b4 = [d.chebyshev(row) for row in d.rows]
    testChebs = d.chebyshevs().rows
    #TEST that chebys is working properly and actually placiong the lowest first
    assert testCheby(d, testChebs)
    return [stats.SOME(b4,f"asIs,{len(d.rows)}")]

def experiment(ex, data) :
    somes = []
    for N in [20, 30, 40 , 50]:
        
        the.last = N
        try:
            d = DATA().adds(csv(data))
            ex.runs += 1
        except:
            # TEST if there was a file issue we should detect this when n is 20
            assert N == 20
            ex.stop = True
            return
        dumb = makeDumb(ex,N,d)
        smart = makeSmart(ex, d)
        # SAVE inconsistensies
        ex.dumbLengthOff += 0 if (len(dumb) == N or len(d.rows) <= N) else 1
        ex.smartLengthOff += 0 if (len(smart) == N or len(d.rows) <= N) else 1
        dNs = stats.SOME(dumb, txt=f"dumb,{N}")
        
        sNs = stats.SOME(smart, txt=f"smart,{N}")

        somes += [dNs] 
        somes += [sNs]
    somes += asIs(data)
    # TEST that at least some statistical reports were produced by all casses
    assert len(somes) >= 3


    size = "sm" if len(d.cols.x) < 6 else "lg"
    with open(file=f"/workspaces/ezr/hw3/out/{size}/{data[data.rindex('/') + 1:]}",mode="w+") as f:
        with redirect_stdout(f):
            stats.report(somes)     

#TEST tests the features of producing dumb and smart guesses, I only un this test when working with multiple datasets
def postEval(ex:EXP):
    assert ex.dumbLengthOff < ex.runs  or ex.dumbNoDiff < ex.runs 
    assert  ex.smartLengthOff <ex.runs or ex.smartNoDiff < ex.runs


#Main experiment code, reads args and performs experiment
ex = EXP()
random.seed(the.seed)
[(experiment(ex, arg)) for arg in sys.argv if arg[-4:] == ".csv"]
if((not ex.stop) and ex.runs >= 5) :
    postEval(ex)