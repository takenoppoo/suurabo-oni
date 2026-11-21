# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; n,k=sp.symbols("n k")
# 6 Σ k(k+1)(k+2) など
def b6(p):
    # sum_{k=1}^{n} k(k+p)
    expr=k*(k+p); S=sp.factor(sp.summation(expr,(k,1,n)))
    N=10; val=sum(j*(j+p) for j in range(1,N+1)); assert S.subs(n,N)==val
    s2=n*(n+1)*(2*n+1)/6; s1=n*(n+1)/2
    t1=D(r"\sum_{k=1}^{n}k(k+%d)=\sum k^2+%d\sum k=\dfrac{n(n+1)(2n+1)}{6}+%d\cdot\dfrac{n(n+1)}{2}"%(p,p,p))
    st=[("展開して分ける","<p>"+t1+"</p>"),("共通因数でくくる","<p>"+D(r"=\dfrac{n(n+1)}{6}\{(2n+1)+%d\}=%s"%(3*p,L(S)))+"</p>"),("確認","<p>"+I("n=10")+" で "+I(str(val))+" に一致。</p>")]
    return r"$\displaystyle\sum_{k=1}^{n}k(k+%d)$ を $n$ の式で表せ。"%p,st,L(S)
o=[b6(p) for p in [1,2,3,4,5]]
build(Z,CH,"Σ k(k+p) の和",o,"<p>展開して $\\sum k^2$ と $\\sum k$ に分け、公式 $\\dfrac{n(n+1)(2n+1)}6,\\ \\dfrac{n(n+1)}2$ を代入。共通因数 $n(n+1)$ でくくる。</p>","項ごとに公式に分解して、最後に同類をまとめる。",6)
# 7 階差数列
def b7(seq_a,d1,dd):
    # a1=seq_a, b_n=a_{n+1}-a_n = d1 + (n-1)dd  -> a_n = a1+ sum
    an=sp.expand(seq_a+sp.summation(d1+(k-1)*dd,(k,1,n-1)))
    vals=[seq_a]
    for j in range(1,8): vals.append(vals[-1]+d1+(j-1)*dd)
    assert all(an.subs(n,j+1)==vals[j] for j in range(8))
    st=[("階差数列","<p>階差数列 "+I(r"b_n=%d%+d(n-1)"%(d1,dd))+"。"+I("a_1,a_2,\\ldots")+"：</p>"+D(r"%s"%(r",\ ".join(str(v) for v in vals[:6]))+r",\ \cdots")),
        ("一般項の公式","<p>"+D(r"a_n=a_1+\sum_{k=1}^{n-1}b_k=%d+\sum_{k=1}^{n-1}(%s)"%(seq_a,L(d1+(k-1)*dd)))+"</p>"),
        ("計算","<p>"+D(r"a_n=%s"%L(an))+"</p><p>"+I("n=1")+" でも成り立つ。</p>")]
    return r"数列 $%s,\ \cdots$ の階差数列が等差数列であるとき、一般項 $a_n$ を求めよ。"%(r",\ ".join(str(v) for v in vals[:6])),st,r"a_n=%s"%L(an)
o=[b7(*v) for v in [(1,2,3),(3,1,2),(2,4,2),(5,-1,3),(4,3,1)]]
build(Z,CH,"階差数列が等差数列のときの一般項",o,"<p>$a_n=a_1+\\sum_{k=1}^{n-1}b_k$。階差が等差数列なら、$\\Sigma$ は等差数列の和で計算できる。<b>$n=1$ でも成り立つか</b>を確認。</p>","階段の段差をたどって、n 段目の高さを出す。",7)
# 8 部分分数
def b8(p,q,m):
    f=lambda j:(p*j+q)
    S=sum(R(1,f(j)*(f(j)+p)*(f(j)+2*p)) for j in range(1,m+1))
    tel=R(1,2*p)*(R(1,f(1)*(f(1)+p))-R(1,(f(m)+p)*(f(m)+2*p)))
    assert S==tel
    A="(%dk%+d)"%(p,q) if p!=1 else "(k%+d)"%q if q else "k"
    A=("%dk"%p if p!=1 else "k")+("%+d"%q if q else "")
    t1="(%s)(%s)(%s)"%(A,A+"+%d"%p,A+"+%d"%(2*p))
    st=[("部分分数","<p>"+D(r"\dfrac1{%s}=\dfrac1{%d}\left\{\dfrac1{(%s)(%s)}-\dfrac1{(%s)(%s)}\right\}"%(t1,2*p,A,A+"+%d"%p,A+"+%d"%p,A+"+%d"%(2*p)))+"</p>"),
        ("和をとる","<p>隣り合う項が打ち消し合い、最初と最後だけが残る。</p>"+D(r"\dfrac1{%d}\left\{\dfrac1{%d\cdot%d}-\dfrac1{%d\cdot%d}\right\}"%(2*p,f(1),f(1)+p,f(m)+p,f(m)+2*p))),
        ("計算",D(L(S)))]
    return r"$\displaystyle\sum_{k=1}^{%d}\dfrac{1}{%s}$ を計算せよ。"%(m,t1),st,L(S)
