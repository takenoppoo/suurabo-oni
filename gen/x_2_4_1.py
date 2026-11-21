# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x")
# 6 a^{1/2}+a^{-1/2}=s
def b6(s):
    p=s*s-2; q=s**3-3*s
    st=[("2乗","<p>"+D(r"\left(a^{\frac12}+a^{-\frac12}\right)^2=a+2+a^{-1}=%d\ \Rightarrow\ a+a^{-1}=%d"%(s*s,p))),
        ("3乗","<p>"+D(r"a^{\frac32}+a^{-\frac32}=\left(a^{\frac12}+a^{-\frac12}\right)^3-3\left(a^{\frac12}+a^{-\frac12}\right)=%d-%d=%d"%(s**3,3*s,q))),
        ("2乗の和","<p>"+D(r"a^2+a^{-2}=(a+a^{-1})^2-2=%d-2=%d"%(p*p,p*p-2)))]
    return r"$a>0$ で $a^{\frac12}+a^{-\frac12}=%d$ のとき、$a+a^{-1},\ a^{\frac32}+a^{-\frac32},\ a^2+a^{-2}$ の値を求めよ。"%s,st,r"%d,\ %d,\ %d"%(p,q,p*p-2)
o=[b6(s) for s in [3,4,5,6,7]]
build(Z,CH,"a^{1/2}+a^{-1/2} から冪の和",o,"<p>$(u+v)^2,\\ (u+v)^3$ の展開で $uv=1$ を使う。$u=a^{1/2},\\ v=a^{-1/2}$ のとき $uv=1$。</p>","積が1だから、和さえ分かれば他の冪の和も全部出る。",6)
# 7 連立
def b7(p,q):
    # 2^x+2^y=p , 2^(x+y)=q ; solve
    u,v=sp.symbols("u v"); sol=sp.solve([u+v-p,u*v-q],[u,v],dict=True)
    sols=[(s_[u],s_[v]) for s_ in sol]; pos=[(a,b) for a,b in sols if a>0 and b>0]
    ans=sorted({(int(math.log2(float(a))),int(math.log2(float(b)))) for a,b in pos})
    st=[("置き換え","<p>"+I("u=2^x,\\ v=2^y\\ (u>0,v>0)")+"。</p>"+D(r"u+v=%d,\qquad uv=%d"%(p,q))),
        ("2次方程式","<p>"+I("u,v")+" は "+I("t^2-%dt+%d=0"%(p,q))+" の解。</p>"+D(r"(t-%d)(t-%d)=0"%tuple(sorted([int(a) for a,b in pos[0:1]]+[int(b) for a,b in pos[0:1]])))),
        ("$x,y$ に戻す","<p>"+D(r"(x,y)=%s"%(r",\ ".join("(%d,%d)"%a for a in ans))))]
    return r"連立方程式 $2^x+2^y=%d,\ 2^{x+y}=%d$ を解け。"%(p,q),st,r"(x,y)=%s"%(r",\ ".join("(%d,%d)"%a for a in ans))
o=[b7(*v) for v in [(12,32),(10,16),(18,32),(9,8),(20,64)]]
build(Z,CH,"指数の連立方程式",o,"<p>$u=2^x,\\ v=2^y$ とおくと、和と積が分かる。$u,v$ は2次方程式 $t^2-(\\text{和})t+(\\text{積})=0$ の解。<b>$u,v>0$</b> を確認。</p>","指数を文字に置き換えて、和と積の問題にする。",7)
# 8 グラフの移動
def b8(a,p,q):
    # y=a^x moved by (p,q), through point? find equation and asymptote
    f=lambda t:float(a)**(t-p)+q
    def dr(ax):
        xs=np.linspace(-3,5,300); ax.plot(xs,float(a)**xs,color="#bbbbbb",lw=1.4,ls="--"); ax.plot(xs,[f(t) for t in xs],color="#b81f36",lw=2)
        ax.plot([-3,5],[q,q],color="#1f6fb8",ls=":"); mark(ax,p,1+q,"(%d,%d)"%(p,1+q),.5,.5)
    fg=gplane("x241_8_%d_%d_%d"%(a,p+9,q+9),(-3,5),(min(-2,q-1)-.5,max(6,q+5)),dr,size=(4.4,3.2),w=54)
    st=[("平行移動","<p>"+I("y=%d^x"%a)+" を "+I("x")+" 方向に "+I("%d"%p)+"、"+I("y")+" 方向に "+I("%d"%q)+" 平行移動。</p>"+D(r"y=%d^{x-%d}%+d"%(a,p,q))),
        ("漸近線","<p>漸近線は直線 "+I("y=%d"%q)+"。</p>"+fg),
        ("通る点","<p>"+I("(0,1)")+" は "+I("(%d,%d)"%(p,1+q))+" に移る。</p>")]
    return r"$y=%d^x$ のグラフを $x$ 軸方向に $%d$、$y$ 軸方向に $%d$ だけ平行移動したグラフの方程式、漸近線の方程式、および $(0,1)$ が移る点の座標を求めよ。"%(a,p,q),st,r"y=%d^{x-%d}%+d,\ \ y=%d,\ \ (%d,%d)"%(a,p,q,q,p,1+q)
