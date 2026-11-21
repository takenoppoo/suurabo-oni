# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,y,t=sp.symbols("x y t")
def conic(ax,a,b,kind="ell"):
    th=np.linspace(0,2*np.pi,400)
    if kind=="ell": ax.plot(a*np.cos(th),b*np.sin(th),color="#b81f36",lw=2)
# 6 楕円の接線（傾き指定）
def b6(a2,b2,m):
    # x^2/a2 + y^2/b2 =1 ; tangent with slope m : y=mx±sqrt(a2 m^2 + b2)
    c2=a2*m*m+b2; c=sp.sqrt(c2)
    # verify tangency: substituting gives discriminant 0
    X=sp.symbols("X"); f=sp.expand(X**2/a2+(m*X+c)**2/b2-1); assert sp.simplify(sp.discriminant(f,X))==0
    a_=math.sqrt(a2);b_=math.sqrt(b2); cf=float(c)
    def dr(ax):
        conic(ax,a_,b_); xs=np.linspace(-a_-1.5,a_+1.5,10)
        ax.plot(xs,m*xs+cf,color="#1f6fb8",lw=1.6); ax.plot(xs,m*xs-cf,color="#1f6fb8",lw=1.6)
    fg=gplane("xc21_6_%d_%d_%d"%(a2,b2,int(m*10)+30),(-a_-2,a_+2),(-b_-3.5,b_+3.5),dr,size=(4.4,3.2),w=54)
    st=[("直線を代入","<p>"+I("y=%sx+k"%L(m))+" を "+I(r"\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1"%(a2,b2))+" に代入して "+I("x")+" の2次方程式にする。</p>"),
        ("重解の条件（判別式 = 0）","<p>"+D(r"(%d+%d%s)x^2+%dkx%s+%d(k^2-%d)=0"%(b2,a2,"m^2"if False else "\\cdot%s"%L(m*m),2*a2*m if False else 0,"",0,0)) if False else "<p>"+D(r"%s"%L(sp.expand(X**2/a2+(m*X+sp.Symbol("k"))**2/b2-1)*a2*b2)+"=0")+"</p><p>"+I("D=0")+" より："+D(r"k^2=%d\cdot%s+%d=%s"%(a2,L(m*m),b2,L(c2)))+fg),
        ("接線",D(r"y=%sx\pm%s"%(L(m),L(c))))]
    return r"楕円 $\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1$ の接線で、傾きが $%s$ であるものの方程式を求めよ。"%(a2,b2,L(m)),st,r"y=%sx\pm%s"%(L(m),L(c))
o=[b6(*v) for v in [(9,4,1),(16,9,R(1,2)),(8,2,2) if False else (4,1,2),(25,9,1),(12,4,2) if False else (9,4,-1)]]
build(Z,CH,"傾きが与えられた楕円の接線",o,"<p>$y=mx+k$ を代入して $x$ の2次方程式にし、<b>判別式 $D=0$</b>。結果は $k^2=a^2m^2+b^2$（接線が2本）。</p>","同じ傾きの平行な接線は、上と下に1本ずつ。",6)
# 7 楕円上の点の焦点距離の和・積の最大
def b7(a,b):
    c=math.sqrt(a*a-b*b); assert abs(c-round(c))<1e-9; c=int(round(c))
    # PF1+PF2=2a ; product max when equal: a^2 ; min = b^2 (at vertex on major axis: (a-c)(a+c)=b^2)
    def dr(ax):
        conic(ax,a,b); mark(ax,c,0,"F",0,-.5); mark(ax,-c,0,"F'",0,-.5); mark(ax,a*.6,b*.8,"P",.4,.4)
        ax.plot([-c,a*.6,c],[0,b*.8,0],color="#333",lw=1.2,ls="--")
    fg=gplane("xc21_7_%d_%d"%(a,b),(-a-1.5,a+1.5),(-b-1.5,b+1.5),dr,size=(4.4,3),w=54)
    st=[("焦点","<p>"+I("c=\\sqrt{a^2-b^2}=%d"%c)+"。焦点 "+I("F(%d,0),\\ F'(-%d,0)"%(c,c))+"。</p>"+fg),
        ("距離の和","<p>楕円の定義：</p>"+D(r"PF+PF'=2a=%d"%(2*a))),
        ("積の最大","<p>相加・相乗平均：</p>"+D(r"PF\cdot PF'\leqq\left(\dfrac{PF+PF'}{2}\right)^2=%d"%(a*a))+"<p>等号は "+I("PF=PF'")+" のとき（"+I("P=(0,\\pm%d)"%b)+"）。最大値 "+I(str(a*a))+"。</p>")]
    return r"楕円 $\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1$ の2つの焦点を $F,F'$ とする。楕円上の点 $P$ について、$PF+PF'$ の値と、$PF\cdot PF'$ の最大値を求めよ。"%(a*a,b*b),st,r"PF+PF'=%d,\ \ PF\cdot PF'\text{の最大値 }%d"%(2*a,a*a)
