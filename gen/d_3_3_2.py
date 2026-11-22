# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane
Z=U_(); CH=[]
R=sp.Rational; _c=[0]
def num(e): return float(sp.N(e))
def quad(f,a,b):
    fl=sp.lambdify(x,f,"numpy"); xs=np.linspace(float(a),float(b),200001); return float(np.trapezoid(fl(xs)*np.ones_like(xs),xs))
def co(c): return "" if c==1 else ("-" if c==-1 else L(c))
def EX(c): return "e" if c==1 else "e^{%s}"%L(c)
# 1 置換型の定積分
def b1(a,n,c):
    f=c*x*(x**2+a)**n; I1=sp.integrate(f,(x,0,1)); val=R(c,2*(n+1))*((1+a)**(n+1)-a**(n+1)); assert sp.simplify(I1-val)==0 and abs(quad(f,0,1)-float(val))<1e-6
    k=R(c,2); up=(1+a)**(n+1); lo=a**(n+1)
    st=[("置換する文字を決める","<p>"+I(r"u=x^2+%s"%L(a))+" とおく。両辺を "+I("x")+" で微分する。</p>"+D(r"\dfrac{du}{dx}=2x\ \Rightarrow\ du=2x\,dx\ \Rightarrow\ x\,dx=\dfrac12du")),
        ("積分範囲を $u$ に対応させる","<p>"+I(r"u=x^2+%s"%L(a))+" に端の値を代入する。</p>"+wtable(["$x$","$0$","$1$"],[["$u$","$0^2+%s=%s$"%(L(a),L(a)),"$1^2+%s=%s$"%(L(a),L(1+a))]])),
        ("$u$ の式に書きかえる","<p>"+D(r"\int_0^1 %sx(x^2+%s)^{%d}dx=%s\int_0^1(x^2+%s)^{%d}\cdot x\,dx"%(co(c),L(a),n,L(c) if c!=1 else "",L(a),n)+(r"" ))+"<p>"+I(r"x^2+%s=u,\ x\,dx=\dfrac12du"%L(a))+" を入れる。</p>"+D(r"=%s\int_{%s}^{%s}u^{%d}\cdot\dfrac12du=%s\int_{%s}^{%s}u^{%d}du"%(L(c) if c!=1 else "",L(a),L(1+a),n,L(k),L(a),L(1+a),n))),
        ("$u$ で積分する","<p>"+I(r"\int u^ndu=\dfrac{u^{n+1}}{n+1}")+" を使う。</p>"+D(r"=%s\left[\dfrac{u^{%d}}{%d}\right]_{%s}^{%s}"%(L(k),n+1,n+1,L(a),L(1+a)))),
        ("上端・下端を代入","<p>（上端の値）$-$（下端の値）。</p>"+D(r"=%s\left\{\dfrac{%s^{%d}}{%d}-\dfrac{%s^{%d}}{%d}\right\}=\dfrac{%s}{%d}\left(%s^{%d}-%s^{%d}\right)"%(L(k),L(1+a),n+1,n+1,L(a),n+1,n+1,L(c),2*(n+1),L(1+a),n+1,L(a),n+1))),
        ("数値を計算する","<p>"+D(r"%s^{%d}=%s,\qquad %s^{%d}=%s"%(L(1+a),n+1,L(up),L(a),n+1,L(lo)))+D(r"=\dfrac{%s}{%d}\left(%s-%s\right)=\dfrac{%s}{%d}\cdot%s=%s"%(L(c),2*(n+1),L(up),L(lo),L(c),2*(n+1),L(up-lo),L(val))))]
    return r"定積分 $\displaystyle\int_0^1 %sx(x^2+%s)^{%d}dx$ の値を求めよ。"%(co(c),L(a),n),st,L(val)
