# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,t=sp.symbols("x t")
def shade(ax,f1,f2,a,b,col="#f6c6cc"):
    xs=np.linspace(a,b,200); y1=np.array([float(f1.subs(x,v)) for v in xs]); y2=np.array([float(f2.subs(x,v)) for v in xs]); ax.fill_between(xs,y1,y2,color=col,alpha=.8)
# 6 放物線と接線で囲まれた面積
def b6(a,p):
    # y=a x^2 and tangent at x=p ; area with y-axis? region between parabola, tangent and x-axis? use: parabola y=a x^2, tangent at x=p, and the y-axis
    f=a*x**2; tl=sp.expand(2*a*p*(x-p)+a*p*p)
    ar=sp.integrate(f-tl,(x,0,p)) if p>0 else sp.integrate(f-tl,(x,p,0))
    ar=abs(ar)
    def dr(ax):
        xs=np.linspace(-1,p+1.5,300); ax.plot(xs,a*xs**2,color="#b81f36",lw=2); ax.plot(xs,[float(tl.subs(x,v)) for v in xs],color="#1f6fb8",lw=1.8)
        shade(ax,f,tl,0,p); mark(ax,p,a*p*p,"(%d,%d)"%(p,a*p*p),.6,.4)
    fg=gplane("x252_6_%d_%d"%(a,p),(-1,p+1.8),(-a*p*p-2,a*(p+1.5)**2+1),dr,size=(4.4,3.2),w=54)
    st=[("接線","<p>"+I("f(x)=%dx^2"%a)+"、"+I("f'(x)=%dx"%(2*a))+"。"+I("x=%d"%p)+" での接線：</p>"+D(r"y=%d(x-%d)+%d=%s"%(2*a*p,p,a*p*p,L(tl)))),
        ("面積の式","<p>放物線が上、接線が下。"+I("0\\leqq x\\leqq%d"%p)+"。</p>"+D(r"\int_0^{%d}\{%dx^2-(%s)\}dx=\int_0^{%d}%s\,dx"%(p,a,L(tl),p,L(sp.factor(f-tl))))+fg),
        ("計算",D(r"%s\int_0^{%d}(x-%d)^2dx=%s\left[\dfrac{(x-%d)^3}{3}\right]_0^{%d}=%s"%(L(a),p,p,L(a),p,p,L(ar))))]
    return r"放物線 $y=%dx^2$ 上の点 $(%d,%d)$ における接線と、この放物線および $y$ 軸で囲まれた図形の面積を求めよ。"%(a,p,a*p*p),st,L(ar)
o=[b6(*v) for v in [(1,2),(2,1),(1,3),(3,1),(2,2)]]
build(Z,CH,"放物線・接線・y軸で囲まれた面積",o,"<p>接線の式を求め、<b>（上の式）$-$（下の式）</b>を積分。差が $a(x-p)^2$ の形になるので $\\dfrac a3(\\cdot)^3$ で計算できる。</p>","接する点では差が2乗でつぶれる。",6)
# 7 3次関数と直線
def b7(a,b):
    # y=x(x-a)(x-b)?? : cubic y = x^3 - ... use y=x^3-3x and line y=? choose y=x(x-a)(x+a)=x^3-a^2 x and y=0 : area = 2*(a^4/4)
    f=x**3-a*a*x; ar=2*sp.integrate(-f,(x,0,a)); 
    # line y=b x -> intersection x^3-(a^2+b)x=0
    g=b*x; s=sp.sqrt(a*a+b); area=2*sp.integrate(g-f,(x,0,s)); area=sp.simplify(area)
    def dr(ax):
        xs=np.linspace(-s-.5,s+.5,300); ax.plot(xs,xs**3-a*a*xs,color="#b81f36",lw=2); ax.plot(xs,b*xs,color="#1f6fb8",lw=1.8)
        shade(ax,f,g,0,float(s)); shade(ax,g,f,-float(s),0)
    fg=gplane("x252_7_%d_%d"%(a,b),(-s-.7,s+.7),(-(float(s)**3)-1,(float(s)**3)+1),dr,size=(4.4,3.2),w=54)
    st=[("交点","<p>"+D(r"x^3-%dx=%dx\ \Rightarrow\ x(x^2-%d)=0\ \Rightarrow\ x=0,\ \pm%s"%(a*a,b,a*a+b,L(s)))+fg),
        ("対称性","<p>原点対称なので "+I("x\\geqq0")+" の部分の2倍。区間 "+I("0\\leqq x\\leqq%s"%L(s))+" で直線が上。</p>"),
        ("面積",D(r"2\int_0^{%s}\left(%s-%s\right)dx=2\left[%s\right]_0^{%s}=%s"%(L(s),L(g),L(f),L(sp.integrate(g-f,x)),L(s),L(area))))]
    return r"曲線 $y=x^3-%dx$ と直線 $y=%dx$ で囲まれた2つの部分の面積の合計を求めよ。"%(a*a,b),st,L(area)
