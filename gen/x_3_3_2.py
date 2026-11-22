# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational;
def co(c): return "" if c==1 else L(c)
def EX(c): return "e" if c==1 else "e^{%s}"%L(c)
def EXx(c): return "e^{x}" if c==1 else "e^{%dx}"%c
def EXm(c): return "e^{-x}" if c==1 else "e^{-%dx}"%c
x,y=sp.symbols("x y")
def shade(ax,f1,f2,a,b):
    xs=np.linspace(float(a),float(b),300); l1=sp.lambdify(x,f1,"numpy"); l2=sp.lambdify(x,f2,"numpy")
    ax.fill_between(xs,l1(xs)*np.ones_like(xs),l2(xs)*np.ones_like(xs),color="#f6c6cc",alpha=.8)
# 6 sin と cos で囲まれた面積
def b6(lo,hi):
    f1=sp.sin(x); f2=sp.cos(x); ar=sp.simplify(sp.integrate(f2-f1,(x,lo,hi)))
    def dr(ax):
        xs=np.linspace(-.3,2*np.pi,400); ax.plot(xs,np.sin(xs),color="#b81f36",lw=2); ax.plot(xs,np.cos(xs),color="#1f6fb8",lw=2)
        shade(ax,f1,f2,lo,hi)
    fg=gplane("x332_6_%d"%int(float(lo)*100),(-.5,2*np.pi),(-1.5,1.5),dr,size=(4.6,3),w=56,xs=np.pi/2,ys=1)
    st=[("交点を求める","<p>"+I(r"\sin x=\cos x")+" の両辺を "+I(r"\cos x")+" でわると "+I(r"\tan x=1")+"。"+I(r"0\leqq x\leqq2\pi")+" で "+I(r"x=\dfrac\pi4,\ \dfrac{5\pi}{4}")+"。"+fg),
        ("上下を確認する","<p>区間の中の値 "+I(r"x=\dfrac\pi2")+" で比べる。"+I(r"\sin\dfrac\pi2=1>\cos\dfrac\pi2=0")+" だから "+I(r"\dfrac\pi4\leqq x\leqq\dfrac{5\pi}4")+" で "+I(r"\sin x\geqq\cos x")+"。</p>"),
        ("面積の式を立てる",D(r"S=\int_{\pi/4}^{5\pi/4}(\sin x-\cos x)\,dx")),
        ("原始関数を求める","<p>"+I(r"\int\sin x\,dx=-\cos x")+"、"+I(r"\int\cos x\,dx=\sin x")+"。</p>"+D(r"\int(\sin x-\cos x)dx=-\cos x-\sin x")),
        ("上端 $x=\\dfrac{5\\pi}4$ を代入","<p>"+I(r"\cos\dfrac{5\pi}4=-\dfrac{\sqrt2}2,\ \sin\dfrac{5\pi}4=-\dfrac{\sqrt2}2")+"。</p>"+D(r"-\left(-\dfrac{\sqrt2}2\right)-\left(-\dfrac{\sqrt2}2\right)=\dfrac{\sqrt2}2+\dfrac{\sqrt2}2=\sqrt2")),
        ("下端 $x=\\dfrac\\pi4$ を代入","<p>"+I(r"\cos\dfrac\pi4=\sin\dfrac\pi4=\dfrac{\sqrt2}2")+"。</p>"+D(r"-\dfrac{\sqrt2}2-\dfrac{\sqrt2}2=-\sqrt2")),
        ("（上端）$-$（下端）",D(r"S=\sqrt2-(-\sqrt2)=2\sqrt2"))]
    return r"$0\leqq x\leqq2\pi$ において、曲線 $y=\sin x$ と $y=\cos x$ で囲まれる図形のうち、$\dfrac\pi4\leqq x\leqq\dfrac{5\pi}4$ の部分の面積を求めよ。",st,r"2\sqrt2"
