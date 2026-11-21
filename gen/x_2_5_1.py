# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,k,t=sp.symbols("x k t")
# 6 解の個数
def b6(a,b):
    # x^3-3a x + ... f(x)=x^3-3a^2... choose f=x^3 - 3 a x^2? use f = x^3-3x^2*? simple: x^3 - 3 a x = k
    f=x**3-3*a*x; fp=sp.diff(f,x); r=sp.sqrt(a); mx=f.subs(x,-r); mn=f.subs(x,r)
    kk=[sp.Integer(b)]
    def dr(ax):
        xs=np.linspace(-3,3,300); ax.plot(xs,xs**3-3*a*xs,color="#b81f36",lw=2)
        ax.plot([-3,3],[b,b],color="#1f6fb8",ls="--"); mark(ax,-float(r),float(mx),"",0,0); mark(ax,float(r),float(mn))
    fg=gplane("x251_6_%d_%d"%(a,b+30),(-3.2,3.2),(-14,14),dr,size=(4.4,3.2),w=54,ys=4)
    # count solutions
    cnt=len(set(sp.Poly(f-b,x).nroots(n=15,maxsteps=200)) if False else [rr for rr in np.roots([1,0,-3*a,-b]) if abs(rr.imag)<1e-9 and True]) 
    rts=np.roots([1,0,-3*a,-b]); real=sorted({round(rr.real,6) for rr in rts if abs(rr.imag)<1e-7}); n=len(real)
    st=[("定数を分離","<p>"+I("x^3-%dx=k"%(3*a) if True else "")+" の実数解は、"+I("y=x^3-%dx"%(3*a))+" と "+I("y=k")+" の共有点の個数。</p>"),
        ("増減","<p>"+D(r"y'=3x^2-%d=0\ \Rightarrow\ x=\pm%s"%(3*a,L(r)))+"<p>極大値 "+I(L(mx))+"、極小値 "+I(L(mn))+"。</p>"+fg),
        ("個数","<p>"+I("k=%d"%b)+" のとき "+I(str(n))+" 個。</p>")]
    return r"方程式 $x^3-%dx=%d$ の異なる実数解の個数を求めよ。"%(3*a,b),st,str(n)
o=[b6(*v) for v in [(1,1),(1,2),(1,3),(4,10),(4,16)]]
# also one with k=-2 etc ok
build(Z,CH,"3次方程式の実数解の個数（定数分離）",o,"<p>定数 $k$ を<b>右辺に分離</b>し、$y=f(x)$ のグラフと水平線 $y=k$ の共有点を数える。極大値・極小値との大小で個数が決まる。</p>","グラフに水平線を引いて、何か所で交わるか数える。",6)
# 7 極値をもつ条件
def b7(a):
    # f=x^3+ a x^2 + 3a x +1 : f'=3x^2+2a x+3a ; D>0 -> a<0 or a>9/4? compute
    f=x**3+a*x**2+k*x if False else None
    return None
def b7(m):
    # f=x^3 + k x^2 + m x + 1 ; f' = 3x^2+2kx+m ; extreme iff D=4k^2-12m>0 -> k^2>3m
    r=sp.solve(k*k-3*m,k); 
    st=[("導関数","<p>"+D(r"f'(x)=3x^2+2kx+%d"%m)+"<p>極値をもつ $\\iff f'(x)=0$ が<b>異なる2つの実数解</b>をもつ（符号が変わる）。</p>"),
        ("判別式","<p>"+D(r"\dfrac D4=k^2-3\cdot%d=k^2-%d>0"%(m,3*m))),
        ("答え",D(r"k<%s,\ \ k>%s"%(L(min(r)),L(max(r)))))] if m>0 else None
    return r"関数 $f(x)=x^3+kx^2+%dx+1$ が極値をもつような定数 $k$ の値の範囲を求めよ。"%m,st,r"k<%s,\ k>%s"%(L(min(r)),L(max(r)))
o=[b7(m) for m in [3,12,12,27,6]]
o=[b7(m) for m in [3,12,6,27,9]]
build(Z,CH,"3次関数が極値をもつ条件",o,"<p>極値をもつ $\\iff f'(x)=0$ が<b>異なる2つの実数解</b> $\\iff D>0$。（$D=0$ の重解では符号が変わらず極値なし。）</p>","導関数の符号が変わる場所が極値。",7)
# 8 共通接線
def b8(a,b,c):
    # y=x^2 and y=-(x-a)^2 + b? common tangent: tangent to y=x^2 at t: y=2t x - t^2; tangent to y=-x^2+c... find t
    # curves y=x^2 , y=-x^2+4x+c0 : common tangent
    t,u=sp.symbols("t u")
    # tangent of C1 at t: y=2t x - t^2 ; C2: y=-x^2+4x+c at u: slope -2u+4 ; y=(-2u+4)x+u^2+c
    sol=sp.solve([2*t-(-2*u+4),-t*t-(u*u+c)],[t,u],dict=True)
    lines=[sp.expand(2*s_[t]*x-s_[t]**2) for s_ in sol]
    # verify tangency
    for L_ in lines:
        assert sp.discriminant(sp.expand(L_-x**2),x)==0 and sp.discriminant(sp.expand(L_-(-x**2+4*x+c)),x)==0
    xs_=np.linspace(-2,6,300)
    def dr(ax):
        ax.plot(xs_,xs_**2,color="#b81f36",lw=2); ax.plot(xs_,-xs_**2+4*xs_+c,color="#1f6fb8",lw=2)
        for L_ in lines: ax.plot(xs_,[float(L_.subs(x,v)) for v in xs_],color="#333",ls="--",lw=1)
    fg=gplane("x251_8_%d"%(c+20),(-2,6),(-12,16),dr,size=(4.4,3.2),w=54,ys=4)
    st=[("接線を一般に","<p>"+I("y=x^2")+" の点 "+I("(t,t^2)")+" での接線 "+I("y=2tx-t^2")+"。</p>"+fg),
        ("もう一方にも接する","<p>"+I("y=-x^2+4x%+d"%c)+" の点 "+I("u")+" での接線 "+I("y=(-2u+4)x+u^2%+d"%c)+"。係数を比べて</p>"+D(r"2t=-2u+4,\qquad -t^2=u^2%+d"%c)),
        ("解く","<p>"+D(r"\text{接線：}\quad %s"%(r",\quad ".join("y=%s"%L(l_) for l_ in lines))))]
    return r"2つの放物線 $y=x^2$ と $y=-x^2+4x%+d$ の共通接線の方程式をすべて求めよ。"%c,st,r"%s"%(r",\ ".join("y=%s"%L(l_) for l_ in lines))