V=[(1,2,3),(2,3,4),(1,3,2),(3,2,4),(1,4,5)]
o=[b1(*v) for v in V]
build(Z,CH,"置換積分による定積分",o,r"<p>置換積分では<b>積分範囲も $u$ に変える</b>。$x$ に戻す必要はない。</p>","範囲も一緒に引っ越し。戻らなくてよい。",1)
# 2 部分積分の定積分
def b2(n):
    f=x**n*sp.log(x); val=(sp.E**(n+1)*R(n,(n+1)**2)+R(1,(n+1)**2)); v=sp.integrate(f,(x,1,sp.E)); assert sp.simplify(v-val)==0
    m=n+1; m2=m*m
    st=[("部分積分の形にする","<p>"+I(r"\int fg'\,dx=fg-\int f'g\,dx")+" で、微分して簡単になる "+I(r"\log x")+" を "+I("f")+" にとる。</p>"+D(r"f=\log x,\ f'=\dfrac1x,\qquad g'=x^{%d},\ g=\dfrac{x^{%d}}{%d}"%(n,m,m))),
        ("公式に当てはめる",D(r"\int x^{%d}\log x\,dx=\dfrac{x^{%d}}{%d}\log x-\int\dfrac1x\cdot\dfrac{x^{%d}}{%d}dx"%(n,m,m,m,m))),
        ("残りの積分を計算する","<p>"+I(r"\dfrac1x\cdot x^{%d}=x^{%d}"%(m,n))+" なので、</p>"+D(r"\int\dfrac1x\cdot\dfrac{x^{%d}}{%d}dx=\dfrac1{%d}\int x^{%d}dx=\dfrac1{%d}\cdot\dfrac{x^{%d}}{%d}=\dfrac{x^{%d}}{%d}"%(m,m,m,n,m,m,m,m,m2))+D(r"\int x^{%d}\log x\,dx=\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}"%(n,m,m,m,m2))),
        ("上端 $x=e$ を代入","<p>"+I(r"\log e=1")+"。</p>"+D(r"\dfrac{e^{%d}}{%d}\cdot1-\dfrac{e^{%d}}{%d}=e^{%d}\left(\dfrac1{%d}-\dfrac1{%d}\right)=\dfrac{%d\,e^{%d}}{%d}"%(m,m,m,m2,m,m,m2,n,m,m2) if n>1 else "")),
        ("下端 $x=1$ を代入","<p>"+I(r"\log1=0")+"、"+I(r"1^{%d}=1"%m)+"。</p>"+D(r"\dfrac{1^{%d}}{%d}\cdot0-\dfrac{1^{%d}}{%d}=-\dfrac1{%d}"%(m,m,m,m2,m2))),
        ("（上端）$-$（下端）",D(r"\dfrac{%d\,e^{%d}}{%d}-\left(-\dfrac1{%d}\right)=\dfrac{%d\,e^{%d}+1}{%d}"%(n,m,m2,m2,n,m,m2)))]
    return r"定積分 $\displaystyle\int_1^e x^{%d}\log x\,dx$ の値を求めよ。"%n,st,r"\dfrac{%d\,e^{%d}+1}{%d}"%(n,m,m2)
