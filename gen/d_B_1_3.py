# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
n=sp.Symbol('n'); k=sp.Symbol('k')
R=sp.Rational
def iterate(f,a1,N):
    a=[R(a1)]
    for _ in range(N-1): a.append(f(a[-1]))
    return a
# 例題1 a_{n+1}=p a_n+q
def b1(p,q,a1):
    al=R(q)/(1-p); g=sp.expand(sp.powsimp(al+(a1-al)*sp.Integer(p)**(n-1)))
    seq=iterate(lambda v:p*v+q,a1,9); assert all(g.subs(n,i+1)==seq[i] for i in range(9))
    st=[("特性方程式で $\\alpha$ を求める","<p>"+I(r"\alpha=p\alpha+q")+" を解く。</p>"+D(r"\alpha=%s\alpha+%s\ \Rightarrow\ \alpha=%s"%(L(p),P(q),L(al)))),
        ("等比数列の形にする","<p>漸化式から "+I(r"\alpha")+" をひく。</p>"+D(r"a_{n+1}-%s=%s\left(a_n-%s\right)"%(P(al),L(p),P(al)))+"<p>数列 "+I(r"\{a_n-%s\}"%P(al))+" は、初項 "+I(r"a_1-%s=%s"%(P(al),L(a1-al)))+"、公比 "+I(L(p))+" の等比数列。</p>"),
        ("一般項",D(r"a_n-%s=%s\cdot%s^{n-1}"%(P(al),L(a1-al),P(p)))+D(r"a_n=%s"%L(g)))]
    return r"$a_1=%d,\ \ a_{n+1}=%s a_n%s$ で定められる数列の一般項を求めよ。"%(a1,L(p) if p!=1 else "",("+"+L(q) if q>0 else L(q))),st,r"a_n=%s"%L(g)
V=[(3,-2,2),(2,3,1),(4,-3,2),(-2,3,2),(3,4,1)]
o=[b1(*v) for v in V]
build(Z,CH,"基本型 a(n+1)=p·a(n)+q",o,r"<p>$\alpha=p\alpha+q$ の解 $\alpha$ を求め、<b>$a_{n+1}-\alpha=p(a_n-\alpha)$</b> と変形する。$\{a_n-\alpha\}$ は公比 $p$ の等比数列。</p>","変わらない値（$\alpha$）を基準にずらすと、ただの等比数列に見える。",1)
# 例題2 階差型
def b2(a1,a,b):
    g=sp.expand(a1+a*(n-1)*n/2+b*(n-1)); seq=iterate(None,0,0) if False else None
    s=[R(a1)]
    for j in range(1,10): s.append(s[-1]+a*j+b)
    assert all(g.subs(n,i+1)==s[i] for i in range(10))
    st=[("階差が $n$ の式","<p>"+I(r"a_{n+1}-a_n=%s"%L(a*n+b))+"。階差数列 "+I(r"b_n=%s"%L(a*n+b))+"。</p>"),
        ("$a_n$ を和で表す","<p>$n\\geqq2$ のとき</p>"+D(r"a_n=a_1+\sum_{k=1}^{n-1}\left(%s\right)=%d+\sum_{k=1}^{n-1}\left(%s\right)"%(L(a*k+b),a1,L(a*k+b)))),
        ("Σを計算する",D(r"a_n=%d+%s\cdot\dfrac{(n-1)n}{2}+%s(n-1)=%s"%(a1,P(a),P(b),L(g)))),
        ("$n=1$ の確認","<p>"+I(r"%s"%L(g.subs(n,1)))+"、つまり $a_1=%d$ と一致するので $n=1$ でも成り立つ。</p>"%a1)]
    return r"$a_1=%d,\ \ a_{n+1}=a_n+%s$ で定められる数列の一般項を求めよ。"%(a1,L(a*n+b)),st,r"a_n=%s"%L(g)
