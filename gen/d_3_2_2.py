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
    tk=L(k); tt="%st"%L(k) if True else ""
    st=[("接点を $t$ とおく","<p>接点を "+I(r"(t,\,e^{%st})"%L(k))+" とおく。</p>"),
        ("導関数を求める","<p>"+I(r"(e^{u})'=e^{u}\cdot u'")+" より、</p>"+D(r"f'(x)=%se^{%sx}"%(L(k),L(k)))+"<p>"+I("x=t")+" での傾きは "+I(r"f'(t)=%se^{%st}"%(L(k),L(k)))+"。</p>"),
        ("接線の方程式を書く","<p>点 "+I(r"(t,\,e^{%st})"%L(k))+"、傾き "+I(r"%se^{%st}"%(L(k),L(k)))+" の直線。</p>"+D(r"y-e^{%st}=%se^{%st}(x-t)"%(L(k),L(k),L(k)))),
        ("原点を通る条件を使う","<p>"+I("(x,\\ y)=(0,\\ 0)")+" を代入する。</p>"+D(r"0-e^{%st}=%se^{%st}(0-t)"%(L(k),L(k),L(k)))+D(r"-e^{%st}=-%ste^{%st}"%(L(k),L(k),L(k)))),
        ("$t$ を求める","<p>両辺を "+I(r"-e^{%st}"%L(k))+"（"+I(r"\ne0")+"）でわる。</p>"+D(r"1=%st\ \Rightarrow\ t=%s"%(L(k),L(t0)))),
        ("傾きと接線の式","<p>"+I(r"t=%s"%L(t0))+" のとき "+I(r"%st=1"%L(k))+" だから "+I(r"e^{%st}=e^{1}=e"%L(k))+"。</p>"+D(r"\text{傾き}=%se^{%st}=%se"%(L(k),L(k),L(k)))+"<p>原点を通るので、</p>"+D(r"y=%sex"%cf(k)))]
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
    ke=L(k); K="-%sx"%ke; YV=r"\dfrac{%d}{%se}"%(xm.p,"" if xm.q==1 else str(xm.q))
    st=[("積の微分で導関数を求める","<p>"+I(r"(e^{%s})'=-%se^{%s}"%(K,ke,K))+"。</p>"+D(r"f'(x)=1\cdot e^{%s}+x\cdot(-%s)e^{%s}"%(K,ke,K))+"<p>"+I("e^{%s}"%K)+" でくくる。</p>"+D(r"=(1-%sx)e^{%s}"%(cf(k),K))),
        ("$f'(x)=0$ を解く","<p>"+I("e^{%s}>0"%K)+" だから、"+I(r"1-%sx=0"%cf(k))+"。</p>"+D(r"x=%s"%L(xm))),
        ("増減表をかく","<p>"+I("f'(x)")+" の符号は "+I(r"1-%sx"%cf(k))+" の符号と同じ。</p>"+wtable(["$x$","$\\cdots$","$%s$"%L(xm),"$\\cdots$"],[["$f'(x)$","$+$","$0$","$-$"],["$f(x)$","↗","極大","↘"]])),
        ("極大値を求める","<p>"+I("x=%s"%L(xm))+" を "+I("f(x)")+" に代入。"+I(r"-%s\cdot%s=-1"%(ke,L(xm)))+" だから、</p>"+D(r"f\!\left(%s\right)=%s\,e^{-%s\cdot%s}=%s\,e^{-1}=%s"%(L(xm),L(xm),ke,L(xm),L(xm),YV)))]
    return r"関数 $f(x)=xe^{-%sx}$ の極値を求めよ。"%L(k),st,r"x=%s\ \text{で極大値 }%s"%(L(xm),YV)
