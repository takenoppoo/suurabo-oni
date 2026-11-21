# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational
X,Y,T=sp.symbols('x y t'); _c=[0]
def v2(a): return r"\left(%s,\ %s\right)"%(L(a[0]),L(a[1]))
# 例題1 媒介変数の消去
def b1(p,q,r,s,u):
    xt=p*T+q; yt=r*T**2+s*T+u; yx=sp.expand(yt.subs(T,(X-q)/p)); 
    for tv in (-2,-1,0,1,3): assert (yx.subs(X,xt.subs(T,tv))-yt.subs(T,tv))==0
    _c[0]+=1
    def dr(ax):
        tt=np.linspace(-3,3,300); ax.plot([float(xt.subs(T,v)) for v in tt],[float(yt.subs(T,v)) for v in tt],color="#b81f36",lw=2)
        for tv in (-1,0,1,2): ax.plot(float(xt.subs(T,tv)),float(yt.subs(T,tv)),"o",color="#222",ms=4.5); ax.text(float(xt.subs(T,tv))+.15,float(yt.subs(T,tv))+.3,"t=%d"%tv,fontsize=9)
    fig=plane("ic22_a%d"%_c[0],(-7,7),(-4,10),dr,size=(3.8,3.4),w=46)
    st=[("$t$ を $x$ で表す",D(r"x=%s\ \Rightarrow\ t=%s"%(L(xt),L(sp.expand((X-q)/p))))),
        ("$y$ に代入する",D(r"y=%s=%s"%(L(yt.subs(T,sp.Symbol('(t)'))) if False else L(yt),L(yt.subs(T,(X-q)/p))))),
        ("展開して整理する",D(r"y=%s"%L(yx))+"<p>$t$ はすべての実数をとり $x$ もすべての実数をとるので、<b>放物線全体</b>になる。</p>"+fig)]
    return r"媒介変数 $t$ で表された曲線 $x=%s,\ y=%s$ を、$x,\ y$ の方程式で表せ。"%(L(xt),L(yt)),st,r"y=%s"%L(yx)
