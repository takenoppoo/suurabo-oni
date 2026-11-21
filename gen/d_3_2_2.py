# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
Z=U_(); CH=[]
R=sp.Rational; _c=[0]
E=sp.E
# 1 原点から引いた接線
def b1(k):
    t=sp.Symbol('t'); f=sp.exp(k*x); ln=lambda tt: f.subs(x,tt)+sp.diff(f,x).subs(x,tt)*(x-tt)
    sol=sp.solve(sp.simplify(ln(t).subs(x,0)),t); assert sol==[R(1,k)]; t0=sol[0]; m=sp.simplify(sp.diff(f,x).subs(x,t0)); assert sp.simplify(m-k*E)==0
    st=[("接点を $t$ とおく","<p>"+I(r"f'(x)=%se^{%sx}"%(L(k),L(k)))+"。接点 "+I(r"(t,\,e^{%st})"%L(k))+" での接線：</p>"+D(r"y-e^{%st}=%se^{%st}(x-t)"%(L(k),L(k),L(k)))),
        ("原点を通る条件","<p>"+I("(0,0)")+" を代入。</p>"+D(r"0-e^{%st}=%se^{%st}(0-t)\ \Rightarrow\ e^{%st}(%st-1)=0"%(L(k),L(k),L(k),L(k),L(k)))+D(r"t=%s"%L(t0))),
        ("接線の式","<p>傾き "+I(r"%se^{1}=%se"%(L(k),L(k)))+"、原点を通るので</p>"+D(r"y=%sex"%cf(k)))]
    return r"原点から曲線 $y=e^{%sx}$ に引いた接線の方程式を求めよ。"%L(k),st,r"y=%sex"%cf(k)
V=[2,3,R(1,2),4,5]
o=[b1(v) for v in V]
build(Z,CH,"原点から引いた接線（指数関数）",o,r"<p>接点を $(t,f(t))$ とおき、接線の式に<b>外の点を代入</b>して $t$ を決める。</p>","接点がわからないときは文字でおいて、通る条件で確定させる。",1)
# 2 極値
def b2(k):
    f=x*sp.exp(-k*x); fp=sp.simplify(sp.diff(f,x)); assert sp.simplify(fp-(1-k*x)*sp.exp(-k*x))==0; xm=R(1,k); ym=sp.simplify(f.subs(x,xm)); assert sp.simplify(ym-1/(k*E))==0
    _c[0]+=1; nm="i322_b%d"%_c[0]
    kk=float(k)
    def dr(ax):
        xs_=np.linspace(-0.3/kk,5/kk,400); ax.plot(xs_,xs_*np.exp(-kk*xs_),color="#b81f36",lw=2); mark(ax,1/kk,1/(kk*np.e),"",0,0)
    fig=gplane(nm,(-0.3/kk,5/kk),(-0.05,0.5/kk+0.05) if False else (-0.1/kk,0.5/kk),dr,xs=1/kk,ys=1/(2*kk)) if False else ""
    st=[("導関数",D(r"f'(x)=1\cdot e^{-%sx}+x\cdot(-%s)e^{-%sx}=(1-%sx)e^{-%sx}"%(L(k),L(k),L(k),cf(k),L(k)))),
        ("符号を調べる","<p>"+I(r"e^{-%sx}>0"%L(k))+" なので "+I("f'(x)")+" の符号は "+I(r"1-%sx"%cf(k))+" と同じ。</p>"+D(r"f'(x)=0\iff x=%s"%L(xm))+"<p>"+I("x<%s"%L(xm))+" で "+I("f'>0")+"（増加）、"+I("x>%s"%L(xm))+" で "+I("f'<0")+"（減少）。</p>"),
        ("極値",D(r"f\!\left(%s\right)=%s\,e^{-1}=\dfrac{%s}{e}"%(L(xm),L(xm),L(xm))))]
    return r"関数 $f(x)=xe^{-%sx}$ の極値を求めよ。"%L(k),st,r"x=%s\ \text{で極大値 }\dfrac{%s}{e}"%(L(xm),L(xm))
V=[2,3,R(1,2),4,5]
o=[b2(v) for v in V]
build(Z,CH,"指数関数を含む関数の極値",o,r"<p>$f'(x)=0$ を解き、<b>増減表（符号の変化）</b>で極大・極小を判断。$e^{(\cdots)}>0$ は符号に影響しないので、残りの因数の符号だけ見る。</p>","$e^x$ は常に正。符号を決めるのは、くくり出した多項式の部分だけ。",2)
# 3 最小値
def b3(a):
    f=x-a*sp.log(x); fp=sp.diff(f,x); assert sp.solve(fp,x)==[a]; ym=a-a*sp.log(a)
    st=[("導関数",D(r"f'(x)=1-\dfrac{%s}{x}=\dfrac{x-%s}{x}\quad(x>0)"%(L(a),L(a)))),
        ("増減","<p>"+I("x>0")+" なので符号は "+I(r"x-%s"%L(a))+" と同じ。</p>"+D(r"0<x<%s:\ f'<0,\qquad x>%s:\ f'>0"%(L(a),L(a)))+"<p>"+I("x=%s"%L(a))+" で最小。</p>"),
        ("最小値",D(r"f(%s)=%s-%s\log %s"%(L(a),L(a),L(a),L(a))))]
    return r"$x>0$ における関数 $f(x)=x-%s\log x$ の最小値を求めよ。"%L(a),st,r"%s-%s\log %s\ (x=%s)"%(L(a),L(a),L(a),L(a))
