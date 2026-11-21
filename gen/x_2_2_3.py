# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math, itertools
Z=U_(); CH=[]; R=sp.Rational; x,y,k=sp.symbols("x y k")
# 6 放物線の頂点の軌跡
def b6(a,b,c):
    # y = x^2 - 2 k a' ... use y=x^2-2*a*k*x+ b*k^2 + c*k ; vertex at x=a k, y=(b-a^2)k^2+c k
    X=a*k; Y=sp.expand((b-a*a)*k**2+c*k)
    # eliminate k: k=x/a
    loc=sp.expand(Y.subs(k,x/a))
    def dr(ax):
        xs=np.linspace(-4,6,300)
        for kv in [-1,0,1,2]:
            ax.plot(xs,xs**2-2*a*kv*xs+b*kv**2+c*kv,color="#bbbbbb",lw=1)
        curve(ax,loc,(-4,6),"#b81f36")
        for kv in [-1,0,1,2]: mark(ax,a*kv,float((b-a*a)*kv**2+c*kv))
    fg=gplane("x223_6_%d_%d_%d"%(a,b+9,c+9),(-4,6),(-6,8),dr,size=(4.2,3.2),w=50)
    st=[("頂点の座標","<p>"+D(r"y=x^2-%dkx%s=(x-%dk)^2%s"%(2*a,L(b*k**2+c*k) if False else "%+dk^2%+dk"%(b,c),a,"%+dk^2%+dk"%(b-a*a,c)))+"<p>頂点 "+I(r"(x,y)=(%s,\ %s)"%(L(X),L(Y)))+"。</p>"),
        ("$k$ を消去","<p>"+I("x=%s"%L(X))+" より "+I("k=%s"%L(x/a))+"。これを "+I("y")+" に代入。</p>"+D(r"y=%s"%L(loc))+fg),
        ("軌跡","<p>"+I("k")+" はすべての実数をとれるので、放物線全体。</p>")]
    return r"放物線 $y=x^2-%dkx%+dk^2%+dk$ の頂点は、$k$ がすべての実数値をとって変化するとき、どんな曲線を描くか。その方程式を求めよ。"%(2*a,b,c) if a!=1 else r"放物線 $y=x^2-2kx%+dk^2%+dk$ の頂点は、$k$ がすべての実数値をとって変化するとき、どんな曲線を描くか。その方程式を求めよ。"%(b,c),st,r"y=%s"%L(loc)
o=[b6(*v) for v in [(1,0,2),(1,-1,3),(1,2,-2),(2,1,3),(1,3,0)]]
build(Z,CH,"放物線の頂点の軌跡",o,"<p>平方完成で<b>頂点を $k$ の式</b>で表し、$x,y$ から $k$ を消去する。$k$ の範囲に制限があれば軌跡も一部になる。</p>","頂点を追いかけて、$k$ を消すと動く道筋が見える。",6)
# 7 PA^2+PB^2=c
def b7(a,c):
    A=(a,0);B=(-a,0)
    r2=R(c-2*a*a,2); assert r2>0
    r=sp.sqrt(r2)
    fg=geo("x223_7_%d_%d"%(a,c),circles=[(0,0,float(r),"#b81f36","-")],pts=[("A",a,0,.0,-.5),("B",-a,0,.0,-.5),("P",float(r)*.7,float(r)*.7,.45,.35)],segs=[(a,0,float(r)*.7,float(r)*.7,"#999","--"),(-a,0,float(r)*.7,float(r)*.7,"#999","--")],w=44,size=(3.6,3.2))
    st=[("P の座標をおく","<p>"+I("P(x,y)")+"。</p>"+D(r"PA^2+PB^2=(x-%d)^2+y^2+(x+%d)^2+y^2=2x^2+2y^2+%d"%(a,a,2*a*a))),
        ("条件","<p>"+D(r"2x^2+2y^2+%d=%d\ \Longrightarrow\ x^2+y^2=%s"%(2*a*a,c,L(r2)))+fg),
        ("軌跡","<p>原点中心、半径 "+I(L(r))+" の円。</p>")]
    return r"2点 $A(%d,0),\ B(-%d,0)$ に対して $PA^2+PB^2=%d$ をみたす点 $P$ の軌跡を求めよ。"%(a,a,c),st,r"x^2+y^2=%s"%L(r2)