V=[(1,1,1,-2,0),(2,-1,1,1,0),(1,-2,-1,4,1),(2,0,1,-4,3),(-1,3,2,1,-2)]
o=[b1(*x_) for x_ in V]
build(Z,CH,"媒介変数表示の曲線（消去）",o,r"<p>$x=f(t)$ を $t$ について解き、$y=g(t)$ に代入して <b>$t$ を消去</b>する。$t$ のとりうる範囲から、$x,y$ の範囲に制限がつかないか確認する。</p>","$t$ は「時刻」。時刻を消して、描かれる軌跡の式だけを残す。",1)
# 例題2 円の媒介変数と最大最小
def b2(h,k,r,a):
    R_=r*sp.sqrt(1+a**2); mx=h+a*k+R_; mn=h+a*k-R_
    th=np.linspace(0,2*np.pi,200001); vals=h+r*np.cos(th)+a*(k+r*np.sin(th)); assert abs(vals.max()-float(mx))<1e-6 and abs(vals.min()-float(mn))<1e-6
    _c[0]+=1
    def dr(ax):
        t=np.linspace(0,2*np.pi,300); ax.plot(h+r*np.cos(t),k+r*np.sin(t),color="#b81f36",lw=2)
        xs=np.array([-8,8]); 
        for val,col in ((float(mx),"#1f6fb8"),(float(mn),"#1f6fb8")): ax.plot(xs,(val-xs)/a,color=col,ls="--",lw=1.2)
    M=r+max(abs(h),abs(k))+2
    fig=plane("ic22_b%d"%_c[0],(-M-1,M+1),(-M-1,M+1),dr,size=(3.6,3.4),w=44,step=max(1,int(M)//4))
    st=[("円を媒介変数で表す","<p>円 "+I(r"(x-%s)^2+(y-%s)^2=%d"%(P(h),P(k),r**2))+" 上の点は</p>"+D(r"x=%s+%d\cos\theta,\quad y=%s+%d\sin\theta"%(L(h),r,L(k),r))),
        ("1次式を $\\theta$ で表す",D(r"x%s%sy=%s+%d\cos\theta%s%s\left(%s+%d\sin\theta\right)"%("+" if a>0 else "",cf(a) if a!=1 else "",L(h),r,"+" if a>0 else "",cf(a),L(k),r)) if a!=1 else D(r"x+y=%s+%d\cos\theta+%s+%d\sin\theta"%(L(h),r,L(k),r))),
        ("三角関数の合成",D(r"x+%sy=%s+%d\left(\cos\theta+%s\sin\theta\right)=%s+%s\sin(\theta+\alpha)"%(cf(a),L(h+a*k),r,cf(a),L(h+a*k),L(R_)))+"<p>"+I(r"\sqrt{1+%d^2}=\sqrt{%d}"%(a,1+a**2))+" を使った。</p>"),
        ("最大・最小","<p>"+I(r"-1\leqq\sin(\theta+\alpha)\leqq1")+" より</p>"+D(r"\text{最大値 }%s,\qquad \text{最小値 }%s"%(L(sp.simplify(mx)),L(sp.simplify(mn))))+fig)]
    return r"点 $P(x,y)$ が円 $(x-%s)^2+(y-%s)^2=%d$ 上を動くとき、$x+%sy$ の最大値と最小値を求めよ。"%(P(h),P(k),r**2,cf(a)),st,r"\text{最大 }%s,\ \text{最小 }%s"%(L(sp.simplify(mx)),L(sp.simplify(mn)))
V=[(1,2,2,1),(0,0,5,2),(-1,1,2,2),(2,0,3,1),(1,-1,1,3)]
o=[b2(*x_) for x_ in V]
build(Z,CH,"円上の点の1次式の最大・最小",o,r"<p>円 $(x-h)^2+(y-k)^2=r^2$ 上の点は $x=h+r\cos\theta,\ y=k+r\sin\theta$。1次式 $x+ay$ に代入して $\cos\theta+a\sin\theta$ を<b>合成</b>し、$-1\leqq\sin\leqq1$ で最大・最小。</p>","円周上の点を角 $\\theta$ 1つで表せば、あとは三角関数の最大・最小。",2)
# 例題3 極座標
PI=sp.pi
P1=[(4,PI/6),(2,PI/3),(6,3*PI/4),(3,PI),(2,3*PI/2)]
P2=[(1,1),(-1,sp.sqrt(3)),(sp.sqrt(3),-1),(-2,-2),(0,3)]
def b3(i):
    r,th=P1[i]; xx=sp.simplify(r*sp.cos(th)); yy=sp.simplify(r*sp.sin(th)); x2,y2=P2[i]; r2=sp.sqrt(x2**2+y2**2); th2=sp.atan2(y2,x2); 
    if th2<0: th2+=2*PI
    assert abs(float(r2*sp.cos(th2))-float(x2))<1e-9
    st=[("極座標→直交座標","<p>"+I(r"x=r\cos\theta,\quad y=r\sin\theta")+"。</p>"+D(r"x=%s\cos%s=%s,\quad y=%s\sin%s=%s"%(L(r),L(th),L(xx),L(r),L(th),L(yy)))+D(r"\left(%s,\ %s\right)"%(L(xx),L(yy)))),
        ("直交座標→極座標：$r$","<p>"+I(r"r=\sqrt{x^2+y^2}")+"。</p>"+D(r"r=\sqrt{%s^2+%s^2}=%s"%(P(x2),P(y2),L(r2)))),
        ("直交座標→極座標：$\\theta$","<p>"+I(r"\cos\theta=\dfrac xr,\ \sin\theta=\dfrac yr")+"。</p>"+D(r"\cos\theta=%s,\quad \sin\theta=%s\ \Rightarrow\ \theta=%s\quad(0\leqq\theta<2\pi)"%(L(sp.simplify(x2/r2)),L(sp.simplify(y2/r2)),L(th2)))+D(r"\left(%s,\ %s\right)"%(L(r2),L(th2))))]
    return r"(1) 極座標が $\left(%s,\ %s\right)$ である点の直交座標を求めよ。(2) 直交座標が $%s$ である点の極座標 $(r,\theta)$ を、$r>0,\ 0\leqq\theta<2\pi$ で求めよ。"%(L(r),L(th),v2(P2[i])),st,r"\text{(1) }%s\quad\text{(2) }\left(%s,\ %s\right)"%(v2((xx,yy)),L(r2),L(th2))
o=[b3(i) for i in range(5)]
build(Z,CH,"極座標と直交座標の変換",o,r"<p>$x=r\cos\theta,\ y=r\sin\theta$。逆に $r=\sqrt{x^2+y^2}$、$\cos\theta=\dfrac xr,\ \sin\theta=\dfrac yr$ から $\theta$ を決める（<b>象限に注意</b>）。</p>","原点からの「距離」と「向き」で場所を言うのが極座標。縦横の歩数で言うのが直交座標。",3)
# 例題4 極方程式
def b4(i):
    cases=[(r"r=4\cos\theta",r"x^2+y^2=4x",r"(x-2)^2+y^2=4",r"\text{中心 }(2,0)\text{、半径 }2\text{ の円}",lambda th:4*math.cos(th),"両辺に $r$ をかけて"),
           (r"r=6\sin\theta",r"x^2+y^2=6y",r"x^2+(y-3)^2=9",r"\text{中心 }(0,3)\text{、半径 }3\text{ の円}",lambda th:6*math.sin(th),"両辺に $r$ をかけて"),
           (r"r\cos\theta=3",r"x=3",r"x=3",r"\text{直線 }x=3",None,"$r\\cos\\theta=x$ より"),
           (r"r(\cos\theta+\sin\theta)=2",r"x+y=2",r"x+y=2",r"\text{直線 }x+y=2",None,"$r\\cos\\theta=x,\\ r\\sin\\theta=y$ より"),
           (r"r^2\cos2\theta=8",r"x^2-y^2=8",r"x^2-y^2=8",r"\text{双曲線 }x^2-y^2=8",None,"$\\cos2\\theta=\\cos^2\\theta-\\sin^2\\theta$ より")]
    pe,mid,final,desc,fn,how=cases[i]
    mids={0:r"r^2=4r\cos\theta",1:r"r^2=6r\sin\theta",2:r"x=3",3:r"r\cos\theta+r\sin\theta=2",4:r"r^2\cos^2\theta-r^2\sin^2\theta=8"}[i]
    st=[("置き換えの準備","<p>"+I(r"x=r\cos\theta,\ y=r\sin\theta,\ x^2+y^2=r^2")+" を使う。"+how+"</p>"+D(mids)),
        ("$x,\\ y$ で書く",D(mid)),
        ("整理して図形を判定",D(final)+"<p>"+I(desc)+"。</p>")]
    return r"極方程式 $%s$ が表す曲線を、直交座標 $x,\ y$ の方程式で表せ。また、どんな図形か答えよ。"%pe,st,r"%s\ \ (%s)"%(final,desc)
o=[b4(i) for i in range(5)]
build(Z,CH,"極方程式を直交座標の方程式に直す",o,r"<p>$r\cos\theta=x$、$r\sin\theta=y$、$r^2=x^2+y^2$ を使って $x,y$ の式に直す。$r=\cdots\cos\theta$ や $r=\cdots\sin\theta$ は<b>両辺に $r$ をかける</b>と置き換えられる。</p>","極座標の言葉（$r,\\theta$）を、縦横の言葉（$x,y$）に翻訳する。",4)
# 例題5 中点の軌跡
def b5(p,q):
    ym=sp.expand(((2*X-p)**2+q)/2)
    for tv in (-2,0,1,3): assert ym.subs(X,R(tv+p,2))==R(tv**2+q,2)
    _c[0]+=1
    def dr(ax):
        t=np.linspace(-3,5,300); ax.plot(t,t**2,color="#1f6fb8",lw=1.4,ls="--"); xs=np.linspace(-1.5,4.5,300); ax.plot(xs,[float(ym.subs(X,v)) for v in xs],color="#b81f36",lw=2)
        ax.plot(p,q,"o",color="#222",ms=5); ax.text(p+.2,q+.3,"A",fontsize=11)
    fig=plane("ic22_e%d"%_c[0],(-3,6),(-3,11),dr,size=(3.8,3.4),w=46)
    st=[("動点を媒介変数 $t$ で表す","<p>$P$ は放物線 "+I("y=x^2")+" 上なので "+I("P(t,t^2)")+"。</p>"),
        ("中点 $M$ の座標",D(r"M\left(\dfrac{t+%s}{2},\ \dfrac{t^2+%s}{2}\right)"%(P(p),P(q)))+"<p>"+I(r"M(x,y)")+" とおく。</p>"+D(r"x=\dfrac{t+%s}{2},\quad y=\dfrac{t^2+%s}{2}"%(P(p),P(q)))),
        ("$t$ を消去する",D(r"t=2x-%s\ \Rightarrow\ y=\dfrac{(2x-%s)^2+%s}{2}"%(P(p),P(p),P(q)))+D(r"y=%s"%L(ym))+"<p>$t$ はすべての実数なので、放物線全体。</p>"+fig)]
    return r"点 $A(%d,\ %d)$ と放物線 $y=x^2$ 上の動点 $P$ を結ぶ線分 $AP$ の中点 $M$ の軌跡の方程式を求めよ。"%(p,q),st,r"y=%s"%L(ym)
V=[(2,0),(4,2),(-2,2),(0,-4),(1,3)]
o=[b5(*x_) for x_ in V]
build(Z,CH,"中点の軌跡（媒介変数の利用）",o,r"<p>動点を<b>媒介変数</b>で表し、求める点の座標 $x,y$ を $t$ で表して $t$ を消去する。動点が通る範囲から、軌跡全体か一部かも確認する。</p>","動点を $t$ で追いかけ、中点の動きの式から $t$ だけを消す。",5)
UNIT=finish(Z,CH,1,1,"平面上の曲線と複素数平面","媒介変数表示・極座標","媒介変数の消去、円の媒介変数と最大・最小、極座標、極方程式、中点の軌跡まで、曲線の難問に挑みます。",subject="C")
