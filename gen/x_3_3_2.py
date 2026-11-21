# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,y=sp.symbols("x y")
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
    st=[("交点","<p>"+I(r"\sin x=\cos x")+" より "+I(r"x=\dfrac\pi4,\ \dfrac{5\pi}{4}")+"。"+fg),
        ("上下","<p>"+I(r"\dfrac\pi4\leqq x\leqq\dfrac{5\pi}4")+" で "+I(r"\sin x\geqq\cos x")+"。</p>"),
        ("積分","<p>"+D(r"\int_{\pi/4}^{5\pi/4}(\sin x-\cos x)dx=\left[-\cos x-\sin x\right]_{\pi/4}^{5\pi/4}=2\sqrt2"))]
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
    st=[("上下の関係","<p>"+I(r"0\leqq x\leqq\pi")+" で "+I(r"\sin x\geqq%s\sin x"%L(k))+"。</p>"+fg),
        ("積分","<p>"+D(r"\int_0^{\pi}(1-%s)\sin x\,dx=%s\left[-\cos x\right]_0^{\pi}=%s\cdot2=%s"%(L(k),L(1-k),L(1-k),L(ar))))]
    return r"$0\leqq x\leqq\pi$ で、曲線 $y=\sin x$ と $y=%s\sin x$ で囲まれる図形の面積を求めよ。"%L(k),st,L(ar)
o=[o[0]]+[b6b(k) for k in [R(1,2),R(1,3),R(2,3),R(1,4)]]
build(Z,CH,"三角関数のグラフで囲まれた面積",o,"<p>交点・上下関係を確認し、<b>（上）$-$（下）</b>を積分。$\\int\\sin x=-\\cos x$ を使う。</p>","2本の波に挟まれた形の面積を、積分で。",6)
# 7 x軸まわりの回転体 sin
def b7(a):
    f=sp.sin(a*x); V=sp.pi*sp.integrate(f**2,(x,0,sp.pi/a)); 
    def dr(ax):
        xs=np.linspace(0,np.pi/a,300); ax.fill_between(xs,np.sin(a*xs),0,color="#f6c6cc"); ax.plot(xs,np.sin(a*xs),color="#b81f36",lw=2)
    fg=gplane("x332_7_%d"%a,(-.3,np.pi/a+.3),(-.4,1.4),dr,size=(4.4,3),w=52,xs=np.pi/(2*a),ys=.5)
    st=[("体積の公式","<p>"+D(r"V=\pi\int_0^{\pi/%d}y^2dx=\pi\int_0^{\pi/%d}\sin^2%dx\,dx"%(a,a,a))+fg),
        ("半角の公式","<p>"+D(r"\sin^2%dx=\dfrac{1-\cos%dx}{2}"%(a,2*a))),
        ("計算","<p>"+D(r"V=\dfrac\pi2\left[x-\dfrac{\sin%dx}{%d}\right]_0^{\pi/%d}=%s"%(2*a,2*a,a,L(sp.simplify(V)))))]
    return r"曲線 $y=\sin%dx\ \left(0\leqq x\leqq\dfrac{\pi}{%d}\right)$ と $x$ 軸で囲まれた図形を $x$ 軸のまわりに1回転してできる立体の体積を求めよ。"%(a,a),st,L(sp.simplify(V))
o=[b7(a) for a in [1,2,3,4,5]]
build(Z,CH,"sin ax の回転体の体積",o,"<p>$V=\\pi\\int y^2dx$。$\\sin^2\\theta=\\dfrac{1-\\cos2\\theta}{2}$ で次数を下げて積分する。</p>","薄い円板を積み重ねた体積。",7)
# 8 y 軸まわりの回転（円筒）
def b8(a):
    # y=x^2 (0<=x<=a), rotate about y-axis: V=pi∫_0^{a^2} y dy = pi a^4/2
    V=sp.pi*a**4/2
    def dr(ax):
        xs=np.linspace(0,a,200); ax.plot(xs,xs**2,color="#b81f36",lw=2); ax.fill_between(xs,xs**2,a*a,color="#f6c6cc")
    fg=gplane("x332_8_%d"%a,(-.5,a+.5),(-.5,a*a+.8),dr,size=(4.2,3),w=50)
    st=[("y 軸のまわり","<p>"+I("y")+" を決めたときの断面は円（半径 "+I("x=\\sqrt y")+"）。</p>"+D(r"V=\pi\int_0^{%d}x^2\,dy=\pi\int_0^{%d}y\,dy"%(a*a,a*a))+fg),
        ("計算","<p>"+D(r"\pi\left[\dfrac{y^2}{2}\right]_0^{%d}=%s"%(a*a,L(V)))+"<p>（放物線の内側・直線 "+I("y=%d"%(a*a))+" の下側を切り取る）。</p>")]
    return r"曲線 $y=x^2\ (0\leqq x\leqq%d)$ と直線 $y=%d$、$y$ 軸で囲まれた図形を $y$ 軸のまわりに1回転してできる立体の体積を求めよ。"%(a,a*a),st,L(V)