V=[2,3,R(1,2),4,5]
o=[b2(v) for v in V]
build(Z,CH,"指数関数を含む関数の極値",o,r"<p>$f'(x)=0$ を解き、<b>増減表（符号の変化）</b>で極大・極小を判断。$e^{(\cdots)}>0$ は符号に影響しないので、残りの因数の符号だけ見る。</p>","$e^x$ は常に正。符号を決めるのは、くくり出した多項式の部分だけ。",2)
# 3 最小値
def b3(a):
    f=x-a*sp.log(x); fp=sp.diff(f,x); assert sp.solve(fp,x)==[a]; ym=a-a*sp.log(a)
    st=[("導関数を求める","<p>"+I(r"(\log x)'=\dfrac1x")+"。</p>"+D(r"f'(x)=1-%s\cdot\dfrac1x=1-\dfrac{%s}{x}"%(L(a),L(a)))+"<p>通分する。</p>"+D(r"=\dfrac{x-%s}{x}\quad(x>0)"%L(a))),
        ("$f'(x)=0$ を解く","<p>分母 "+I("x")+" は正なので、"+I(r"x-%s=0"%L(a))+" より "+I("x=%s"%L(a))+"。</p>"),
        ("増減表をかく","<p>"+I("x>0")+" なので "+I("f'(x)")+" の符号は "+I(r"x-%s"%L(a))+" と同じ。</p>"+wtable(["$x$","$0$","$\\cdots$","$%s$"%L(a),"$\\cdots$"],[["$f'(x)$","","$-$","$0$","$+$"],["$f(x)$","","↘","最小","↗"]])),
        ("最小値を求める","<p>"+I("x=%s"%L(a))+" を代入する。</p>"+D(r"f(%s)=%s-%s\log %s"%(L(a),L(a),L(a),L(a))))]
    return r"$x>0$ における関数 $f(x)=x-%s\log x$ の最小値を求めよ。"%L(a),st,r"%s-%s\log %s\ (x=%s)"%(L(a),L(a),L(a),L(a))
