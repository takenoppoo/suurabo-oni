# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; n=sp.symbols("n",positive=True); k=sp.symbols("k",positive=True)
# 6 Σ 1/(n(n+d))
def b6(d):
    S=sp.summation(R(1,1)/(k*(k+d)),(k,1,sp.oo)); assert S==sp.harmonic(d)/d
    st=[("部分分数","<p>"+D(r"\dfrac1{k(k+%d)}=\dfrac1{%d}\left(\dfrac1k-\dfrac1{k+%d}\right)"%(d,d,d))),
        ("部分和","<p>"+D(r"S_n=\dfrac1{%d}\left\{\left(1+\dfrac12+\cdots+\dfrac1{%d}\right)-\left(\dfrac1{n+1}+\cdots+\dfrac1{n+%d}\right)\right\}"%(d,d,d))),
        ("極限","<p>後ろの括弧は 0 に近づく。</p>"+D(r"\lim_{n\to\infty}S_n=\dfrac1{%d}\left(%s\right)=%s"%(d,"+".join(r"\dfrac1{%d}"%i for i in range(1,d+1)),L(S))))]
    return r"無限級数 $\displaystyle\sum_{k=1}^{\infty}\dfrac{1}{k(k+%d)}$ の和を求めよ。"%d,st,L(S)
o=[b6(d) for d in [1,2,3,4,5]]
build(Z,CH,"1/(k(k+d)) の無限級数",o,"<p>部分分数 $\\dfrac1d\\left(\\dfrac1k-\\dfrac1{k+d}\\right)$ で<b>部分和 $S_n$</b>を作り、$n\\to\\infty$ とする。打ち消されずに残るのは最初の $d$ 項。</p>","差の形に直せば、途中は全部消える。",6)
# 7 Σ n r^{n-1}
def b7(r):
    S=sp.summation(k*r**(k-1),(k,1,sp.oo)); assert S==1/(1-r)**2
    st=[("部分和","<p>"+I("S_n=\\sum_{k=1}^{n}k\\,r^{k-1}")+"、"+I("rS_n")+" を引く。</p>"+D(r"(1-r)S_n=1+r+\cdots+r^{n-1}-nr^n=\dfrac{1-r^n}{1-r}-nr^n")),
        ("極限","<p>"+I("|r|<1")+" のとき "+I("r^n\\to0,\\ nr^n\\to0")+"。</p>"+D(r"(1-r)S=\dfrac1{1-r}\ \Rightarrow\ S=\dfrac1{(1-r)^2}")),
        ("値","<p>"+I("r=%s"%L(r))+"：</p>"+D(r"S=\dfrac1{\left(1-%s\right)^2}=%s"%(L(r),L(S))))]
    return r"無限級数 $\displaystyle\sum_{k=1}^{\infty}k\left(%s\right)^{k-1}$ の和を求めよ。"%L(r),st,L(S)
o=[b7(r) for r in [R(1,2),R(1,3),R(-1,2),R(2,3),R(-1,3)]]
build(Z,CH,"(等差)×(等比) の無限級数",o,"<p>$S_n-rS_n$ で等比数列の和に帰着。$|r|<1$ のとき $r^n\\to0,\\ nr^n\\to0$。結果は $\\dfrac1{(1-r)^2}$。</p>","ずらして引いて、掛け算の部分を消す。",7)
# 8 図形の面積の総和（正方形の内接）
def b8(a):
    # square side a; connect midpoints -> square with side a/sqrt2 ; area ratio 1/2 ; sum of areas = a^2/(1-1/2)=2a^2
    S=2*a*a
    fg=geo("x312_8_%d"%a,polys=[([(0,0),(4,0),(4,4),(0,4)],"#b81f36"),([(2,0),(4,2),(2,4),(0,2)],"#1f6fb8"),([(2,2-0),(3,1),(2,0)]  if False else [(1,1),(3,1),(3,3),(1,3)],"#333")],w=34,size=(3.2,3.2))
    st=[("面積の列","<p>各辺の中点を結んで作る正方形の面積は、元の "+I(r"\dfrac12")+" 倍。</p>"+D(r"S_1=%d,\quad S_2=%s,\quad S_3=%s,\ \ldots"%(a*a,L(R(a*a,2)),L(R(a*a,4))))+fg),
        ("初項と公比","<p>初項 "+I(str(a*a))+"、公比 "+I(r"\dfrac12")+"。</p>"),
        ("総和","<p>"+D(r"\dfrac{%d}{1-\dfrac12}=%d"%(a*a,S)))]
    return r"1辺 $%d$ の正方形がある。各辺の中点を結んで正方形を作り、さらにその正方形の各辺の中点を結ぶ操作を限りなくくり返す。できる正方形（もとのものを含む）の面積の総和を求めよ。"%a,st,str(S)
