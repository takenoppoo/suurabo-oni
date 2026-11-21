# -*- coding: utf-8 -*-
from bh import *
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; s=sp.symbols("s")
def V(a,b): return r"\begin{pmatrix}%s\\%s\end{pmatrix}"%(L(a),L(b))
# 6 点が一直線上
def b6(a,b,p,q):
    # OP = x OA + y OB ; A,B,P collinear -> x+y=1 ; given OP = (p/q)... solve: OP=sOA+tOB with condition ... 
    # P divides AB 3:2 ... generic: OP = k OA + (1/3)*OB collinear with A,B -> k=2/3
    t=R(a,b)
    k=1-t
    st=[("一直線の条件","<p>点 "+I("P")+" が直線 "+I("AB")+" 上 "+I(r"\iff \overrightarrow{OP}=x\overrightarrow{OA}+y\overrightarrow{OB},\ x+y=1")+"。</p>"),
        ("係数の和が1","<p>"+D(r"\overrightarrow{OP}=k\overrightarrow{OA}+%s\overrightarrow{OB}\ \Rightarrow\ k+%s=1"%(L(t),L(t)))),
        ("$k$",D(r"k=%s"%L(k)))]
    return r"$\triangle OAB$ に対して $\overrightarrow{OP}=k\overrightarrow{OA}+%s\overrightarrow{OB}$ とする。3点 $A,\ B,\ P$ が一直線上にあるとき、$k$ の値を求めよ。また $P$ は線分 $AB$ をどのような比に内分するか。"%L(t),st,r"k=%s,\ AP:PB=%s:%s"%(L(k),L(t),L(k))
o=[b6(a,b,0,0) for a,b in [(1,3),(2,5),(3,4),(1,4),(2,7)]]
build(Z,CH,"3点が一直線上にある条件（係数の和＝1）",o,"<p>$\\overrightarrow{OP}=x\\overrightarrow{OA}+y\\overrightarrow{OB}$ で <b>$x+y=1$</b> ならば $P$ は直線 $AB$ 上。さらに $x,y>0$ なら線分 $AB$ を $y:x$ に内分。</p>","係数の合計が1なら、2点を結ぶ直線から外れない。",6)
# 7 2直線の交点を s,t で
def b7(a1,a2,b1,b2,ra,rb):
    # OA=(a1,a2)... triangle O A B, P on OA with OP=ra OA, Q on OB with OQ=rb OB ; AQ and BP intersect: OX
    A=sp.Matrix([a1,a2]); B=sp.Matrix([b1,b2]); P=ra*A; Q=rb*B
    u,v=sp.symbols("u v")
    X1=A+u*(Q-A); X2=B+v*(P-B)
    sol=sp.solve(list(X1-X2),[u,v],dict=True)[0]
    X=X1.subs(sol)
    # coefficients in OA,OB
    cA=1-sol[u]; cB=sol[u]*rb
    st=[("2通りに表す","<p>"+I("AQ")+" 上："+I(r"\overrightarrow{OX}=(1-u)\overrightarrow{OA}+u\,%s\overrightarrow{OB}"%L(rb))+"。<br>"+I("BP")+" 上："+I(r"\overrightarrow{OX}=%s\,v\,\overrightarrow{OA}+(1-v)\overrightarrow{OB}"%L(ra))+"。</p>"),
        ("係数比較","<p>"+I(r"\overrightarrow{OA},\overrightarrow{OB}")+" は1次独立なので</p>"+D(r"1-u=%s\,v,\qquad %s\,u=1-v"%(L(ra),L(rb)))),
        ("解く","<p>"+D(r"u=%s,\quad v=%s"%(L(sol[u]),L(sol[v])))+"</p><p>"+D(r"\overrightarrow{OX}=%s\overrightarrow{OA}+%s\overrightarrow{OB}"%(L(cA),L(cB)))+"</p>")]
    return r"$\triangle OAB$ で、辺 $OA$ 上に $OP:PA=%s$、辺 $OB$ 上に $OQ:QB=%s$ となる点 $P,Q$ をとる。線分 $AQ$ と $BP$ の交点を $X$ とするとき、$\overrightarrow{OX}$ を $\overrightarrow{OA},\overrightarrow{OB}$ で表せ。"%("%s:%s"%(ra.p,ra.q-ra.p),"%s:%s"%(rb.p,rb.q-rb.p)),st,r"\overrightarrow{OX}=%s\overrightarrow{OA}+%s\overrightarrow{OB}"%(L(cA),L(cB))
