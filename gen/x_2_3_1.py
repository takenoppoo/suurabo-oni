# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x"); th=sp.symbols(r"\theta"); pi=sp.pi
def PI(v): return L(v*pi) if v!=0 else "0"
# 6 弓形の面積
def b6(r,a):
    # a = central angle as rational multiple of pi
    ang=a*pi; seg=sp.simplify(R(1,2)*r*r*(ang-sp.sin(ang)))
    fg=geo("x231_6_%d_%d_%d"%(r,a.p,a.q),circles=[(0,0,r,"#b81f36","-")],segs=[(0,0,r,0,"#333","-"),(0,0,float(r*sp.cos(ang)),float(r*sp.sin(ang)),"#333","-"),(r,0,float(r*sp.cos(ang)),float(r*sp.sin(ang)),"#1f6fb8","-")],pts=[("O",0,0,-.4,-.4),("A",r,0,.5,0),("B",float(r*sp.cos(ang)),float(r*sp.sin(ang)),.0,.6)],w=40,size=(3.4,3.2))
    st=[("扇形の面積","<p>中心角 "+I(PI(a))+"、半径 "+I(str(r))+"。</p>"+D(r"\dfrac12r^2\theta=\dfrac12\cdot%d^2\cdot%s=%s"%(r,PI(a),L(sp.simplify(R(1,2)*r*r*ang))))+fg),
        ("三角形 OAB の面積","<p>"+D(r"\dfrac12r^2\sin\theta=\dfrac12\cdot%d^2\cdot%s=%s"%(r,L(sp.sin(ang)),L(sp.simplify(R(1,2)*r*r*sp.sin(ang)))))),
        ("引いて弓形",D(r"%s-%s=%s"%(L(sp.simplify(R(1,2)*r*r*ang)),L(sp.simplify(R(1,2)*r*r*sp.sin(ang))),L(seg))))]
    return r"半径 $%d$、中心角 $%s$ の扇形 $OAB$ について、弦 $AB$ と弧 $AB$ で囲まれた部分（弓形）の面積を求めよ。"%(r,PI(a)),st,L(seg)
o=[b6(*v) for v in [(6,R(1,3)),(4,R(1,2)),(8,R(2,3)),(6,R(1,6)),(12,R(5,6))]]
build(Z,CH,"弓形の面積（扇形 − 三角形）",o,"<p>弓形 $=$ 扇形 $\\dfrac12r^2\\theta$ $-$ 三角形 $\\dfrac12r^2\\sin\\theta$。弧度法のままで計算できる。</p>","丸いパイから、三角形の切れ端を引く。",6)
# 7 sinθ+cosθ=k
def b7(k):
    s=sp.symbols("s"); sc=R(k*k-1,2)
    c3=R(k)*(1-R(3,2)*(k*k-1)/1) if False else None
    # sin^3+cos^3=(s+c)^3 -3sc(s+c)
    v3=k**3-3*sc*k; v4=1-2*sc**2; 
    st=[("両辺を2乗","<p>"+D(r"(\sin\theta+\cos\theta)^2=1+2\sin\theta\cos\theta=%s"%L(k*k))),
        ("積","<p>"+D(r"\sin\theta\cos\theta=%s"%L(sc))),
        ("3乗の和","<p>"+D(r"\sin^3\theta+\cos^3\theta=(\sin\theta+\cos\theta)^3-3\sin\theta\cos\theta(\sin\theta+\cos\theta)=%s-3\cdot%s\cdot%s=%s"%(L(R(k)**3),L(sc),L(R(k)),L(v3)))),
        ("4乗の和","<p>"+D(r"\sin^4\theta+\cos^4\theta=1-2\sin^2\theta\cos^2\theta=%s"%L(v4)))]
    return r"$\sin\theta+\cos\theta=%s$ のとき、$\sin\theta\cos\theta,\ \sin^3\theta+\cos^3\theta,\ \sin^4\theta+\cos^4\theta$ の値を求めよ。"%L(R(k)),st,r"%s,\ %s,\ %s"%(L(sc),L(v3),L(v4))
