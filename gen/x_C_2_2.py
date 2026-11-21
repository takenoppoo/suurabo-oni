# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,y,t=sp.symbols("x y t")
# 6 x=t+1/t 型の消去
def b6(a,b):
    # x = a(t+1/t), y = b(t-1/t)  (t>0) -> x^2/(4a^2) - y^2/(4b^2) =1 , x>=2a
    X=a*(t+1/t); Y=b*(t-1/t)
    assert sp.simplify(X**2/(4*a*a)-Y**2/(4*b*b)-1)==0
    def dr(ax):
        tt=np.linspace(.2,5,300); ax.plot(a*(tt+1/tt),b*(tt-1/tt),color="#b81f36",lw=2)
    fg=gplane("xc22_6_%d_%d"%(a,b),(-1,6*a),(-5*b,5*b),dr,size=(4.2,3.2),w=50)
    st=[("2乗の差","<p>"+D(r"\dfrac{x}{%d}=t+\dfrac1t,\qquad \dfrac{y}{%d}=t-\dfrac1t"%(a,b))),
        ("消去","<p>"+D(r"\left(\dfrac{x}{%d}\right)^2-\left(\dfrac{y}{%d}\right)^2=\left(t+\dfrac1t\right)^2-\left(t-\dfrac1t\right)^2=4"%(a,b))),
        ("範囲","<p>"+I("t>0")+" で "+I(r"t+\dfrac1t\geqq2")+" より "+I("x\\geqq%d"%(2*a))+"。</p>"+D(r"\dfrac{x^2}{%d}-\dfrac{y^2}{%d}=1\quad(x\geqq%d)"%(4*a*a,4*b*b,2*a))+fg)]
    return r"$t>0$ のとき、$x=%d\left(t+\dfrac1t\right),\ y=%d\left(t-\dfrac1t\right)$ で表される曲線の方程式を求めよ。（$x$ の範囲にも注意）"%(a,b),st,r"\dfrac{x^2}{%d}-\dfrac{y^2}{%d}=1\ (x\geqq%d)"%(4*a*a,4*b*b,2*a)
o=[b6(*v) for v in [(1,1),(2,1),(1,2),(3,2),(2,3)]]
build(Z,CH,"媒介変数 t+1/t を消去（範囲に注意）",o,"<p>$\\dfrac xa,\\dfrac yb$ を作り、<b>2乗の差</b>で $t$ を消去。さらに $t>0$ のもとで $t+\\dfrac1t\\geqq2$（相加・相乗平均）から $x$ の範囲が決まる。</p>","文字を消すだけでなく、動く範囲も引き継ぐ。",6)
# 7 極方程式から直交座標へ（円）
def b7(a,k):
    # r = 2a cos th + 2k sin th -> (x-a)^2+(y-k)^2 = a^2+k^2
    r2=a*a+k*k
    def dr(ax):
        th=np.linspace(0,2*np.pi,400); ax.plot(a+math.sqrt(r2)*np.cos(th),k+math.sqrt(r2)*np.sin(th),color="#b81f36",lw=2); mark(ax,a,k,"C",.3,.4); mark(ax,0,0,"O",-.3,-.5)
    fg=gplane("xc22_7_%d_%d"%(a,k),(-math.sqrt(r2)+a-1,math.sqrt(r2)+a+1),(-math.sqrt(r2)+k-1,math.sqrt(r2)+k+1),dr,size=(4.2,3.2),w=50)
    st=[("両辺に r をかける","<p>"+D(r"r^2=%dr\cos\theta+%dr\sin\theta"%(2*a,2*k))),
        ("直交座標へ","<p>"+I(r"x=r\cos\theta,\ y=r\sin\theta,\ r^2=x^2+y^2")+"。</p>"+D(r"x^2+y^2=%dx+%dy"%(2*a,2*k))),
        ("平方完成","<p>"+D(r"(x-%d)^2+(y-%d)^2=%d"%(a,k,r2))+fg)]
    return r"極方程式 $r=%d\cos\theta+%d\sin\theta$ を直交座標 $(x,y)$ の方程式で表し、どんな図形か答えよ。"%(2*a,2*k),st,r"(x-%d)^2+(y-%d)^2=%d\ （中心 (%d,%d)、半径 %s の円）"%(a,k,r2,a,k,L(sp.sqrt(r2)))
o=[b7(*v) for v in [(1,1),(2,1),(1,2),(3,0),(2,2)]]
build(Z,CH,"極方程式 r=2a cosθ+2b sinθ の直交座標表示",o,"<p>両辺に $r$ をかけて $r\\cos\\theta=x,\\ r\\sin\\theta=y,\\ r^2=x^2+y^2$ を代入。平方完成して円の中心・半径を読む。原点を通る円。</p>","極座標は、距離と角度。かけ算で x と y に翻訳。",7)
# 8 楕円のパラメータ表示と内接長方形
def b8(a,b):
    # area of inscribed rectangle: 4ab sin th cos th = 2ab sin 2th max 2ab
    ar=2*a*b
    def dr(ax):
        th=np.linspace(0,2*np.pi,400); ax.plot(a*np.cos(th),b*np.sin(th),color="#b81f36",lw=2)
        p=np.pi/4; xx,yy=a*np.cos(p),b*np.sin(p); ax.plot([xx,-xx,-xx,xx,xx],[yy,yy,-yy,-yy,yy],color="#1f6fb8",lw=1.8); mark(ax,xx,yy,"P",.3,.4)
    fg=gplane("xc22_8_%d_%d"%(a,b),(-a-1.5,a+1.5),(-b-1.5,b+1.5),dr,size=(4.2,3),w=50)
    st=[("パラメータ表示","<p>"+I(r"P(%d\cos\theta,\ %d\sin\theta)\ \left(0<\theta<\dfrac\pi2\right)"%(a,b))+"。長方形は軸に平行で4点が対称。</p>"+fg),
        ("面積","<p>"+D(r"S=(2\cdot%d\cos\theta)(2\cdot%d\sin\theta)=%d\sin\theta\cos\theta=%d\sin2\theta"%(a,b,4*a*b,2*a*b))),
        ("最大","<p>"+I(r"\sin2\theta=1")+"、つまり "+I(r"\theta=\dfrac\pi4")+" のとき最大値 "+I(str(ar))+"。</p>")]
    return r"楕円 $\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1$ に内接し、辺が座標軸に平行な長方形の面積の最大値を求めよ。"%(a*a,b*b),st,str(ar)