o=[b7(*v) for v in [(2,26),(3,40),(1,10),(4,50),(5,76)]]
build(Z,CH,"2点からの距離の平方の和が一定",o,"<p>$P(x,y)$ とおいて<b>条件を $x,y$ の式</b>にする。展開すると $x^2+y^2=$ 定数（原点中心の円）。</p>","動く点を文字でおいて、条件をそのまま式にする。",7)
# 8 領域の面積
def b8(l):
    # region y>=0 ; y<=a x ; y<=-b x + c  (triangle)
    pass
def b8(m1,m2,c):
    # y>=m1 x (m1>=0)? use: x>=0,y>=0, x/m1... triangle region: y>=0, y<=m1*x, y<=-m2*x+c -> vertices (0,0),(c/m2,0),(c/(m1+m2),m1c/(m1+m2))
    P=[(R(0),R(0)),(R(c,m2),R(0)),(R(c,m1+m2),R(m1*c,m1+m2))]
    ar=abs((P[1][0]-P[0][0])*(P[2][1]-P[0][1])-(P[2][0]-P[0][0])*(P[1][1]-P[0][1]))/R(2)
    def dr(ax):
        xs=np.linspace(0,c/m2+.5,100)
        ax.fill([float(p[0]) for p in P],[float(p[1]) for p in P],color="#f6c6cc")
        ax.plot(xs,m1*xs,color="#b81f36"); ax.plot(xs,-m2*xs+c,color="#1f6fb8")
        for p,t,d in zip(P,"OAB",[(-.3,-.4),(.2,-.5),(0,.5)]): mark(ax,p[0],p[1],t,*d)
    xm=float(P[1][0])+1; ym=float(P[2][1])+1.5
    fg=gplane("x223_8_%d_%d_%d"%(m1,m2,c),(-1,xm),(-1,ym),dr,size=(4.2,3),w=50)
    st=[("境界線と頂点","<p>"+I("y=%dx"%m1)+" と "+I("y=-%dx+%d"%(m2,c) if m2!=1 else "y=-x+%d"%c)+" の交点 "+I("B(%s,\\ %s)"%(L(P[2][0]),L(P[2][1])))+"、第2の直線と "+I("x")+" 軸の交点 "+I("A(%s,\\ 0)"%L(P[1][0]))+"。"+fg),
        ("底辺と高さ","<p>底辺 "+I("OA=%s"%L(P[1][0]))+"、高さ "+I("%s"%L(P[2][1]))+"。</p>"),
        ("面積",D(r"\dfrac12\cdot%s\cdot%s=%s"%(L(P[1][0]),L(P[2][1]),L(ar))))]
    return r"連立不等式 $y\geqq0,\ y\leqq %dx,\ y\leqq -%dx+%d$ の表す領域の面積を求めよ。"%(m1,m2,c) if m2!=1 else r"連立不等式 $y\geqq0,\ y\leqq %dx,\ y\leqq -x+%d$ の表す領域の面積を求めよ。"%(m1,c),st,L(ar)
o=[b8(*v) for v in [(1,1,6),(2,1,6),(1,2,8),(3,1,8),(2,2,8)]]
build(Z,CH,"連立不等式の領域の面積",o,"<p>各不等式の境界線を引いて領域を図示し、<b>頂点の座標</b>を求めて三角形の面積を計算する。</p>","まず図を描いて、囲まれた形の頂点を出す。",8)
# 9 領域で原点との距離の最小
def b9(a,b,c):
    # region ax+by>=c, x>=0, y>=0 ; min of x^2+y^2 = c^2/(a^2+b^2)
    mn=R(c*c,a*a+b*b); foot=(R(a*c,a*a+b*b),R(b*c,a*a+b*b))
    def dr(ax):
        xs=np.linspace(0,c/a+.5,50); ax.plot(xs,(c-a*xs)/b,color="#1f6fb8")
        ax.fill_between(xs,np.maximum((c-a*xs)/b,0),(c/b)+1.5,color="#f6c6cc",alpha=.7)
        mark(ax,foot[0],foot[1],"H",.3,.3); ax.plot([0,float(foot[0])],[0,float(foot[1])],"--",color="#333")
        mark(ax,0,0,"O",-.3,-.5)
    fg=gplane("x223_9_%d_%d_%d"%(a,b,c),(-1,c/a+1),(-1,c/b+1.5),dr,size=(4.2,3),w=50)
    st=[("領域と図","<p>"+I("%dx+%dy\\geqq%d"%(a,b,c))+"（右上側）、"+I("x\\geqq0,\\ y\\geqq0")+"。"+I("x^2+y^2")+" は原点との距離の2乗。</p>"+fg),
        ("最小の点","<p>原点から直線への垂線の足 "+I("H")+" が領域内にあるので、最小値は距離の2乗。</p>"+D(r"\left(\dfrac{|%d|}{\sqrt{%d^2+%d^2}}\right)^2=\dfrac{%d}{%d}=%s"%(c,a,b,c*c,a*a+b*b,L(mn)))),
        ("最小値","<p>"+I("(x,y)=\\left(%s,\\ %s\\right)"%(L(foot[0]),L(foot[1])))+" のとき。</p>")]
    return r"$x\geqq0,\ y\geqq0,\ %dx+%dy\geqq%d$ のとき、$x^2+y^2$ の最小値を求めよ。"%(a,b,c),st,L(mn)
