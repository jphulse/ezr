# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv

import sys,random

from ezr import the, DATA, SYM, COL, NUM, csv, dot

def show(lst):
  return print(*[f"{word:6}" for word in lst], sep="\t")

def myfun(train):
  d    = DATA().adds(csv(train))
  symCount = 0
  col = 0
  numCount = 0
  x    = len(d.cols.x)
  size = len(d.rows)
  dim  = "small" if x <= 5 else ("med" if x < 12 else "hi")
  size = "small" if size< 500 else ("med" if size<5000 else "hi")
  for col in d.cols.all :
    if(isinstance(col, SYM)) :
        symCount += 1
    else :
      numCount += 1
    
  return [dim, size, x,len(d.cols.y), symCount, numCount, len(d.rows), train[17:]]

random.seed(the.seed) #  not needed here, but good practice to always take care of seeds
show(["dim", "size","xcols","ycols", "scols", "ncols", "rows","file"])
show(["------"] * 8)
[show(myfun(arg)) for arg in sys.argv if arg[-4:] == ".csv"]