V=[(1,2,1),(2,3,-1),(5,4,0),(1,-2,5),(3,6,-3)]
o=[b2(*v) for v in V]
build(Z,CH,"階差型 a(n+1)=a(n)+f(n)",o,r"<p>$a_{n+1}-a_n=f(n)$ は階差数列が $f(n)$。$n\geqq2$ で $a_n=a_1+\displaystyle\sum_{k=1}^{n-1}f(k)$ を計算し、$n=1$ を確かめる。</p>","1歩ごとの上がり幅が分かっている。足し合わせれば現在地。",2)
# 例題3 a_{n+1}=p a_n+q r^n
def b3(p,q,r,a1):
    B=R(q,r-p); g=sp.expand(B*sp.Integer(r)**n+(a1-B*r)*sp.Integer(p)**(n-1))
    seq=iterate(None,0,0) if False else None
    s=[R(a1)]
    for j in range(1,9): s.append(p*s[-1]+q*r**j)
    assert all(g.subs(n,i+1)==s[i] for i in range(9))
    c1=R(a1,r); cp=R(p,r); cq=R(q,r); al=cq/(1-cp); coef=c1-al
    st=[("両辺を $%d^{n+1}$ でわる"%r,D(r"\dfrac{a_{n+1}}{%d^{n+1}}=\dfrac{%d}{%d}\cdot\dfrac{a_n}{%d^{n}}+\dfrac{%d}{%d}"%(r,p,r,r,q,r))),
        ("$c_n=\\dfrac{a_n}{%d^n}$ とおく"%r,D(r"c_{n+1}=%s\,c_n+%s,\quad c_1=\dfrac{%d}{%d}=%s"%(L(cp),L(cq),a1,r,L(c1)))),
        ("$c_{n+1}=pc_n+q$ 型を解く",D(r"\alpha=%s\alpha+%s\ \Rightarrow\ \alpha=%s"%(L(cp),L(cq),L(al)))+D(r"c_n-%s=\left(%s\right)\left(%s\right)^{n-1}"%(P(al),L(coef),L(cp)))+D(r"c_n=%s+%s\left(%s\right)^{n-1}"%(L(al),P(coef),L(cp)))),
        ("$a_n$ にもどす",D(r"a_n=%d^n c_n=%s"%(r,L(g))))]
    return r"$a_1=%d,\ \ a_{n+1}=%d a_n+%s\cdot%d^{n}$ で定められる数列の一般項を求めよ。"%(a1,p,L(q),r),st,r"a_n=%s"%L(g)
V=[(3,1,2,1),(2,1,3,2),(3,2,5,4),(2,6,5,1),(5,2,3,3)]
o=[b3(*v) for v in V]
build(Z,CH,"指数つき a(n+1)=p·a(n)+q·r^n 型",o,r"<p>両辺を $r^{n+1}$ でわり、$c_n=\dfrac{a_n}{r^n}$ とおくと $c_{n+1}=\dfrac pr c_n+\dfrac qr$。前の型（$a_{n+1}=pa_n+q$）に帰着して解き、$a_n=r^nc_n$ にもどす。</p>","$r^n$ という「ものさし」でわって、単位をそろえてから解く。",3)
# 例題4 3項間
def b4(al,be,a1,a2):
    g=sp.expand((( a2-al*a1)*sp.Integer(be)**(n-1)-(a2-be*a1)*sp.Integer(al)**(n-1))/R(be-al))
    s=[R(a1),R(a2)]
    for _ in range(8): s.append((al+be)*s[-1]-al*be*s[-2])
    assert all(g.subs(n,i+1)==s[i] for i in range(10))
    S_=al+be; Pr=al*be
    st=[("2通りに変形する","<p>"+I(r"x^2=%sx%s"%(L(S_),("+"+L(-Pr) if -Pr>0 else L(-Pr))))+" の解は "+I(r"x=%s,\ %s"%(L(al),L(be)))+"。</p>"+D(r"a_{n+2}-%s a_{n+1}=%s\left(a_{n+1}-%s a_n\right)"%(P(al),L(be),P(al)))+D(r"a_{n+2}-%s a_{n+1}=%s\left(a_{n+1}-%s a_n\right)"%(P(be),L(al),P(be)))),
        ("等比数列として一般項を出す","<p>"+I(r"a_2-%sa_1=%s,\ \ a_2-%sa_1=%s"%(P(al),L(a2-al*a1),P(be),L(a2-be*a1)))+" より</p>"+D(r"a_{n+1}-%s a_n=%s\cdot%s^{n-1}\quad\cdots\text{①}"%(P(al),L(a2-al*a1),P(be)))+D(r"a_{n+1}-%s a_n=%s\cdot%s^{n-1}\quad\cdots\text{②}"%(P(be),L(a2-be*a1),P(al)))),
        ("①−② で $a_{n+1}$ を消す",D(r"%s a_n=%s\cdot%s^{n-1}-%s\cdot%s^{n-1}"%(P(be-al),L(a2-al*a1),P(be),P(a2-be*a1),P(al)))+D(r"a_n=%s"%L(g)))]
    pb=(r"$a_1=%d,\ a_2=%d,\ \ a_{n+2}=%s a_{n+1}%s a_n$ で定められる数列の一般項を求めよ。"%(a1,a2,L(S_),("-"+L(Pr) if Pr>0 else "+"+L(-Pr))))
    return pb.replace("=1 a_","=a_").replace("+1 a_","+a_").replace("-1 a_","-a_"),st,r"a_n=%s"%L(g)
