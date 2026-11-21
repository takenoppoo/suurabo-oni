# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,t=sp.symbols("x t")
# 6 速度と加速度
def b6(a,b):
    # x=a sin t + b cos? circular motion x=r cos wt, y=r sin wt : speed r w
    xf=a*sp.cos(b*t); yf=a*sp.sin(b*t)
    vx=sp.diff(xf,t); vy=sp.diff(yf,t); sp_=sp.simplify(sp.sqrt(vx**2+vy**2)); ax=sp.diff(xf,t,2); ay=sp.diff(yf,t,2); ac=sp.simplify(sp.sqrt(ax**2+ay**2))
    assert sp_==a*b and ac==a*b*b
    def dr(axx):
        th=np.linspace(0,2*np.pi,300); axx.plot(a*np.cos(th),a*np.sin(th),color="#b81f36",lw=2)
        mark(axx,a*math.cos(1.0),a*math.sin(1.0),"P",.4,.4)
    fg=gplane("x322_6_%d_%d"%(a,b),(-a-1.5,a+1.5),(-a-1.5,a+1.5),dr,size=(4,3.2),w=46)
    st=[("速度ベクトル","<p>"+D(r"\vec v=\left(\dfrac{dx}{dt},\dfrac{dy}{dt}\right)=\left(-%d\sin%dt,\ %d\cos%dt\right)"%(a*b,b,a*b,b))+fg),
        ("速さ","<p>"+D(r"|\vec v|=\sqrt{%d^2\sin^2%dt+%d^2\cos^2%dt}=%d"%(a*b,b,a*b,b,a*b))),
        ("加速度の大きさ","<p>"+D(r"\vec\alpha=\left(-%d\cos%dt,\ -%d\sin%dt\right),\qquad |\vec\alpha|=%d"%(a*b*b,b,a*b*b,b,a*b*b)))]
    return r"点 $P$ が $x=%d\cos%dt,\ y=%d\sin%dt$ にしたがって動く。時刻 $t$ における速さと加速度の大きさを求めよ。"%(a,b,a,b),st,r"\text{速さ }%d,\ \text{加速度の大きさ }%d"%(a*b,a*b*b)
o=[b6(*v) for v in [(2,3),(3,2),(5,1),(4,3),(6,2)]]
build(Z,CH,"等速円運動の速さと加速度",o,"<p>速度 $=\\left(\\dfrac{dx}{dt},\\dfrac{dy}{dt}\\right)$、速さはその大きさ。加速度は速度をさらに $t$ で微分。等速円運動では加速度は中心を向く。</p>","位置を微分すると速度、速度を微分すると加速度。",6)
# 7 近似式
def b7(f,a,h,label):
    fa=f.subs(x,a); fp=sp.diff(f,x).subs(x,a); approx=fa+fp*h; exact=float(f.subs(x,a+h))
    st=[("1次近似の公式","<p>"+I(r"f(a+h)\fallingdotseq f(a)+f'(a)h")+"（"+I("|h|")+" が小さいとき）。</p>"),
        ("値","<p>"+I("f(x)=%s"%L(f))+"、"+I("f(%s)=%s,\\ f'(%s)=%s"%(L(a),L(fa),L(a),L(sp.simplify(fp))))+"。</p>"),
        ("近似","<p>"+D(r"%s\fallingdotseq%s+%s\times%s=%s"%(label,L(fa),L(sp.simplify(fp)),L(h),L(sp.nsimplify(approx))))+"<p>（真の値 "+I("%.5f"%exact)+"）。</p>")]
    return r"1次近似を用いて、$%s$ の近似値を求めよ。"%label,st,L(sp.nsimplify(approx))
o=[b7(sp.sqrt(x),4,R(1,10) if False else R(1,5),r"\sqrt{4.2}"),b7(x**R(1,3),8,R(3,10),r"\sqrt[3]{8.3}"),b7(1/x,2,R(-1,10),r"\dfrac1{1.9}"),b7(sp.log(x),1,R(1,10),r"\log1.1"),b7(x**3,10,R(1,10),r"10.1^3")]
build(Z,CH,"1次近似による近似値",o,"<p>$f(a+h)\\fallingdotseq f(a)+f'(a)h$。接線の高さで近似する。$a$ は計算しやすい近くの値を選ぶ。</p>","曲線のそばは、接線でほぼ代用できる。",7)
# 8 漸近線とグラフ
def b8(f,name):
    fp=sp.simplify(sp.diff(f,x)); crit=sp.solve(fp,x); 
    vals=[sp.simplify(f.subs(x,c)) for c in crit]
    def dr(ax):
        xs=np.linspace(-6,6,500); fl=sp.lambdify(x,f,"numpy"); ax.plot(xs,fl(xs),color="#b81f36",lw=2)
        for c,v in zip(crit,vals): mark(ax,float(c),float(v),"",0,0)
    fg=gplane("x322_8_"+name,(-6.2,6.2),(-1.2,1.2),dr,size=(4.4,3),w=52,xs=2,ys=.5)
    mx=max(vals,key=float); mn=min(vals,key=float)
    st=[("導関数","<p>"+D(r"f'(x)=%s"%L(fp))+"<p>"+I("f'(x)=0")+" より "+I("x=%s"%(r",\ ".join(L(c) for c in crit)))+"。</p>"),
        ("増減と極値","<p>"+D(r"\text{極大値 }%s,\qquad \text{極小値 }%s"%(L(mx),L(mn)))+fg),
        ("漸近線","<p>"+D(r"\lim_{x\to\pm\infty}f(x)=0")+"<p>漸近線は "+I("y=0")+"。</p>")]
    return r"関数 $f(x)=%s$ の極値と漸近線を求め、グラフの概形をかけ。"%L(f),st,r"\text{極大値 }%s,\ \text{極小値 }%s,\ \text{漸近線 }y=0"%(L(mx),L(mn))
