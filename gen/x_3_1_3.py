# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x")
# 6 (1-cos ax)/x^2
def b6(a,b):
    lim=sp.limit((1-sp.cos(a*x))/(b*x**2),x,0); assert lim==R(a*a,2*b)
    A="" if a==1 else str(a); ux=L(R(a,2))+"x" if a!=2 else "x"; ux=ux.replace(r"\dfrac12x",r"\dfrac x2") if a==1 else ux
    Bc="" if b==1 else str(b); dn=r"\dfrac{2}{%d}"%b if b>1 else "2"
    st=[("半角の公式で書きかえる","<p>"+I(r"1-\cos\theta=2\sin^2\dfrac\theta2")+" で "+I(r"\theta=%sx"%A)+" とする。</p>"+D(r"1-\cos %sx=2\sin^2%s"%(A,ux))),
        ("式に代入して整理する","<p>"+D(r"\dfrac{1-\cos %sx}{%sx^2}=\dfrac{2\sin^2%s}{%sx^2}=%s\left(\dfrac{\sin %s}{x}\right)^2"%(A,Bc,ux,Bc,dn,ux))),
        ("基本形にそろえる",("<p>"+I(r"\dfrac{\sin x}{x}")+" はそのまま基本形。</p>"+D(r"%s\left(\dfrac{\sin x}{x}\right)^2"%dn)) if a==2 else ("<p>"+I(r"u=%s"%ux)+" とおくと "+I("x=%su"%(L(R(2,a)) if a!=1 else "2"))+"。"+I(r"\dfrac{\sin u}{x}")+" を "+I(r"\dfrac{\sin u}{u}")+" の形にするため、"+I("u")+" をかけてわる。</p>"+D(r"\dfrac{\sin u}{x}=\dfrac{\sin u}{u}\cdot\dfrac{u}{x}=\dfrac{\sin u}{u}\cdot%s"%L(R(a,2)))+D(r"%s\left(\dfrac{\sin u}{x}\right)^2=%s\cdot\left(%s\right)^2\left(\dfrac{\sin u}{u}\right)^2"%(dn,dn,L(R(a,2)))))),
        ("極限を求める","<p>"+I(r"x\to0")+" のとき "+I(r"u\to0")+"、"+I(r"\dfrac{\sin u}{u}\to1")+"。</p>"+D(r"\to%s\cdot%s\cdot1^2=%s"%(dn,L(R(a*a,4)),L(lim)) if a!=2 else r"\to%s\cdot1^2=%s"%(dn,L(lim))))]
    return r"$\displaystyle\lim_{x\to0}\dfrac{1-\cos %sx}{%sx^2}$ を求めよ。"%(A,Bc),st,L(lim)
o=[b6(*v) for v in [(2,1),(4,3),(3,2),(6,5),(1,1)]]
build(Z,CH,"(1−cos ax)/x² の極限",o,"<p>$1-\\cos t=2\\sin^2\\dfrac t2$ とし、$\\dfrac{\\sin u}{u}\\to1$ の形に整理。（$\\dfrac{1-\\cos x}{x^2}\\to\\dfrac12$ は公式として覚える。）</p>","1−cos は、sin の2乗にして基本形へ。",6)
# 7 (e^x - 1)/x 型
def b7(a,b):
    lim=sp.limit((sp.exp(a*x)-1)/(b*x),x,0); assert lim==R(a,b)
    st=[("基本極限","<p>"+I(r"\lim_{t\to0}\dfrac{e^t-1}{t}=1")+"。</p>"),
        ("形をそろえる","<p>"+D(r"\dfrac{e^{%dx}-1}{%dx}=\dfrac{%d}{%d}\cdot\dfrac{e^{%dx}-1}{%dx}"%(a,b,a,b,a,a))),
        ("極限","<p>"+I("t=%dx\\to0"%a)+" として "+I(r"\dfrac{e^t-1}{t}\to1")+"。</p>"+D(L(lim)))]
    return r"$\displaystyle\lim_{x\to0}\dfrac{e^{%dx}-1}{%dx}$ を求めよ。"%(a,b),st,L(lim)
o=[b7(*v) for v in [(3,2),(5,4),(2,7),(6,3),(4,5)]]
build(Z,CH,"(e^{ax}−1)/(bx) の極限",o,"<p>$\\dfrac{e^t-1}{t}\\to1$ と $t=ax$ のおきかえ。分母を $ax$ にそろえて外に $\\dfrac ab$ を出す。</p>","分母を指数と同じ形にそろえるのがコツ。",7)
# 8 中間値の定理
def b8(f,a,b):
    fa=f.subs(x,a);fb=f.subs(x,b); assert fa*fb<0
    def dr(ax):
        xs=np.linspace(a-.3,b+.3,300); curve(ax,f,(a-.3,b+.3)); ax.plot([a-.3,b+.3],[0,0],color="#333")
    fg=gplane("x313_8_%d"%(abs(hash(str(f)))%100000),(a-.5,b+.5),(-4,4),dr,size=(4.2,3),w=50) if False else ""
    st=[("連続関数","<p>"+I("f(x)=%s"%L(f))+" は連続。</p>"),
        ("端点の符号","<p>"+D(r"f(%s)=%s<0,\qquad f(%s)=%s>0"%(L(a),L(fa),L(b),L(fb)) if fa<0 else r"f(%s)=%s>0,\qquad f(%s)=%s<0"%(L(a),L(fa),L(b),L(fb)))),
        ("中間値の定理","<p>"+I("f(%s)f(%s)<0"%(L(a),L(b)))+" なので、"+I("%s<x<%s"%(L(a),L(b)))+" に "+I("f(x)=0")+" の実数解が少なくとも1つ存在する。</p>")]
    return r"方程式 $%s=0$ は、区間 $(%s,\ %s)$ に少なくとも1つの実数解をもつことを示せ。"%(L(f),L(a),L(b)),st,r"\text{証明終}"
