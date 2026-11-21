# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane
Z=U_(); CH=[]
R=sp.Rational; _c=[0]
def num(e): return float(sp.N(e))
def quad(f,a,b):
    fl=sp.lambdify(x,f,"numpy"); xs=np.linspace(float(a),float(b),200001); return float(np.trapezoid(fl(xs)*np.ones_like(xs),xs))
# 1 置換型の定積分
def b1(a,n,c):
    f=c*x*(x**2+a)**n; I1=sp.integrate(f,(x,0,1)); val=R(c,2*(n+1))*((1+a)**(n+1)-a**(n+1)); assert sp.simplify(I1-val)==0 and abs(quad(f,0,1)-float(val))<1e-6
    st=[("置換",  "<p>"+I(r"u=x^2+%s"%L(a))+"、"+I(r"du=2x\,dx")+"。範囲は "+I(r"x:0\to1")+" のとき "+I(r"u:%s\to%s"%(L(a),L(1+a)))+"。</p>"),
        ("$u$ で定積分",D(r"\int_0^1 %sx(x^2+%s)^{%d}dx=%s\int_{%s}^{%s}u^{%d}du=%s\left[\dfrac{u^{%d}}{%d}\right]_{%s}^{%s}"%(L(c),L(a),n,L(R(c,2)),L(a),L(1+a),n,L(R(c,2)),n+1,n+1,L(a),L(1+a)))),
        ("計算",D(r"=\dfrac{%s}{%d}\left\{%s^{%d}-%s^{%d}\right\}=%s"%(L(c),2*(n+1),L(1+a),n+1,L(a),n+1,L(val))))]
    return r"定積分 $\displaystyle\int_0^1 %sx(x^2+%s)^{%d}dx$ の値を求めよ。"%(L(c),L(a),n),st,L(val)
V=[(1,2,3),(2,3,4),(1,3,2),(3,2,4),(1,4,5)]
o=[b1(*v) for v in V]
build(Z,CH,"置換積分による定積分",o,r"<p>置換積分では<b>積分範囲も $u$ に変える</b>。$x$ に戻す必要はない。</p>","範囲も一緒に引っ越し。戻らなくてよい。",1)
# 2 部分積分の定積分
def b2(n):
    f=x**n*sp.log(x); val=(n*sp.exp(0)*0+ (sp.E**(n+1)*n/(n+1)**2+R(1,(n+1)**2))) if False else (sp.E**(n+1)*R(n,(n+1)**2)+R(1,(n+1)**2)); v=sp.integrate(f,(x,1,sp.E)); assert sp.simplify(v-val)==0
    st=[("不定積分を求める（部分積分）",D(r"\int x^{%d}\log x\,dx=\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}"%(n,n+1,n+1,n+1,(n+1)**2))),
        ("上端・下端を代入",D(r"\left[\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}\right]_1^e=\left(\dfrac{e^{%d}}{%d}-\dfrac{e^{%d}}{%d}\right)-\left(0-\dfrac1{%d}\right)"%(n+1,n+1,n+1,(n+1)**2,n+1,n+1,n+1,(n+1)**2,(n+1)**2))),
        ("整理",D(r"=\dfrac{%s\,e^{%d}+1}{%d}"%(L(n),n+1,(n+1)**2)))]
    return r"定積分 $\displaystyle\int_1^e x^{%d}\log x\,dx$ の値を求めよ。"%n,st,r"\dfrac{%s\,e^{%d}+1}{%d}"%(L(n),n+1,(n+1)**2)
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
    st=[("上下を確認","<p>"+I(r"0\leqq x\leqq %s"%L(a))+" で "+I(r"e^x\geqq e^{-x}")+"（"+I("x=0")+" で一致）。</p>"+fig),
        ("面積の式",D(r"S=\int_0^{%s}\left(e^x-e^{-x}\right)dx=\left[e^x+e^{-x}\right]_0^{%s}"%(L(a),L(a)))),
        ("計算",D(r"=\left(e^{%s}+e^{-%s}\right)-(1+1)=e^{%s}+e^{-%s}-2"%(L(a),L(a),L(a),L(a))))]
    return r"2曲線 $y=e^x,\ y=e^{-x}$ と直線 $x=%s$ で囲まれた部分の面積を求めよ。"%L(a),st,r"e^{%s}+e^{-%s}-2"%(L(a),L(a))
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
    st=[("面積の式","<p>"+I(r"1\leqq x\leqq e^{%s}"%L(k))+" で "+I(r"\log x\geqq0")+"。</p>"+D(r"S=\int_1^{e^{%s}}\log x\,dx"%L(k))+fig),
        ("不定積分（部分積分）",D(r"\int\log x\,dx=x\log x-x")),
        ("代入",D(r"S=\left[x\log x-x\right]_1^{e^{%s}}=\left(%se^{%s}-e^{%s}\right)-(0-1)=%s"%(L(k),L(k),L(k),L(k),r"%s"%(("(%s)e^{%s}+1"%(L(k-1),L(k))) if k>2 else "e^{%s}+1"%L(k)))))]
    return r"曲線 $y=\log x$、$x$ 軸、直線 $x=e^{%s}$ で囲まれた部分の面積を求めよ。"%L(k),st,(r"(%s)e^{%s}+1"%(L(k-1),L(k)) if k>2 else r"e^{%s}+1"%L(k))
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"対数曲線と軸で囲まれた面積",o,r"<p>$\int\log x\,dx=x\log x-x+C$（部分積分で $1\cdot\log x$ とみる）。端点 $x=e^k$ では $\log e^k=k$。</p>","$\\log x$ は「1×$\\log x$」と見て部分積分する裏ワザ。",4)
# 5 回転体の体積
def b5(k):
    V=sp.pi*(sp.exp(2*k)-1)/(2*k); v=sp.pi*sp.integrate(sp.exp(2*k*x),(x,0,1)); assert sp.simplify(v-V)==0
    st=[("体積の公式","<p>$x$ 軸のまわりの回転体：</p>"+D(r"V=\pi\int_a^b\{f(x)\}^2dx")),
        ("積分の式",D(r"V=\pi\int_0^1\left(e^{%sx}\right)^2dx=\pi\int_0^1e^{%sx}dx"%(L(k),L(2*k)))),
        ("計算",D(r"V=\pi\left[\dfrac{e^{%sx}}{%s}\right]_0^1=\dfrac{\pi\left(e^{%s}-1\right)}{%s}"%(L(2*k),L(2*k),L(2*k),L(2*k))))]
    return r"曲線 $y=e^{%sx}\ (0\leqq x\leqq1)$ と $x$ 軸、$y$ 軸、直線 $x=1$ で囲まれた部分を $x$ 軸のまわりに回転してできる立体の体積を求めよ。"%L(k),st,r"\dfrac{\pi\left(e^{%s}-1\right)}{%s}"%(L(2*k),L(2*k))
V=[R(5,2),2,3,R(3,2),4]
o=[b5(v) for v in V]
build(Z,CH,"回転体の体積",o,r"<p>$x$ 軸のまわりの回転体の体積は $V=\pi\displaystyle\int_a^b y^2dx$。$y^2$ を先に計算してから積分。</p>","輪切りにした円板（面積 $\\pi y^2$）を積み重ねる。",5)
UNIT=finish(Z,CH,2,1,"積分法","定積分と面積・体積","定積分の計算、面積、回転体の体積まで、積分法の応用の難問に挑みます。",subject="3")
