# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, itertools, math
Z=U_(); CH=[]; R=sp.Rational; x,y,k=sp.symbols("x y k")
def tri_fig(name,P,lab,extra=None,xr=(-1,9),yr=(-1,8),ln=None):
    def dr(ax):
        pts=[(float(a),float(b)) for a,b in P]
        ax.plot([p[0] for p in pts+[pts[0]]],[p[1] for p in pts+[pts[0]]],color="#b81f36",lw=2)
        for (a,b),t,(dx,dy) in zip(pts,lab,[(-.4,-.5),(.4,-.5),(0,.5)]): mark(ax,a,b,t,dx,dy)
        if extra: extra(ax)
    return gplane(name,xr,yr,dr,size=(4.2,3.2),w=50)
# 6 3点が一直線上
def b6(A,B,m):
    # C=(m, t)  collinear -> t
    t=sp.symbols("t"); slope=R(B[1]-A[1],B[0]-A[0]); val=A[1]+slope*(m-A[0])
    st=[("直線 AB の傾き","<p>"+D(r"\dfrac{%d-%d}{%d-%d}=%s"%(B[1],A[1],B[0],A[0],L(slope)))),
        ("C が直線 AB 上","<p>"+I("A,B,C")+" が一直線上 "+I(r"\iff")+" 直線 "+I("AC")+" の傾きも同じ。</p>"+D(r"\dfrac{t-%d}{%d-%d}=%s"%(A[1],m,A[0],L(slope)))),
        ("解く",D(r"t=%s"%L(val)))]
    return r"3点 $A(%d,%d),\ B(%d,%d),\ C(%d,t)$ が一直線上にあるとき、$t$ の値を求めよ。"%(A[0],A[1],B[0],B[1],m),st,r"t=%s"%L(val)
o=[b6(*v) for v in [((1,2),(4,8),7),((-1,3),(2,-3),5),((0,1),(3,4),-2),((2,-1),(5,5),4),((-3,2),(1,6),6)]]
build(Z,CH,"3点が一直線上にある条件",o,"<p>2点間の<b>傾きが等しい</b>（または直線 AB の式に C を代入）。</p>","同じ坂道の上にいるなら、どこでも傾きは同じ。",6)
# 7 三角形をつくらない
def b7(l1,l2,l3):
    # l: (a,b,c) a x+b y=c ; third has parameter k in a: (ka... )  l3=(a3,b3,c3) with k in b: l3 = x + k y = c3
    pass
def b7(c1,c2,c3):
    # lines: x+y=c1 ; x-y=c2 ; x+k y=c3  -> not forming triangle
    P=(R(c1+c2,2),R(c1-c2,2))
    kv=[]
    # parallel to x+y=c1: k=1 (c3!=c1); parallel to x-y: k=-1 ; pass through P: P.x+k P.y=c3
    k1,k2=1,-1; k3=sp.Rational(c3-P[0],1)/P[1] if P[1]!=0 else None
    kk=sorted({k1,k2,k3})
    # brute check with sympy: for each k test no triangle
    def tri(kv):
        Ls=[(1,1,c1),(1,-1,c2),(1,kv,c3)]
        if any(a*d-b*c_==0 for (a,b,_),(c_,d,_) in itertools.combinations(Ls,2)): return False
        return Ls[2][0]*P[0]+Ls[2][1]*P[1]!=c3
    for v in kk: assert not tri(v)
    assert tri(sp.Rational(7,3)) 
    fg=geo("x221_7_%d_%d_%d"%(c1,c2,c3),segs=[(-1,c1+1,c1+1,-1,"#b81f36","-"),(c2-2,-2,c2+4,4,"#1f6fb8","-")],pts=[("P",float(P[0]),float(P[1]),.4,.4)],w=42,size=(3.4,3),lim=(-1,c1+2,-2,c1+2)) if False else ""
    st=[("三角形ができない場合","<p>(1) 2直線が平行　(2) 3直線が1点で交わる。</p>"),
        ("平行になる $k$","<p>"+I("x+ky=%d"%c3)+" が "+I("x+y=%d"%c1)+" または "+I("x-y=%d"%c2)+" と平行："+I("k=1,\\ -1")+"。</p>"),
        ("1点で交わる","<p>"+I("x+y=%d"%c1)+"、"+I("x-y=%d"%c2)+" の交点 "+I("(%s,\\ %s)"%(L(P[0]),L(P[1])))+" を通る。</p>"+D(r"%s+%s\,k=%d\ \Longrightarrow\ k=%s"%(L(P[0]),L(P[1]),c3,L(k3)))),
        ("答え",D(r"k=%s"%(r",\ ".join(L(v) for v in kk))))]
    return r"3直線 $x+y=%d,\ x-y=%d,\ x+ky=%d$ が三角形をつくらないような定数 $k$ の値をすべて求めよ。"%(c1,c2,c3),st,r"k=%s"%(r",\ ".join(L(v) for v in kk))