o=[b8(*v) for v in [(0,0,-2),(0,0,-6),(0,0,-10) if False else (0,0,-4),(0,0,-12) if False else (0,0,-8),(0,0,-14) if False else (0,0,-16)]]
build(Z,CH,"2つの放物線の共通接線",o,"<p>それぞれの曲線上の接点を文字でおき、<b>接線の傾きと切片が一致</b>する条件を連立。または接線を求めて、もう一方と<b>重解（$D=0$）</b>。</p>","同じ直線が、2つの曲線に同時に触れる。",8)
# 9 箱の体積の最大
def b9(a):
    # square sheet a x a, cut x from corners: V=x(a-2x)^2 ; max at x=a/6
    V=x*(a-2*x)**2; xm=R(a,6); mx=V.subs(x,xm)
    def dr(ax):
        xs=np.linspace(0,a/2,300); ax.plot(xs,xs*(a-2*xs)**2,color="#b81f36",lw=2); mark(ax,float(xm),float(mx),"",0,0)
    fg=gplane("x251_9_%d"%a,(-.5,a/2+.5),(-.1*float(mx),1.3*float(mx)),dr,size=(4.4,3),w=52,xs=a/6,ys=float(mx)/3)
    st=[("体積の式","<p>"+I("0<x<%s"%L(R(a,2)))+"。</p>"+D(r"V=x(%d-2x)^2=%s"%(a,L(sp.expand(V))))),
        ("増減","<p>"+D(r"V'=%s=%s"%(L(sp.expand(sp.diff(V,x))),L(sp.factor(sp.diff(V,x)))))+"<p>"+I("V'=0")+" より "+I("x=%s,\\ %s"%(L(xm),L(R(a,2))))+"。範囲内は "+I("x=%s"%L(xm))+"。</p>"+fg),
        ("最大値",D(r"V(%s)=%s"%(L(xm),L(mx))))]
    return r"1辺 $%d$ cm の正方形の厚紙の四隅から、1辺 $x$ cm の正方形を切り取って折り曲げ、ふたのない箱を作る。体積が最大となる $x$ と、そのときの体積を求めよ。"%a,st,r"x=%s,\ V=%s"%(L(xm),L(mx))
o=[b9(a) for a in [12,18,24,30,6]]
build(Z,CH,"箱の体積の最大（微分の応用）",o,"<p>変数 $x$ の範囲を確認し、体積を $x$ の3次関数で表す。<b>微分して増減表</b>をかき、範囲内の極大値が最大値。</p>","条件をそのまま式にして、微分で山の頂上を探す。",9)
# 10 不等式の証明
def b10(a):
    # x^3 - 3 a^2 x + 2 a^3 >= 0 for x>=0 : f' =3x^2-3a^2 ; min at x=a: f(a)=0
    f=x**3-3*a*a*x+2*a**3
    assert sp.factor(f)==(x-a)**2*(x+2*a)
    def dr(ax):
        xs=np.linspace(0,3*a,300); ax.plot(xs,xs**3-3*a*a*xs+2*a**3,color="#b81f36",lw=2); mark(ax,a,0,"",0,0)
    fg=gplane("x251_10_%d"%a,(-.5,3*a),(-3*a**3,10*a**3),dr,size=(4.4,3),w=52,xs=a,ys=2*a**3)
    st=[("差を関数に","<p>"+I("f(x)=%s"%L(f))+" とおき、"+I("x\\geqq0")+" で "+I("f(x)\\geqq0")+" を示す。</p>"),
        ("増減","<p>"+D(r"f'(x)=%s=%s"%(L(sp.diff(f,x)),L(sp.factor(sp.diff(f,x)))))+"<p>"+I("x\\geqq0")+" で "+I("x=%d"%a)+" が極小。</p>"+fg),
        ("最小値","<p>"+D(r"f(%d)=%d\ \Rightarrow\ f(x)\geqq0"%(a,f.subs(x,a)))+"<p>等号は "+I("x=%d"%a)+"。</p>")]
    return r"$x\geqq0$ のとき、不等式 $x^3+%d\geqq%dx$ を証明せよ。"%(2*a**3,3*a*a),st,r"\text{証明終}"
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"不等式の証明（最小値を調べる）",o,"<p>（左辺）$-$（右辺）$=f(x)$ とおき、<b>$f(x)$ の最小値が $0$ 以上</b>であることを増減表で示す。</p>","差の関数の一番低いところが0以上なら、常に成り立つ。",10)
XU=finishx(Z,CH)
