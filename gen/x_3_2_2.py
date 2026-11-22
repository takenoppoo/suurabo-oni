# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,t=sp.symbols("x t")
def co(c): return "" if c==1 else L(c)
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
    B=co(b); AB=a*b; AB2=a*b*b
    st=[("位置を $t$ で微分して速度を求める","<p>"+I(r"(\cos %st)'=-%s\sin %st"%(B,L(b) if b!=1 else "",B)).replace("-1\\sin","-\\sin")+"、"+I(r"(\sin %st)'=%s\cos %st"%(B,L(b) if b!=1 else "",B))+"。</p>"+D(r"\vec v=\left(\dfrac{dx}{dt},\dfrac{dy}{dt}\right)=\left(-%s\sin %st,\ %s\cos %st\right)"%(co(AB),B,co(AB),B))+fg),
        ("速さを求める","<p>速さは速度ベクトルの大きさ。</p>"+D(r"|\vec v|=\sqrt{%s^2\sin^2%st+%s^2\cos^2%st}"%(L(AB),B,L(AB),B))+"<p>"+I(r"%s^2"%L(AB))+" でくくり、"+I(r"\sin^2\theta+\cos^2\theta=1")+" を使う。</p>"+D(r"=\sqrt{%s\left(\sin^2%st+\cos^2%st\right)}=\sqrt{%s}=%s"%(L(AB*AB),B,B,L(AB*AB),L(AB)))),
        ("速度をさらに微分して加速度を求める","<p>"+D(r"\vec\alpha=\left(\dfrac{d^2x}{dt^2},\dfrac{d^2y}{dt^2}\right)=\left(-%s\cos %st,\ -%s\sin %st\right)"%(co(AB2),B,co(AB2),B))),
        ("加速度の大きさを求める","<p>同様に "+I(r"\sin^2+\cos^2=1")+" を使う。</p>"+D(r"|\vec\alpha|=\sqrt{%s^2\left(\cos^2%st+\sin^2%st\right)}=%s"%(L(AB2),B,B,L(AB2))))]
    return r"点 $P$ が $x=%s\cos %st,\ y=%s\sin %st$ にしたがって動く。時刻 $t$ における速さと加速度の大きさを求めよ。"%(a,B,a,B),st,r"\text{速さ }%d,\ \text{加速度の大きさ }%d"%(a*b,a*b*b)
