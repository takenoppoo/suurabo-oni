# -*- coding: utf-8 -*-
from bh import *
import math, itertools
from fractions import Fraction as Fr
Z=U_(); CH=[]; R=sp.Rational
def dist_tab(pairs):
    xs=[a for a,_ in pairs]
    return r"\begin{array}{c|%s|c}X&%s&\text{計}\\\hline P&%s&1\end{array}"%("c"*len(xs),"&".join(str(a) for a in xs),"&".join(L(p) for _,p in pairs))
# 6 さいころ2個の和の分布
def b6(kind):
    outs=list(itertools.product(range(1,7),repeat=2))
    fn={"max":max,"min":min,"diff":lambda t:abs(t[0]-t[1]),"sum":sum,"prod":lambda t:t[0]*t[1]%6 if False else (t[0]+t[1])%3}[kind]
    from collections import Counter
    c=Counter(fn(t) for t in outs); xs=sorted(c); pr=[(x_,R(c[x_],36)) for x_ in xs]
    E=sum(x_*p for x_,p in pr); V=sum(x_*x_*p for x_,p in pr)-E**2
    name={"max":"大きい方の目","min":"小さい方の目","diff":"目の差の絶対値","sum":"目の和を3で割った余り"}[kind]
    st=[("確率分布","<p>36通りを数える。</p>"+D(dist_tab(pr))),
        ("期待値",D(r"E(X)=%s=%s"%("+".join(r"%d\cdot%s"%(x_,L(p)) for x_,p in pr if x_!=0) or "0",L(E)))),
        ("分散","<p>"+D(r"V(X)=E(X^2)-\{E(X)\}^2=%s-\left(%s\right)^2=%s"%(L(sum(x_*x_*p for x_,p in pr)),L(E),L(V))))]
    return r"大小2つのさいころを投げ、%sを $X$ とする。$X$ の確率分布、期待値 $E(X)$、分散 $V(X)$ を求めよ。"%name,st,r"E(X)=%s,\ V(X)=%s"%(L(E),L(V))
o=[b6(k) for k in ["max","min","diff","sum","max"]]
o[4]=b6("diff")
build(Z,CH,"さいころ2個から作る確率変数の分布",o,"<p>36通りの根元事象を<b>表に書き</b>、$X$ の値ごとに個数を数える。期待値 $E=\\sum xp$、分散 $V=E(X^2)-E(X)^2$。</p>","全部書き出して数えるのが一番確実。",6)
# 7 E(X+Y), V(X+Y)
def b7(n,m):
    # X: sum of n dice faces? use X = value of one die, Y=2nd coin ... simple: X number of heads in n tosses (p=1/2) ... use independent
    EX=R(7,2); VX=R(35,12)
    E=n*EX; V=n*VX
    st=[("1個のさいころ","<p>"+D(r"E(X_i)=\dfrac72,\qquad V(X_i)=\dfrac{35}{12}")),
        ("和の期待値","<p>"+I("S=X_1+\\cdots+X_%d"%n)+"。期待値は常に和：</p>"+D(r"E(S)=%d\cdot\dfrac72=%s"%(n,L(E)))),
        ("和の分散","<p>独立なので分散も和：</p>"+D(r"V(S)=%d\cdot\dfrac{35}{12}=%s,\qquad \sigma(S)=\sqrt{%s}"%(n,L(V),L(V)))+"<p>"+I("T=%dS+%d"%(m,3))+" なら："+I("E(T)=%s"%L(m*E+3))+"、"+I("V(T)=%s"%L(m*m*V))+"。</p>")]
    return r"さいころを $%d$ 回投げて出た目の和を $S$ とする。$E(S),\ V(S)$ を求めよ。また $T=%dS+3$ の $E(T),\ V(T)$ を求めよ。"%(n,m),st,r"E(S)=%s,\ V(S)=%s,\ E(T)=%s,\ V(T)=%s"%(L(E),L(V),L(m*E+3),L(m*m*V))
