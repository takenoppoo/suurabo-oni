# -*- coding: utf-8 -*-
from bh import *
from math import comb
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x")
def b6(n,a,b,k):
    # (a x + b/x)^n  x^k coefficient
    r=(n-k)//2 if False else None
    # term C(n,r)(ax)^(n-r)(b/x)^r ; x power n-2r=k
    assert (n-k)%2==0; r=(n-k)//2
    c=comb(n,r)*a**(n-r)*b**r
    assert sp.expand((a*x+b/x)**n).coeff(x,k)==c
    st=[("一般項","<p>"+D(r"{}_{%d}C_r(%dx)^{%d-r}\left(\dfrac{%d}{x}\right)^r={}_{%d}C_r\cdot%d^{%d-r}%d^{r}\,x^{%d-2r}"%(n,a,n,b,n,a,n,b,n))),
        ("$x^{%d}$ の項"%k,"<p>"+I("%d-2r=%d"%(n,k))+" より "+I("r=%d"%r)+"。</p>"),
        ("係数",D(r"{}_{%d}C_{%d}\cdot%d^{%d}\cdot%d^{%d}=%d"%(n,r,a,n-r,b,r,c)))]
    return r"$\left(%dx+\dfrac{%d}{x}\right)^{%d}$ の展開式における $x^{%d}$ の項の係数を求めよ。"%(a,b,n,k) if k!=0 else r"$\left(%dx+\dfrac{%d}{x}\right)^{%d}$ の展開式における定数項を求めよ。"%(a,b,n),st,str(c)