o=[b7(k) for k in [R(1,2),R(3,5),R(1,3),R(7,5),R(4,5)]]
build(Z,CH,"sinθ+cosθ=k から積・3乗の和・4乗の和",o,"<p>まず<b>2乗して $\\sin\\theta\\cos\\theta$</b> を求める。3乗の和は $(a+b)^3-3ab(a+b)$、4乗の和は $1-2(\\sin\\theta\\cos\\theta)^2$ で。</p>","和と積が分かれば、どんな対称式も組み立てられる。",7)
# 8 グラフから式
def b8(A,b,c):
    # y = A sin(b th - c)  : read amplitude, period, shift
    f=A*sp.sin(b*th-c)
    per=2*pi/b; sh=c/b
    def dr(ax):
        xs=np.linspace(-.3,2*np.pi+.3,400); ax.plot(xs,float(A)*np.sin(float(b)*xs-float(c)),color="#b81f36",lw=2)
        mark(ax,float(sh),0,"",0,0); mark(ax,float(sh+per),0)
    fg=gplane("x231_8_%d_%d_%d"%(A,b,int(c*12)),(-.5,6.6),(-float(A)-1,float(A)+1),dr,size=(4.4,3),w=52,xs=np.pi/2,ys=1)
    st=[("振幅","<p>最大値 "+I(str(A))+"、最小値 "+I("-%d"%A)+" より "+I("a=%d"%A)+"。</p>"+fg),
        ("周期","<p>周期 "+I(L(per))+" より "+I(r"\dfrac{2\pi}{b}=%s"%L(per))+"、"+I("b=%d"%b)+"。</p>"),
        ("ずれ","<p>"+I("y=0")+" で上り始める点が "+I("\\theta=%s"%L(sh))+" だから "+I(r"b\theta-c=0\ \Rightarrow\ c=%s"%L(c))+"。</p>"),
        ("式",D(r"y=%d\sin\left(%s\right)"%(A,L(b*th-c))))]
    return r"$y=a\sin(b\theta-c)$（$a>0,\ b>0,\ 0\leqq c<\pi$）のグラフが図のようになった。最大値 $%d$、周期 $%s$、$\theta=%s$ で $y=0$ から増加する。$a,b,c$ を求めよ。"%(A,L(per),L(sh)),st,r"a=%d,\ b=%d,\ c=%s"%(A,b,L(c))
o=[b8(*v) for v in [(3,2,pi/3),(2,3,pi/2),(4,2,pi/4),(1,4,pi/2),(5,1,pi/6)]]
build(Z,CH,"グラフから y=a sin(bθ−c) の係数を読み取る",o,"<p>最大値＝振幅 $a$、周期＝$\\dfrac{2\\pi}{b}$、グラフが $0$ から増加し始める点 $\\theta_0=\\dfrac cb$。この3つを順に読む。</p>","波の高さ・波長・出発点の3つが分かれば式が決まる。",8)
# 9 公式で簡単に