o=[b8(a) for a in [2,3,4,1,5]]
build(Z,CH,"y 軸まわりの回転体（放物線）",o,"<p>$y$ 軸まわりは<b>$y$ について積分</b>：$V=\\pi\\int x^2\\,dy$。$x^2$ を $y$ で表して代入する。</p>","y を決めた輪切りが、半径 x の円板。",8)
# 9 曲線の長さ
def b9(a):
    # y = (e^{ax}+e^{-ax})/(2a) catenary: ds = cosh(a x) ; length 0..1 = sinh(a)/a
    f=(sp.exp(a*x)+sp.exp(-a*x))/(2*a); fp=sp.diff(f,x); integrand=sp.simplify(sp.sqrt(1+fp**2)); 
    L1=sp.simplify(sp.integrate((sp.exp(a*x)+sp.exp(-a*x))/2,(x,0,1)))
    st=[("導関数","<p>"+D(r"y'=\dfrac{e^{%dx}-e^{-%dx}}{2}"%(a,a))),
        ("被積分関数","<p>"+D(r"1+y'^2=\left(\dfrac{e^{%dx}+e^{-%dx}}{2}\right)^2"%(a,a))+"<p>"+I(r"\sqrt{1+y'^2}=\dfrac{e^{%dx}+e^{-%dx}}{2}"%(a,a))+"。</p>"),
        ("曲線の長さ","<p>"+D(r"\int_0^{1}\dfrac{e^{%dx}+e^{-%dx}}{2}dx=\dfrac{e^{%d}-e^{-%d}}{2%d}=%s"%(a,a,a,a,a,L(L1))))]
    return r"曲線 $y=\dfrac{e^{%dx}+e^{-%dx}}{%d}\ (0\leqq x\leqq1)$ の長さを求めよ。"%(a,a,2*a),st,L(L1)
o=[b9(a) for a in [1,2,3,4,5]]
build(Z,CH,"懸垂線の長さ",o,"<p>曲線の長さ $=\\int\\sqrt{1+(y')^2}\\,dx$。$1+y'^2$ が完全平方になる曲線（懸垂線）では根号がはずれる。</p>","ひもが垂れ下がった形。長さは積分で正確に出せる。",9)
# 10 媒介変数の面積
def b10(a):
    # x=a(t-sin t), y=a(1-cos t), 0<=t<=2pi : area = 3 pi a^2
    A=3*sp.pi*a*a
    def dr(ax):
        tt=np.linspace(0,2*np.pi,400); ax.plot(a*(tt-np.sin(tt)),a*(1-np.cos(tt)),color="#b81f36",lw=2); ax.fill_between(a*(tt-np.sin(tt)),a*(1-np.cos(tt)),0,color="#f6c6cc")
    fg=gplane("x332_10_%d"%a,(-.5*a,2*np.pi*a+.5*a),(-.3*a,2.4*a),dr,size=(4.6,2.8),w=56)
    st=[("置換","<p>"+D(r"S=\int y\,dx=\int_0^{2\pi}%d(1-\cos t)\cdot%d(1-\cos t)\,dt"%(a,a))+fg),
        ("展開","<p>"+D(r"=%d\int_0^{2\pi}(1-2\cos t+\cos^2t)dt=%d\int_0^{2\pi}\left(\dfrac32-2\cos t+\dfrac{\cos2t}{2}\right)dt"%(a*a,a*a))),
        ("計算","<p>"+D(r"=%d\cdot\dfrac32\cdot2\pi=%s"%(a*a,L(A))))]
    return r"サイクロイド $x=%d(t-\sin t),\ y=%d(1-\cos t)\ (0\leqq t\leqq2\pi)$ と $x$ 軸で囲まれた図形の面積を求めよ。"%(a,a),st,L(A)
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"サイクロイドが囲む面積",o,"<p>媒介変数の面積は $S=\\int y\\,dx=\\int y\\dfrac{dx}{dt}dt$。$x:0\\to2\\pi a$ に対応する $t:0\\to2\\pi$。</p>","車輪の一点がえがく曲線の下の面積は、円の3倍。",10)
XU=finishx(Z,CH)