o=[b6(*v) for v in [(2,3),(3,2),(5,1),(4,3),(6,2)]]
build(Z,CH,"等速円運動の速さと加速度",o,"<p>速度 $=\\left(\\dfrac{dx}{dt},\\dfrac{dy}{dt}\\right)$、速さはその大きさ。加速度は速度をさらに $t$ で微分。等速円運動では加速度は中心を向く。</p>","位置を微分すると速度、速度を微分すると加速度。",6)
# 7 近似式
def b7(f,a,h,label):
    fa=f.subs(x,a); fp=sp.diff(f,x).subs(x,a); approx=fa+fp*h; exact=float(f.subs(x,a+h))
    fpx=sp.diff(f,x); fpa=sp.simplify(fp)
    st=[("1次近似の公式を確認する","<p>"+I(r"f(a+h)\fallingdotseq f(a)+f'(a)h")+"（"+I("|h|")+" が小さいとき）。</p>"),
        ("$a,\\ h$ を決める","<p>"+I(label)+" を "+I("f(a+h)")+" の形に見る。"+I("f(x)=%s"%L(f))+" とし、計算しやすい近くの値 "+I("a=%s"%L(a))+" をとる。</p>"+D(r"a+h=%s+%s\ \Rightarrow\ h=%s"%(L(a),L(h),L(h)))),
        ("$f(a)$ を求める",D(r"f(%s)=%s"%(L(a),L(fa)))),
        ("$f'(x)$ と $f'(a)$ を求める","<p>"+D(r"f'(x)=%s"%L(fpx))+D(r"f'(%s)=%s"%(L(a),L(fpa)))),
        ("公式に代入する","<p>"+D(r"%s\fallingdotseq f(%s)+f'(%s)\cdot h=%s+%s\times%s"%(label,L(a),L(a),L(fa),L(fpa),L(h)))+D(r"=%s"%L(sp.nsimplify(approx)))+"<p>（真の値 "+I("%.5f"%exact)+"）。</p>")]
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
    nm_,dn_=sp.fraction(sp.together(f)); p_=sp.Poly(nm_,x).coeff_monomial(x); q_=sp.Poly(dn_,x).coeff_monomial(1)
    rq=sp.sqrt(q_); xmax=rq; xmin=-rq
    st=[("商の微分で導関数を求める","<p>"+I(r"f=%sx,\ g=x^2+%s"%(co(p_),L(q_)))+"。"+I(r"f'=%s,\ g'=2x"%L(p_))+"。</p>"+D(r"f'(x)=\dfrac{%s(x^2+%s)-%sx\cdot2x}{(x^2+%s)^2}=\dfrac{%s}{(x^2+%s)^2}"%(L(p_),L(q_),co(p_),L(q_),L(sp.expand(p_*(q_-x**2))),L(q_)))),
        ("$f'(x)=0$ を解く","<p>分母は正なので、分子 "+I(r"%s=0"%L(sp.expand(p_*(q_-x**2))))+" を解く。</p>"+D(r"x^2=%s\ \Rightarrow\ x=\pm%s"%(L(q_),L(rq)))),
        ("増減表をかく","<p>"+I("f'(x)")+" の符号は分子 "+I(L(sp.expand(p_*(q_-x**2))))+" の符号と同じ。</p>"+wtable(["$x$","$\\cdots$","$-%s$"%L(rq),"$\\cdots$","$%s$"%L(rq),"$\\cdots$"],[["$f'(x)$","$-$","$0$","$+$","$0$","$-$"],["$f(x)$","↘","$%s$（極小）"%L(mn),"↗","$%s$（極大）"%L(mx),"↘"]])+fg),
        ("極値を求める","<p>"+D(r"f\left(%s\right)=\dfrac{%s}{%s}%s,\qquad f\left(-%s\right)=%s"%(L(rq),L(p_*rq),L(2*q_),("" if L(sp.Rational(1))=="" else ("" if r"\dfrac{%s}{%s}"%(L(p_*rq),L(2*q_))==L(mx) else "=%s"%L(mx))),L(rq),L(mn)))),
        ("漸近線を調べる","<p>分子・分母を "+I("x^2")+" でわる。</p>"+D(r"f(x)=\dfrac{%s/x}{1+%s/x^2}"%(L(p_),L(q_)))+"<p>"+I(r"x\to\pm\infty")+" のとき "+I(r"\dfrac1x\to0,\ \dfrac1{x^2}\to0")+"。</p>"+D(r"\lim_{x\to\pm\infty}f(x)=\dfrac{0}{1+0}=0")+"<p>漸近線は "+I("y=0")+"。</p>")]
    return r"関数 $f(x)=%s$ の極値と漸近線を求め、グラフの概形をかけ。"%L(f),st,r"\text{極大値 }%s,\ \text{極小値 }%s,\ \text{漸近線 }y=0"%(L(mx),L(mn))
o=[b8(x/(x**2+1),"a"),b8(2*x/(x**2+4),"b"),b8(x/(x**2+9),"c"),b8(3*x/(x**2+1),"d"),b8(4*x/(x**2+16),"e")]
build(Z,CH,"分数関数のグラフ（極値と漸近線）",o,"<p>導関数の符号で増減を調べ、極値を求める。$x\\to\\pm\\infty$ の極限から漸近線。奇関数なら原点対称。</p>","山と谷の位置と、遠くでの落ち着き先がわかればグラフが描ける。",8)
# 9 不等式 e^x >= 1+x 系
def b9(a):
    f=sp.exp(a*x)-(1+a*x); fp=sp.diff(f,x)
    def dr(ax):
        xs=np.linspace(-2.5,2.5,300); ax.plot(xs,np.exp(a*xs),color="#b81f36",lw=2); ax.plot(xs,1+a*xs,color="#1f6fb8",lw=1.6); mark(ax,0,1)
    fg=gplane("x322_9_%d"%a,(-2.6,2.6),(-3,8),dr,size=(4.2,3),w=50)
    A=co(a); EA="e^{%sx}"%A if a!=1 else "e^{x}"
    st=[("差の関数をつくる","<p>"+I(r"f(x)=%s-(1+%sx)"%(EA,A))+" とおき、"+I(r"f(x)\geqq0")+" を示す。</p>"),
        ("導関数を求める","<p>"+I(r"(%s)'=%s%s"%(EA,A,EA))+"。</p>"+D((r"f'(x)=%s%s-%s=%s(%s-1)"%(A,EA,L(a),L(a),EA)) if a!=1 else r"f'(x)=e^{x}-1")),
        ("$f'(x)=0$ を解く","<p>"+I(r"%s=1=e^0"%EA)+" より "+(I(r"%sx=0"%A)+"、つまり "+I("x=0") if a!=1 else I("x=0"))+"。</p>"),
        ("増減表をかく","<p>"+I("e^{t}")+" は "+I("t")+" とともに増えるので、"+I("x<0")+" では "+I(r"%s<1"%EA)+"、"+I("x>0")+" では "+I(r"%s>1"%EA)+"。</p>"+wtable(["$x$","$\\cdots$","$0$","$\\cdots$"],[["$f'(x)$","$-$","$0$","$+$"],["$f(x)$","↘","$0$（最小）","↗"]])+fg),
        ("最小値を求める","<p>"+D(r"f(0)=e^0-1=1-1=0")+"<p>最小値が "+I("0")+" なので、すべての "+I("x")+" で "+I(r"f(x)\geqq0")+"。等号は "+I("x=0")+" のとき。</p>")]
    return r"すべての実数 $x$ について $%s\geqq1+%sx$ が成り立つことを証明せよ。"%(EA,A),st,r"\text{証明終}"
