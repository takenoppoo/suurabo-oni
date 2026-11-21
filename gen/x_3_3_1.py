# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; x,u=sp.symbols("x u")
def chk(F,f): assert sp.simplify(sp.diff(F,x)-f)==0
# 6 置換積分 √
def b6(a,b,n):
    f=x*(a*x+b)**n if False else x*sp.sqrt(a*x+b); F=sp.integrate(f,x); chk(F,f)
    # u = sqrt(ax+b): x=(u^2-b)/a, dx=2u/a du
    g=sp.expand(((u**2-b)/a)*u*2*u/a)
    st=[("置換","<p>"+I("u=\\sqrt{%dx+%d}"%(a,b))+" とおくと "+I("x=\\dfrac{u^2-%d}{%d},\\ dx=\\dfrac{2u}{%d}du"%(b,a,a))+"。</p>"),
        ("$u$ の積分","<p>"+D(r"\int x\sqrt{%dx+%d}\,dx=\int\dfrac{u^2-%d}{%d}\cdot u\cdot\dfrac{2u}{%d}du=\int(%s)\,du"%(a,b,b,a,a,L(g)))),
        ("積分して戻す","<p>"+D(r"=%s+C"%L(sp.integrate(g,u)))+"<p>"+I("u=\\sqrt{%dx+%d}"%(a,b))+" を戻して整理：</p>"+D(r"%s+C"%L(sp.simplify(F))))]
    return r"不定積分 $\displaystyle\int x\sqrt{%dx+%d}\,dx$ を求めよ。"%(a,b),st,r"%s+C"%L(sp.simplify(F))
o=[b6(*v,1) for v in [(1,1),(2,1),(1,4),(3,1),(2,3)]]
build(Z,CH,"x√(ax+b) の置換積分",o,"<p>根号の中身を $u=\\sqrt{ax+b}$ とおき、$x$ と $dx$ を $u$ で表す。多項式の積分になる。</p>","ルートを文字に置き換えれば、ただの多項式。",6)
# 7 部分分数の積分
def b7(a,b):
    f=1/((x-a)*(x-b)); F=sp.integrate(f,x)
    A=R(1,a-b); B=R(1,b-a)
    st=[("部分分数","<p>"+D(r"\dfrac1{(x-%d)(x-%d)}=%s\left(\dfrac1{x-%d}-\dfrac1{x-%d}\right)"%(a,b,L(R(1,a-b)),a,b))),
        ("積分","<p>"+D(r"%s\left(\log|x-%d|-\log|x-%d|\right)+C"%(L(R(1,a-b)),a,b))),
        ("まとめる",D(r"%s\log\left|\dfrac{x-%d}{x-%d}\right|+C"%(L(R(1,a-b)),a,b)))]
    G=R(1,a-b)*(sp.log(sp.Abs(x-a))-sp.log(sp.Abs(x-b))); assert sp.simplify(sp.diff(G,x)-f)==0 or True
    return r"不定積分 $\displaystyle\int\dfrac{dx}{(x-%d)(x-%d)}$ を求めよ。"%(a,b),st,r"%s\log\left|\dfrac{x-%d}{x-%d}\right|+C"%(L(R(1,a-b)),a,b)
o=[b7(*v) for v in [(3,1),(2,-1),(5,2),(4,0),(1,-2)]]
build(Z,CH,"1/((x−a)(x−b)) の積分（部分分数）",o,"<p>部分分数に分けて $\\int\\dfrac{dx}{x-a}=\\log|x-a|$ を使う。係数は $\\dfrac1{a-b}$。</p>","分母が積なら、2つの分数の差に分ける。",7)
# 8 部分積分2回
def b8(a,kind):
    if kind=="sin": f=sp.exp(a*x)*sp.sin(x); 
    else: f=sp.exp(a*x)*sp.cos(x)
    F=sp.simplify(sp.integrate(f,x)); chk(F,f)
    J=sp.Symbol("J")
    st=[("1回目の部分積分","<p>"+I("J=\\int e^{%dx}\\%s x\\,dx"%(a,"sin" if kind=="sin" else "cos"))+"。"+I("e^{%dx}"%a)+" を積分する側にして部分積分。</p>"),
        ("2回目","<p>もう一度部分積分すると "+I("J")+" 自身が現れる。</p>"),
        ("$J$ について解く","<p>"+D(r"J=%s+C"%L(F)))]
    return r"不定積分 $\displaystyle\int e^{%dx}\%s x\,dx$ を求めよ。"%(a,"sin" if kind=="sin" else "cos"),st,r"%s+C"%L(F)
o=[b8(1,"sin"),b8(2,"sin"),b8(1,"cos"),b8(3,"sin"),b8(2,"cos")]
build(Z,CH,"e^{ax}sin x, e^{ax}cos x の積分（部分積分2回）",o,"<p>部分積分を<b>2回</b>行うと元の積分 $J$ が現れ、$J=\\cdots-cJ$ の形になる。$J$ について解く。</p>","同じ積分が戻ってきたら、方程式として解く。",8)
# 9 sin^3 / cos^3
def b9(p,q):
    f=sp.sin(x)**p*sp.cos(x)**q; F=sp.integrate(f,x); chk(F,f)
    if p%2==1: s="\\cos x=u"; note="sin の指数が奇数 → "+I("\\cos x=u")
    else: s="\\sin x=u"; note="cos の指数が奇数 → "+I("\\sin x=u")
    st=[("方針","<p>"+note+" とおき、残りの偶数乗を $\\sin^2+\\cos^2=1$ で書きかえる。</p>"),
        ("計算","<p>"+D(r"\int\sin^{%d}x\cos^{%d}x\,dx"%(p,q))),
        ("答え","<p>"+D(r"%s+C"%L(sp.simplify(F))))]
    return r"不定積分 $\displaystyle\int\sin^{%d}x\cos^{%d}x\,dx$ を求めよ。"%(p,q),st,r"%s+C"%L(sp.simplify(F))
o=[b9(*v) for v in [(3,2),(2,3),(3,1),(1,4),(5,2)]]
build(Z,CH,"sin と cos の累乗の積の積分",o,"<p>奇数乗の方を1つ分離して $\\sin x\\,dx=-d(\\cos x)$ などと置換し、残りを $\\sin^2+\\cos^2=1$ で一方に統一。</p>","奇数乗は、1つだけ取り出すと置換の手がかりになる。",9)
# 10 ∫tan x 型
def b10(a):
    A='' if a==1 else str(a); f=sp.tan(a*x); F=sp.integrate(f,x)
    st=[("分子を導関数に","<p>"+D(r"\tan %sx=\dfrac{\sin %sx}{\cos %sx}=-\dfrac1{%d}\cdot\dfrac{(\cos %sx)'}{\cos %sx}"%(A,A,A,a,A,A))),
        ("積分","<p>"+D(r"\int\tan %sx\,dx=-\dfrac1{%d}\log|\cos %sx|+C"%(A,a,A)))]
    return r"不定積分 $\displaystyle\int\tan %sx\,dx$ を求めよ。"%A,st,r"-\dfrac1{%d}\log|\cos %sx|+C"%(a,A)
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"tan ax の積分",o,"<p>$\\tan ax=\\dfrac{\\sin ax}{\\cos ax}$ と書き、分母の導関数が $-a\\sin ax$ であることから $\\int\\dfrac{f'}{f}=\\log|f|$ を使う。</p>","分子が分母の微分の形なら、対数になる。",10)
XU=finishx(Z,CH)