o=[b7(*v) for v in [(5,3),(13,5),(5,4),(10,6),(17,15)]]
build(Z,CH,"楕円の2焦点からの距離の和と積",o,"<p>楕円の定義 $PF+PF'=2a$（定数）。積の最大は<b>相加・相乗平均</b>で $a^2$、$PF=PF'$ となる短軸の端点で達成。</p>","2本の糸の長さの合計が、ずっと同じ。",7)
# 8 双曲線の漸近線と接線で囲む三角形の面積
def b8(a,b):
    # tangent at P(x0,y0) of x^2/a^2 - y^2/b^2=1 ; triangle with asymptotes area = ab
    area=a*b
    x0=sp.Rational(5,4)*a; y0=sp.Rational(3,4)*b
    assert sp.simplify(x0**2/a**2-y0**2/b**2-1)==0
    def dr(ax):
        th=np.linspace(-1.5,1.5,300)
        ax.plot(a*np.cosh(th),b*np.sinh(th),color="#b81f36",lw=2); ax.plot(-a*np.cosh(th),b*np.sinh(th),color="#b81f36",lw=2)
        xs=np.linspace(-2*a,2*a,10); ax.plot(xs,b/a*xs,color="#999",ls="--"); ax.plot(xs,-b/a*xs,color="#999",ls="--")
        mark(ax,float(x0),float(y0),"P",.3,.4)
    fg=gplane("xc21_8_%d_%d"%(a,b),(-2*a,2*a),(-2*b,2*b),dr,size=(4.4,3.2),w=54)
    st=[("接線と漸近線","<p>"+I("P(%s,\\ %s)"%(L(x0),L(y0)))+" での接線：</p>"+D(r"\dfrac{%s\,x}{%d}-\dfrac{%s\,y}{%d}=1"%(L(x0),a*a,L(y0),b*b))+"<p>漸近線 "+I("y=\\pm\\dfrac{%d}{%d}x"%(b,a))+"。</p>"+fg),
        ("交点","<p>接線と2本の漸近線の交点 "+I("A,B")+"。双曲線の性質として、<b>三角形 OAB の面積は点 P によらず一定</b>で "+I("ab")+"。</p>"),
        ("面積",D(r"ab=%d\times%d=%d"%(a,b,area)))]
    return r"双曲線 $\dfrac{x^2}{%d}-\dfrac{y^2}{%d}=1$ 上の点 $P\left(%s,\ %s\right)$ における接線と、2本の漸近線とで囲まれる三角形（原点 $O$ を頂点にもつ）の面積を求めよ。"%(a*a,b*b,L(x0),L(y0)),st,str(area)
