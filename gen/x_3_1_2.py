# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
def co(c): return '' if c==1 else ('-' if c==-1 else L(c))
R=sp.Rational; n=sp.symbols("n",positive=True); k=sp.symbols("k",positive=True)
# 6 Σ 1/(n(n+d))
def b6(d):
    S=sp.summation(R(1,1)/(k*(k+d)),(k,1,sp.oo)); assert S==sp.harmonic(d)/d
    Hd="+".join(r"\dfrac1{%d}"%i for i in range(1,d+1)); Td="+".join(r"\dfrac1{n+%d}"%i for i in range(1,d+1)); cf=co(R(1,d))
    st=[("部分分数に分ける","<p>"+I(r"\dfrac1k-\dfrac1{k+%d}=\dfrac{(k+%d)-k}{k(k+%d)}=\dfrac{%d}{k(k+%d)}"%(d,d,d,d,d))+" だから、</p>"+D(r"\dfrac1{k(k+%d)}=%s\left(\dfrac1k-\dfrac1{k+%d}\right)"%(d,r"\dfrac1{%d}"%d if d>1 else "",d))),
        ("部分和 $S_n$ を書き並べる","<p>"+D(r"S_n=%s\left\{\left(\dfrac11-\dfrac1{%d}\right)+\left(\dfrac12-\dfrac1{%d}\right)+\cdots+\left(\dfrac1n-\dfrac1{n+%d}\right)\right\}"%(r"\dfrac1{%d}"%d if d>1 else "",1+d,2+d,d))+"<p>"+I(r"-\dfrac1{k+%d}"%d)+" は "+I("%d"%d)+" 項あとの "+I(r"+\dfrac1{k+%d}"%d)+" と打ち消し合う。残るのは最初の "+I(str(d))+" 個の正の項と、最後の "+I(str(d))+" 個の負の項。</p>"+D(r"S_n=%s\left\{\left(%s\right)-\left(%s\right)\right\}"%(r"\dfrac1{%d}"%d if d>1 else "",Hd,Td))),
        ("$n\\to\\infty$ とする","<p>"+I(r"n\to\infty")+" のとき "+I(r"\dfrac1{n+1},\ \dots,\ \dfrac1{n+%d}\to0"%d)+"。</p>"+D(r"\lim_{n\to\infty}S_n=%s\left(%s\right)=%s"%(r"\dfrac1{%d}"%d if d>1 else "",Hd,L(S))))]
    return r"無限級数 $\displaystyle\sum_{k=1}^{\infty}\dfrac{1}{k(k+%d)}$ の和を求めよ。"%d,st,L(S)