o=[b7(*v) for v in [(6,2,5),(8,2,9),(4,0,7),(10,4,3),(6,-2,9)]]
build(Z,CH,"3直線が三角形をつくらない条件",o,"<p>三角形ができないのは<b>(1)どの2本かが平行　(2)3本が1点で交わる</b>のとき。それぞれ $k$ を求めて合わせる。</p>","平行か、1点集中。この2パターンを見落とさない。",7)
# 8 垂直二等分線
def b8(A,B):
    M=((A[0]+B[0])/2,(A[1]+B[1])/2); m=R(B[1]-A[1],B[0]-A[0]); 
    eq=sp.Eq(y-M[1],-1/m*(x-M[0])); f=sp.expand(sp.solve(eq,y)[0])
    X=(x-A[0])**2+(y-A[1])**2-((x-B[0])**2+(y-B[1])**2); g=sp.expand(X)
    assert sp.simplify(sp.solve(g,y)[0]-f)==0
    fg=geo("x221_8_%d_%d_%d_%d"%(A[0]+9,A[1]+9,B[0]+9,B[1]+9),segs=[(A[0],A[1],B[0],B[1],"#333","-"),(M[0]-3,float(f.subs(x,M[0]-3)),M[0]+3,float(f.subs(x,M[0]+3)),"#b81f36","-")],pts=[("A",A[0],A[1],-.4,.0),("B",B[0],B[1],.4,.0),("M",M[0],M[1],.4,-.4)],w=44,size=(3.4,3))
    st=[("中点と傾き","<p>"+"中点 "+I("M(%s,\\ %s)"%(L(M[0]),L(M[1])))+"、"+I("AB")+" の傾き "+I(L(m))+"。垂直なので傾きは "+I(L(-1/m))+"。</p>"+fg),
        ("直線の式",D(r"y-%s=%s(x-%s)"%(L(M[1]),L(-1/m),L(M[0])))),
        ("整理",D(r"y=%s"%L(f)))]
    return r"2点 $A(%d,%d),\ B(%d,%d)$ から等距離にある点の軌跡（線分 $AB$ の垂直二等分線）の方程式を求めよ。"%(A[0],A[1],B[0],B[1]),st,r"y=%s"%L(f)
o=[b8(*v) for v in [((1,1),(5,3)),((0,4),(6,0)),((-2,1),(4,5)),((1,-3),(5,1)),((-1,-1),(3,5))]]
build(Z,CH,"線分の垂直二等分線",o,"<p>「中点を通り、傾きが（$AB$ の傾きの逆数の符号を変えた）直線」。または $PA^2=PB^2$ を式にして展開してもよい。</p>","2点から同じ距離にある点が並ぶ線。",8)
# 9 角の二等分線
def b9(l1,l2):
    (a1,b1,c1),(a2,b2,c2)=l1,l2
    n1=sp.sqrt(a1*a1+b1*b1); n2=sp.sqrt(a2*a2+b2*b2); assert n1.is_integer and n2.is_integer
    e1=sp.expand(n2*(a1*x+b1*y+c1)-n1*(a2*x+b2*y+c2)); e2=sp.expand(n2*(a1*x+b1*y+c1)+n1*(a2*x+b2*y+c2))
    st=[("距離が等しい点","<p>角の二等分線上の点 "+I("(x,y)")+" は2直線からの距離が等しい。</p>"+D(r"\dfrac{|%s|}{%s}=\dfrac{|%s|}{%s}"%(L(a1*x+b1*y+c1),L(n1),L(a2*x+b2*y+c2),L(n2)))),
        ("絶対値をはずす","<p>"+D(r"%d(%s)=\pm%d(%s)"%(n2,L(a1*x+b1*y+c1),n1,L(a2*x+b2*y+c2)))),
        ("2本の二等分線",D(r"%s=0,\qquad %s=0"%(L(sp.factor(e1)) if False else L(e1/math.gcd(*[int(c) for c in sp.Poly(e1,x,y).coeffs()])),L(e2/math.gcd(*[int(c) for c in sp.Poly(e2,x,y).coeffs()])))))]
    g1=math.gcd(*[int(c) for c in sp.Poly(e1,x,y).coeffs()]); g2=math.gcd(*[int(c) for c in sp.Poly(e2,x,y).coeffs()])
    return r"2直線 $%s=0,\ %s=0$ のなす角の二等分線の方程式を求めよ。"%(L(a1*x+b1*y+c1),L(a2*x+b2*y+c2)),st,r"%s=0,\ \ %s=0"%(L(e1/g1),L(e2/g2))