o=[b8(*v) for v in [(x**3-3*x+1,0,1),(x**3+x-1,0,1),(sp.exp(x)-3*x,0,1) if False else (x**3-2*x-1,1,2),(sp.cos(x)-x,0,1),(sp.log(x)+x-2,1,2)]]
build(Z,CH,"中間値の定理で解の存在を示す",o,"<p>$f$ が区間で連続で、<b>端点で符号が異なる</b>（$f(a)f(b)<0$）なら、$f(x)=0$ の解が区間内に存在する。連続性にも触れる。</p>","谷から山へつながっていれば、ゼロの高さをどこかで通る。",8)
# 9 片側極限
def b9(a):
    f=(x**2-a*a)/abs(x-a)
    lp=sp.limit(f,x,a,'+'); lm=sp.limit(f,x,a,'-'); assert lp==2*a and lm==-2*a
    st=[("場合分け","<p>"+I("x>%d"%a)+" のとき "+I("|x-%d|=x-%d"%(a,a))+"、"+I("x<%d"%a)+" のとき "+I("|x-%d|=-(x-%d)"%(a,a))+"。</p>"),
        ("右側から","<p>"+D(r"\lim_{x\to%d{+}0}\dfrac{(x-%d)(x+%d)}{x-%d}=%d"%(a,a,a,a,2*a))),
        ("左側から","<p>"+D(r"\lim_{x\to%d{-}0}\dfrac{(x-%d)(x+%d)}{-(x-%d)}=-%d"%(a,a,a,a,2*a))+"<p>右側と左側が異なるので、極限は<b>存在しない</b>。</p>")]
    return r"$\displaystyle\lim_{x\to%d}\dfrac{x^2-%d}{|x-%d|}$ は存在するか。右側極限・左側極限を調べて答えよ。"%(a,a*a,a),st,r"\text{右側 }%d,\ \text{左側 }-%d\ \text{より極限は存在しない}"%(2*a,2*a)
o=[b9(a) for a in [1,2,3,4,5]]
build(Z,CH,"絶対値を含む関数の片側極限",o,"<p>絶対値は<b>$x>a$ と $x<a$ で場合分け</b>して外す。右側極限と左側極限が<b>一致すれば</b>極限が存在、異なれば存在しない。</p>","右から近づく値と左から近づく値が違えば、極限は決まらない。",9)
# 10 連続の条件（場合分け関数）
def b10(a,b):
    # f(x)= (x^2-a^2)/(x-a) for x!=a, = k at x=a ; continuous iff k=2a ; and another piece
    k=sp.symbols("k")
    # f(x)=(x^2+bx... ) use f(x) = (sqrt(x+b)-c)/(x-a) with c=sqrt(a+b)
    c=sp.sqrt(a+b); assert c.is_integer
    lim=sp.limit((sp.sqrt(x+b)-c)/(x-a),x,a); assert lim==R(1,2*c)
    st=[("連続の条件","<p>"+I("x=%d"%a)+" で連続 "+I(r"\iff \lim_{x\to%d}f(x)=f(%d)"%(a,a))+"。</p>"),
        ("極限を求める","<p>有理化：</p>"+D(r"\dfrac{\sqrt{x+%d}-%d}{x-%d}=\dfrac{(x+%d)-%d}{(x-%d)(\sqrt{x+%d}+%d)}=\dfrac{1}{\sqrt{x+%d}+%d}\to\dfrac1{%d}"%(b,c,a,b,a+b,a,b,c,b,c,2*c))),
        ("定数","<p>"+D(r"k=%s"%L(lim)))]
    return r"関数 $f(x)=\begin{cases}\dfrac{\sqrt{x+%d}-%d}{x-%d}&(x\neq%d)\\ k&(x=%d)\end{cases}$ が $x=%d$ で連続となるような定数 $k$ の値を求めよ。"%(b,c,a,a,a,a),st,r"k=%s"%L(lim)
o=[b10(*v) for v in [(3,1),(5,4),(2,2),(6,3),(7,2)]]
build(Z,CH,"場合分けの関数が連続となる定数",o,"<p>$x=a$ で連続 $\\iff \\lim_{x\\to a}f(x)=f(a)$。$x\\ne a$ の式の極限（有理化など）を求め、$f(a)=k$ と等しくおく。</p>","穴のあいた所を、極限の値でうめれば連続になる。",10)
XU=finishx(Z,CH)