o=[b6(*v) for v in [(8,2,1,2),(6,3,2,0),(7,1,2,3),(9,2,3,1),(10,1,3,0)]]
build(Z,CH,"(ax+b/x)^n の特定の項",o,"<p>一般項 ${}_nC_r(ax)^{n-r}(b/x)^r$ を $x$ の指数にそろえ、指定の次数になる $r$ を決める。</p>","指数だけに注目して、何番目の項かを割り出す。",6)
def b7(n,a,b):
    # (1+ax+bx^2)^n coefficient of x^2? use (1+x+x^2)^n x^k
    r=sum(1 for _ in [0])
    c=sp.expand((1+a*x+b*x**2)**n).coeff(x,3)
    # x^3: choose p of ax and q of bx^2: p+2q=3
    terms=[]
    for q in range(0,2):
        p=3-2*q
        if p+q<=n: terms.append((p,q,sp.factorial(n)//(sp.factorial(p)*sp.factorial(q)*sp.factorial(n-p-q))*a**p*b**q))
    assert sum(t[2] for t in terms)==c
    st=[("3つの項の展開","<p>"+I("(1+%sx+%sx^2)^{%d}"%(L(a),L(b),n))+" の一般項は "+I(r"\dfrac{%d!}{p!\,q!\,s!}(%sx)^p(%sx^2)^q\cdot1^s"%(n,L(a),L(b)))+"。</p>"),
        ("$x^3$ になる組","<p>"+I("p+2q=3")+"："+"、".join(I("(p,q)=(%d,%d)"%(t[0],t[1])) for t in terms)+"。</p>"),
        ("係数",D("+".join(L(t[2]) for t in terms)+"=%s"%L(c)))]
    return r"$(1+%sx+%sx^2)^{%d}$ の展開式における $x^3$ の係数を求めよ。"%(L(a),L(b),n),st,L(c)
o=[b7(*v) for v in [(5,2,1),(6,1,3),(4,3,2),(7,1,1),(5,-1,2)]]
build(Z,CH,"3項の累乗の x^3 の係数",o,"<p>一般項は $\\dfrac{n!}{p!\\,q!\\,s!}$ 型。指数の和が $3$ になる $(p,q)$ をすべて拾って足す。</p>","組合せごとに「何個ずつ選ぶか」を書き出す。",7)
def b8(n):
    S=sum(k*comb(n,k) for k in range(n+1)); assert S==n*2**(n-1)
    st=[("$k\\,{}_nC_k$ の変形","<p>"+I(r"k\,{}_nC_k=n\,{}_{n-1}C_{k-1}")+"。</p>"),
        ("和の計算","<p>"+D(r"\sum_{k=1}^{n}k\,{}_nC_k=n\sum_{k=1}^{n}{}_{n-1}C_{k-1}=n\cdot2^{n-1}")),
        ("値",D(r"%d\cdot2^{%d}=%d"%(n,n-1,S)))]
    return r"${}_{%d}C_1\cdot1+{}_{%d}C_2\cdot2+\cdots+{}_{%d}C_{%d}\cdot%d$ の値を求めよ。"%(n,n,n,n,n),st,str(S)
o=[b8(n) for n in [6,8,10,7,9]]
build(Z,CH,"k·nCk の和",o,"<p>$k\\,{}_nC_k=n\\,{}_{n-1}C_{k-1}$ と変形して、二項係数の和 $2^{n-1}$ に帰着。</p>","「k 人から代表を1人」は「先に代表を選ぶ」と同じ。",8)
def b9(a,n,m):
    # remainder of a^n divided by m with a=m+1 type: (m+1)^n mod m^2
    v=pow(a,n,m*m); 
    st=[("二項定理で展開","<p>"+I("%d=%d+1"%(a,m))+" とみて</p>"+D(r"(%d+1)^{%d}=1+%d\cdot%d+(%d^2\text{の倍数})"%(m,n,n,m,m))),
        ("余り","<p>"+I("%d^2=%d"%(m,m*m))+" で割った余り：</p>"+D(r"1+%d=%d\ (\text{ただし }%d<%d)"%(n*m,(1+n*m)%(m*m),(1+n*m)%(m*m),m*m)))]
    assert (1+n*m)%(m*m)==v
    return r"$%d^{%d}$ を $%d$ で割った余りを求めよ。"%(a,n,m*m),st,str(v)
o=[b9(m+1,n,m) for m,n in [(10,25),(7,30),(9,50),(8,40),(11,15)]]
build(Z,CH,"(m+1)^n を m^2 で割った余り",o,"<p>$(m+1)^n=1+nm+{}_nC_2m^2+\\cdots$。$m^2$ 以上の項はすべて $m^2$ の倍数なので、<b>最初の2項</b>だけ見ればよい。</p>","大きな累乗も、先頭の2項で余りが決まる。",9)
def b10(n):
    S=sum(comb(n,k)*(-1)**k*2**(n-k) for k in range(n+1)); assert S==1
    T=sum(comb(n,k)*2**k for k in range(0,n+1,2))
    st=[("二項定理","<p>"+D(r"(2+1)^n+(2-1)^n=2\sum_{k\ \text{偶数}}{}_nC_k\,2^{k}\cdot1")+"</p>"),
        ("代入","<p>"+I(r"n=%d"%n)+" で</p>"+D(r"3^{%d}+1=%d,\qquad \dfrac{%d}{2}=%d"%(n,3**n+1,3**n+1,(3**n+1)//2)))]
    assert T==(3**n+1)//2
    return r"${}_{%d}C_0+{}_{%d}C_2\cdot2^2+{}_{%d}C_4\cdot2^4+\cdots$（偶数番目だけ、最後まで）の値を求めよ。"%(n,n,n) if False else r"$\displaystyle\sum_{k\,(\text{偶数})}{}_{%d}C_k\,2^k$ の値を求めよ。"%n,st,str(T)
o=[b10(n) for n in [4,6,8,10,12]]
build(Z,CH,"偶数番目の項の和",o,"<p>$(1+2)^n$ と $(1-2)^n$ を足すと、奇数番目の項が消えて偶数番目の項の2倍が残る。</p>","足して奇数側を消す、引いて偶数側を消す。",10)
XU=finishx(Z,CH)
