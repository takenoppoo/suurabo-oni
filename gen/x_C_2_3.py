# -*- coding: utf-8 -*-
from bh import *
import numpy as np, math, cmath
Z=U_(); CH=[]; R=sp.Rational; I_=sp.I; z=sp.symbols("z")
def cx(v): return L(sp.nsimplify(sp.simplify(v)))
# 6 回転
def b6(al,be,deg):
    th=sp.rad(deg); w=sp.simplify(al+(sp.cos(th)+I_*sp.sin(th))*(be-al)); w=sp.expand(sp.simplify(w))
    A=complex(al);B=complex(be);W=complex(w)
    assert abs(abs(W-A)-abs(B-A))<1e-9
    lim=max(abs(A),abs(B),abs(W))+1.5
    fg=geo("xc23_6_%d"%(abs(hash((str(al),str(be),deg)))%100000),segs=[(A.real,A.imag,B.real,B.imag,"#333","-"),(A.real,A.imag,W.real,W.imag,"#b81f36","-")],pts=[("A",A.real,A.imag,-.4,-.4),("B",B.real,B.imag,.4,-.3),("C",W.real,W.imag,.0,.5)],w=42,size=(3.6,3))
    st=[("αを原点に移す","<p>"+D(r"\beta-\alpha=%s-(%s)=%s"%(cx(be),cx(al),cx(be-al)))),
        ("回転","<p>"+I(r"%d^\circ"%deg)+" 回転は "+I(r"\cos%d^\circ+i\sin%d^\circ=%s"%(deg,deg,cx(sp.cos(th)+I_*sp.sin(th))))+" をかける。</p>"+D(r"\gamma-\alpha=\left(%s\right)(%s)"%(cx(sp.cos(th)+I_*sp.sin(th)),cx(be-al)))),
        ("もとに戻す","<p>"+D(r"\gamma=\alpha+(\gamma-\alpha)=%s"%cx(w))+fg)]
    return r"複素数平面上で、点 $\beta=%s$ を、点 $\alpha=%s$ を中心に $%d^\circ$ 回転した点 $\gamma$ を求めよ。"%(cx(be),cx(al),deg),st,r"\gamma=%s"%cx(w)
o=[b6(*v) for v in [(1+I_,3+I_,90),(2,4+2*I_,60),(-1+2*I_,1+2*I_,90),(1,5,120) if False else (1-I_,4-I_,60),(2+I_,2+3*I_,-90)]]
build(Z,CH,"点を別の点のまわりに回転する",o,"<p>回転の中心 $\\alpha$ を原点に移し、$\\gamma-\\alpha=(\\cos\\theta+i\\sin\\theta)(\\beta-\\alpha)$。最後に $\\alpha$ を足す。</p>","中心を原点に平行移動 → 回す → 戻す。",6)
# 7 正三角形
def b7(al,be):
    d=be-al; g1=sp.expand(al+(R(1,2)+sp.sqrt(3)/2*I_)*d); g2=sp.expand(al+(R(1,2)-sp.sqrt(3)/2*I_)*d)
    A=complex(al);B=complex(be);G=complex(g1)
    assert abs(abs(G-A)-abs(B-A))<1e-9 and abs(abs(G-B)-abs(B-A))<1e-9
    fg=geo("xc23_7_%d"%(abs(hash((str(al),str(be))))%100000),polys=[([(A.real,A.imag),(B.real,B.imag),(G.real,G.imag)],"#b81f36")],pts=[("A",A.real,A.imag,-.4,-.3),("B",B.real,B.imag,.4,-.3),("C",G.real,G.imag,0,.5)],w=42,size=(3.6,3))
    st=[("α から見て 60°","<p>正三角形なので "+I(r"\gamma-\alpha")+" は "+I(r"\beta-\alpha")+" を "+I(r"\pm60^\circ")+" 回転したもの。</p>"+D(r"\gamma-\alpha=\left(\dfrac12\pm\dfrac{\sqrt3}{2}i\right)(\beta-\alpha)=\left(\dfrac12\pm\dfrac{\sqrt3}{2}i\right)(%s)"%cx(d))),
        ("2つの解","<p>"+D(r"\gamma=%s\quad\text{または}\quad \gamma=%s"%(cx(g1),cx(g2)))+fg)]
    return r"複素数平面上の2点 $\alpha=%s,\ \beta=%s$ を2頂点とする正三角形の第3の頂点 $\gamma$ をすべて求めよ。"%(cx(al),cx(be)),st,r"\gamma=%s,\ %s"%(cx(g1),cx(g2))
o=[b7(*v) for v in [(0,2),(1,1+4*I_),(1+I_,5+I_),(-1,3+2*I_) if False else (-2,2),(2*I_,2*I_+6)]]
build(Z,CH,"2点を頂点とする正三角形の第3の頂点",o,"<p>第3の頂点は、$\\beta-\\alpha$ を<b>$\\pm60^\\circ$ 回転</b>して $\\alpha$ を足した点（2つ）。$\\dfrac12\\pm\\dfrac{\\sqrt3}2i$ をかける。</p>","線分の両側に、正三角形のてっぺんが2つ。",7)
# 8 (z-α)/(z-β) が実数/純虚数
def b8(al,be):
    x,y=sp.symbols("x y",real=True); zz=x+I_*y
    w=sp.simplify((zz-al)/(zz-be)); num=sp.expand((zz-al)*sp.conjugate(zz-be))
    im=sp.simplify(sp.im(num)); re=sp.simplify(sp.re(num))
    st=[("共役をかける","<p>"+I("z=x+yi")+"、"+I(r"w=\dfrac{z-\alpha}{z-\beta}=\dfrac{(z-\alpha)\overline{(z-\beta)}}{|z-\beta|^2}")+"。</p>"),
        ("実数になる条件","<p>分子の虚部 "+I("=0")+"：</p>"+D(r"%s=0"%L(im))+"<p>3点 "+I(r"\alpha,\beta,z")+" が一直線上。</p>"),
        ("純虚数になる条件","<p>分子の実部 "+I("=0")+"（"+I(r"z\neq\alpha,\beta")+"）：</p>"+D(r"%s=0"%L(sp.expand(re)))+"<p>"+I(r"\alpha\beta")+" を直径とする円。</p>")]
    return r"複素数 $z$ について、$w=\dfrac{z-(%s)}{z-(%s)}$ が実数となる $z$ の軌跡と、純虚数となる $z$ の軌跡を求めよ。"%(cx(al),cx(be)),st,r"\text{実数：}%s=0,\ \ \text{純虚数：}%s=0"%(L(im),L(sp.expand(re)))