o=[b6(d) for d in [1,2,3,4,5]]
build(Z,CH,"1/(k(k+d)) の無限級数",o,"<p>部分分数 $\\dfrac1d\\left(\\dfrac1k-\\dfrac1{k+d}\\right)$ で<b>部分和 $S_n$</b>を作り、$n\\to\\infty$ とする。打ち消されずに残るのは最初の $d$ 項。</p>","差の形に直せば、途中は全部消える。",6)
# 7 Σ n r^{n-1}
def b7(r):
    S=sp.summation(k*r**(k-1),(k,1,sp.oo)); assert S==1/(1-r)**2
    st=[("$S_n$ と $rS_n$ を書く","<p>"+D(r"S_n=1+2r+3r^2+\cdots+nr^{n-1}")+D(r"rS_n=\ \ \ \ r+2r^2+\cdots+(n-1)r^{n-1}+nr^{n}")),
        ("ひき算する","<p>項の次数をそろえて引く。</p>"+D(r"(1-r)S_n=1+r+r^2+\cdots+r^{n-1}-nr^{n}")+"<p>右辺の前半は初項 "+I("1")+"、公比 "+I("r")+"、項数 "+I("n")+" の等比数列の和。</p>"+D(r"(1-r)S_n=\dfrac{1-r^n}{1-r}-nr^n")),
        ("$n\\to\\infty$ とする","<p>"+I("|r|<1")+" のとき "+I(r"r^n\to0,\ nr^n\to0")+"。</p>"+D(r"(1-r)S=\dfrac{1-0}{1-r}-0=\dfrac1{1-r}")+"<p>両辺を "+I("1-r")+" でわる。</p>"+D(r"S=\dfrac1{(1-r)^2}")),
        ("値を代入する","<p>"+I("r=%s"%L(r))+"：</p>"+D(r"1-%s=%s,\qquad S=\dfrac1{\left(%s\right)^2}=\dfrac1{%s}=%s"%(("\\left(%s\\right)"%L(r)) if r<0 else L(r),L(1-r),L(1-r),L((1-r)**2),L(S))))]
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
    s1=a*a+4; s2=a*a-4; v=lambda e:(a-math.sqrt(e))/2 ; w=lambda e:(a+math.sqrt(e))/2
    st=[("収束条件を式にする","<p>公比 "+I("r=x^2-%dx"%a)+" の無限等比級数が収束する条件は "+I(r"|r|<1")+"。</p>"+D(r"-1<x^2-%dx<1"%a)+"<p>連立不等式として、2つに分ける。</p>"+D(r"\begin{cases}x^2-%dx<1\\ x^2-%dx>-1\end{cases}"%(a,a))),
        ("$x^2-%dx-1<0$ を解く"%a,"<p>"+I(r"x^2-%dx-1=0"%a)+" を解の公式で解く。</p>"+D(r"x=\dfrac{%d\pm\sqrt{%d^2+4}}{2}=\dfrac{%d\pm\sqrt{%d}}{2}"%(a,a,a,s1))+"<p>下に凸なので、解の間。</p>"+D(r"\dfrac{%d-\sqrt{%d}}{2}<x<\dfrac{%d+\sqrt{%d}}{2}"%(a,s1,a,s1))),
        ("$x^2-%dx+1>0$ を解く"%a,"<p>"+I(r"x^2-%dx+1=0"%a)+" を解く。</p>"+D(r"x=\dfrac{%d\pm\sqrt{%d^2-4}}{2}=\dfrac{%d\pm\sqrt{%d}}{2}"%(a,a,a,s2))+"<p>下に凸なので、解の外側。</p>"+D(r"x<\dfrac{%d-\sqrt{%d}}{2}\ \text{または}\ x>\dfrac{%d+\sqrt{%d}}{2}"%(a,s2,a,s2))),
        ("数直線で共通部分をとる","<p>端の値を小数で比べる。</p>"+wtable(["","$\\dfrac{%d-\\sqrt{%d}}{2}$"%(a,s1),"$\\dfrac{%d-\\sqrt{%d}}{2}$"%(a,s2),"$\\dfrac{%d+\\sqrt{%d}}{2}$"%(a,s2),"$\\dfrac{%d+\\sqrt{%d}}{2}$"%(a,s1)],[["約","$%.2f$"%v(s1),"$%.2f$"%v(s2),"$%.2f$"%w(s2),"$%.2f$"%w(s1)]])+"<p>小さい順に並ぶので、2つの不等式の共通部分は2つの区間になる。</p>")]
    ans=r"\dfrac{%d-\sqrt{%d}}{2}<x<\dfrac{%d-\sqrt{%d}}{2},\ \ \dfrac{%d+\sqrt{%d}}{2}<x<\dfrac{%d+\sqrt{%d}}{2}"%(a,a*a+4,a,a*a-4,a,a*a-4,a,a*a+4)
    return r"無限級数 $\displaystyle\sum_{n=1}^{\infty}(x^2-%dx)^n$ が収束するような $x$ の値の範囲を求めよ。"%a,st,ans
o=[b9(a) for a in [3,4,5,6,7]]
build(Z,CH,"無限等比級数が収束する x の範囲",o,"<p>公比 $r$ が $-1<r<1$ のとき収束（初項が 0 の場合は別）。$-1<f(x)<1$ を<b>2つの不等式</b>に分けて解き、共通部分を取る。</p>","公比の大きさが1未満なら、足していっても発散しない。",9)
# 10 発散
def b10(a):
    Sn="+".join(r"\sqrt{n+%d}"%j for j in range(1,a+1)); Sm="+".join(r"\sqrt{%d}"%j if j>1 else "1" for j in range(1,a+1))
    st=[("部分和を書き並べる","<p>"+D(r"S_n=\sum_{k=1}^{n}\left(\sqrt{k+%d}-\sqrt{k}\right)"%a)+"<p>"+I(r"\sqrt{k+%d}"%a)+" と "+I(r"\sqrt k")+" で打ち消し合う項を整理する。</p>"+D(r"S_n=\sum_{k=%d}^{n+%d}\sqrt k-\sum_{k=1}^{n}\sqrt k"%(a+1,a))),
        ("打ち消して整理する","<p>共通の "+I(r"\sqrt{%d},\dots,\sqrt n"%(a+1))+" が消えて、</p>"+D(r"S_n=\left(%s\right)-\left(%s\right)"%(Sn,Sm))),
        ("$n\\to\\infty$ の様子","<p>"+I(r"n\to\infty")+" のとき "+I(r"\sqrt{n+j}\to\infty")+"（"+I("j=1,\\dots,%d"%a)+"）で、引く部分は定数。</p>"+D(r"S_n\to\infty")+"<p>部分和が無限大になるので、この級数は<b>発散</b>する。（一般項 "+I(r"\sqrt{k+%d}-\sqrt k=\dfrac{%d}{\sqrt{k+%d}+\sqrt k}\to0"%(a,a,a))+" でも、和は有限にならない。）</p>")]
    return r"無限級数 $\displaystyle\sum_{k=1}^{\infty}\left(\sqrt{k+%d}-\sqrt{k}\right)$ は収束するか。収束するならその和を求めよ。"%a,st,r"\text{発散する}"
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"一般項が 0 に近づいても発散する例",o,"<p>一般項 $\\to0$ は収束のための<b>必要条件</b>であって十分条件ではない。部分和が $n\\to\\infty$ で無限大になるなら発散。</p>","小さな足し算でも、いつまでも続ければ無限大。",10)
XU=finishx(Z,CH)