V=[2,3,4,5,6]
o=[b2(v) for v in V]
build(Z,CH,"部分積分による定積分",o,r"<p>$\int_a^b fg'dx=[fg]_a^b-\int_a^b f'g\,dx$。$\log 1=0$、$\log e=1$ を使って代入を整理する。</p>","端の値の代入で、$\\log1=0$ が計算を軽くしてくれる。",2)
# 3 面積 e^x, e^-x
def b3(a):
    S=sp.exp(a)+sp.exp(-a)-2; v=sp.integrate(sp.exp(x)-sp.exp(-x),(x,0,a)); assert sp.simplify(v-S)==0
    _c[0]+=1; nm="i332_a%d"%_c[0]; af=float(a)
    def dr(ax):
        xs_=np.linspace(-0.2,af+0.4,300); ax.plot(xs_,np.exp(xs_),color="#b81f36",lw=2); ax.plot(xs_,np.exp(-xs_),color="#1f6fb8",lw=2)
        xf=np.linspace(0,af,300); ax.fill_between(xf,np.exp(-xf),np.exp(xf),color="#f4b6bf",alpha=.6); ax.plot([af,af],[0,np.exp(af)],color="#555",lw=1,ls="--")
        ax.text(af+.05,np.exp(af)*0.95,"y=e^x",fontsize=9,color="#b81f36"); ax.text(af+.05,np.exp(-af)+.3,"y=e^{-x}",fontsize=9,color="#1f6fb8")
    fig=gplane(nm,(-0.2,af+0.9),(-0.3,float(sp.exp(a))+0.8),dr,xs=1,ys=2)
    st=[("交点と上下を確認","<p>"+I(r"e^x=e^{-x}")+" とすると "+I(r"e^{2x}=1")+" より "+I("x=0")+"。"+I(r"0\leqq x\leqq %s"%L(a))+" では "+I(r"e^x\geqq e^{-x}")+"（上が "+I("e^x")+"、下が "+I("e^{-x}")+"）。</p>"+fig),
        ("面積の式を立てる","<p>（上）$-$（下）を "+I(r"x=0")+" から "+I("x=%s"%L(a))+" まで積分する。</p>"+D(r"S=\int_0^{%s}\left(e^x-e^{-x}\right)dx"%L(a))),
        ("原始関数を求める","<p>"+I(r"\int e^xdx=e^x")+"、"+I(r"\int e^{-x}dx=-e^{-x}")+"（"+I(r"(e^{-x})'=-e^{-x}")+" だから）。</p>"+D(r"\int\left(e^x-e^{-x}\right)dx=e^x-\left(-e^{-x}\right)=e^x+e^{-x}")),
        ("上端 $x=%s$ を代入"%L(a),D(r"e^{%s}+e^{-%s}"%(L(a),L(a))).replace("e^{1}","e")),
        ("下端 $x=0$ を代入","<p>"+I(r"e^0=1")+"。</p>"+D(r"e^0+e^0=1+1=2")),
        ("（上端）$-$（下端）",D(r"S=\left(%s+%s\right)-2=%s+%s-2"%(EX(a),EX(-a),EX(a),EX(-a))))]
    return r"2曲線 $y=e^x,\ y=e^{-x}$ と直線 $x=%s$ で囲まれた部分の面積を求めよ。"%L(a),st,r"%s+%s-2"%(EX(a),EX(-a))