o=[b9(*v) for v in [((3,4,-5),(5,-12,0)),((4,3,0),(12,-5,13)),((3,4,10),(8,6,0)),((5,12,-13),(3,-4,0)),((8,-6,5),(5,12,0))]]
build(Z,CH,"2直線のなす角の二等分線",o,"<p>二等分線上の点は2直線までの<b>距離が等しい</b>。点と直線の距離の式を等しくおき、絶対値を $\\pm$ ではずすと<b>2本</b>得られる。</p>","両側から同じ距離にある点の集まり。",9)
# 10 面積を分ける直線
def b10(A,B,C,r,s):
    D_=(R(s*B[0]+r*C[0],r+s),R(s*B[1]+r*C[1],r+s))
    m=R(D_[1]-A[1],1)/(D_[0]-A[0]) if D_[0]!=A[0] else None
    ar=lambda P,Q,Rr:abs((Q[0]-P[0])*(Rr[1]-P[1])-(Rr[0]-P[0])*(Q[1]-P[1]))/R(2)
    assert ar(A,B,D_)/ar(A,D_,C)==R(r,s)
    fg=geo("x221_10_%s"%("_".join(str(v+9) for v in (*A,*B,*C,r,s))),polys=[([A,B,C],"#b81f36")],segs=[(A[0],A[1],D_[0],D_[1],"#1f6fb8","--")],pts=[("A",A[0],A[1],-.4,.3),("B",B[0],B[1],-.4,-.3),("C",C[0],C[1],.4,-.3),("D",float(D_[0]),float(D_[1]),.5,0)],w=44,size=(3.6,3))
    st=[("面積比は底辺の比","<p>頂点 "+I("A")+" を通る直線が "+I("BC")+" と交わる点を "+I("D")+" とすると、高さが共通なので "+I(r"\triangle ABD:\triangle ADC=BD:DC")+"。</p>"+fg),
        ("D を求める","<p>"+I("BD:DC=%d:%d"%(r,s))+" だから "+I("D")+" は "+I("BC")+" を "+I("%d:%d"%(r,s))+" に内分。</p>"+D(r"D\left(%s,\ %s\right)"%(L(D_[0]),L(D_[1])))),
        ("直線 AD",D(r"y=%s(x-%d)+%d"%(L(m),A[0],A[1]) if m is not None else r"x=%d"%A[0]))]
    return r"$A(%d,%d),\ B(%d,%d),\ C(%d,%d)$ を頂点とする三角形の面積を、頂点 $A$ を通る直線で $%d:%d$ に分けたい。その直線の方程式を求めよ。"%(A[0],A[1],B[0],B[1],C[0],C[1],r,s),st,(r"y=%s"%L(sp.expand(m*(x-A[0])+A[1])) if m is not None else r"x=%d"%A[0])
o=[b10(*v) for v in [((0,0),(8,1),(2,6),1,1),((1,1),(9,2),(3,7),1,2),((0,2),(6,0),(4,8),2,1),((0,0),(10,2),(2,8),1,4),((1,0),(7,3),(3,9),3,1)]]
build(Z,CH,"頂点を通る直線で面積を分ける",o,"<p>頂点 $A$ を通る直線では、<b>高さが共通</b>なので面積比＝底辺 $BC$ の分割比。内分点の公式で $D$ を求める。</p>","同じ高さの三角形は、底辺の比が面積の比。",10)
XU=finishx(Z,CH)