o=[b6(sp.pi/4,5*sp.pi/4)]*5
o=[o[0]]
def b6b(k):
    # area between sin x and k sin x ... area under sin over [0,pi] =2 ; area between y=sin x and y=a sin x ...
    f=sp.sin(x); ar=2*(1-k)
    def dr(ax):
        xs=np.linspace(0,np.pi,300); ax.plot(xs,np.sin(xs),color="#b81f36",lw=2); ax.plot(xs,k*np.sin(xs),color="#1f6fb8",lw=2)
        shade(ax,f,k*f,0,np.pi)
    fg=gplane("x332_6b_%d"%int(k*10),(-.3,np.pi+.3),(-.2,1.3),dr,size=(4.4,3),w=52,xs=np.pi/2,ys=.5)
    st=[("上下を確認する","<p>"+I(r"0\leqq x\leqq\pi")+" では "+I(r"\sin x\geqq0")+" で、"+I(r"%s<1"%L(k))+" だから "+I(r"\sin x\geqq%s\sin x"%L(k))+"。上が "+I(r"y=\sin x")+"。</p>"+fg),
        ("面積の式を立てる","<p>"+D(r"S=\int_0^{\pi}\left(\sin x-%s\sin x\right)dx"%L(k))+"<p>"+I(r"\sin x")+" でくくる。</p>"+D(r"=\int_0^{\pi}(1-%s)\sin x\,dx=%s\int_0^{\pi}\sin x\,dx"%(L(k),L(1-k)))),
        ("原始関数を求める","<p>"+I(r"\int\sin x\,dx=-\cos x")+"。</p>"+D(r"%s\left[-\cos x\right]_0^{\pi}"%L(1-k))),
        ("端の値を代入する","<p>"+I(r"\cos\pi=-1,\ \cos0=1")+"。</p>"+D(r"\left[-\cos x\right]_0^{\pi}=(-\cos\pi)-(-\cos0)=1-(-1)=2")),
        ("計算する",D(r"S=%s\cdot2=%s"%(L(1-k),L(ar))))]
    return r"$0\leqq x\leqq\pi$ で、曲線 $y=\sin x$ と $y=%s\sin x$ で囲まれる図形の面積を求めよ。"%L(k),st,L(ar)
o=[o[0]]+[b6b(k) for k in [R(1,2),R(1,3),R(2,3),R(1,4)]]
build(Z,CH,"三角関数のグラフで囲まれた面積",o,"<p>交点・上下関係を確認し、<b>（上）$-$（下）</b>を積分。$\\int\\sin x=-\\cos x$ を使う。</p>","2本の波に挟まれた形の面積を、積分で。",6)
# 7 x軸まわりの回転体 sin
def b7(a):
    f=sp.sin(a*x); V=sp.pi*sp.integrate(f**2,(x,0,sp.pi/a)); 
    def dr(ax):
        xs=np.linspace(0,np.pi/a,300); ax.fill_between(xs,np.sin(a*xs),0,color="#f6c6cc"); ax.plot(xs,np.sin(a*xs),color="#b81f36",lw=2)
    fg=gplane("x332_7_%d"%a,(-.3,np.pi/a+.3),(-.4,1.4),dr,size=(4.4,3),w=52,xs=np.pi/(2*a),ys=.5)
    sa=r"\sin %sx"%co(a); s2=r"\sin %dx"%(2*a); c2=r"\cos %dx"%(2*a); up=r"\pi" if a==1 else r"\dfrac\pi{%d}"%a
    st=[("体積の公式","<p>$x$ 軸のまわりの回転体は、断面が半径 "+I("y")+" の円板。</p>"+D(r"V=\pi\int_0^{%s}y^2dx=\pi\int_0^{%s}\sin^2%sx\,dx"%(up,up,co(a)))+fg),
        ("半角の公式で次数を下げる","<p>"+I(r"\sin^2\theta=\dfrac{1-\cos2\theta}{2}")+" で "+I(r"\theta=%sx"%co(a))+" とする。</p>"+D(r"\sin^2%sx=\dfrac{1-%s}{2}"%(co(a),c2))+D(r"V=\pi\int_0^{%s}\dfrac{1-%s}{2}dx=\dfrac\pi2\int_0^{%s}(1-%s)\,dx"%(up,c2,up,c2))),
        ("原始関数を求める","<p>"+I(r"\int1\,dx=x")+"、"+I(r"\int%s\,dx=\dfrac{%s}{%d}"%(c2,s2,2*a))+"（"+I(r"(%s)'=%d%s"%(s2,2*a,c2))+" だから）。</p>"+D(r"\dfrac\pi2\left[x-\dfrac{%s}{%d}\right]_0^{%s}"%(s2,2*a,up))),
        ("端の値を代入する","<p>"+I(r"\sin%s=0"%(r"2\pi" if a>=1 else ""))+"、"+I(r"\sin0=0")+"。</p>"+D(r"\left[x-\dfrac{%s}{%d}\right]_0^{%s}=\left(%s-\dfrac{\sin2\pi}{%d}\right)-\left(0-\dfrac{\sin0}{%d}\right)=%s"%(s2,2*a,up,up,2*a,2*a,up))),
        ("計算する",D(r"V=\dfrac\pi2\cdot%s=%s"%(up,L(sp.simplify(V)))))]
    return r"曲線 $y=\sin %sx\ \left(0\leqq x\leqq%s\right)$ と $x$ 軸で囲まれた図形を $x$ 軸のまわりに1回転してできる立体の体積を求めよ。"%(co(a),up),st,L(sp.simplify(V))
