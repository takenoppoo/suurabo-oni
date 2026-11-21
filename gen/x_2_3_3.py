# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; th=sp.symbols(r"\theta"); pi=sp.pi
def deg(v): return "%d^\\circ"%v
# 6 cos2θ を含む方程式
def b6(a,b):
    # cos2θ + a cosθ + b =0 ; 2c^2-1+a c+b=0
    c=sp.symbols("c"); P=2*c**2+a*c+b-1; rts=sp.solve(P,c)
    ok=[r for r in rts if -1<=r<=1]
    sols=[]
    for r in ok:
        for t in range(0,360):
            if abs(math.cos(math.radians(t))-float(r))<1e-9: sols.append(t)
    # brute
    br=[t for t in range(0,360) if abs(math.cos(2*math.radians(t))+a*math.cos(math.radians(t))+b)<1e-9]
    assert sorted(sols)==br
    st=[("cosθ にそろえる","<p>"+I(r"\cos2\theta=2\cos^2\theta-1")+"。</p>"+D(r"%s=0"%L(2*c**2+a*c+b-1).replace("c",r"\cos\theta"))),
        ("因数分解","<p>"+I(r"\cos\theta=t\ (-1\leqq t\leqq1)")+"。</p>"+D(r"%s=0\ \Rightarrow\ t=%s"%(L(sp.factor(P)).replace("c","t"),r",\ ".join(L(r) for r in rts)))),
        ("範囲の確認","<p>"+I(r"-1\leqq t\leqq1")+" をみたすものは "+I(r",\ ".join("t=%s"%L(r) for r in ok))+"。</p>"),
        ("解",D(r"\theta=%s"%(r",\ ".join(deg(t) for t in br))))]
    return r"$0^\circ\leqq\theta<360^\circ$ のとき、方程式 $\cos2\theta%+d\cos\theta%+d=0$ を解け。"%(a,b),st,r"\theta=%s"%(r",\ ".join(deg(t) for t in br))
o=[b6(*v) for v in [(3,1),(1,0),(-1,0),(1,1),(3,2)]]
build(Z,CH,"cos2θ を含む方程式",o,"<p>$\\cos2\\theta=2\\cos^2\\theta-1$ で <b>$\\cos\\theta$ だけにそろえ</b>、$t=\\cos\\theta$ の2次方程式にする。<b>$-1\\leqq t\\leqq1$</b> の確認を忘れない。</p>","2倍角で1種類に統一して、置き換えて解く。",6)
# 7 合成して最大最小 + 角
def b7(a,b,lo,hi):
    # y=a sinθ + b cosθ on 0<=θ<=π (hi-lo etc.)
    f=lambda t:a*math.sin(t)+b*math.cos(t)
    ts=np.linspace(lo,hi,200001); v=np.array([f(t) for t in ts])
    mx,mn=v.max(),v.min()
    r=math.hypot(a,b)
    def dr(ax):
        xs=np.linspace(lo-.3,hi+.3,300); ax.plot(xs,[f(t) for t in xs],color="#b81f36",lw=2)
        for tt in [ts[v.argmax()],ts[v.argmin()]]: mark(ax,tt,f(tt))
    fg=gplane("x233_7_%d_%d_%d_%d"%(a+9,b+9,int(lo*10),int(hi*10)),(lo-.4,hi+.4),(-r-.7,r+.7),dr,size=(4.4,3),w=54,xs=np.pi/2,ys=1)
    return mx,mn,fg
def b7(a,b,lo,hi):
    mx,mn,fg=b7_(a,b,lo,hi) if False else (None,None,None)