o=[b8(*v) for v in [(1,0,10),(2,-1,8),(3,-2,6),(1,1,12),(2,1,9)]]
build(Z,CH,"3つの1次式の積の逆数の和（部分分数）",o,"<p>$\\dfrac1{P(P+p)(P+2p)}=\\dfrac1{2p}\\left\\{\\dfrac1{P(P+p)}-\\dfrac1{(P+p)(P+2p)}\\right\\}$。隣り合う項が打ち消し合い、<b>最初と最後</b>だけが残る。</p>","差の形に直せば、真ん中は全部消える。",8)
# 9 (等差)x(等比)
def b9(r,m):
    S=sum(j*r**(j-1) for j in range(1,m+1))
    # formula: (1 - (m+1) r^m + m r^(m+1))/(1-r)^2
    assert S==R(1-(m+1)*r**m+m*r**(m+1),(1-r)**2)
    st=[("$S$ と $rS$","<p>"+D(r"S=1+2r+3r^2+\cdots+%dr^{%d}"%(m,m-1))+D(r"rS=\ \ \ \ \ r+2r^2+\cdots+%dr^{%d}"%(m-1,m-1)+r"+%dr^{%d}"%(m,m))),
        ("引く","<p>"+D(r"(1-r)S=1+r+r^2+\cdots+r^{%d}-%dr^{%d}"%(m-1,m,m))+"<p>"+I("r=%d"%r)+" を代入して計算。</p>"),
        ("値",D(r"S=%d"%S))]
    return r"$\displaystyle\sum_{k=1}^{%d}k\cdot%d^{k-1}$ を求めよ。"%(m,r),st,str(S)
o=[b9(*v) for v in [(2,8),(3,6),(2,10),(3,5),(4,5)]]
build(Z,CH,"Σ k·r^{k-1} の計算",o,"<p>和を $S$ とし、$rS$ をずらして書いて引く。$(1-r)S$ は<b>等比数列の和 $-$ 最後の項</b>になる。</p>","公比をかけてずらして引くと、掛け算の部分が消える。",9)
# 10 和から一般項（Snが与えられる）
def b10(a,b,c):
    Sn=a*n**2+b*n+c; an=sp.expand(Sn-Sn.subs(n,n-1)); a1=Sn.subs(n,1)
    ok=(an.subs(n,1)==a1)
    st=[("$n\\geqq2$","<p>"+D(r"a_n=S_n-S_{n-1}=(%s)-(%s)=%s"%(L(Sn),L(Sn.subs(n,n-1)),L(an)))),
        ("$n=1$ の確認","<p>"+D(r"a_1=S_1=%d,\qquad %s\ \text{に }n=1\text{ を代入}=%d"%(a1,L(an),an.subs(n,1)))+("<p>一致するので全ての "+I("n\\geqq1")+" で成り立つ。</p>" if ok else "<p>一致しないので "+I("a_1=%d"%a1)+" と "+I("n\\geqq2")+" で場合分け。</p>"))]
    ans=r"a_n=%s"%L(an) if ok else r"a_1=%d,\ a_n=%s\ (n\geqq2)"%(a1,L(an))
    return r"数列 $\{a_n\}$ の初項から第 $n$ 項までの和が $S_n=%s$ であるとき、一般項 $a_n$ を求めよ。"%L(Sn),st,ans
o=[b10(*v) for v in [(1,2,0),(2,-1,3),(1,1,2),(3,0,-1),(2,3,0)]]
build(Z,CH,"和 Sn から一般項（n=1 の確認）",o,"<p>$n\\geqq2$ で $a_n=S_n-S_{n-1}$。<b>$a_1=S_1$ とは別に計算</b>し、$n\\geqq2$ の式に $n=1$ を入れた値と一致するかを必ず確認する。</p>","1つ前までの合計との差が、その1項。",10)
XU=finishx(Z,CH)