o=[b9(*v) for v in [(1,2,5),(2,1,10),(3,4,25) if False else (3,4,10),(1,1,6),(2,3,13) if False else (2,3,26)]]
build(Z,CH,"領域における $x^2+y^2$ の最小値",o,"<p>$x^2+y^2=r^2$ は原点中心の円。領域に接する（触れる）最小の円を考える。<b>垂線の足</b>が領域内ならそこが最小。</p>","原点からだんだん大きくなる円をふくらませ、領域に最初に触れる所。",9)
# 10 領域で y/x の最大・最小
def b10(P):
    # triangle with vertices P (3 points), none with x<=0
    sl=[R(p[1],p[0]) for p in P]; mx=max(sl); mn=min(sl)
    # brute
    best=[]
    for u in np.linspace(0,1,41):
        for v in np.linspace(0,1-u,41):
            X=u*P[0][0]+v*P[1][0]+(1-u-v)*P[2][0]; Y=u*P[0][1]+v*P[1][1]+(1-u-v)*P[2][1]; best.append(Y/X)
    assert abs(max(best)-float(mx))<1e-9 and abs(min(best)-float(mn))<1e-9
    def dr(ax):
        pts=[(float(p[0]),float(p[1])) for p in P]
        ax.fill([p[0] for p in pts],[p[1] for p in pts],color="#f6c6cc")
        for p,t in zip(pts,"ABC"): mark(ax,p[0],p[1],t,.3,.3)
        ax.plot([0,8],[0,8*float(mx)],"--",color="#b81f36"); ax.plot([0,8],[0,8*float(mn)],"--",color="#1f6fb8"); mark(ax,0,0,"O",-.3,-.5)
    fg=gplane("x223_10_%s"%("_".join(str(v) for p in P for v in p)),(-1,9),(-1,8),dr,size=(4.2,3),w=50)
    st=[("傾きとみる","<p>"+I(r"\dfrac yx")+" は原点と点 "+I("(x,y)")+" を結ぶ直線の<b>傾き</b>。</p>"+fg),
        ("頂点で調べる","<p>三角形の頂点での傾き：</p>"+D(r"\text{"+"},\ \text{".join("%s"%("ABC"[i]+"："+L(sl[i])) for i in range(3))+r"}") if False else "<p>"+"、".join("%s：%s"%("ABC"[i],I(L(sl[i]))) for i in range(3))+"。</p>"),
        ("最大・最小","<p>傾きは頂点で最大・最小になる。</p>"+D(r"\text{最大 }%s,\qquad \text{最小 }%s"%(L(mx),L(mn))))]
    return r"3点 $A(%d,%d),\ B(%d,%d),\ C(%d,%d)$ を頂点とする三角形の周および内部を点 $(x,y)$ が動くとき、$\dfrac yx$ の最大値と最小値を求めよ。"%(P[0][0],P[0][1],P[1][0],P[1][1],P[2][0],P[2][1]),st,r"\text{最大 }%s,\ \text{最小 }%s"%(L(mx),L(mn))
o=[b10(P) for P in [((2,1),(6,2),(4,6)),((1,2),(5,1),(3,5)),((2,3),(7,2),(4,7)),((3,1),(7,3),(5,7)),((1,1),(6,2),(2,6))]]
build(Z,CH,"領域における y/x の最大・最小（傾き）",o,"<p>$\\dfrac yx$ は<b>原点を通る直線の傾き</b>。原点から領域に引いた直線を回転させ、接する位置（多角形なら頂点）で最大・最小。</p>","原点から領域をのぞく視線の角度が傾き。",10)
XU=finishx(Z,CH)