b7_=None
def b7(a,b,lo,hi):
    f=lambda t:a*math.sin(t)+b*math.cos(t)
    ts=np.linspace(lo,hi,400001); v=a*np.sin(ts)+b*np.cos(ts)
    mx,mn=v.max(),v.min(); r=math.hypot(a,b); al=math.atan2(b,a)
    def dr(ax):
        xs=np.linspace(lo-.3,hi+.3,300); ax.plot(xs,a*np.sin(xs)+b*np.cos(xs),color="#b81f36",lw=2)
        for tt in [ts[v.argmax()],ts[v.argmin()]]: mark(ax,tt,a*math.sin(tt)+b*math.cos(tt))
    fg=gplane("x233_7_%d_%d_%d_%d"%(a+9,b+9,int(lo*10),int(hi*10)),(lo-.4,hi+.4),(-r-.7,r+.7),dr,size=(4.4,3),w=54,xs=np.pi/2,ys=1)
    # exact: r=sqrt(a^2+b^2)=2 or 2sqrt? 
    st=[("合成","<p>"+D(r"%d\sin\theta+%d\cos\theta=%s\sin\left(\theta+%s\right)"%(a,b,L(sp.sqrt(a*a+b*b)),L(sp.nsimplify(al/math.pi,[sp.pi])*pi if False else R(round(al/math.pi*12),12)*pi)))),
        ("範囲","<p>"+I(r"%s\leqq\theta\leqq%s"%(L(R(round(lo/math.pi*12),12)*pi),L(R(round(hi/math.pi*12),12)*pi)))+" より "+I(r"\theta+%s"%L(R(round(al/math.pi*12),12)*pi))+" の範囲は "+I(r"%s\sim%s"%(L((R(round(lo/math.pi*12),12)+R(round(al/math.pi*12),12))*pi),L((R(round(hi/math.pi*12),12)+R(round(al/math.pi*12),12))*pi)))+"。</p>"+fg),
        ("最大・最小","<p>"+D(r"\text{最大 }%s,\qquad \text{最小 }%s"%(L(sp.nsimplify(round(mx,6),[sp.sqrt(3),sp.sqrt(2)])),L(sp.nsimplify(round(mn,6),[sp.sqrt(3),sp.sqrt(2)])))))]
    return r"$%s\leqq\theta\leqq%s$ のとき、$y=%d\sin\theta+%d\cos\theta$ の最大値と最小値を求めよ。"%(L(R(round(lo/math.pi*12),12)*pi),L(R(round(hi/math.pi*12),12)*pi),a,b),st,r"\text{最大 }%s,\ \text{最小 }%s"%(L(sp.nsimplify(round(mx,6),[sp.sqrt(3),sp.sqrt(2)])),L(sp.nsimplify(round(mn,6),[sp.sqrt(3),sp.sqrt(2)])))
o=[b7(*v) for v in [(1,math.sqrt(3) if False else 1,0,math.pi),(1,1,0,math.pi/2),(1,-1,0,math.pi),(1,1,math.pi/2,math.pi),(-1,1,0,math.pi)]]
build(Z,CH,"範囲つきの合成と最大・最小",o,"<p>$r\\sin(\\theta+\\alpha)$ に合成し、<b>$\\theta+\\alpha$ のとりうる範囲</b>で $\\sin$ の最大・最小を調べる（端点も要チェック）。</p>","合成のあと、角の範囲が変わることに注意。",7)
# 8 tan を含む不等式
def b8(c):
    s=sp.Symbol("s")
    # tanθ > c on 0<=θ<π, θ≠π/2
    a=math.degrees(math.atan(c)); 
    st=[("グラフ","<p>"+I(r"y=\tan\theta")+" は "+I(r"\theta=90^\circ")+" で定義されない。"+I(r"\tan\theta=%s"%L(c))+" となる角は "+I("%d^\\circ"%round(a))+"。</p>"),
        ("不等式","<p>"+I(r"\tan\theta>%s"%L(c))+" をみたす範囲：</p>"+D(r"%d^\circ<\theta<90^\circ,\qquad 90^\circ<\theta\ ?"%round(a) if False else r"%d^\circ<\theta<90^\circ"%round(a))+"<p>（"+I(r"90^\circ<\theta<180^\circ")+" では "+I(r"\tan\theta<0")+" で不適。）</p>")]
    return r"$0^\circ\leqq\theta<180^\circ$ のとき、不等式 $\tan\theta>%s$ を解け。"%L(c),st,r"%d^\circ<\theta<90^\circ"%round(a)
o=[b8(c) for c in [1,sp.sqrt(3),sp.sqrt(3)/3,sp.Integer(1) if False else sp.Rational(1,1),sp.sqrt(3)]]
# vary: use different strictness
o=[b8(c) for c in [1,sp.sqrt(3),sp.sqrt(3)/3,sp.sqrt(3)*1,1]][0:3]+[b8(1),b8(sp.sqrt(3))]
build(Z,CH,"tanθ の不等式",o,"<p>$\\tan\\theta$ のグラフ（$\\theta=90^\\circ$ で漸近線）で、$y=$ 定数 より上の部分を読む。$90^\\circ$ は含まない。</p>","グラフが基準線より上にあるところ。",8)
# 9 パラメータと解の個数
def b9(lo_):
    # sinθ = k has exactly n solutions in 0<=θ<2π ... use 2sin^2θ - sinθ = k : count solutions
    # f(t)=2t^2 - t, t=sinθ in [-1,1]; number of θ solutions as function of k
    t=sp.symbols("t")
    # sample k values and count
    def cnt(kv):
        rts=sp.solve(2*t**2-t-kv,t); n=0
        for r in rts:
            if r.is_real:
                r=float(r)
                if abs(r)<1-1e-12: n+=2
                elif abs(abs(r)-1)<1e-9: n+=1
        return n
    return None
def b9(k):
    # number of solutions of sin^2θ... choose: 2cos^2θ ... use  sin^2θ - sinθ + k... let's: (sinθ - a)^2 = b form
    pass