o=[b8(x/(x**2+1),"a"),b8(2*x/(x**2+4),"b"),b8(x/(x**2+9),"c"),b8(3*x/(x**2+1),"d"),b8(4*x/(x**2+16),"e")]
build(Z,CH,"分数関数のグラフ（極値と漸近線）",o,"<p>導関数の符号で増減を調べ、極値を求める。$x\\to\\pm\\infty$ の極限から漸近線。奇関数なら原点対称。</p>","山と谷の位置と、遠くでの落ち着き先がわかればグラフが描ける。",8)
# 9 不等式 e^x >= 1+x 系
def b9(a):
    f=sp.exp(a*x)-(1+a*x); fp=sp.diff(f,x)
    def dr(ax):
        xs=np.linspace(-2.5,2.5,300); ax.plot(xs,np.exp(a*xs),color="#b81f36",lw=2); ax.plot(xs,1+a*xs,color="#1f6fb8",lw=1.6); mark(ax,0,1)
    fg=gplane("x322_9_%d"%a,(-2.6,2.6),(-3,8),dr,size=(4.2,3),w=50)
    st=[("差の関数","<p>"+I("f(x)=e^{%dx}-(1+%dx)"%(a,a))+"。"+D(r"f'(x)=%de^{%dx}-%d=%d(e^{%dx}-1)"%(a,a,a,a,a))),
        ("増減","<p>"+I("f'(x)=0")+" は "+I("x=0")+"。"+I("x<0")+" で減少、"+I("x>0")+" で増加。</p>"+fg),
        ("最小値","<p>"+D(r"f(0)=1-1=0\ \Rightarrow\ f(x)\geqq0")+"<p>等号は "+I("x=0")+"。</p>")]
    return r"すべての実数 $x$ について $e^{%dx}\geqq1+%dx$ が成り立つことを証明せよ。"%(a,a),st,r"\text{証明終}"
o=[b9(a) for a in [1,2,3,4,5]]
build(Z,CH,"e^{ax} ≥ 1+ax の証明",o,"<p>差を $f(x)$ とおき、<b>最小値が 0</b> になることを増減で示す。接線の下に曲線がない（下に凸）という見方もできる。</p>","e^x のグラフは、点 (0,1) の接線の上に乗っている。",9)
# 10 最大最小（距離・面積）
def b10(a):
    # rectangle inscribed in y=e^{-x}... use  point P on y=e^{-x}(x>0), rectangle O..P area xy = x e^{-x}; max at x=1 -> 1/e
    f=x*sp.exp(-a*x); xm=sp.solve(sp.diff(f,x),x)[0]; mx=sp.simplify(f.subs(x,xm))
    def dr(ax):
        xs=np.linspace(0,5,300); ax.plot(xs,np.exp(-a*xs),color="#b81f36",lw=2)
        xx=float(xm); yy=math.exp(-a*xx); ax.fill([0,xx,xx,0],[0,0,yy,yy],color="#f6c6cc"); mark(ax,xx,yy,"P",.3,.3)
    fg=gplane("x322_10_%d"%a,(-.5,5),(-.3,1.3),dr,size=(4.2,3),w=50,ys=.5)
    st=[("面積の式","<p>"+I("P(x,\\ e^{-%dx})"%a)+"。長方形 "+I("O,\\ (x,0),\\ P,\\ (0,e^{-%dx})"%a)+" の面積：</p>"+D(r"S(x)=xe^{-%dx}\ (x>0)"%a)+fg),
        ("増減","<p>"+D(r"S'(x)=(1-%dx)e^{-%dx}"%(a,a))+"<p>"+I("x=%s"%L(xm))+" で増加から減少へ。</p>"),
        ("最大値",D(r"S(%s)=%s"%(L(xm),L(mx))))]
    return r"曲線 $y=e^{-%dx}\ (x>0)$ 上の点 $P$ から $x$ 軸、$y$ 軸に下ろした垂線と両軸が作る長方形の面積の最大値を求めよ。"%a,st,L(mx)
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"曲線上の点が作る長方形の面積の最大",o,"<p>点 $P$ を $x$ で表し、面積を $x$ の関数にして微分。$x>0$ の範囲で増減表。</p>","動く点が作る面積を1つの式にして、山の頂上を探す。",10)
XU=finishx(Z,CH)
