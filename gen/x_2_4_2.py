# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x")
# 6 log_a b = p のとき
def b6(a,b,n,m):
    # given log_2 3 = p ... express log_n m  with n,m products of 2,3
    p,q=sp.symbols("p q")
    f2=sp.factorint(n); f3=sp.factorint(m)
    def lg(N):
        f=sp.factorint(N); return f.get(2,0)*1+f.get(3,0)*p
    num=lg(m); den=lg(n); ex=sp.simplify(num/den)
    val=math.log(m)/math.log(n)
    pv=math.log(3,2)
    assert abs(float(ex.subs(p,pv))-val)<1e-9
    st=[("底を2にそろえる","<p>"+I(r"\log_{%d}%d=\dfrac{\log_2%d}{\log_2%d}"%(n,m,m,n))+"。</p>"),
        ("素因数分解","<p>"+I(r"%d=%s,\ %d=%s"%(m,r"\cdot".join(("%d^{%d}"%(pp,e) if e>1 else str(pp)) for pp,e in sorted(sp.factorint(m).items())),n,r"\cdot".join(("%d^{%d}"%(pp,e) if e>1 else str(pp)) for pp,e in sorted(sp.factorint(n).items()))))+"。</p>"+D(r"\log_2%d=%s,\qquad \log_2%d=%s"%(m,L(num),n,L(den)))),
        ("答え",D(r"\log_{%d}%d=\dfrac{%s}{%s}"%(n,m,L(num),L(den))))]
    return r"$\log_23=p$ とするとき、$\log_{%d}%d$ を $p$ で表せ。"%(n,m),st,r"\dfrac{%s}{%s}"%(L(num),L(den))
o=[b6(2,3,12,18),b6(2,3,6,24),b6(2,3,18,12),b6(2,3,24,36),b6(2,3,36,72)]
build(Z,CH,"log₂3=p から log_n m を表す",o,"<p>底の変換公式で<b>底を 2</b> にそろえ、真数と底をそれぞれ $2^a3^b$ に素因数分解して $\\log_2 2=1,\\ \\log_2 3=p$ を代入。</p>","どの数も 2 と 3 の積に分解して、p で言い換える。",6)
# 7 グラフ移動・対称
def b7(a,p,q):
    f=lambda t:math.log(t-p,a)+q
    def dr(ax):
        xs=np.linspace(.05,10,400); ax.plot(xs,[math.log(t,a) for t in xs],color="#bbbbbb",lw=1.4,ls="--")
        xs2=np.linspace(p+.05,10,400); ax.plot(xs2,[f(t) for t in xs2],color="#b81f36",lw=2)
        ax.plot([p,p],[-4,5],color="#1f6fb8",ls=":"); mark(ax,p+1,q,"(%d,%d)"%(p+1,q),.5,.5)
    fg=gplane("x242_7_%d_%d_%d"%(a,p+9,q+9),(-1,10),(-4,5),dr,size=(4.4,3.2),w=54)
    st=[("平行移動","<p>"+I("y=\\log_%d x"%a)+" を "+I("x")+" 方向に "+I("%d"%p)+"、"+I("y")+" 方向に "+I("%d"%q)+"。</p>"+"<p>"+I("x\\to x-%d,\\ y\\to y-%d"%(p,q))+" と置き換える。</p>"+D(r"y-%d=\log_{%d}(x-%d)"%(q,a,p))+D(r"y=\log_{%d}(x-%d)%+d"%(a,p,q))),
        ("漸近線","<p>漸近線は "+I("x=%d"%p)+"。定義域は "+I("x>%d"%p)+"。</p>"+fg),
        ("通る点","<p>"+I("(1,0)")+" は "+I("x")+" 方向に "+I(str(p))+"、"+I("y")+" 方向に "+I(str(q))+" 動く。</p>"+D(r"(1+%d,\ 0+%d)=(%d,\ %d)"%(p,q,p+1,q)))]
    return r"$y=\log_%d x$ のグラフを $x$ 軸方向に $%d$、$y$ 軸方向に $%d$ だけ平行移動したグラフの方程式、漸近線、定義域を求めよ。"%(a,p,q),st,r"y=\log_{%d}(x-%d)%+d,\ \ x=%d,\ \ x>%d"%(a,p,q,p,p)