o=[b8(*v) for v in [(1,-1),(2*I_,-2*I_),(1+I_,3+I_),(-2,2),(I_,1)]]
build(Z,CH,"(z−α)/(z−β) が実数・純虚数となる z の軌跡",o,"<p>$\\dfrac{z-\\alpha}{z-\\beta}$ が実数 $\\iff$ 3点が一直線上、純虚数 $\\iff$ $\\angle\\alpha z\\beta=90^\\circ$（$\\alpha\\beta$ が直径の円）。式で確認するには分子に共役をかける。</p>","直線上なら実数、直角なら純虚数。",8)
# 9 |z| の最大・最小
def b9(c,r):
    c=sp.nsimplify(c); d=abs(complex(c)); mx=sp.simplify(sp.Abs(c)+r); mn=sp.simplify(abs(sp.Abs(c)-r))
    C=complex(c)
    fg=geo("xc23_9_%d"%(abs(hash((str(c),r)))%100000),circles=[(C.real,C.imag,r,"#b81f36","-")],segs=[(0,0,C.real,C.imag,"#333","--")],pts=[("O",0,0,-.4,-.4),("C",C.real,C.imag,.3,.4)],w=42,size=(3.6,3))
    st=[("図形","<p>"+I("|z-(%s)|=%d"%(cx(c),r))+" は中心 "+I("C(%s)"%cx(c))+"、半径 "+I(str(r))+" の円。"+I("|z|")+" は原点からの距離。</p>"+fg),
        ("中心との距離","<p>"+D(r"OC=|%s|=%s"%(cx(c),L(sp.Abs(c))))),
        ("最大・最小","<p>原点と中心を結ぶ直線上で：</p>"+D(r"\text{最大 }%s+%d=%s,\qquad \text{最小 }|%s-%d|=%s"%(L(sp.Abs(c)),r,L(mx),L(sp.Abs(c)),r,L(mn))))]
    return r"複素数 $z$ が $|z-(%s)|=%d$ をみたして動くとき、$|z|$ の最大値と最小値を求めよ。"%(cx(c),r),st,r"\text{最大 }%s,\ \text{最小 }%s"%(L(mx),L(mn))
o=[b9(*v) for v in [(3+4*I_,2),(6+8*I_,3),(5+12*I_,4),(8+6*I_,5),(4+3*I_,1)]]
build(Z,CH,"円上の点の |z| の最大・最小",o,"<p>$|z|$ は原点からの距離。円の中心 $C$ と原点を結ぶ直線が円と交わる2点が最も遠い点・近い点：$OC\\pm r$（原点が円の外にあるとき）。</p>","原点からのびる一直線が、円の最遠点と最近点を教える。",9)
# 10 z+1/z
def b10(k):
    # z+1/z = k -> z^2+1/z^2 = k^2-2 ; z^3+1/z^3 = k^3-3k
    a2=k*k-2; a3=k**3-3*k
    zs=sp.solve(z**2-k*z+1,z); 
    for zz in zs: assert sp.simplify(zz**3+zz**-3-a3)==0 or abs(complex(zz**3+zz**-3-a3))<1e-9
    st=[("2乗","<p>"+D(r"\left(z+\dfrac1z\right)^2=z^2+2+\dfrac1{z^2}\ \Rightarrow\ z^2+\dfrac1{z^2}=%s^2-2=%s"%(L(k),L(a2)))),
        ("3乗","<p>"+D(r"z^3+\dfrac1{z^3}=\left(z+\dfrac1z\right)^3-3\left(z+\dfrac1z\right)=%s-%s=%s"%(L(k**3),L(3*k),L(a3)))),
        ("確認","<p>"+I("z=%s"%(r",\ ".join(cx(v) for v in zs)))+" は "+I("z^2-%sz+1=0"%L(k))+" の解。</p>")]
    return r"$z+\dfrac1z=%s$ のとき、$z^2+\dfrac1{z^2},\ z^3+\dfrac1{z^3}$ の値を求めよ。"%L(k),st,r"%s,\ %s"%(L(a2),L(a3))
o=[b10(k) for k in [1,sp.sqrt(2),sp.sqrt(3),R(5,2),-1]]
build(Z,CH,"z+1/z の値から冪の和",o,"<p>$\\left(z+\\dfrac1z\\right)^2,\\ ^3$ を展開して $z^2+\\dfrac1{z^2},\\ z^3+\\dfrac1{z^3}$ を $k$ で表す。$k=2\\cos\\theta$ なら $z=\\cos\\theta\\pm i\\sin\\theta$（ド・モアブルと整合）。</p>","z と 1/z の和が決まれば、冪の和も芋づる式。",10)
XU=finishx(Z,CH)