o=[b7(*v) for v in [(1,3),(2,0) if False else (2,5),(1,8),(3,7),(2,12)]]
build(Z,CH,"3次関数と直線で囲まれた面積",o,"<p>交点を求めて区間を分け、<b>上下関係を確認</b>して積分。原点対称なら片側を2倍。</p>","上の関数から下の関数を引いて、区間ごとに足す。",7)
# 8 2放物線
def b8(c,d):
    # y=x^2 and y=-x^2+2c x+d  -> intersection x^2 = -x^2+2c x+d -> 2x^2-2c x-d=0
    f1=x**2; f2=-x**2+2*c*x+d
    rts=sorted(sp.solve(f1-f2,x)); al,be=rts
    ar=sp.simplify(sp.integrate(f2-f1,(x,al,be)))
    def dr(ax):
        xs=np.linspace(float(al)-1,float(be)+1,300); ax.plot(xs,xs**2,color="#b81f36",lw=2); ax.plot(xs,-xs**2+2*c*xs+d,color="#1f6fb8",lw=2)
        shade(ax,f1,f2,float(al),float(be)); mark(ax,al,al**2,"",0,0); mark(ax,be,be**2)
    fg=gplane("x252_8_%d_%d"%(c,d),(float(al)-1.2,float(be)+1.2),(-2,float(max(f2.subs(x,R(c,2)),be**2))+2),dr,size=(4.4,3.2),w=54)
    st=[("交点","<p>"+D(r"x^2=-x^2+%dx%+d\ \Rightarrow\ %s=0\ \Rightarrow\ x=%s"%(2*c,d,L(sp.expand(2*x**2-2*c*x-d)),r",\ ".join(L(v) for v in rts)))+fg),
        ("面積の式","<p>上が "+I("y=%s"%L(f2))+"、下が "+I("y=x^2")+"。差は "+I(L(sp.expand(f2-f1)))+"。</p>"+D(r"\int_{%s}^{%s}(%s)dx=%s\int_{\alpha}^{\beta}(x-\alpha)(\beta-x)dx"%(L(al),L(be),L(sp.expand(f2-f1)),2))),
        ("公式","<p>"+I(r"\displaystyle\int_\alpha^\beta(x-\alpha)(\beta-x)dx=\dfrac{(\beta-\alpha)^3}{6}")+"。</p>"+D(r"2\cdot\dfrac{(%s)^3}{6}=%s"%(L(be-al),L(ar))))]
    return r"2つの放物線 $y=x^2$ と $y=-x^2+%dx%+d$ で囲まれた図形の面積を求めよ。"%(2*c,d),st,L(ar)