o=[b7(1,0,0,1,R(1,2),R(1,3)),b7(1,0,0,1,R(1,3),R(1,2)),b7(1,0,0,1,R(2,3),R(1,4)),b7(1,0,0,1,R(1,4),R(2,3)),b7(1,0,0,1,R(2,5),R(1,2))]
build(Z,CH,"2つの線分の交点の位置ベクトル",o,"<p>交点を<b>2通りの式</b>（それぞれの直線上の点として）で表し、$\\overrightarrow{OA},\\overrightarrow{OB}$ の<b>係数を比較</b>する。</p>","同じ点を2つの道で書き、同じ場所になる条件を使う。",7)
# 8 内積の最大・最小 |a+tb|
def b8(a,b):
    A=np.array(a,dtype=float);B=np.array(b,dtype=float)
    tt=sp.symbols("t")
    Av=sp.Matrix(a);Bv=sp.Matrix(b)
    f=sp.expand((Av+tt*Bv).dot(Av+tt*Bv)); t0=sp.solve(sp.diff(f,tt),tt)[0]; mn=f.subs(tt,t0)
    for t_ in np.linspace(-5,5,1001): assert float(f.subs(tt,t_))>=float(mn)-1e-9
    st=[("2乗する","<p>"+D(r"|\vec a+t\vec b|^2=|\vec a|^2+2t\,\vec a\cdot\vec b+t^2|\vec b|^2=%s"%L(f))),
        ("平方完成","<p>"+D(r"%s\left(t%s\right)^2+%s"%(L(Bv.dot(Bv)),L(-t0) if t0!=0 else "",L(mn)))+"</p>"),
        ("最小","<p>"+I("t=%s"%L(t0))+" のとき "+I("|\\vec a+t\\vec b|^2=%s"%L(mn))+"、最小値は "+I(L(sp.sqrt(mn)))+"。</p>")]
    return r"$\vec a=(%d,%d),\ \vec b=(%d,%d)$ とする。実数 $t$ が変化するとき、$|\vec a+t\vec b|$ の最小値と、そのときの $t$ の値を求めよ。"%(a[0],a[1],b[0],b[1]),st,r"t=%s,\ \text{最小値 }%s"%(L(t0),L(sp.sqrt(mn)))