o=[b8(*v) for v in [(2,1,2),(3,2,-1),(2,-1,1),(2,2,-2),(3,-1,3)]]
build(Z,CH,"指数関数のグラフの平行移動と漸近線",o,"<p>$x\\to x-p,\\ y\\to y-q$ と置き換える。<b>漸近線も同じだけ移る</b>（$y=0$ が $y=q$ に）。基準の点 $(0,1)$ の行き先に注意。</p>","グラフごと平行にずらせば、漸近線も通る点も一緒に動く。",8)
# 9 大小比較
def b9(a,b,c):
    # compare 2^(1/2)... choose numbers like 2^(3/4), 4^(1/3)... use bases
    vals=[a,b,c]
    # compare by raising to common power: values of form n^(p/q)
    ev=[float(base)**float(e) for base,e in vals]
    order=sorted(range(3),key=lambda i:ev[i])
    lcm=12
    st=[("指数をそろえる","<p>"+"、".join(I(r"%d^{%s}"%(vals[i][0],L(vals[i][1]))) for i in range(3))+"。冪を"+I("12")+" 乗して比べる。</p>"),
        ("12乗した値","<p>"+D(r"%s"%(r",\quad ".join(r"(%d^{%s})^{12}=%d"%(vals[i][0],L(vals[i][1]),round(ev[i]**12)) for i in range(3))))),
        ("大小","<p>"+D(r"%s"%(r"<".join(r"%d^{%s}"%(vals[i][0],L(vals[i][1])) for i in order))))]
    return r"$%d^{%s},\ %d^{%s},\ %d^{%s}$ を小さい順に並べよ。"%(a[0],L(a[1]),b[0],L(b[1]),c[0],L(c[1])),st,r"%s"%(r"<".join(r"%d^{%s}"%(vals[i][0],L(vals[i][1])) for i in order))
o=[b9(*v) for v in [((2,R(1,2)),(3,R(1,3)),(5,R(1,4))) if False else ((2,R(1,2)),(3,R(1,3)),(6,R(1,6))) ,((2,R(3,4)),(3,R(2,3)),(4,R(1,2))),((2,R(5,6)),(3,R(1,2)),(5,R(1,3))),((2,R(1,3)),(3,R(1,4)),(5,R(1,6))),((2,R(3,2)),(3,R(5,6)),(5,R(2,3)))]]
build(Z,CH,"指数の大小比較（12乗してそろえる）",o,"<p>指数の分母の<b>最小公倍数乗</b>して整数にそろえて比べる。または底をそろえる。</p>","分数の指数は、同じ冪に乗せて整数の勝負にする。",9)
# 10 4^x - k*2^x + m = 0 の解の個数
def b10(k,m):
    t=sp.symbols("t"); P=t*t-k*t+m; D_=k*k-4*m
    rts=sp.solve(P,t); pos=[r for r in rts if r.is_real and r>0]
    n=len(set(pos))
    def dr(ax):
        xs=np.linspace(0,k+1,100); ax.plot(xs,xs**2-k*xs+m,color="#b81f36",lw=2); ax.plot([0,k+1],[0,0],color="#333")
    fg=gplane("x241_10_%d_%d"%(k,m+9),(-.5,k+1),(-3,max(5,m+2)),dr,size=(4.2,3),w=50)
    st=[("置き換え","<p>"+I("t=2^x>0")+"。</p>"+D(r"t^2-%dt+%d=0"%(k,m))),
        ("正の解の個数","<p>"+I("D=%d^2-4\\cdot%d=%d"%(k,m,D_))+"、解の和 "+I(str(k))+"、積 "+I(str(m))+"（"+("ともに正" if (k>0 and m>0) else "")+"）。</p>"+fg),
        ("個数","<p>"+I("t")+" の正の解 "+I(str(n))+" 個。"+I("t")+" 1つにつき "+I("x")+" は1つ。</p>")]
    return r"方程式 $4^x-%d\cdot2^x+%d=0$ の実数解の個数を求めよ。"%(k,m),st,str(n)
o=[b10(*v) for v in [(5,4),(4,4),(3,5),(6,5),(2,-3)]]
build(Z,CH,"4^x−k·2^x+m=0 の解の個数",o,"<p>$t=2^x>0$ とおき、$t$ の2次方程式の<b>正の解の個数</b>を調べる（判別式・和・積）。$t$ と $x$ は1対1。</p>","文字を置き換えたら、範囲 $t>0$ を忘れない。",10)
XU=finishx(Z,CH)