V=[(1,3,1,2),(2,3,1,4),(1,4,2,3),(2,5,1,3),(-1,2,1,3)]
o=[b4(*v) for v in V]
build(Z,CH,"3項間漸化式",o,r"<p>$x^2=sx-t$ の解 $\alpha,\beta$ を使って <b>$a_{n+2}-\alpha a_{n+1}=\beta(a_{n+1}-\alpha a_n)$</b> と <b>$a_{n+2}-\beta a_{n+1}=\alpha(a_{n+1}-\beta a_n)$</b> の2通りに変形。それぞれ等比数列。引き算で $a_{n+1}$ を消す。</p>","同じ漸化式を2つの見方で書き、2本の等比数列を作ってから、混ぜ物（$a_{n+1}$）を消す。",4)
# 例題5 逆数型
def b5(p,q,a1):
    a1=R(a1); b1_=1/a1; al=R(p)/(1-q); bn=sp.expand(al+(b1_-al)*sp.Integer(q)**(n-1)); g=sp.simplify(1/bn)
    s=[a1]
    for _ in range(8): s.append(s[-1]/(p*s[-1]+q))
    assert all(sp.simplify(g.subs(n,i+1)-s[i])==0 for i in range(9))
    st=[("逆数をとる","<p>"+I(r"a_n\neq0")+"（すべての項が正）。両辺の逆数をとる。</p>"+D(r"\dfrac1{a_{n+1}}=\dfrac{%s a_n+%d}{a_n}=%d+\dfrac{%d}{a_n}"%(cf(p),q,p,q))),
        ("$b_n=\\dfrac1{a_n}$ とおく",D(r"b_{n+1}=%s\,b_n+%d,\quad b_1=%s"%(L(q),p,L(b1_)))),
        ("$b_{n+1}=qb_n+p$ 型を解く",D(r"\alpha=%s\alpha+%d\ \Rightarrow\ \alpha=%s"%(L(q),p,L(al)))+D(r"b_n-%s=%s\cdot%s^{n-1}\ \Rightarrow\ b_n=%s"%(P(al),L(b1_-al),P(q),L(bn)))),
        ("$a_n$ にもどす",D(r"a_n=\dfrac1{b_n}=%s"%L(g)))]
    return r"$a_1=%s,\ \ a_{n+1}=\dfrac{a_n}{%s a_n+%d}$ で定められる数列の一般項を求めよ。"%(L(a1),cf(p),q),st,r"a_n=%s"%L(g)
V=[(1,2,1),(2,3,1),(3,4,1),(1,3,2),(2,2,1)]
o=[b5(*v) for v in V]
build(Z,CH,"分数型漸化式（逆数をとる）",o,r"<p>$a_{n+1}=\dfrac{a_n}{pa_n+q}$ は<b>逆数をとる</b>と $\dfrac1{a_{n+1}}=q\cdot\dfrac1{a_n}+p$。$b_n=\dfrac1{a_n}$ とおけば $b_{n+1}=qb_n+p$ 型。</p>","分数のままでは手が出ない。ひっくり返すと、知っている型に化ける。",5)
UNIT=finish(Z,CH,0,2,"数列","漸化式","基本型、階差型、r^n型、3項間、分数型と、漸化式の主要パターンを総まとめします。",subject="B")