o=[b8(*v) for v in [(3,2),(5,3),(4,1),(6,4),(2,2)]]
build(Z,CH,"楕円に内接する長方形の面積の最大",o,"<p>楕円上の点を $(a\\cos\\theta,\\ b\\sin\\theta)$ とおくと、長方形の面積が $2ab\\sin2\\theta$ となり最大値は $2ab$（$\\theta=\\dfrac\\pi4$）。</p>","パラメータを使えば、三角関数の最大問題に変わる。",8)
# 9 極座標での2点間の距離
def b9(r1,t1,r2,t2):
    th1,th2=math.radians(t1),math.radians(t2)
    d2=r1*r1+r2*r2-2*r1*r2*math.cos(th2-th1)
    A=(r1*math.cos(th1),r1*math.sin(th1)); B=(r2*math.cos(th2),r2*math.sin(th2))
    assert abs(math.hypot(A[0]-B[0],A[1]-B[1])**2-d2)<1e-9
    dd=sp.simplify(r1*r1+r2*r2-2*r1*r2*sp.cos(sp.rad(t2-t1)))
    st=[("余弦定理","<p>"+I("O")+" を原点とすると "+I(r"\angle AOB=%d^\circ"%(abs(t2-t1)))+"。</p>"+D(r"AB^2=OA^2+OB^2-2\cdot OA\cdot OB\cos\angle AOB")),
        ("代入","<p>"+D(r"AB^2=%d^2+%d^2-2\cdot%d\cdot%d\cos%d^\circ=%s"%(r1,r2,r1,r2,abs(t2-t1),L(dd)))),
        ("距離","<p>"+D(r"AB=%s"%L(sp.sqrt(dd))))]
    return r"極座標で表された2点 $A\left(%d,\ %d^\circ\right),\ B\left(%d,\ %d^\circ\right)$ の距離 $AB$ を求めよ。"%(r1,t1,r2,t2),st,L(sp.sqrt(dd))
o=[b9(*v) for v in [(4,0,6,60),(3,30,5,90),(2,0,8,120),(5,15,5,75),(6,0,3,60)]]
build(Z,CH,"極座標で表された2点間の距離",o,"<p>2点と原点がつくる三角形に<b>余弦定理</b>。なす角は $|\\theta_2-\\theta_1|$。直交座標に直して計算してもよい。</p>","距離と角度が分かっているなら、三角形の問題。",9)
# 10 中点の軌跡（媒介）
def b10(a):
    # A(a,0) ... P(t,t^2) parabola ; midpoint of A and P: ((t+a)/2, t^2/2) -> y = 2(x-a/2)^2
    X=(t+a)/2; Y=t**2/2
    eq=sp.simplify(Y-2*(X-R(a,2))**2); assert eq==0
    def dr(ax):
        tt=np.linspace(-2.5,3,300); ax.plot(tt,tt**2,color="#bbbbbb",lw=1.5,ls="--"); ax.plot((tt+a)/2,tt**2/2,color="#b81f36",lw=2); mark(ax,a,0,"A",0,-.5)
    fg=gplane("xc22_10_%d"%(a+9),(-3,a+3),(-1,8),dr,size=(4.2,3),w=50)
    st=[("中点の座標","<p>"+I("P(t,\\ t^2)")+" と "+I("A(%d,0)"%a)+" の中点 "+I("M(x,y)")+"：</p>"+D(r"x=\dfrac{t+%d}{2},\qquad y=\dfrac{t^2}{2}"%a)),
        ("$t$ を消去","<p>"+I("t=2x-%d"%a)+" を代入：</p>"+D(r"y=\dfrac{(2x-%d)^2}{2}=%s"%(a,L(sp.expand(2*(x-R(a,2))**2))))+fg)]
    return r"放物線 $y=x^2$ 上を動く点 $P$ と、定点 $A(%d,\ 0)$ の中点 $M$ の軌跡の方程式を求めよ。"%a,st,r"y=%s"%L(sp.expand(2*(x-R(a,2))**2))
o=[b10(a) for a in [2,4,-2,6,1]]
build(Z,CH,"放物線上の点と定点の中点の軌跡",o,"<p>動点を媒介変数 $t$ で表し、中点の座標を $t$ で書いてから $t$ を消去。中点は元の曲線を<b>拡大縮小・平行移動</b>したものになる。</p>","動く点の影をたどると、似た形の曲線が現れる。",10)
XU=finishx(Z,CH)