o=[b7(a) for a in [1,2,3,4,5]]
build(Z,CH,"sin ax の回転体の体積",o,"<p>$V=\\pi\\int y^2dx$。$\\sin^2\\theta=\\dfrac{1-\\cos2\\theta}{2}$ で次数を下げて積分する。</p>","薄い円板を積み重ねた体積。",7)
# 8 y 軸まわりの回転（円筒）
def b8(a):
    # y=x^2 (0<=x<=a), rotate about y-axis: V=pi∫_0^{a^2} y dy = pi a^4/2
    V=sp.pi*a**4/2
    def dr(ax):
        xs=np.linspace(0,a,200); ax.plot(xs,xs**2,color="#b81f36",lw=2); ax.fill_between(xs,xs**2,a*a,color="#f6c6cc")
    fg=gplane("x332_8_%d"%a,(-.5,a+.5),(-.5,a*a+.8),dr,size=(4.2,3),w=50)
    st=[("断面を考える","<p>"+I("y")+" を決めたときの断面は、半径 "+I("x")+" の円板。"+I(r"y=x^2")+" より "+I(r"x^2=y")+"。</p>"+fg),
        ("体積の式を立てる","<p>"+I("y")+" の範囲は "+I(r"0")+" から "+I(str(a*a))+" まで。</p>"+D(r"V=\pi\int_0^{%d}x^2\,dy=\pi\int_0^{%d}y\,dy"%(a*a,a*a))),
        ("原始関数を求める",D(r"\int y\,dy=\dfrac{y^2}{2}")+D(r"V=\pi\left[\dfrac{y^2}{2}\right]_0^{%d}"%(a*a))),
        ("端の値を代入する",D(r"\pi\left(\dfrac{%d^2}{2}-\dfrac{0^2}{2}\right)=\pi\cdot\dfrac{%d}{2}=%s"%(a*a,a**4,L(V))))]
    return r"曲線 $y=x^2\ (0\leqq x\leqq%d)$ と直線 $y=%d$、$y$ 軸で囲まれた図形を $y$ 軸のまわりに1回転してできる立体の体積を求めよ。"%(a,a*a),st,L(V)
o=[b8(a) for a in [2,3,4,1,5]]
build(Z,CH,"y 軸まわりの回転体（放物線）",o,"<p>$y$ 軸まわりは<b>$y$ について積分</b>：$V=\\pi\\int x^2\\,dy$。$x^2$ を $y$ で表して代入する。</p>","y を決めた輪切りが、半径 x の円板。",8)
# 9 曲線の長さ
def b9(a):
    # y = (e^{ax}+e^{-ax})/(2a) catenary: ds = cosh(a x) ; length 0..1 = sinh(a)/a
    f=(sp.exp(a*x)+sp.exp(-a*x))/(2*a); fp=sp.diff(f,x); integrand=sp.simplify(sp.sqrt(1+fp**2)); 
    L1=sp.simplify(sp.integrate((sp.exp(a*x)+sp.exp(-a*x))/2,(x,0,1)))
    ep=EXx(a); em=EXm(a); Ea=EX(a); Eam=EX(-a)
    st=[("導関数を求める","<p>"+I(r"(%s)'=%s,\ (%s)'=-%s"%(ep,(co(a)+ep) if a!=1 else ep,em,(co(a)+em) if a!=1 else em))+"。</p>"+D(r"y'=\dfrac{%s\left(%s-%s\right)}{%s}=\dfrac{%s-%s}{2}"%(L(a),ep,em,L(2*a),ep,em) if a!=1 else r"y'=\dfrac{%s-%s}{2}"%(ep,em))),
        ("$1+y'^2$ を計算する","<p>"+D(r"y'^2=\dfrac{\left(%s\right)^2-2%s%s+\left(%s\right)^2}{4}=\dfrac{e^{%sx}-2+e^{-%sx}}{4}"%(ep,ep,em,em,L(2*a) if a!=0 else "",L(2*a))+"")+D(r"1+y'^2=\dfrac{4+e^{%sx}-2+e^{-%sx}}{4}=\dfrac{e^{%sx}+2+e^{-%sx}}{4}=\left(\dfrac{%s+%s}{2}\right)^2"%(L(2*a),L(2*a),L(2*a),L(2*a),ep,em))),
        ("根号をはずす","<p>"+I(r"%s+%s>0"%(ep,em))+" だから、</p>"+D(r"\sqrt{1+y'^2}=\dfrac{%s+%s}{2}"%(ep,em))),
        ("曲線の長さの式を立てる",D(r"L=\int_0^1\sqrt{1+y'^2}\,dx=\int_0^1\dfrac{%s+%s}{2}dx"%(ep,em))),
        ("原始関数を求める","<p>"+I(r"\int %s\,dx=%s"%(ep,(r"\dfrac{%s}{%d}"%(ep,a)) if a!=1 else ep))+"、"+I(r"\int %s\,dx=%s"%(em,(r"-\dfrac{%s}{%d}"%(em,a)) if a!=1 else "-"+em))+"。</p>"+D(r"\dfrac12\left[%s\right]_0^1"%((r"\dfrac{%s}{%d}-\dfrac{%s}{%d}"%(ep,a,em,a)) if a!=1 else r"%s-%s"%(ep,em)))),
        ("端の値を代入する","<p>"+I(r"e^0=1")+"、上端と下端の差をとる。</p>"+D(r"L=\dfrac12\left\{\dfrac{%s-%s}{%s}-\dfrac{1-1}{%s}\right\}=\dfrac{%s-%s}{%s}"%(Ea,Eam,L(a),L(a),Ea,Eam,L(2*a)) if a!=1 else r"L=\dfrac12\left\{(e-e^{-1})-(1-1)\right\}=\dfrac{e-e^{-1}}{2}"))]
    return r"曲線 $y=\dfrac{%s+%s}{%s}\ (0\leqq x\leqq1)$ の長さを求めよ。"%(EXx(a),EXm(a),L(2*a)),st,(r"\dfrac{%s-%s}{%s}"%(EX(a),EX(-a),L(2*a)))
