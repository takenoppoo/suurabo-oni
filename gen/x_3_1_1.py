# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; n=sp.symbols("n",positive=True); oo=sp.oo
# 6 sqrt(n^2+an+b)-n
def b6(a,b):
    lim=sp.limit(sp.sqrt(n**2+a*n+b)-n,n,oo); assert lim==R(a,2)
    st=[("有理化","<p>"+D(r"\sqrt{n^2+%dn+%d}-n=\dfrac{(n^2+%dn+%d)-n^2}{\sqrt{n^2+%dn+%d}+n}=\dfrac{%dn+%d}{\sqrt{n^2+%dn+%d}+n}"%(a,b,a,b,a,b,a,b,a,b))),
        ("$n$ で割る","<p>"+D(r"=\dfrac{%d+\dfrac{%d}{n}}{\sqrt{1+\dfrac{%d}{n}+\dfrac{%d}{n^2}}+1}"%(a,b,a,b))),
        ("極限","<p>"+D(r"\to\dfrac{%d}{1+1}=%s"%(a,L(lim))))]
    return r"$\displaystyle\lim_{n\to\infty}\left(\sqrt{n^2+%dn+%d}-n\right)$ を求めよ。"%(a,b),st,L(lim)
o=[b6(*v) for v in [(4,1),(6,2),(2,5),(10,3),(8,1)]]
build(Z,CH,"∞−∞ 型の無理式の極限",o,"<p>$\\infty-\\infty$ は<b>有理化</b>して分子の2次の項を消し、分母・分子を $n$ で割る。</p>","差を和の形に変えて、大きい項どうしを消す。",6)
# 7 比が大きい方
def b7(a,b):
    lim=sp.limit((a**n+b**n)/(a**(n+1)+b**(n+1)),n,oo); big=max(a,b)
    assert lim==R(1,big)
    st=[("底の大きい方でわる","<p>"+I("%d>%d"%(big,min(a,b)))+" なので "+I("%d^n"%big)+" で分母・分子を割る。</p>"+D(r"\dfrac{1+\left(\dfrac{%d}{%d}\right)^n}{%d+%d\left(\dfrac{%d}{%d}\right)^n}"%(min(a,b),big,big,min(a,b),min(a,b),big))),
        ("極限","<p>"+I(r"\left(\dfrac{%d}{%d}\right)^n\to0"%(min(a,b),big))+"。</p>"+D(r"\dfrac{1+0}{%d+0}=%s"%(big,L(lim))))]
    return r"$\displaystyle\lim_{n\to\infty}\dfrac{%d^n+%d^n}{%d^{n+1}+%d^{n+1}}$ を求めよ。"%(a,b,a,b),st,L(lim)
o=[b7(*v) for v in [(2,3),(5,3),(4,7),(6,2),(3,8)]]
build(Z,CH,"a^n+b^n 型の極限（大きい底でわる）",o,"<p>$|r|<1$ なら $r^n\\to0$。<b>底が最大のもので分母・分子を割る</b>と、残りの項は 0 に近づく。</p>","一番強い者で割ると、他は影が薄くなる。",7)
# 8 e の極限
def b8(a,b):
    lim=sp.exp(a*b); 
    st=[("e の定義","<p>"+I(r"\lim_{m\to\infty}\left(1+\dfrac1m\right)^m=e")+"。</p>"),
        ("形をそろえる","<p>"+I("m=%s"%(r"\dfrac{n}{%d}"%a if a!=1 else "n"))+" とおくと "+I(r"\dfrac%dn=\dfrac1m"%a if False else r"\dfrac{%d}{n}=\dfrac1m"%a)+"。</p>"+D(r"\left(1+\dfrac{%d}{n}\right)^{%dn}=\left\{\left(1+\dfrac1m\right)^{m}\right\}^{%d}"%(a,b,a*b))),
        ("極限","<p>"+D(r"\to e^{%d}"%(a*b)))]
    return r"$\displaystyle\lim_{n\to\infty}\left(1+\dfrac{%d}{n}\right)^{%dn}$ を求めよ。"%(a,b),st,r"e^{%d}"%(a*b)