V=[2,3,4,5,6]
o=[b3(v) for v in V]
build(Z,CH,"対数関数を含む関数の最小値",o,r"<p>定義域（$x>0$）に注意。$f'(x)$ を通分して符号を調べ、増減から最小値を求める。</p>","定義域の外は存在しない。谷のいちばん下が最小。",3)
# 4 実数解の個数
def b4(n):
    g=sp.exp(x)/x**n; gp=sp.simplify(sp.diff(g,x)); assert sp.solve(sp.numer(sp.together(gp)),x)==[n] if n>0 else True
    ym=sp.exp(n)/sp.Integer(n)**n
    st=[("定数を分離","<p>"+I("x>0")+" で両辺を "+I("x^{%d}"%n)+" でわり、"+I(r"g(x)=\dfrac{e^x}{x^{%d}}=k"%n)+" と見る。（直線 "+I("y=k")+" とのグラフの交点の個数）</p>"),
        ("$g(x)$ の増減",D(r"g'(x)=\dfrac{e^x x^{%d}-e^x\cdot %dx^{%d}}{x^{%d}}=\dfrac{e^x(x-%d)}{x^{%d}}"%(n,n,n-1,2*n,n,n+1))+"<p>"+I("0<x<%d"%n)+" で減少、"+I("x>%d"%n)+" で増加。最小値 "+I(r"g(%d)=\dfrac{e^{%d}}{%d^{%d}}"%(n,n,n,n))+"。</p>"+D(r"x\to+0,\ x\to\infty\ \text{で}\ g(x)\to\infty")),
        ("範囲",D(r"k>\dfrac{e^{%d}}{%d^{%d}}"%(n,n,n)))]
    return r"方程式 $e^{x}=kx^{%d}$ が $x>0$ に異なる2つの実数解をもつような定数 $k$ の値の範囲を求めよ。"%n,st,r"k>\dfrac{e^{%d}}{%d^{%d}}"%(n,n,n)
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"方程式の実数解の個数（定数分離）",o,r"<p>$f(x)=k$ の形（<b>定数 $k$ を分離</b>）にして、$y=f(x)$ と直線 $y=k$ の共有点の個数を調べる。両端の極限も確認する。</p>","動かすのは水平線。山と谷にぶつかる回数を数える。",4)
# 5 変曲点
def b5(k):
    f=sp.exp(-k*x**2); f2=sp.simplify(sp.diff(f,x,2)); xi=1/sp.sqrt(2*k); assert sp.simplify(f2.subs(x,xi))==0
    assert sp.simplify(f2-(4*k**2*x**2-2*k)*sp.exp(-k*x**2))==0
    yi=sp.exp(-R(1,2))
    st=[("第1・第2導関数",D(r"f'(x)=-%sxe^{-%sx^2}"%(L(2*k),L(k)))+D(r"f''(x)=\left(%sx^2-%s\right)e^{-%sx^2}"%(L(4*k**2),L(2*k),L(k)))),
        ("$f''(x)=0$","<p>"+I(r"e^{-%sx^2}>0"%L(k))+" より</p>"+D(r"%sx^2-%s=0\ \Rightarrow\ x=\pm\dfrac{1}{\sqrt{%s}}"%(L(4*k**2),L(2*k),L(2*k)))+"<p>その前後で "+I("f''")+" の符号が変わる。</p>"),
        ("変曲点の座標",D(r"f\!\left(\pm\dfrac1{\sqrt{%s}}\right)=e^{-\frac12}=\dfrac1{\sqrt e}"%L(2*k)))]
    return r"曲線 $y=e^{-%sx^2}$ の変曲点の座標を求めよ。"%L(k),st,r"\left(\pm\dfrac1{\sqrt{%s}},\ \dfrac1{\sqrt e}\right)"%L(2*k)
V=[5,2,3,R(3,2),4]
o=[b5(v) for v in V]
build(Z,CH,"変曲点（第2次導関数）",o,r"<p>$f''(x)=0$ を解き、<b>前後で $f''$ の符号が変わる</b>点が変曲点。$y$ 座標は $f(x)$ に代入。</p>","曲がり方（上に凸・下に凸）が切り替わる点が変曲点。",5)
UNIT=finish(Z,CH,1,1,"微分法","微分法の応用","接線、極値、最小値、解の個数、変曲点まで、微分法の応用の難問に挑みます。",subject="3")