o=[b9(a) for a in [1,2,3,4,5]]
build(Z,CH,"懸垂線の長さ",o,"<p>曲線の長さ $=\\int\\sqrt{1+(y')^2}\\,dx$。$1+y'^2$ が完全平方になる曲線（懸垂線）では根号がはずれる。</p>","ひもが垂れ下がった形。長さは積分で正確に出せる。",9)
# 10 媒介変数の面積
def b10(a):
    # x=a(t-sin t), y=a(1-cos t), 0<=t<=2pi : area = 3 pi a^2
    A=3*sp.pi*a*a
    def dr(ax):
        tt=np.linspace(0,2*np.pi,400); ax.plot(a*(tt-np.sin(tt)),a*(1-np.cos(tt)),color="#b81f36",lw=2); ax.fill_between(a*(tt-np.sin(tt)),a*(1-np.cos(tt)),0,color="#f6c6cc")
    fg=gplane("x332_10_%d"%a,(-.5*a,2*np.pi*a+.5*a),(-.3*a,2.4*a),dr,size=(4.6,2.8),w=56)
    A_=co(a)
    st=[("$dx$ を $t$ で表す","<p>"+I(r"\dfrac{dx}{dt}=%s(1-\cos t)"%A_)+"。</p>"+D(r"dx=%s(1-\cos t)\,dt"%A_)+"<p>"+I(r"t:0\to2\pi")+" のとき "+I(r"x:0\to%s\pi"%L(2*a) if a!=1 else r"x:0\to2\pi")+"。</p>"+fg),
        ("面積の式を立てる",D(r"S=\int y\,dx=\int_0^{2\pi}%s(1-\cos t)\cdot%s(1-\cos t)\,dt=%s\int_0^{2\pi}(1-\cos t)^2dt"%(A_,A_,L(a*a) if a!=1 else ""))),
        ("展開する","<p>"+D(r"(1-\cos t)^2=1-2\cos t+\cos^2t")+"<p>"+I(r"\cos^2t=\dfrac{1+\cos2t}{2}")+" で次数を下げる。</p>"+D(r"=1-2\cos t+\dfrac{1+\cos2t}{2}=\dfrac32-2\cos t+\dfrac{\cos2t}{2}")),
        ("原始関数を求める",D(r"\int\left(\dfrac32-2\cos t+\dfrac{\cos2t}{2}\right)dt=\dfrac32t-2\sin t+\dfrac{\sin2t}{4}")),
        ("端の値を代入する","<p>"+I(r"\sin2\pi=\sin0=0")+" だから、"+I(r"\sin")+" の項は消える。</p>"+D(r"\left[\dfrac32t-2\sin t+\dfrac{\sin2t}{4}\right]_0^{2\pi}=\dfrac32\cdot2\pi-0=3\pi")),
        ("係数をかける",D((r"S=%s\cdot3\pi=%s"%(L(a*a),L(A))) if a!=1 else r"S=3\pi"))]
    return r"サイクロイド $x=%s(t-\sin t),\ y=%s(1-\cos t)\ (0\leqq t\leqq2\pi)$ と $x$ 軸で囲まれた図形の面積を求めよ。"%(A_,A_),st,L(A)
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"サイクロイドが囲む面積",o,"<p>媒介変数の面積は $S=\\int y\\,dx=\\int y\\dfrac{dx}{dt}dt$。$x:0\\to2\\pi a$ に対応する $t:0\\to2\\pi$。</p>","車輪の一点がえがく曲線の下の面積は、円の3倍。",10)
XU=finishx(Z,CH)