V=[2,3,4,5,6]
o=[b3(v) for v in V]
build(Z,CH,"対数関数を含む関数の最小値",o,r"<p>定義域（$x>0$）に注意。$f'(x)$ を通分して符号を調べ、増減から最小値を求める。</p>","定義域の外は存在しない。谷のいちばん下が最小。",3)
# 4 実数解の個数
def b4(n):
    g=sp.exp(x)/x**n; gp=sp.simplify(sp.diff(g,x)); assert sp.solve(sp.numer(sp.together(gp)),x)==[n] if n>0 else True
    ym=sp.exp(n)/sp.Integer(n)**n
    m1=n-1; M=r"e^x\cdot x^{%d}-e^x\cdot%dx^{%d}"%(n,n,n-1)
    st=[("定数を分離する","<p>"+I("x>0")+" で両辺を "+I("x^{%d}"%n)+"（"+I(">0")+"）でわる。</p>"+D(r"\dfrac{e^x}{x^{%d}}=k"%n)+"<p>"+I(r"g(x)=\dfrac{e^x}{x^{%d}}"%n)+" とおくと、方程式は "+I("g(x)=k")+"。解の個数は、曲線 "+I("y=g(x)")+" と直線 "+I("y=k")+" の共有点の個数。</p>"),
        ("$g'(x)$ を求める","<p>商の微分 "+I(r"\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}")+" で "+I(r"f=e^x,\ g=x^{%d}"%n)+"。</p>"+D(r"g'(x)=\dfrac{e^x\cdot x^{%d}-e^x\cdot%dx^{%d}}{(x^{%d})^2}=\dfrac{e^x\,x^{%d}(x-%d)}{x^{%d}}=\dfrac{e^x(x-%d)}{x^{%d}}"%(n,n,n-1,n,n-1,n,2*n,n,n+1)).replace("x^{1}","x")),
        ("増減表をかく","<p>"+I("e^x>0,\\ x^{%d}>0"%(n+1))+" だから、"+I("g'(x)")+" の符号は "+I("x-%d"%n)+" と同じ。</p>"+wtable(["$x$","$0$","$\\cdots$","$%d$"%n,"$\\cdots$"],[["$g'(x)$","","$-$","$0$","$+$"],["$g(x)$","","↘",r"$\dfrac{e^{%d}}{%d^{%d}}$"%(n,n,n),"↗"]])),
        ("端の様子を調べる","<p>"+I(r"x\to+0")+" のとき "+I("e^x\\to1")+"、"+I(r"x^{%d}\to+0"%n)+" なので "+I(r"g(x)\to+\infty")+"。</p><p>"+I(r"x\to\infty")+" のとき、"+I("e^x")+" は "+I("x^{%d}"%n)+" より速く大きくなるので "+I(r"g(x)\to+\infty")+"。</p>"),
        ("共有点の個数から $k$ の範囲を決める","<p>グラフは "+I("x=%d"%n)+" で最小値 "+I(r"\dfrac{e^{%d}}{%d^{%d}}"%(n,n,n))+" をとり、両端で "+I(r"+\infty")+"。直線 "+I("y=k")+" が2点で交わるのは最小値より上のとき。</p>"+D(r"k>\dfrac{e^{%d}}{%d^{%d}}"%(n,n,n)))]
    return r"方程式 $e^{x}=kx^{%d}$ が $x>0$ に異なる2つの実数解をもつような定数 $k$ の値の範囲を求めよ。"%n,st,r"k>\dfrac{e^{%d}}{%d^{%d}}"%(n,n,n)
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"方程式の実数解の個数（定数分離）",o,r"<p>$f(x)=k$ の形（<b>定数 $k$ を分離</b>）にして、$y=f(x)$ と直線 $y=k$ の共有点の個数を調べる。両端の極限も確認する。</p>","動かすのは水平線。山と谷にぶつかる回数を数える。",4)
# 5 変曲点
def b5(k):
    f=sp.exp(-k*x**2); f2=sp.simplify(sp.diff(f,x,2)); xi=1/sp.sqrt(2*k); assert sp.simplify(f2.subs(x,xi))==0
    assert sp.simplify(f2-(4*k**2*x**2-2*k)*sp.exp(-k*x**2))==0
    yi=sp.exp(-R(1,2))
    kk2=L(2*k); kk4=L(4*k**2); KX="-%sx^2"%L(k)
    st=[("第1導関数を求める","<p>"+I(r"(e^{u})'=e^{u}\cdot u'")+"、"+I(r"u=%s"%KX)+" の導関数は "+I("-%sx"%kk2)+"。</p>"+D(r"f'(x)=-%sxe^{%s}"%(kk2,KX))),
        ("第2導関数を求める","<p>積の微分を使う。</p>"+D(r"f''(x)=-%se^{%s}+(-%sx)\cdot(-%sx)e^{%s}"%(kk2,KX,kk2,kk2,KX))+"<p>"+I("e^{%s}"%KX)+" でくくる。</p>"+D(r"=\left(%sx^2-%s\right)e^{%s}"%(kk4,kk2,KX))),
        ("$f''(x)=0$ を解く","<p>"+I("e^{%s}>0"%KX)+" より "+I(r"%sx^2-%s=0"%(kk4,kk2))+"。</p>"+D(r"x^2=\dfrac{%s}{%s}=\dfrac1{%s}\ \Rightarrow\ x=\pm\dfrac{1}{\sqrt{%s}}"%(kk2,kk4,kk2,kk2))),
        ("符号の変化を確認する","<p>"+I("f''(x)")+" の符号は "+I(r"%sx^2-%s"%(kk4,kk2))+" と同じ。</p>"+wtable(["$x$","$\\cdots$",r"$-\dfrac1{\sqrt{%s}}$"%kk2,"$\\cdots$",r"$\dfrac1{\sqrt{%s}}$"%kk2,"$\\cdots$"],[["$f''(x)$","$+$","$0$","$-$","$0$","$+$"],["$f(x)$","下に凸","変曲点","上に凸","変曲点","下に凸"]])),
        ("$y$ 座標を求める","<p>"+I(r"x^2=\dfrac1{%s}"%kk2)+" だから "+I(r"%sx^2=%s\cdot\dfrac1{%s}=\dfrac12"%(L(k),L(k),kk2))+"。</p>"+D(r"f\!\left(\pm\dfrac1{\sqrt{%s}}\right)=e^{-\frac12}=\dfrac1{\sqrt e}"%kk2))]
    return r"曲線 $y=e^{-%sx^2}$ の変曲点の座標を求めよ。"%L(k),st,r"\left(\pm\dfrac1{\sqrt{%s}},\ \dfrac1{\sqrt e}\right)"%L(2*k)
V=[5,2,3,R(3,2),4]
o=[b5(v) for v in V]
build(Z,CH,"変曲点（第2次導関数）",o,r"<p>$f''(x)=0$ を解き、<b>前後で $f''$ の符号が変わる</b>点が変曲点。$y$ 座標は $f(x)$ に代入。</p>","曲がり方（上に凸・下に凸）が切り替わる点が変曲点。",5)
UNIT=finish(Z,CH,1,1,"微分法","微分法の応用","接線、極値、最小値、解の個数、変曲点まで、微分法の応用の難問に挑みます。",subject="3")
