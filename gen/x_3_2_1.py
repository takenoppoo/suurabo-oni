# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; x,t=sp.symbols("x t")
# 6 媒介変数の微分
def b6(xf,yf,t0):
    dx=sp.diff(xf,t); dy=sp.diff(yf,t); m=sp.simplify(dy/dx); v=sp.simplify(m.subs(t,t0))
    px=sp.simplify(xf.subs(t,t0)); py=sp.simplify(yf.subs(t,t0))
    st=[("$t$ で微分","<p>"+D(r"\dfrac{dx}{dt}=%s,\qquad \dfrac{dy}{dt}=%s"%(L(dx),L(dy)))),
        ("$\\dfrac{dy}{dx}$","<p>"+D(r"\dfrac{dy}{dx}=\dfrac{dy/dt}{dx/dt}=%s"%L(m))),
        ("接線","<p>"+I("t=%s"%L(t0))+" のとき 点 "+I("(%s,\\ %s)"%(L(px),L(py)))+"、傾き "+I(L(v))+"。</p>"+D(r"y-%s=%s(x-%s)"%(L(py),L(v),L(px))))]
    return r"曲線 $x=%s,\ y=%s$ の $t=%s$ に対応する点における接線の傾きと接線の方程式を求めよ。"%(L(xf),L(yf),L(t0)),st,r"\text{傾き }%s,\ \ y-%s=%s(x-%s)"%(L(v),L(py),L(v),L(px))
o=[b6(*v) for v in [(t**2+1,t**3,1),(2*sp.cos(t),3*sp.sin(t),sp.pi/3),(sp.exp(t),sp.exp(-t),0),(t-sp.sin(t),1-sp.cos(t),sp.pi/2),(sp.log(t),t**2,1)]]
build(Z,CH,"媒介変数表示の曲線の接線",o,"<p>$\\dfrac{dy}{dx}=\\dfrac{dy/dt}{dx/dt}$。$t$ の値から点と傾きを求め、接線の式を作る。</p>","時間で割った速度の比が、傾きになる。",6)
# 7 陰関数
def b7(a2,b2,p):
    y=sp.symbols("y"); F=x**2/a2+y**2/b2-1
    # point on ellipse
    yv=sp.sqrt(b2*(1-p**2/a2)); 
    d=sp.simplify(-sp.diff(F,x)/sp.diff(F,y)); m=sp.simplify(d.subs({x:p,y:yv}))
    tl=sp.simplify(m*(x-p)+yv)
    st=[("両辺を $x$ で微分","<p>"+D(r"\dfrac{2x}{%d}+\dfrac{2y}{%d}\cdot\dfrac{dy}{dx}=0"%(a2,b2))),
        ("$\\dfrac{dy}{dx}$","<p>"+D(r"\dfrac{dy}{dx}=-\dfrac{%dx}{%dy}"%(b2,a2))),
        ("接線","<p>"+I("(%s,\\ %s)"%(L(p),L(yv)))+" で傾き "+I(L(m))+"。</p>"+D(r"y=%s"%L(sp.expand(tl))))]
    return r"楕円 $\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1$ 上の点 $\left(%s,\ %s\right)$ における接線の方程式を、陰関数の微分で求めよ。"%(a2,b2,L(p),L(yv)),st,r"y=%s"%L(sp.expand(tl))