o=[b8(*v) for v in [(4,3),(2,1),(6,2),(4,2),(5,3)]]
build(Z,CH,"双曲線の接線と漸近線で囲む三角形の面積",o,"<p>双曲線 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1$ 上の任意の点での接線と漸近線で囲む三角形の面積は常に $ab$。実際に交点を求めて確認してもよい。</p>","どこで接しても、面積は変わらない不思議な性質。",8)
# 9 放物線の焦点を通る弦
def b9(p,m):
    # y^2=4px ; chord through focus (p,0) with slope m: length = 4p(1+m^2)/m^2
    X=sp.symbols("X"); line=m*(X-p); 
    f=sp.expand(line**2-4*p*X); rts=sp.solve(f,X)
    ys=[line.subs(X,r) for r in rts]; ch=sp.sqrt((rts[0]-rts[1])**2+(ys[0]-ys[1])**2)
    assert sp.simplify(ch-4*p*(1+m*m)/(m*m))==0
    def dr(ax):
        ys_=np.linspace(-6,6,300); ax.plot(ys_**2/(4*p),ys_,color="#b81f36",lw=2); xs=np.linspace(-.5,8,10); ax.plot(xs,float(m)*(xs-p),color="#1f6fb8"); mark(ax,p,0,"F",.3,-.6)
        ax.plot([-p,-p],[-6,6],color="#999",ls="--")
    fg=gplane("xc21_9_%d_%d"%(p,int(m*10)),(-p-1,9),(-6,6),dr,size=(4.4,3),w=54)
    st=[("焦点と直線","<p>放物線 "+I("y^2=%dx"%(4*p))+" の焦点 "+I("F(%d,0)"%p)+"。直線 "+I("y=%s(x-%d)"%(L(m),p))+"。</p>"+fg),
        ("交点の x 座標","<p>"+D(r"%s=0\ \Rightarrow\ x=%s"%(L(f),r",\ ".join(L(r) for r in rts)))+"</p>"),
        ("弦の長さ","<p>焦点を通る弦は "+I("AB=x_1+x_2+2p")+"（準線までの距離の和）。</p>"+D(r"AB=%s+%d=%s"%(L(sum(rts)),2*p,L(ch))))]
    return r"放物線 $y^2=%dx$ の焦点を通り、傾き $%s$ の直線が放物線と交わる2点を $A,B$ とする。弦 $AB$ の長さを求めよ。"%(4*p,L(m)),st,L(ch)
o=[b9(*v) for v in [(1,1),(1,2),(2,1),(1,R(1,2)),(2,2)]]
build(Z,CH,"放物線の焦点を通る弦の長さ",o,"<p>焦点を通る弦の長さは <b>$AB=x_1+x_2+2p$</b>（各点から焦点までの距離 = 準線までの距離 $x+p$ の和）。$x_1+x_2$ は2次方程式の解と係数の関係。</p>","焦点までの距離は、準線までの距離と等しい。",9)
# 10 離心率
def b10(a,c):
    e=R(c,a); b2=a*a-c*c
    def dr(ax):
        conic(ax,a,math.sqrt(b2)); mark(ax,c,0,"F",0,-.5); mark(ax,-c,0,"F'",0,-.5)
    fg=gplane("xc21_10_%d_%d"%(a,c),(-a-1.5,a+1.5),(-a,a),dr,size=(4.2,3),w=50)
    st=[("離心率","<p>"+D(r"e=\dfrac ca=\dfrac{%d}{%d}=%s"%(c,a,L(e)))+"</p>"),
        ("短軸","<p>"+D(r"b^2=a^2-c^2=%d-%d=%d"%(a*a,c*c,b2))+fg),
        ("方程式","<p>"+D(r"\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1"%(a*a,b2)))]
    return r"焦点が $(\pm%d,\ 0)$、長軸の長さが $%d$ の楕円の方程式と離心率を求めよ。"%(c,2*a),st,r"\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1,\ \ e=%s"%(a*a,b2,L(e))
o=[b10(*v) for v in [(5,3),(13,5),(10,6),(17,8),(25,7)]]
build(Z,CH,"焦点と長軸から楕円の方程式・離心率",o,"<p>長軸の長さ $2a$、焦点 $(\\pm c,0)$ から $b^2=a^2-c^2$。離心率 $e=\\dfrac ca$（$0<e<1$）。$e$ が $0$ に近いほど円に近い。</p>","c/a が大きいほど、つぶれた楕円。",10)
XU=finishx(Z,CH)