o=[b8(*v) for v in [(1,0),(2,0),(1,4) if False else (2,6),(3,0),(2,10)]]
build(Z,CH,"2つの放物線で囲まれた面積（6分の1公式）",o,"<p>交点の $x$ 座標 $\\alpha,\\beta$ を求め、差を $-2(x-\\alpha)(x-\\beta)$ とみると $\\dfrac{2(\\beta-\\alpha)^3}{6}$。<b>$\\dfrac16$ 公式</b>で一気に計算できる。</p>","2次の差は、2つの交点だけで面積が決まる。",8)
# 9 面積を2等分
def b9(a):
    # parabola y=x(a-x)... area between curve and x axis; line y=m x through origin bisects area
    f=x*(a-x); tot=sp.integrate(f,(x,0,a)); m=sp.symbols("m")
    # line y=m x meets curve at x=a-m ; area between = (a-m)^3/6 = tot/2 -> (a-m)^3 = tot*3
    c=(3*tot).evalf()
    am=sp.Integer(round(float(sp.cbrt(3*tot)))) if sp.cbrt(3*tot).is_rational else None
    ans=sp.cbrt(3*tot); mm=a-ans
    def dr(ax):
        xs=np.linspace(0,a,200); ax.plot(xs,xs*(a-xs),color="#b81f36",lw=2); ax.plot(xs,float(mm)*xs,color="#1f6fb8",lw=1.8)
        shade(ax,f,m*x if False else mm*x,0,float(a-mm))
    fg=gplane("x252_9_%d"%a,(-.5,a+.5),(-1,float(a*a)/4+1.5),dr,size=(4.4,3),w=52)
    st=[("全体の面積","<p>"+I("y=x(%d-x)"%a)+" と "+I("x")+" 軸：</p>"+D(r"\int_0^{%d}x(%d-x)dx=\dfrac{%d^3}{6}=%s"%(a,a,a,L(tot)))),
        ("直線 y=mx","<p>放物線との交点は "+I("x=%d-m"%a)+"。間の面積：</p>"+D(r"\dfrac{(%d-m)^3}{6}=\dfrac12\cdot%s"%(a,L(tot)))+fg),
        ("m を求める","<p>"+D(r"(%d-m)^3=%s\ \Rightarrow\ m=%d-%s=%s"%(a,L(3*tot),a,L(ans),L(mm))))]
    return r"放物線 $y=x(%d-x)$ と $x$ 軸で囲まれた図形の面積を、原点を通る直線 $y=mx$ ($0<m<%d$) が2等分するとき、$m$ の値を求めよ。"%(a,a),st,L(mm)
o=[b9(a) for a in [2,4,6,3,5]]
build(Z,CH,"放物線の面積を直線で2等分",o,"<p>全体の面積 $\\dfrac{a^3}{6}$ と、直線で切った部分の面積 $\\dfrac{(\\beta-\\alpha)^3}{6}$ を比べて $m$ の方程式を作る。</p>","6分の1公式で、一部の面積も全体と同じ形で書ける。",9)
# 10 定積分が最小になる a
def b10(c):
    # I(a)=∫_0^c |x-a| dx for 0<=a<=c : min at a=c/2 -> c^2/4 ; or ∫0^c (x-a)^2 dx min at a=c/2
    a=sp.symbols("a"); I_=sp.integrate((x-a)**2,(x,0,c)); mnv=I_.subs(a,R(c,2))
    def dr(ax):
        aa=np.linspace(-1,c+1,200); ax.plot(aa,[float(I_.subs(a,v)) for v in aa],color="#b81f36",lw=2); mark(ax,R(c,2),mnv,"",0,0)
    fg=gplane("x252_10_%d"%c,(-1.2,c+1.2),(-1,float(I_.subs(a,-1))+1),dr,size=(4.4,3),w=52)
    st=[("積分を計算","<p>"+D(r"F(a)=\int_0^{%d}(x-a)^2dx=\left[\dfrac{(x-a)^3}{3}\right]_0^{%d}=%s"%(c,c,L(sp.expand(I_))))),
        ("平方完成","<p>"+D(r"F(a)=%s"%L(sp.expand(I_)))+D(r"=%s\left(a-%s\right)^2+%s"%(L(c),L(R(c,2)),L(mnv)))+fg),
        ("最小","<p>"+I("a=%s"%L(R(c,2)))+" のとき最小値 "+I(L(mnv))+"。</p>")]
    return r"定数 $a$ に対して $F(a)=\displaystyle\int_0^{%d}(x-a)^2dx$ とおく。$F(a)$ を最小にする $a$ と、そのときの最小値を求めよ。"%c,st,r"a=%s,\ \text{最小値 }%s"%(L(R(c,2)),L(mnv))
o=[b10(c) for c in [2,4,6,3,5]]
build(Z,CH,"積分を含む関数 F(a) の最小",o,"<p>まず<b>定積分を実行して $a$ の関数</b>にし、平方完成（または微分）で最小を求める。積分変数は $x$、$a$ は定数として扱う。</p>","積分が終わったら、普通の2次関数の問題。",10)
XU=finishx(Z,CH)
