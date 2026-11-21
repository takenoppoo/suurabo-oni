# -*- coding: utf-8 -*-
from bh import *
import math, itertools
Z=U_(); CH=[]; R=sp.Rational; n=sp.symbols("n")
# 6 a(n+1)=p a(n)+q n+r
def b6(a1,p,q,r):
    al,be=sp.symbols("al be")
    sol=sp.solve([al*(n+1)+be-(p*(al*n+be)+q*n+r)],[al,be],dict=True) if False else None
    # alpha n + beta fixed: alpha(n+1)+beta = p(alpha n+beta)+q n + r  -> alpha = p alpha + q ; alpha+beta = p beta + r
    A=R(q,p-1); B=R(r+A,p-1)
    c1=a1+A*1+B  # a_1 + A*1 + B
    # a_n + A n + B = (a1+A+B) p^{n-1}
    an=sp.expand(c1*p**(n-1)-A*n-B)
    seq=[a1]
    for j in range(1,8): seq.append(p*seq[-1]+q*j+r)
    assert all(an.subs(n,j+1)==seq[j] for j in range(8))
    st=[("特殊解を探す","<p>"+I("a_n+An+B")+" の形に直す：</p>"+D(r"a_{n+1}+A(n+1)+B=%d\{a_n+An+B\}"%p)+"<p>係数比較で "+I("A=%s,\\ B=%s"%(L(A),L(B)))+"。</p>"),
        ("等比数列","<p>"+D(r"a_{n+1}%+s(n+1)%+s=%d\left(a_n%+s\,n%+s\right)"%(L(A) if A!=1 else "1",L(B),p,L(A),L(B))).replace("+s","+")+"<p>初項 "+I("a_1+A+B=%s"%L(c1))+"、公比 "+I(str(p))+"。</p>"),
        ("一般項",D(r"a_n=%s\cdot%d^{n-1}%s"%(L(c1),p,L(-A*n-B) if (-A*n-B)!=0 else "")))]
    return r"$a_1=%d,\ a_{n+1}=%da_n%+dn%+d$ で定まる数列の一般項を求めよ。"%(a1,p,q,r),st,r"a_n=%s"%L(an)
o=[b6(*v) for v in [(1,2,1,0),(2,3,2,1),(0,2,3,-1),(1,3,-2,2),(3,2,-1,4)]]
build(Z,CH,"a(n+1)=p·a(n)+qn+r 型の漸化式",o,"<p>$a_{n+1}+A(n+1)+B=p\\{a_n+An+B\\}$ の形に直せるよう $A,B$ を係数比較で決め、$\\{a_n+An+B\\}$ を<b>等比数列</b>として解く。</p>","1次式のズレを吸収する形に組み替える。",6)
# 7 連立
def b7(a1,b1,p,q):
    # a_{n+1}=p a_n + q b_n ; b_{n+1}=q a_n + p b_n
    s,d=sp.symbols("s d")
    sn=lambda m:None
    A=[a1];B=[b1]
    for j in range(8): A.append(p*A[-1]+q*B[-1]); B.append(q*A[-2]+p*B[-1]) if False else None
    A=[a1];B=[b1]
    for j in range(8):
        A,B=A+[p*A[-1]+q*B[-1]],B+[q*A[-1]+p*B[-1]]
    S0=a1+b1; D0=a1-b1; r1=p+q; r2=p-q
    an=sp.expand(R(1,2)*(S0*r1**(n-1)+D0*r2**(n-1))); bn=sp.expand(R(1,2)*(S0*r1**(n-1)-D0*r2**(n-1)))
    assert all(an.subs(n,j+1)==A[j] and bn.subs(n,j+1)==B[j] for j in range(8))
    st=[("和と差","<p>"+D(r"a_{n+1}+b_{n+1}=%d(a_n+b_n),\qquad a_{n+1}-b_{n+1}=%d(a_n-b_n)"%(r1,r2))+"</p>"),
        ("2つの等比数列","<p>"+D(r"a_n+b_n=%d\cdot%d^{n-1},\qquad a_n-b_n=%d\cdot(%d)^{n-1}"%(S0,r1,D0,r2))+"</p>"),
        ("一般項","<p>"+D(r"a_n=\dfrac{%d\cdot%d^{n-1}%+d\cdot(%d)^{n-1}}{2}"%(S0,r1,D0,r2))+D(r"b_n=\dfrac{%d\cdot%d^{n-1}%+d\cdot(%d)^{n-1}}{2}"%(S0,r1,-D0,r2)))]
    return r"$a_1=%d,\ b_1=%d,\ a_{n+1}=%da_n+%db_n,\ b_{n+1}=%da_n+%db_n$ で定まる数列 $\{a_n\},\{b_n\}$ の一般項を求めよ。"%(a1,b1,p,q,q,p),st,r"a_n=%s,\ b_n=%s"%(L(an),L(bn))