o=[b8(*v) for v in [((3,1),(1,2)),((2,4),(1,1)),((5,0),(1,2)),((1,3),(2,-1)),((4,2),(1,3))]]
build(Z,CH,"|a+tb| の最小値",o,"<p>$|\\vec a+t\\vec b|^2$ を<b>2乗して $t$ の2次式</b>にし、平方完成。幾何的には $\\vec a$ から直線への垂線の長さ。</p>","直線上を動く点と定点の最短距離。",8)
# 9 重心・内心
def b9(a,b,c):
    # triangle with sides a,b,c : incenter OI=(aOA+bOB+cOC)/(a+b+c)
    A=np.array([0,0.]);B=np.array([c,0.]); 
    # place triangle: AB=c, BC=a, CA=b
    x=(b*b+c*c-a*a)/(2*c); y=math.sqrt(max(b*b-x*x,0)); C=np.array([x,y])
    I_=(a*A+b*B+c*C)/(a+b+c)
    # distances to sides equal
    def dist(P,Q,Rr): 
        d=Q-P; n=np.array([-d[1],d[0]]); n/=np.linalg.norm(n); return abs((Rr-P)@n)
    r1=dist(A,B,I_);r2=dist(B,C,I_);r3=dist(C,A,I_); assert abs(r1-r2)<1e-9 and abs(r2-r3)<1e-9
    fg=geo("xc11_9_%d_%d_%d"%(a,b,c),polys=[([tuple(A),tuple(B),tuple(C)],"#b81f36")],circles=[(I_[0],I_[1],r1,"#1f6fb8","-")],pts=[("A",A[0],A[1],-.4,-.4),("B",B[0],B[1],.4,-.4),("C",C[0],C[1],0,.5),("I",I_[0],I_[1],0,.0,True)],w=44,size=(3.6,3))
    st=[("内心の位置ベクトル","<p>"+I(r"BC=%d,\ CA=%d,\ AB=%d"%(a,b,c))+"。角の二等分線の比から："+D(r"\overrightarrow{AI}=\dfrac{%d\,\overrightarrow{AA}+%d\,\overrightarrow{AB}+%d\,\overrightarrow{AC}}{%d+%d+%d}=\dfrac{%d\overrightarrow{AB}+%d\overrightarrow{AC}}{%d}"%(a,c,b,a,b,c,c,b,a+b+c))+fg),
        ("重心との違い","<p>重心は "+I(r"\dfrac{\overrightarrow{AB}+\overrightarrow{AC}}{3}")+"（係数が等しい）。内心は<b>向かい合う辺の長さ</b>が係数。</p>")]
    return r"$\triangle ABC$ で $BC=%d,\ CA=%d,\ AB=%d$ とする。内心 $I$ について $\overrightarrow{AI}$ を $\overrightarrow{AB},\ \overrightarrow{AC}$ で表せ。"%(a,b,c),st,r"\overrightarrow{AI}=\dfrac{%d}{%d}\overrightarrow{AB}+\dfrac{%d}{%d}\overrightarrow{AC}"%(b,a+b+c,c,a+b+c) if False else r"\overrightarrow{AI}=%s\overrightarrow{AB}+%s\overrightarrow{AC}"%(L(R(b,a+b+c)),L(R(c,a+b+c)))
o=[b9(*v) for v in [(5,4,3),(13,14,15) if False else (7,5,6),(5,5,6),(13,12,5),(10,8,6)]]
build(Z,CH,"内心の位置ベクトル",o,"<p>内心 $I$ は $\\dfrac{a\\overrightarrow{OA}+b\\overrightarrow{OB}+c\\overrightarrow{OC}}{a+b+c}$（$a,b,c$ は各頂点の<b>向かい側の辺の長さ</b>）。角の二等分線が対辺を隣辺の比に分ける定理から導かれる。</p>","長い辺に向かい合う頂点ほど、内心を引っぱる力が強い。",9)
# 10 垂直・平行条件
def b10(a,b,c):
    # find t such that a + t b ⟂ c  / parallel
    Av=sp.Matrix(a);Bv=sp.Matrix(b);Cv=sp.Matrix(c); t=sp.symbols("t")
    tp=sp.solve((Av+t*Bv).dot(Cv),t)[0]
    st=[("垂直条件","<p>"+I(r"(\vec a+t\vec b)\cdot\vec c=0")+"。</p>"+D(r"(%d+%dt)\cdot%d+(%d+%dt)\cdot%d=0"%(a[0],b[0],c[0],a[1],b[1],c[1]))),
        ("解く",D(r"%s\,t%+d=0\ \Rightarrow\ t=%s"%(L(Bv.dot(Cv)),Av.dot(Cv),L(tp))))]
    return r"$\vec a=(%d,%d),\ \vec b=(%d,%d),\ \vec c=(%d,%d)$ のとき、$\vec a+t\vec b$ が $\vec c$ と垂直になるような実数 $t$ の値を求めよ。"%(a+b+c),st,r"t=%s"%L(tp)
o=[b10(*v) for v in [((3,1),(1,2),(2,1)),((1,4),(2,-1),(3,2)),((2,5),(1,3),(1,2)),((4,1),(1,1),(1,3)),((5,2),(2,1),(1,4))]]
build(Z,CH,"a+tb が c と垂直になる t",o,"<p>垂直 $\\iff$ 内積 $=0$。$(\\vec a+t\\vec b)\\cdot\\vec c=0$ を成分で書いて $t$ の1次方程式に。</p>","直角のサインは、内積がゼロ。",10)
XU=finishx(Z,CH)