V=[1,2,3,R(3,2),R(5,2)]
o=[b3(v) for v in V]
build(Z,CH,"2曲線で囲まれた部分の面積",o,r"<p>面積 $=\displaystyle\int_a^b\{(\text{上})-(\text{下})\}dx$。グラフで上下を確認し、交点・端点を押さえる。</p>","上から下を引いて、縦に切った細い帯を積み重ねる。",3)
# 4 対数曲線の面積
def b4(k):
    S=(k-1)*sp.exp(k)+1; v=sp.integrate(sp.log(x),(x,1,sp.exp(k))); assert sp.simplify(v-S)==0
    _c[0]+=1; nm="i332_b%d"%_c[0]; up=float(sp.exp(k))
    def dr(ax):
        xs_=np.linspace(0.1,up+0.6,400); ax.plot(xs_,np.log(xs_),color="#b81f36",lw=2); xf=np.linspace(1,up,300); ax.fill_between(xf,0,np.log(xf),color="#f4b6bf",alpha=.6)
        ax.plot([up,up],[0,float(k)],color="#555",lw=1,ls="--")
    fig=gplane(nm,(-0.3,up+1.2),(-0.7,float(k)+0.8),dr,xs=max(1,int(up//6)),ys=1)
    st=[("正負を確認する","<p>"+I(r"1\leqq x\leqq e^{%s}"%L(k))+" では "+I(r"\log x\geqq0")+"（"+I(r"\log1=0")+"、増加）。グラフは "+I("x")+" 軸の上側。</p>"+fig),
        ("面積の式を立てる",D(r"S=\int_1^{e^{%s}}\log x\,dx"%L(k))),
        ("原始関数を求める（部分積分）","<p>"+I(r"\log x=1\cdot\log x")+" とみて、"+I(r"f=\log x,\ g'=1")+" とおく。</p>"+D(r"f'=\dfrac1x,\ g=x")+D(r"\int\log x\,dx=x\log x-\int\dfrac1x\cdot x\,dx=x\log x-\int1\,dx=x\log x-x")),
        ("上端 $x=e^{%s}$ を代入"%L(k),"<p>"+I(r"\log e^{%s}=%s"%(L(k),L(k)))+"。</p>"+D(r"e^{%s}\log e^{%s}-e^{%s}=%se^{%s}-e^{%s}"%(L(k),L(k),L(k),L(k),L(k),L(k)))),
        ("下端 $x=1$ を代入",D(r"1\cdot\log1-1=0-1=-1")),
        ("（上端）$-$（下端）",D(r"S=\left(%se^{%s}-e^{%s}\right)-(-1)=%s"%(L(k),L(k),L(k),(("(%s)e^{%s}+1"%(L(k-1),L(k))) if k>2 else "e^{%s}+1"%L(k)))))]
    return r"曲線 $y=\log x$、$x$ 軸、直線 $x=e^{%s}$ で囲まれた部分の面積を求めよ。"%L(k),st,(r"(%s)e^{%s}+1"%(L(k-1),L(k)) if k>2 else r"e^{%s}+1"%L(k))
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"対数曲線と軸で囲まれた面積",o,r"<p>$\int\log x\,dx=x\log x-x+C$（部分積分で $1\cdot\log x$ とみる）。端点 $x=e^k$ では $\log e^k=k$。</p>","$\\log x$ は「1×$\\log x$」と見て部分積分する裏ワザ。",4)
# 5 回転体の体積
def b5(k):
    V=sp.pi*(sp.exp(2*k)-1)/(2*k); v=sp.pi*sp.integrate(sp.exp(2*k*x),(x,0,1)); assert sp.simplify(v-V)==0
    st=[("体積の公式","<p>$x$ 軸のまわりの回転体は、断面が半径 "+I("y")+" の円板。</p>"+D(r"V=\pi\int_a^b\{f(x)\}^2dx")),
        ("被積分関数を計算する","<p>"+D(r"\left(e^{%sx}\right)^2=e^{%sx\cdot2}=e^{%sx}"%(L(k),L(k),L(2*k)))+D(r"V=\pi\int_0^1e^{%sx}dx"%L(2*k))),
        ("原始関数を求める","<p>"+I(r"\left(e^{%sx}\right)'=%se^{%sx}"%(L(2*k),L(2*k),L(2*k)))+" だから、</p>"+D(r"\int e^{%sx}dx=\dfrac{e^{%sx}}{%s}"%(L(2*k),L(2*k),L(2*k)))),
        ("上端 $x=1$ を代入",D(r"\dfrac{e^{%s}}{%s}"%(L(2*k),L(2*k)))),
        ("下端 $x=0$ を代入","<p>"+I(r"e^0=1")+"。</p>"+D(r"\dfrac{e^{0}}{%s}=\dfrac1{%s}"%(L(2*k),L(2*k)))),
        ("（上端）$-$（下端）",D(r"V=\pi\left(\dfrac{e^{%s}}{%s}-\dfrac1{%s}\right)=\dfrac{\pi\left(e^{%s}-1\right)}{%s}"%(L(2*k),L(2*k),L(2*k),L(2*k),L(2*k))))]
    return r"曲線 $y=e^{%sx}\ (0\leqq x\leqq1)$ と $x$ 軸、$y$ 軸、直線 $x=1$ で囲まれた部分を $x$ 軸のまわりに回転してできる立体の体積を求めよ。"%L(k),st,r"\dfrac{\pi\left(e^{%s}-1\right)}{%s}"%(L(2*k),L(2*k))
V=[R(5,2),2,3,R(3,2),4]
o=[b5(v) for v in V]
build(Z,CH,"回転体の体積",o,r"<p>$x$ 軸のまわりの回転体の体積は $V=\pi\displaystyle\int_a^b y^2dx$。$y^2$ を先に計算してから積分。</p>","輪切りにした円板（面積 $\\pi y^2$）を積み重ねる。",5)
UNIT=finish(Z,CH,2,1,"積分法","定積分と面積・体積","定積分の計算、面積、回転体の体積まで、積分法の応用の難問に挑みます。",subject="3")