o=[b7(*v) for v in [(2,1,2),(2,2,-1),(3,1,1),(2,-1,1) if False else (2,3,-2),(3,2,2)]]
build(Z,CH,"対数関数のグラフの平行移動・漸近線・定義域",o,"<p>$x\\to x-p,\\ y\\to y-q$。漸近線は $y$ 軸 $x=0$ が $x=p$ に。<b>真数 $>0$</b> から定義域も同じだけずれる。</p>","グラフをずらせば、漸近線も定義域も一緒にずれる。",7)
# 8 連立対数方程式
def b8(x0,y0):
    # log_2 x + log_2 y = s ; x - y = d
    s=int(math.log2(x0*y0)); d=x0-y0
    assert 2**s==x0*y0
    st=[("真数条件","<p>"+I("x>0,\\ y>0")+"。</p>"),
        ("積にまとめる","<p>"+D(r"\log_2x+\log_2y=\log_2xy=%d\ \Rightarrow\ xy=%d"%(s,x0*y0))),
        ("連立","<p>"+D(r"x-y=%d,\quad xy=%d\ \Rightarrow\ y(y+%d)=%d"%(d,x0*y0,d,x0*y0))+"<p>"+I("y=%d"%y0)+"、"+I("x=%d"%x0)+"（"+I("y>0")+"）。</p>")]
    return r"連立方程式 $\log_2x+\log_2y=%d,\ x-y=%d$ を解け。"%(s,d),st,r"(x,y)=(%d,%d)"%(x0,y0)
o=[b8(*v) for v in [(8,2),(16,4),(8,4) if False else (16,2),(32,2),(8,1)]]
build(Z,CH,"連立対数方程式",o,"<p>真数条件 → 対数の和を<b>積の対数</b>にまとめる → $xy=$ 定数 と $x-y=$ 定数 の連立。最後に真数条件を確認。</p>","対数を外して、普通の連立方程式に戻す。",8)
# 9 対数不等式
def b9(a,b):
    # log_(1/2)(x-a) > log_(1/2)... use log_2(x-a)+log_2(x-b) < c
    c=3; 
    # (x-a)(x-b)<2^c, x>max(a,b)
    xs=sp.symbols("x"); hi=sp.solve(xs*xs-(a+b)*xs+a*b-2**c,xs); hi=max(hi)
    hi_=float(hi)
    st=[("真数条件","<p>"+I("x-%d>0,\\ x-%d>0"%(a,b))+" より "+I("x>%d"%max(a,b))+"。</p>"),
        ("まとめて指数に","<p>"+D(r"\log_2(x-%d)(x-%d)<3\ \Rightarrow\ (x-%d)(x-%d)<8"%(a,b,a,b))),
        ("解く","<p>"+D(r"%s<0\ \Rightarrow\ %s<x<%s"%(L(sp.expand((xs-a)*(xs-b)-8)),L(min(sp.solve(xs*xs-(a+b)*xs+a*b-8,xs))),L(hi)))+"<p>真数条件と合わせて</p>"+D(r"%d<x<%s"%(max(a,b),L(hi))))]
    # check hi
    return r"不等式 $\log_2(x-%d)+\log_2(x-%d)<3$ を解け。"%(a,b),st,r"%d<x<%s"%(max(a,b),L(hi))
o=[b9(*v) for v in [(1,2),(0,1),(2,3),(-1,1),(1,4)]]
build(Z,CH,"対数不等式（真数条件と共通範囲）",o,"<p>① 真数条件 ② 底が $1$ より大きいので、不等号の向きはそのまま真数の大小に。③ ①と②の共通範囲。</p>","条件を2つ出して、最後に重なる部分を取る。",9)
# 10 log x + log y の最大
def b10(s):
    # x+y=s, x>0,y>0: max log_2 x + log_2 y = log_2 (s^2/4)
    mx=2*math.log2(s/2)
    st=[("積の対数","<p>"+D(r"\log_2x+\log_2y=\log_2xy")+"</p>"),
        ("積の最大","<p>"+D(r"x+y=%d\ \Rightarrow\ xy\leqq\left(\dfrac{x+y}{2}\right)^2=%s"%(s,L(R(s*s,4))))+"<p>等号は "+I("x=y=%s"%L(R(s,2)))+"。</p>"),
        ("最大値",D(r"\log_2%s=%s"%(L(R(s*s,4)),L(sp.simplify(sp.log(R(s*s,4),2))))))]
    return r"$x>0,\ y>0,\ x+y=%d$ のとき、$\log_2x+\log_2y$ の最大値を求めよ。"%s,st,L(sp.simplify(sp.log(R(s*s,4),2)))
o=[b10(s) for s in [8,16,4,32,12]]
build(Z,CH,"和が一定のときの log x + log y の最大",o,"<p>$\\log_2x+\\log_2y=\\log_2xy$。底が $1$ より大きいので<b>積 $xy$ が最大</b>のとき最大。和が一定なら $x=y$ のとき積が最大。</p>","対数は増加関数。大きな積が、大きな対数を連れてくる。",10)
XU=finishx(Z,CH)
