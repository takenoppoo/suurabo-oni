# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
def cnt(N,f): return sum(1 for i in range(1,N+1) if f(i))
# 6 3つの倍数
def b6(N,a,b,c):
    A=N//a; B=N//b; C=N//c; AB=N//(a*b); BC=N//(b*c); CA=N//(c*a); ABC=N//(a*b*c)
    v=A+B+C-AB-BC-CA+ABC; assert v==cnt(N,lambda i:i%a==0 or i%b==0 or i%c==0)
    nv=N-v; assert nv==cnt(N,lambda i:i%a and i%b and i%c)
    st=[("集合を決める","<p>"+I(r"A:%d\text{の倍数},\ B:%d\text{の倍数},\ C:%d\text{の倍数}"%(a,b,c))+"（1〜%d）。"%N+I("a,b,c")+" は互いに素。</p>"+D(r"n(A)=%d,\ n(B)=%d,\ n(C)=%d"%(A,B,C))),
        ("共通部分","<p>互いに素なので積の倍数。</p>"+D(r"n(A\cap B)=%d,\ n(B\cap C)=%d,\ n(C\cap A)=%d,\ n(A\cap B\cap C)=%d"%(AB,BC,CA,ABC))),
        ("包除原理で和集合",D(r"n(A\cup B\cup C)=%d+%d+%d-%d-%d-%d+%d=%d"%(A,B,C,AB,BC,CA,ABC,v))),
        ("補集合","<p>どれでも割り切れない数：</p>"+D(r"%d-%d=%d"%(N,v,nv)))]
    return r"$1$ から $%d$ までの整数のうち、$%d,\ %d,\ %d$ のどれでも割り切れない数の個数を求めよ。"%(N,a,b,c),st,str(nv)
o=[b6(*v) for v in [(300,2,3,5),(500,2,3,7),(420,3,4,5),(1000,2,5,7),(600,3,5,7)]]
build(Z,CH,"3つの倍数（包除原理と補集合）",o,r"<p>$n(A\cup B\cup C)=n(A)+n(B)+n(C)-n(A\cap B)-n(B\cap C)-n(C\cap A)+n(A\cap B\cap C)$。<b>どれでもない数</b>は全体から引く。</p>","重なりを引きすぎたら、最後の三重の重なりを足し戻す。",6)
# 7 部分集合の個数
def b7(n,inc,exc):
    v=2**(n-inc-exc); 
    # brute
    import itertools
    full=list(range(1,n+1)); c=0
    for m in range(1<<n):
        S={full[i] for i in range(n) if m>>i&1}
        if all(k in S for k in range(1,inc+1)) and all(k not in S for k in range(inc+1,inc+exc+1)): c+=1
    assert c==v
    st=[("決まっている要素","<p>"+I(r"1\sim%d"%inc)+" は必ず含み、"+I(r"%d\sim%d"%(inc+1,inc+exc))+" は含まない。計 "+I(str(inc+exc))+" 個の要素が決まる。</p>"),
        ("残りの要素","<p>残り "+I("%d-%d=%d"%(n,inc+exc,n-inc-exc))+" 個は含む・含まないの自由。</p>"),
        ("個数",D(r"2^{%d}=%d"%(n-inc-exc,v)))]
    return r"集合 $\{1,2,\cdots,%d\}$ の部分集合のうち、$1$ から $%d$ までのすべての要素を含み、$%d$ から $%d$ までの要素を含まないものの個数を求めよ。"%(n,inc,inc+1,inc+exc),st,str(v)
o=[b7(*v) for v in [(8,2,1),(9,1,2),(10,3,2),(7,2,2),(12,3,3)]]
build(Z,CH,"条件つきの部分集合の個数",o,r"<p>要素ごとに「入れる・入れない」を選ぶと $2$ 通り。<b>条件で決まる要素を除いた残り</b>の個数を $m$ として $2^m$。</p>","スイッチのON/OFFの組み合わせ。固定のスイッチは数えない。",7)
# 8 ド・モルガン
def b8(U,A,B,AB):
    nAorB=A+B-AB; neither=U-nAorB; onlyA=A-AB; onlyB=B-AB; assert neither>=0
    st=[("ド・モルガンの法則","<p>"+I(r"\overline A\cap\overline B=\overline{A\cup B}")+"。</p>"),
        ("和集合の個数",D(r"n(A\cup B)=n(A)+n(B)-n(A\cap B)=%d+%d-%d=%d"%(A,B,AB,nAorB))),
        ("補集合・差集合",D(r"n(\overline A\cap\overline B)=%d-%d=%d"%(U,nAorB,neither))+D(r"n(A\cap\overline B)=%d-%d=%d"%(A,AB,onlyA)))]
    return r"全体集合 $U$ の要素の個数が $%d$、$n(A)=%d,\ n(B)=%d,\ n(A\cap B)=%d$ のとき、$n(\overline A\cap\overline B)$ と $n(A\cap\overline B)$ を求めよ。"%(U,A,B,AB),st,r"n(\overline A\cap\overline B)=%d,\ \ n(A\cap\overline B)=%d"%(neither,onlyA)