o=[b7(*v) for v in [(2,2),(3,2),(4,3),(5,1),(6,2)]]
build(Z,CH,"独立な確率変数の和の期待値・分散",o,"<p>$E(X+Y)=E(X)+E(Y)$（常に）。<b>独立なら</b> $V(X+Y)=V(X)+V(Y)$。$V(aX+b)=a^2V(X)$。</p>","平均は足せる。ばらつきは独立のとき足せる。",7)
# 8 復元抽出 期待値
def b8(r_,w):
    N=r_+w; p=R(r_,N)
    # draw until first red with replacement: geometric E=1/p ; draw n times count red: E=np
    E=1/p
    st=[("確率","<p>1回で赤が出る確率 "+I("p=%s"%L(p))+"（取り出した玉をもどす）。</p>"),
        ("$k$ 回目に初めて赤","<p>"+D(r"P(X=k)=(1-p)^{k-1}p=\left(%s\right)^{k-1}%s"%(L(1-p),L(p)))),
        ("期待値","<p>"+D(r"E(X)=\sum_{k=1}^{\infty}k(1-p)^{k-1}p=\dfrac1p=%s"%L(E))+"<p>（公式 "+I(r"\sum kq^{k-1}=\dfrac1{(1-q)^2}")+"）。</p>")]
    return r"赤玉 $%d$ 個と白玉 $%d$ 個が入った袋から1個取り出して色を見てもどす操作をくり返す。初めて赤玉が出るまでの回数 $X$ の期待値を求めよ。"%(r_,w),st,L(E)
o=[b8(*v) for v in [(2,4),(1,5),(3,9),(2,8),(4,8)]]
build(Z,CH,"初めて赤が出るまでの回数（復元抽出）の期待値",o,"<p>$P(X=k)=(1-p)^{k-1}p$。期待値は $\\dfrac1p$。「確率 $p$ の事象は平均 $\\dfrac1p$ 回で起きる」と覚える。</p>","確率 1/5 なら、平均して 5 回で1回当たる。",8)
# 9 E(XY)
def b9(a,b):
    # independent X (die) Y (coin 0/1)? compute E(XY)=E(X)E(Y) and cov
    EX=R(7,2); EY=R(a,b)
    st=[("独立","<p>"+I("X")+"（さいころの目）と "+I("Y")+"（"+I(str(a)+"/"+str(b))+" の確率で 1、そうでなければ 0）は独立。</p>"),
        ("積の期待値","<p>独立なら "+I("E(XY)=E(X)E(Y)")+"。</p>"+D(r"E(XY)=\dfrac72\cdot%s=%s"%(L(EY),L(EX*EY)))),
        ("共分散","<p>"+D(r"\text{Cov}(X,Y)=E(XY)-E(X)E(Y)=0"))]
    return r"さいころを1回投げて出た目を $X$、これと独立な、確率 $%s$ で $1$、確率 $%s$ で $0$ をとる確率変数を $Y$ とする。$E(XY)$ を求めよ。"%(L(EY),L(1-EY)),st,L(EX*EY)
o=[b9(*v) for v in [(1,2),(1,3),(2,3),(1,4),(3,5)]]
build(Z,CH,"独立な確率変数の積の期待値",o,"<p>独立な $X,Y$ について $E(XY)=E(X)E(Y)$。共分散は 0。</p>","独立なら、平均の積が積の平均。",9)
# 10 最大値の期待値
def b10(n,k):
    # n個の玉 1..n から k個取り出す(非復元) max の期待値 = k(n+1)/(k+1)
    from itertools import combinations
    E=sum(max(c) for c in combinations(range(1,n+1),k))/math.comb(n,k); assert abs(E-k*(n+1)/(k+1))<1e-9
    ans=R(k*(n+1),k+1)
    st=[("$X=m$ となる確率","<p>"+D(r"P(X=m)=\dfrac{{}_{m-1}C_{%d}}{{}_{%d}C_{%d}}"%(k-1,n,k))+"<p>"+I("m=%d,\\ldots,%d"%(k,n))+"。</p>"),
        ("期待値","<p>"+D(r"E(X)=\sum_{m=%d}^{%d}m\cdot\dfrac{{}_{m-1}C_{%d}}{{}_{%d}C_{%d}}=\dfrac{%d(%d+1)}{%d+1}=%s"%(k,n,k-1,n,k,k,n,k,L(ans))))]
    return r"$1,2,\ldots,%d$ の番号をつけた玉から同時に $%d$ 個を取り出すとき、番号の最大値 $X$ の期待値を求めよ。"%(n,k),st,L(ans)
o=[b10(*v) for v in [(6,2),(7,3),(8,2),(9,3),(10,4)]]
build(Z,CH,"取り出した玉の番号の最大値の期待値",o,"<p>最大値が $m$ となる組は、$m$ を1つ選び、残りを $m$ 未満から選ぶ：${}_{m-1}C_{k-1}$ 通り。期待値は $\\dfrac{k(n+1)}{k+1}$。</p>","最大値は、番号全体を k+1 等分した位置になる。",10)
XU=finishx(Z,CH)