def b9(k0):
    # equation: sin^2θ + sinθ = k, 0<=θ<2π. t=sinθ in[-1,1]: g(t)=t^2+t, min -1/4 at t=-1/2, g(-1)=0,g(1)=2
    t=sp.symbols("t")
    def cnt(kv):
        n=0
        for r in sp.solve(t*t+t-kv,t):
            if r.is_real:
                r=float(r)
                if abs(r)<1-1e-12: n+=2
                elif abs(abs(r)-1)<1e-9: n+=1
        return n
    def dr(ax):
        xs=np.linspace(-1.2,1.2,200); ax.plot(xs,xs**2+xs,color="#b81f36",lw=2)
        ax.plot([-1.2,1.2],[float(k0)]*2,color="#1f6fb8",ls="--")
    fg=gplane("x233_9_%d_%d"%(k0.p,k0.q),(-1.3,1.3),(-.6,2.4),dr,size=(4.2,3),w=50,xs=.5,ys=.5)
    n=cnt(k0)
    st=[("置き換え","<p>"+I(r"\sin\theta=t\ (-1\leqq t\leqq1)")+"、"+I("g(t)=t^2+t=\\left(t+\\dfrac12\\right)^2-\\dfrac14")+"。</p>"),
        ("グラフ","<p>"+I("y=g(t)")+" と "+I("y=%s"%L(k0))+" の共有点の "+I("t")+" の個数と、各 "+I("t")+" に対する "+I(r"\theta")+" の個数（"+I(r"-1<t<1")+" は2個、"+I(r"t=\pm1")+" は1個）を数える。</p>"+fg),
        ("個数","<p>"+I(r"k=%s"%L(k0))+" のとき "+I(str(n))+" 個。</p>")]
    return r"$0\leqq\theta<2\pi$ のとき、方程式 $\sin^2\theta+\sin\theta=%s$ をみたす $\theta$ は何個あるか。"%L(k0),st,str(n)
o=[b9(k) for k in [R(1,2),R(-1,8),R(0),R(2),R(-1,4)]]
build(Z,CH,"置き換えと解の個数（グラフ利用）",o,"<p>$t=\\sin\\theta$ とおき、$t$ の範囲 $-1\\leqq t\\leqq1$ で解の個数を<b>グラフ</b>で調べる。$t$ が1つ決まると $\\theta$ は2個（$t=\\pm1$ のときだけ1個）。</p>","まず t の解を数え、次に角に翻訳する。",9)
# 10 sinθ cosθ 置換
def b10(a):
    # y = sinθ+cosθ + a sinθcosθ  : t=sinθ+cosθ, sinθcosθ=(t²-1)/2
    t=sp.symbols("t"); f=t+a*(t*t-1)/2
    ts=np.linspace(-math.sqrt(2),math.sqrt(2),400001); v=[float(f.subs(t,tt)) for tt in ts[::2000]]
    # brute over θ
    th_=np.linspace(0,2*np.pi,400001); y=np.sin(th_)+np.cos(th_)+a*np.sin(th_)*np.cos(th_)
    # candidate critical
    crit=[-sp.sqrt(2),sp.sqrt(2)]+[sp.solve(sp.diff(f,t),t)[0]] 
    crit=[c for c in crit if -sp.sqrt(2)<=c<=sp.sqrt(2)]
    vals=[sp.nsimplify(sp.simplify(f.subs(t,c))) for c in crit]
    mx=max(vals,key=float); mn=min(vals,key=float)
    assert abs(float(mx)-y.max())<1e-6 and abs(float(mn)-y.min())<1e-6
    st=[("置き換え","<p>"+I(r"t=\sin\theta+\cos\theta=\sqrt2\sin\left(\theta+\dfrac\pi4\right)")+" より "+I(r"-\sqrt2\leqq t\leqq\sqrt2")+"。</p><p>"+I(r"\sin\theta\cos\theta=\dfrac{t^2-1}{2}")+"。</p>"),
        ("$t$ の関数","<p>"+D(r"y=%s=%s"%(L(f),L(sp.expand(f))))),
        ("最大・最小","<p>"+D(r"\text{最大 }%s,\qquad \text{最小 }%s"%(L(mx),L(mn))))]
    return r"$0\leqq\theta<2\pi$ のとき、$y=\sin\theta+\cos\theta%+d\sin\theta\cos\theta$ の最大値と最小値を求めよ。"%a if a!=1 else r"$0\leqq\theta<2\pi$ のとき、$y=\sin\theta+\cos\theta+\sin\theta\cos\theta$ の最大値と最小値を求めよ。",st,r"\text{最大 }%s,\ \text{最小 }%s"%(L(mx),L(mn))
o=[b10(a) for a in [1,2,-1,3,-2]]
build(Z,CH,"sinθ+cosθ=t の置き換え（sinθcosθ を含む）",o,"<p>$t=\\sin\\theta+\\cos\\theta$ とおくと $\\sin\\theta\\cos\\theta=\\dfrac{t^2-1}{2}$。<b>$t$ の範囲 $-\\sqrt2\\leqq t\\leqq\\sqrt2$</b> での2次関数の最大・最小。</p>","和を t とおけば、積も t で書ける。",10)
XU=finishx(Z,CH)