o=[b9(a) for a in [1,2,3,4,5]]
build(Z,CH,"e^{ax} ≥ 1+ax の証明",o,"<p>差を $f(x)$ とおき、<b>最小値が 0</b> になることを増減で示す。接線の下に曲線がない（下に凸）という見方もできる。</p>","e^x のグラフは、点 (0,1) の接線の上に乗っている。",9)
# 10 最大最小（距離・面積）
def b10(a):
    # rectangle inscribed in y=e^{-x}... use  point P on y=e^{-x}(x>0), rectangle O..P area xy = x e^{-x}; max at x=1 -> 1/e
    ANS=r"\dfrac{1}{%se}"%('' if a==1 else str(a)); f=x*sp.exp(-a*x); xm=sp.solve(sp.diff(f,x),x)[0]; mx=sp.simplify(f.subs(x,xm))
    def dr(ax):
        xs=np.linspace(0,5,300); ax.plot(xs,np.exp(-a*xs),color="#b81f36",lw=2)
        xx=float(xm); yy=math.exp(-a*xx); ax.fill([0,xx,xx,0],[0,0,yy,yy],color="#f6c6cc"); mark(ax,xx,yy,"P",.3,.3)
    fg=gplane("x322_10_%d"%a,(-.5,5),(-.3,1.3),dr,size=(4.2,3),w=50,ys=.5)
    A=co(a); EA="e^{-%sx}"%A
    st=[("面積を $x$ の式で表す","<p>"+I(r"P(x,\ %s)"%EA)+"。長方形の横が "+I("x")+"、縦が "+I(EA)+"。</p>"+D(r"S(x)=x\,%s\ (x>0)"%EA)+fg),
        ("積の微分で $S'(x)$ を求める","<p>"+I(r"(%s)'=-%s%s"%(EA,A,EA))+"。</p>"+D(r"S'(x)=1\cdot %s+x\cdot(-%s%s)"%(EA,A,EA))+"<p>"+I(EA)+" でくくる。</p>"+D(r"=(1-%sx)%s"%(A,EA))),
        ("$S'(x)=0$ を解く","<p>"+I(EA+">0")+" だから "+I(r"1-%sx=0"%A)+"。</p>"+D(r"x=%s"%L(xm))),
        ("増減表をかく","<p>"+I("S'(x)")+" の符号は "+I(r"1-%sx"%A)+" と同じ。</p>"+wtable(["$x$","$0$","$\\cdots$","$%s$"%L(xm),"$\\cdots$"],[["$S'(x)$","","$+$","$0$","$-$"],["$S(x)$","","↗","最大","↘"]])),
        ("最大値を求める","<p>"+I("x=%s"%L(xm))+" を代入。"+I(r"%sx=1"%A)+" だから "+I(r"%s=e^{-1}"%EA)+"。</p>"+D(r"S(%s)=%s\cdot e^{-1}=%s"%(L(xm),L(xm),ANS)))]
    return r"曲線 $y=%s\ (x>0)$ 上の点 $P$ から $x$ 軸、$y$ 軸に下ろした垂線と両軸が作る長方形の面積の最大値を求めよ。"%EA,st,ANS
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"曲線上の点が作る長方形の面積の最大",o,"<p>点 $P$ を $x$ で表し、面積を $x$ の関数にして微分。$x>0$ の範囲で増減表。</p>","動く点が作る面積を1つの式にして、山の頂上を探す。",10)
XU=finishx(Z,CH)