o=[b8(*v) for v in [(1,2),(2,1),(3,2),(1,5),(2,3)]]
build(Z,CH,"(1+a/n)^{bn} の極限（e）",o,"<p>$\\left(1+\\dfrac an\\right)^{n}\\to e^{a}$。$\\dfrac an=\\dfrac1m$ と置いて $\\left(1+\\dfrac1m\\right)^m\\to e$ の形に直す。</p>","利率の複利計算が、無限回の極限で e になる。",8)
# 9 a(n+1)=sqrt(k+a_n)
def b9(k,a1):
    # fixed point alpha = sqrt(k+alpha) -> alpha^2-alpha-k=0
    al=(1+math.sqrt(1+4*k))/2; 
    A=[a1]
    for j in range(60): A.append(math.sqrt(k+A[-1]))
    assert abs(A[-1]-al)<1e-9
    st=[("極限が存在すると仮定","<p>"+I(r"\lim a_n=\alpha")+" とすると "+I(r"\alpha=\sqrt{%d+\alpha}"%k)+"。</p>"+D(r"\alpha^2-\alpha-%d=0\ \Rightarrow\ \alpha=%s\quad(\alpha>0)"%(k,L(sp.simplify((1+sp.sqrt(1+4*k))/2))))),
        ("収束の確認","<p>"+I("a_1=%d"%a1)+" から "+I("a_n")+" は増加（または減少）し、"+I(r"\alpha")+" をこえない（有界な単調数列は収束）。</p>"+D(r"a_2=%.4f,\ a_3=%.4f,\ a_4=%.4f"%(A[1],A[2],A[3]))),
        ("答え",D(r"\lim_{n\to\infty}a_n=%s"%L(sp.simplify((1+sp.sqrt(1+4*k))/2))))]
    return r"$a_1=%d,\ a_{n+1}=\sqrt{%d+a_n}$ で定まる数列の極限を求めよ。（収束することを認めてよい）"%(a1,k),st,L(sp.simplify((1+sp.sqrt(1+4*k))/2))
o=[b9(*v) for v in [(2,1),(6,1),(12,2),(20,1),(2,3)]]
build(Z,CH,"a(n+1)=√(k+a(n)) の極限",o,"<p>収束するなら極限を $\\alpha$ として漸化式で $a_{n+1},a_n\\to\\alpha$。$\\alpha=\\sqrt{k+\\alpha}$ の<b>正の解</b>が極限。</p>","行き着く先では、次の値と今の値が同じになる。",9)
# 10 区分求積
def b10(p):
    S=sp.limit(sum(sp.Symbol("k")**p for _ in [0]),n,oo) if False else None
    k=sp.symbols("k"); val=R(1,p+1)
    st=[("区分求積の形","<p>"+D(r"\sum_{k=1}^{n}\dfrac{k^{%d}}{n^{%d}}=\dfrac1n\sum_{k=1}^{n}\left(\dfrac kn\right)^{%d}"%(p,p+1,p))),
        ("定積分に","<p>"+D(r"\lim_{n\to\infty}\dfrac1n\sum_{k=1}^{n}f\left(\dfrac kn\right)=\int_0^1f(x)\,dx")+"<p>"+I("f(x)=x^{%d}"%p)+"。</p>"),
        ("計算",D(r"\int_0^1x^{%d}dx=\dfrac1{%d}"%(p,p+1)))]
    return r"$\displaystyle\lim_{n\to\infty}\dfrac{1^{%d}+2^{%d}+\cdots+n^{%d}}{n^{%d}}$ を求めよ。"%(p,p,p,p+1),st,L(val)
o=[b10(p) for p in [2,3,4,5,1]]
build(Z,CH,"区分求積法による和の極限",o,"<p>$\\dfrac1n\\sum f\\!\\left(\\dfrac kn\\right)\\to\\int_0^1f(x)dx$ の形に整理。分母の $n^{p+1}$ を $\\dfrac1n\\cdot n^p$ と分けて $\\left(\\dfrac kn\\right)^p$ を作る。</p>","細い短冊の面積を足していくと積分になる。",10)
XU=finishx(Z,CH)