o=[b7(*v) for v in [(3,1,2,1),(5,1,3,1),(4,2,2,3),(6,2,1,2),(7,3,3,2)]]
build(Z,CH,"対称な連立漸化式（和と差）",o,"<p>2式を<b>足す</b>と $a_n+b_n$ の、<b>引く</b>と $a_n-b_n$ の漸化式（公比 $p\\pm q$ の等比数列）が得られる。</p>","足して1本、引いて1本。2つの等比数列が見つかる。",7)
# 8 Sn 与えられた漸化式
def b8(c,m):
    # S_n = c a_n + m n ... S_n=2a_n - n  generalized: S_n = 2 a_n + m n (c=2)
    # a_1 = S_1: a1=2a1+m -> a1=-m ; a_{n+1}=S_{n+1}-S_n = 2a_{n+1}-2a_n+m -> a_{n+1}=2a_n - m
    a1=-m; an=sp.expand(-m + (a1+m)*2**(n-1)) if False else None
    # a_{n+1}=2a_n-m -> a_n-m =2(a_{n-1}-m) ... fixed point alpha=2alpha-m -> alpha=m
    an=sp.expand(m+(a1-m)*2**(n-1))
    A=[a1]
    for j in range(7): A.append(2*A[-1]-m)
    assert all(an.subs(n,j+1)==A[j] for j in range(8))
    S=lambda N:sum(A[:N]); assert all(S(N)==2*A[N-1]+m*N for N in range(1,8))
    st=[("初項","<p>"+I("n=1")+"：</p>"+D(r"S_1=a_1=2a_1%+d\ \Rightarrow\ a_1=%d"%(m,a1))),
        ("漸化式をつくる","<p>"+D(r"a_{n+1}=S_{n+1}-S_n=(2a_{n+1}%+d(n+1))-(2a_n%+dn)\ \Rightarrow\ a_{n+1}=2a_n%+d"%(m,m,-m))),
        ("一般項","<p>"+I("a_{n+1}-%d=2(a_n-%d)"%(m,m))+"。</p>"+D(r"a_n=%s"%L(an)))]
    return r"数列 $\{a_n\}$ の初項から第 $n$ 項までの和 $S_n$ が $S_n=2a_n%+dn$ をみたすとき、$a_1$ と一般項 $a_n$ を求めよ。"%m,st,r"a_1=%d,\ a_n=%s"%(a1,L(an))