o=[b7(*v) for v in [(9,4,R(9,5) if False else 0) if False else (25,9,3),(16,4,2),(9,1,0) if False else (25,16,3),(4,1,1),(36,9,3)]]
build(Z,CH,"陰関数の微分と接線",o,"<p>$y$ を $x$ の関数とみて両辺を $x$ で微分（$y^2$ の微分は $2y\\dfrac{dy}{dx}$）。$\\dfrac{dy}{dx}$ を解いて接線を作る。</p>","y は x に依存するので、合成関数の微分を忘れない。",7)
# 8 n次導関数
def b8(a,kind):
    f=sp.sin(a*x) if kind=="sin" else sp.exp(a*x)*x if kind=="xe" else sp.log(x)
    d4=sp.simplify(sp.diff(f,x,4)); n=sp.symbols("n")
    if kind=="sin":
        gen=a**n*sp.sin(a*x+n*sp.pi/2)
        for N in range(1,7): assert sp.simplify(sp.diff(f,x,N)-gen.subs(n,N))==0
        st=[("順に微分","<p>"+D(r"f'=%d\cos%dx=%d\sin\left(%dx+\dfrac\pi2\right),\ \ f''=-%d\sin%dx=%d\sin(%dx+\pi)"%(a,a,a,a,a*a,a,a*a,a))),
            ("規則","<p>微分のたびに "+I(r"\times%d"%a)+"、角が "+I(r"+\dfrac\pi2")+"。</p>"),
            ("一般形",D(r"f^{(n)}(x)=%d^n\sin\left(%dx+\dfrac{n\pi}{2}\right)"%(a,a)))]
        return r"$f(x)=\sin%dx$ の第 $n$ 次導関数を求めよ。"%a,st,r"%d^n\sin\left(%dx+\dfrac{n\pi}{2}\right)"%(a,a)
    if kind=="xe":
        gen=(a**n*x+n*a**(n-1))*sp.exp(a*x)
        for N in range(1,7): assert sp.simplify(sp.diff(f,x,N)-gen.subs(n,N))==0
        st=[("順に微分","<p>"+D(r"f'=(%dx+1)e^{%dx},\quad f''=(%dx+%d)e^{%dx},\quad f'''=(%dx+%d)e^{%dx}"%(a,a,a*a,2*a,a,a**3,3*a*a,a))),
            ("規則","<p>"+I("x")+" の係数は "+I("%d^n"%a)+"、定数項は "+I("n\\cdot%d^{n-1}"%a)+"。</p>"),
            ("一般形",D(r"f^{(n)}(x)=(%d^nx+n\cdot%d^{n-1})e^{%dx}"%(a,a,a)))]
        return r"$f(x)=xe^{%dx}$ の第 $n$ 次導関数を求めよ。"%a,st,r"(%d^nx+n\cdot%d^{n-1})e^{%dx}"%(a,a,a)
o=[b8(2,"sin"),b8(3,"sin"),b8(2,"xe"),b8(3,"xe"),b8(4,"sin")]
build(Z,CH,"n 次導関数を推定する",o,"<p>2〜3回微分して<b>規則を見つけ</b>、一般形を予想する。（厳密には数学的帰納法で証明できる。）</p>","微分をくり返すと、決まったパターンが現れる。",8)
# 9 微分係数の定義
def b9(f,a):
    fp=sp.diff(f,x).subs(x,a)
    st=[("微分係数の定義","<p>"+D(r"f'(a)=\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}")),
        ("極限を導関数に","<p>"+I("f(x)=%s"%L(f))+"。"+I("f'(x)=%s"%L(sp.diff(f,x)))+"。</p>"),
        ("値","<p>"+D(r"f'(%s)=%s"%(L(a),L(sp.simplify(fp)))))]
    return r"$f(x)=%s$ のとき、$\displaystyle\lim_{h\to0}\dfrac{f(%s+h)-f(%s)}{h}$ を、微分係数の定義を用いて求めよ。"%(L(f),L(a),L(a)),st,L(sp.simplify(fp))
o=[b9(*v) for v in [(sp.exp(2*x),0),(sp.log(x),2),(sp.sin(x),sp.pi/3),(sp.sqrt(x),4),(x*sp.exp(x),1)]]
build(Z,CH,"極限を微分係数として求める",o,"<p>$\\lim_{h\\to0}\\dfrac{f(a+h)-f(a)}{h}=f'(a)$。極限の式を<b>定義の形</b>と見て、導関数を計算して $a$ を代入。</p>","極限の形に見えたら、微分係数の定義を疑ってみる。",9)
# 10 x^x の微分
def b10(a):
    f=x**(a*x); fp=sp.simplify(sp.diff(f,x))
    st=[("両辺の対数","<p>"+D(r"\log y=%dx\log x"%a)),
        ("両辺を $x$ で微分","<p>"+D(r"\dfrac{y'}{y}=%d\log x+%d"%(a,a))),
        ("答え","<p>"+D(r"y'=%s\,(\log x+1)\cdot%d"%(L(f),a)))]
    assert sp.simplify(fp-a*f*(sp.log(x)+1))==0
    return r"$y=x^{%dx}\ (x>0)$ を微分せよ。"%a,st,r"y'=%d\,x^{%dx}(\log x+1)"%(a,a)
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"x^{ax} の微分（対数微分法）",o,"<p>底にも指数にも $x$ があるときは<b>両辺の対数</b>をとってから微分。$\\dfrac{y'}{y}=(\\log y)'$。</p>","掛け算に直してから微分すれば、積の微分で済む。",10)
XU=finishx(Z,CH)
