.

# Easier AI

by Tim Menzies and the EZRites  
(c) 2024, CC-SA 4.0  
http://github.com/timm/ezr

In the beginning there was the data and the data was without form,
and void; and confusion was upon the face of the humans.  And the
programmer  said, let there be workflows that find signals within
that noise;   and there was light.

And in that workflow there was tabular data whose first row defined
column types. And upper case words were numeric and the others were
symbols. And some of the words were goals were marked with "!+-"
denoting things we wanted to predict of  minimize of maximize.  Like
so:

    Clndrs,Volume,HpX,Model,origin,Lbs-,Acc+,Mpg+

This describes cars. We've decided to ignore horsepower (so it ends
with and `X`). ALso, we want light cars (since they are cheaper to
build and buy), fast acceleration, and good miles per gallon. So
these get marked with `Lhs-,Acc+,Mpg+`

And the programmer wrote code to turn these names into NUMeric and
SYMbolic columns, then to store all of them in `all` and (for
convenience) also in `x` (the independent variables) and `y` (for
the dependent goals that we want to predict of minimize or maximize).

	# define a COLS struct
	def COL(names): return o(x=[], y=[], all=[], klass=None, names=names)
	
	# COLS constructor
	def cols(names):
	  cols1 = COLS(names)
	  cols1.all = [_cols(cols1,n,s) for n,s in enumerate(names)]
	  return cols1
	
	def _cols(cols1, n, s):
	  col = (NUM if s[0].isupper() else SYM)(txt=s, at=n)
	  if s[-1] == "!": cols1.klass = col
	  if s[-1] != "X": (cols1.y if s[-1] in "!+-" else cols1.x).append(col)
	  return col

And the code needed some help. NUM and SYM summarize streams of number
and symbols. Both these know the `txt` of their column name; what
column position they are `at`;  and how many `n` items they have
seen so far. SYMs get a count of symbols seen so far in `has`, while for NUMs,
keeping the numbers in `has` is optional.  NUMs also track the `lo`est and
`hi`est values seen so far as well as their mean `mu`. And anything not ending
in `-` is a numeric goal to be `maximzed`.

	def SYM(txt=" ", at=0): 
      return o(isNum=False, txt=txt, at=at, n=0, has={})
	
	def NUM(txt=" ", at=0, has=None):
	  return o(isNum=True,  txt=txt, at=at, n=0, hi=-1E30, lo=1E30, 
	           has=has, rank=0, # if has non-nil, used by the stats package
	           mu=0, m2=0, maximize = txt[-1] != "-")

To distinguish NUMs from SYMs, the programmer added a `isNum` flag (which
as false for SYMs.

Internally, NUM and SYM are both `o`bjects where `o` is a handy dandy
struct that knows how to pretty-print itself.

	class o:
	  def __init__(i,**d): i.__dict__.update(d)
	  def __repr__(i): return i.__class__.__name__+str(show(i.__dict__))
	
	def show(x):
	  it = type(x)
	  if it == float:  return round(x,the.decs)
	  if it == list:   return [show(v) for v in x]
	  if it == dict:   return "("+' '.join([f":{k} {show(v)}" for k,v in x.items()])+")"
	  if it == o:      return show(x.__dict__)
	  if it == str:    return '"'+str(x)+'"'
	  if callable(x):  return x.__name__
	  return x

The programmer did place the rows in a DATA object that held the rows, and their
summary in a COLS object.

    # define a DATA struct
    def DATA(): return o(rows=[], cols=[])

    # DATA constructor
	def data(src=None, rank=False):
	  data1=DATA()
	  [append(data1,lst) for  lst in src or []]
	  if rank: data1.rows.sort(key = lambda lst:d2h(data1,lst))
	  return data1

In her wisdom, the programmer added a sort function that could order the rows
best to worse using `d2h`, or distance to heaven [^rowOrder]. Given a goal
normalized to the range 0..1 for min..max, then "heaven" is 0 (if minimizing)
and 1 (if maximizing). Given N goals there there is a list of heaven points
and `d2h` is the distance from some goals to that  heaven.

	def d2h(data,row):
	  n = sum(abs(norm(num,row[num.at]) - num.maximize)**the.p for num in data.cols.y)
	  return (n / len(data.cols.y))**(1/the.p)
	
	def norm(num,x): return x if x=="?" else (x-num.lo)/(num.hi - num.lo - 1E-30)

The general Minkowski distance  says that the distance between things
comes from the distance between their independent `x` columns,  raised to some power $p$.
Boring old Euclidean distance uses $p=2$, but our programmer knew that
this is a parameter that can be tuned. She stored all such tuneables
in a `the` variable. So our Minkowski distance function is:

$$d(x,y)=\left(\sum^n_i (x_i - y_i)^p \)^{1/p}\right)/\left(n^{1/p}\right)$$

This disance is defined bif nuermisa dn is XXX
Which, in Pythons is:
	
	# Distance between two rows
	def dists(data,row1,row2):
	  n = sum(dist(col, row1[col.at], row2[col.at])**the.p for col in data.cols.x)
	  return (n / len(data.cols.x))**(1/the.p)
	
	# Distance between two values (called by dists).
	def dist(col,x,y):
	  if  x==y=="?": return 1
	  if not col.isNum: return x != y
	  x, y = norm(col,x), norm(col,y)
	  x = x if x !="?" else (1 if y<0.5 else 0)
	  y = y if y !="?" else (1 if x<0.5 else 0)
	  return abs(x-y)
	
We divide by $n^{1/p}$ so all our distances fall between zero and one.

doty. fing deta between best and rest.


The programmer did pause and lok at all

[^rowRoder:] There are many ways to rank examples with multiple objectives. 
_Binary domination_ says...
The _Zitler says__
Peter Chen.