o=[b8(2,m) for m in [-1,3,-2,4,-3]]
build(Z,CH,"和と一般項の関係式から漸化式",o,"<p>$n=1$ で $a_1=S_1$ から初項。$a_{n+1}=S_{n+1}-S_n$ で $a_{n+1}$ と $a_n$ の漸化式をつくり、特性方程式で解く。</p>","合計の変化量が、その項そのもの。",8)
# 9 a(n+1)=2 a(n)^3 型
def b9(p,q,a1):
    # a_{n+1}=q*a_n^p with a1: take log base a1? use a1=2,q power of 2: a_{n+1}=2^m a_n^p
    # use log2: b_n=log2 a_n ; b_{n+1}=m + p b_n ; b1=log2 a1=e
    m,e=q,a1  # q=exponent m (a_{n+1}=2^m a_n^p), a1=2^e
    b1=e; al=R(m,1-p)
    bn=sp.expand((b1-al)*p**(n-1)+al)
    B=[b1]
    for j in range(5): B.append(m+p*B[-1])
    assert all(bn.subs(n,j+1)==B[j] for j in range(6))
    st=[("対数をとる","<p>"+I("b_n=\\log_2a_n")+" とおく（"+I("a_n>0")+"）。</p>"+D(r"b_{n+1}=\log_2(2^{%d}a_n^{%d})=%d+%db_n,\qquad b_1=%d"%(m,p,m,p,b1))),
        ("線形漸化式","<p>"+I("b_{n+1}+%s=%d(b_n+%s)"%(L(-al) if al!=0 else "0",p,L(-al)))+" の形。</p>"+D(r"b_n=%s"%L(bn))),
        ("一般項",D(r"a_n=2^{b_n}=2^{%s}"%L(bn)))]
    return r"$a_1=2^{%d},\ a_{n+1}=2^{%d}a_n^{%d}$ で定まる正の数列の一般項を求めよ。"%(e,m,p),st,r"a_n=2^{%s}"%L(bn)
o=[b9(*v) for v in [(3,1,1),(2,1,1),(3,2,1),(2,3,2),(4,1,1)]]
build(Z,CH,"a(n+1)=2^m·a(n)^p 型（両辺の対数）",o,"<p>$\\log_2$ をとって $b_n=\\log_2a_n$ とおくと、$b_{n+1}=m+pb_n$ という<b>1次の漸化式</b>に変わる。</p>","冪はかけ算の指数。対数を取ると足し算の世界。",9)
# 10 確率漸化式
def b10(q):
    p=sp.symbols("p")
    # p_n: probability number of heads even after n tosses, head prob q
    pn=lambda N:sum(math.comb(N,k)*float(q)**k*(1-float(q))**(N-k) for k in range(0,N+1,2))
    r_=1-2*q; an=sp.expand(R(1,2)+R(1,2)*r_**n)
    assert all(abs(float(an.subs(n,N))-pn(N))<1e-9 for N in range(1,9))
    st=[("漸化式をつくる","<p>"+I("p_n")+"：表の回数が偶数の確率。"+I("n+1")+" 回目に表が出ると偶奇が入れかわる。</p>"+D(r"p_{n+1}=p_n(1-%s)+(1-p_n)%s=%s\,p_n+%s,\qquad p_0=1"%(L(q),L(q),L(r_),L(q)))),
        ("特性方程式","<p>"+I("\\alpha=%s\\alpha+%s"%(L(r_),L(q)))+" より "+I("\\alpha=\\dfrac12")+"。</p>"+D(r"p_{n+1}-\dfrac12=%s\left(p_n-\dfrac12\right)"%L(r_))),
        ("一般項",D(r"p_n=\dfrac12+\dfrac12\left(%s\right)^n"%L(r_)))]
    return r"表の出る確率が $%s$ の硬貨を $n$ 回投げるとき、表が出る回数が偶数である確率 $p_n$ を求めよ（$0$ 回も偶数とする）。"%L(q),st,r"p_n=\dfrac12+\dfrac12\left(%s\right)^n"%L(r_)
o=[b10(q) for q in [R(1,3),R(1,4),R(2,5),R(1,5),R(1,6)]]
build(Z,CH,"確率と漸化式（表の回数が偶数）",o,"<p>$n+1$ 回目の結果で場合分けして<b>確率の漸化式</b>をつくる。$p_{n+1}=ap_n+b$ の型なので、特性方程式 $\\alpha=a\\alpha+b$ で解く。</p>","直前までの状態と、今回の結果で次の状態が決まる。",10)
XU=finishx(Z,CH)