o=[b8(a) for a in [4,6,8,10,12]]
build(Z,CH,"中点を結ぶ正方形の面積の総和",o,"<p>面積比が一定 $\\dfrac12$ の無限等比級数。初項 $a^2$、公比 $\\dfrac12$、和 $\\dfrac{a^2}{1-\\frac12}$。</p>","毎回、面積が半分になる。足していくとちょうど2倍で止まる。",8)
# 9 収束条件
def b9(a):
    # sum (x^2 - a x)^n ... converge when |x^2-a x|<1
    x=sp.symbols("x",real=True)
    st=[("収束条件","<p>公比 "+I("r=x^2-%dx"%a)+" の無限等比級数が収束 "+I(r"\iff |r|<1")+"。</p>"+D(r"-1<x^2-%dx<1"%a)),
        ("2つの不等式","<p>"+D(r"x^2-%dx-1<0\ \Rightarrow\ \dfrac{%d-\sqrt{%d}}{2}<x<\dfrac{%d+\sqrt{%d}}{2}"%(a,a,a*a+4,a,a*a+4))+"<p>"+D(r"x^2-%dx+1>0\ \Rightarrow\ x<\dfrac{%d-\sqrt{%d}}{2}\ \text{または}\ x>\dfrac{%d+\sqrt{%d}}{2}"%(a,a,a*a-4,a,a*a-4))),
        ("共通部分","<p>数直線で重ねて答えを出す。</p>")]
    lo1=(a-math.sqrt(a*a+4))/2;hi1=(a+math.sqrt(a*a+4))/2;lo2=(a-math.sqrt(a*a-4))/2;hi2=(a+math.sqrt(a*a-4))/2
    ans=r"\dfrac{%d-\sqrt{%d}}{2}<x<\dfrac{%d-\sqrt{%d}}{2},\ \ \dfrac{%d+\sqrt{%d}}{2}<x<\dfrac{%d+\sqrt{%d}}{2}"%(a,a*a+4,a,a*a-4,a,a*a-4,a,a*a+4)
    return r"無限級数 $\displaystyle\sum_{n=1}^{\infty}(x^2-%dx)^n$ が収束するような $x$ の値の範囲を求めよ。"%a,st,ans
o=[b9(a) for a in [3,4,5,6,7]]
build(Z,CH,"無限等比級数が収束する x の範囲",o,"<p>公比 $r$ が $-1<r<1$ のとき収束（初項が 0 の場合は別）。$-1<f(x)<1$ を<b>2つの不等式</b>に分けて解き、共通部分を取る。</p>","公比の大きさが1未満なら、足していっても発散しない。",9)
# 10 発散
def b10(a):
    st=[("部分和","<p>"+I(r"S_n=\sum_{k=1}^{n}\left(\sqrt{k+%d}-\sqrt{k}\right)"%a)+"。</p>"),
        ("有理化","<p>"+D(r"\sqrt{k+%d}-\sqrt k=\dfrac{%d}{\sqrt{k+%d}+\sqrt k}"%(a,a,a))),
        ("発散","<p>"+I(r"\dfrac{%d}{\sqrt{k+%d}+\sqrt k}>\dfrac{%d}{2\sqrt{k+%d}}"%(a,a,a,a))+" などで評価でき、部分和は無限大に発散する。または"+D(r"\sqrt{k+%d}-\sqrt k=\dfrac{%d}{\sqrt{k+%d}+\sqrt k}\to0\ \text{だが、和は発散}"%(a,a,a)))]
    return r"無限級数 $\displaystyle\sum_{k=1}^{\infty}\left(\sqrt{k+%d}-\sqrt{k}\right)$ は収束するか。収束するならその和を求めよ。"%a,st,r"\text{発散する}"
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"一般項が 0 に近づいても発散する例",o,"<p>一般項 $\\to0$ は収束のための<b>必要条件</b>であって十分条件ではない。部分和が $n\\to\\infty$ で無限大になるなら発散。</p>","小さな足し算でも、いつまでも続ければ無限大。",10)
XU=finishx(Z,CH)