def rotfig(name,k):
    """θ を k×90° 回転した点 Q の座標を、単位円の上で見せる"""
    import matplotlib.patches as pa
    lab={0:(r"\cos\theta",r"\sin\theta"),1:(r"-\sin\theta",r"\cos\theta"),2:(r"-\cos\theta",r"-\sin\theta"),3:(r"\sin\theta",r"-\cos\theta")}[k]
    def fn(ax):
        ax.set_aspect("equal"); ax.set_xlim(-2.3,2.3); ax.set_ylim(-1.5,1.5); ax.axis("off")
        t=np.linspace(0,2*np.pi,300); ax.plot(np.cos(t),np.sin(t),color="#555",lw=1.3)
        ax.annotate("",xy=(1.5,0),xytext=(-1.5,0),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        ax.annotate("",xy=(0,1.42),xytext=(0,-1.42),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        a=np.radians(35); b=a+k*np.pi/2
        for ang,col,nm,(cx_,sy_) in [(a,"#b81f36","P",(r"\cos\theta",r"\sin\theta")),(b,"#1f6fb8","Q",lab)]:
            px,py=np.cos(ang),np.sin(ang); ax.plot([0,px],[0,py],color=col,lw=2); ax.plot([px],[py],"o",color=col,zorder=5)
            ax.text(px+(.1 if px>=0 else -.1),py+(.12 if py>=0 else -.18),nm+"$\\left("+cx_+",\\ "+sy_+"\\right)$",color=col,fontsize=10,ha=("left" if px>=0 else "right"))
        if k: ax.add_patch(pa.Arc((0,0),.7,.7,theta1=35,theta2=35+k*90,color="#1f8a5b",lw=1.6)); ax.text(.52*np.cos(a+k*np.pi/4),.52*np.sin(a+k*np.pi/4),"$%d\\times 90^\\circ$"%k,fontsize=9,color="#1f8a5b",ha="center",bbox=dict(fc="white",ec="none",pad=1))
    make_fig(name,fn,size=(4.2,3.1))
    return img(name,50,"θ を %d×90° 回した点 Q の座標を読む"%k)
def b9(n):
    # sin(π/2+θ)... compute  value of sin(θ+nπ/2)
    ex={0:"\\sin\\theta",1:"\\cos\\theta",2:"-\\sin\\theta",3:"-\\cos\\theta"}
    th_=sp.Rational(7,5)
    e1=sp.sin(th+n*pi/2); v=sp.simplify(sp.expand_trig(e1))
    assert abs(float(e1.subs(th,th_))-float(v.subs(th,th_)))<1e-9
    k=n%4; fg=rotfig("x231_9_%d"%k,k)
    st=[("%d を使って"%n,"<p>単位円の点 "+I(r"P(\cos\theta,\ \sin\theta)")+" を、原点のまわりに "+I(r"%d\times90^\circ"%k)+" 回した点を "+I("Q")+" とする。"+I("Q")+" の "+I("y")+" 座標が "+I(r"\sin\left(\theta+%s\right)"%L(k*pi/2))+" である。</p>"+fg+"<p>"+I(r"\sin\left(\theta+%s\right)"%L(n*pi/2))+" の周期・対称性を使う。2π ごとに戻るので "+I(r"\dfrac{%d\pi}{2}"%n)+" を "+I(r"\dfrac{%d\pi}{2}"%(n%4))+" としてよい。</p>"),
        ("公式を適用","<p>"+D(r"\sin\left(\theta+%s\right)=%s"%(L((n%4)*pi/2),L(v))))]
    return r"$\sin\left(\theta+\dfrac{%d\pi}{2}\right)$ を、$\sin\theta$ または $\cos\theta$ を使って表せ。"%n,st,L(v)
o=[b9(n) for n in [5,7,6,9,11]]
build(Z,CH,"θ+nπ/2 の三角関数の変換",o,"<p>$2\\pi$ の整数倍は取り除いて $\\dfrac{\\pi}{2},\\pi,\\dfrac{3\\pi}{2}$ に直す。$\\sin\\left(\\theta+\\dfrac\\pi2\\right)=\\cos\\theta$ などの公式を使う。</p>","一周したら元に戻る。余りの分だけ回転を考える。",9)
# 10 周期
def b10(p,q):
    # y=sin(p th)+cos(q th) period = lcm of 2π/p, 2π/q
    per=sp.lcm(R(2,p),R(2,q)) if False else None
    from math import gcd
    a=R(2,p); b=R(2,q)
    # lcm of rationals
    num=sp.ilcm(a.p*1,b.p)  # placeholder
    lcm=R(sp.ilcm(a.p,b.p),sp.igcd(a.q,b.q))
    f=lambda t:math.sin(p*t)+math.cos(q*t)
    ts=np.linspace(0,10,50)
    assert all(abs(f(t)-f(t+float(lcm)*math.pi))<1e-9 for t in ts)
    st=[("それぞれの周期","<p>"+I(r"\sin %d\theta"%p)+" の周期 "+I(r"\dfrac{2\pi}{%d}=%s"%(p,L(R(2,p)*pi)))+"、"+I(r"\cos %d\theta"%q)+" の周期 "+I(r"%s"%L(R(2,q)*pi))+"。</p>"),
        ("最小公倍数","<p>2つの周期の<b>最小公倍数</b>が全体の周期。それぞれを整数倍して等しくなる最小のところを探す。</p>"+D(r"%s\times%s=%s,\quad %s\times%s=%s"%(L(R(2,p)*pi),L(R(lcm*p,2)),L(lcm*pi),L(R(2,q)*pi),L(R(lcm*q,2)),L(lcm*pi)))+"<p>よって</p>"+D(r"\text{周期}=%s"%L(lcm*pi)))]
    return r"関数 $y=\sin %d\theta+\cos %d\theta$ の周期を求めよ。"%(p,q),st,L(lcm*pi)
o=[b10(*v) for v in [(2,3),(3,4),(2,5),(4,6),(3,6)]]
build(Z,CH,"和の関数の周期（周期の最小公倍数）",o,"<p>$\\sin p\\theta$ の周期 $\\dfrac{2\\pi}{p}$、$\\cos q\\theta$ の周期 $\\dfrac{2\\pi}{q}$。和の周期は<b>2つの周期の最小公倍数</b>。</p>","2つの波が同時に元の形に戻る最短の時間。",10)
XU=finishx(Z,CH)