o=[b8(*v) for v in [(100,60,45,30),(80,50,40,25),(120,70,65,40),(90,55,35,20),(150,90,80,55)]]
build(Z,CH,"ド・モルガンの法則と個数",o,r"<p>$\overline A\cap\overline B=\overline{A\cup B}$。まず $n(A\cup B)$ を出して全体から引く。「$A$ だけ」は $n(A)-n(A\cap B)$。</p>","「どちらでもない」は「どちらか」の反対。","8" if False else 8)
# 9 不等式で表された集合
def b9(a,b,c):
    # A={x| x^2 - (a+b)x + ab <=0}, B={x| x>=c}; A∩B 空でない条件? answer c<=b
    st=[("$A$ を解く","<p>"+I(r"x^2-%dx+%d\leqq0"%(a+b,a*b))+" を因数分解。</p>"+D(r"(x-%d)(x-%d)\leqq0\ \Rightarrow\ %d\leqq x\leqq %d"%(a,b,a,b))),
        ("共通部分が空でない条件","<p>"+I("A\\cap B\\neq\\varnothing")+" となるのは、"+I("B")+" の左端 "+I("c")+" が "+I("A")+" の右端以下のとき。</p>"+D(r"c\leqq %d"%b)),
        ("端点を確認","<p>"+I("c=%d"%b)+" のとき "+I("x=%d"%b)+" が共通部分に入るので成立。</p>"+D(r"c\leqq %d"%b))]
    return r"$A=\{x\mid x^2-%dx+%d\leqq0\}$、$B=\{x\mid x\geqq c\}$ について、$A\cap B\neq\varnothing$ となる定数 $c$ の範囲を求めよ。"%(a+b,a*b),st,r"c\leqq %d"%b
o=[b9(*v) for v in [(1,4,0),(2,5,0),(-1,3,0),(1,6,0),(3,7,0)]]
build(Z,CH,"2次不等式で表された集合の共通部分",o,r"<p>集合を<b>数直線</b>に描く。$A\cap B\neq\varnothing$ は、$B$ の端点が $A$ の右端以下のとき。端点で等号が成り立つか必ず確認する。</p>","2つの区間が少しでも重なるかを、数直線で目視する。",9)
# 10 平方数または立方数
def b10(N):
    sq=int(N**0.5); cu=round(N**(1/3)); 
    while cu**3>N: cu-=1
    while (cu+1)**3<=N: cu+=1
    s6=round(N**(1/6))
    while s6**6>N: s6-=1
    while (s6+1)**6<=N: s6+=1
    v=sq+cu-s6; assert v==cnt(N,lambda i:round(i**.5)**2==i or round(i**(1/3))**3==i or (round(i**(1/3)+1e-9))**3==i)
    st=[("集合を決める","<p>"+I(r"A:\text{平方数},\ B:\text{立方数}")+"（1〜%d）。</p>"%N+D(r"n(A)=%d\ (%d^2\leqq %d),\qquad n(B)=%d\ (%d^3\leqq %d)"%(sq,sq,N,cu,cu,N))),
        ("共通部分","<p>平方数かつ立方数 "+I(r"\iff 6\text{乗数}")+"。</p>"+D(r"n(A\cap B)=%d\ (%d^6\leqq %d)"%(s6,s6,N))),
        ("和集合",D(r"n(A\cup B)=%d+%d-%d=%d"%(sq,cu,s6,v)))]
    return r"$1$ から $%d$ までの自然数のうち、平方数または立方数であるものの個数を求めよ。"%N,st,str(v)
o=[b10(N) for N in [100,500,1000,2000,5000]]
build(Z,CH,"平方数または立方数の個数",o,r"<p>平方数 $k^2\leqq N$ の個数は $\lfloor\sqrt N\rfloor$、立方数は $\lfloor\sqrt[3]N\rfloor$。<b>両方に入る数は6乗数</b>なので、重なりを引く。</p>","重なる数（6乗数）を二重に数えたら、1回分引く。",10)
XU=finishx(Z,CH)
