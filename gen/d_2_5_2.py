# -*- coding: utf-8 -*-
# 積分法（定積分・面積）（数学II 微分・積分）
from bh import *
from d_2_5_1 import gplane,curve,mark,poly
Z=U_(); CH=[]
_c=[0]
def shade(ax,f,g,lo,hi,col="#f4b6c0"):
    xs_=np.linspace(float(lo),float(hi),400); one=np.ones_like(xs_)
    fl=sp.lambdify(x,f,"numpy"); gl=sp.lambdify(x,g,"numpy"); ax.fill_between(xs_,fl(xs_)*one,gl(xs_)*one,color=col,alpha=.8,zorder=1)
def rngs(fs,lo,hi):
    ys_=[float(f.subs(x,v)) for f in fs for v in np.linspace(float(lo),float(hi),200)]+[0.0]
    a,b=min(ys_),max(ys_); sp_=b-a; ys=1 if sp_<=9 else (2 if sp_<=20 else (5 if sp_<=50 else 10))
    return (float(np.floor(a/ys)*ys-ys),float(np.ceil(b/ys)*ys+ys)),ys
def F_(f): return sp.integrate(f,x)
def defint(f,lo,hi): return sp.integrate(f,(x,lo,hi))
def Ftex(f): return L(F_(f))
def evalF(f,lo,hi):
    F=F_(f); return D(r"F(%s)=%s,\quad F(%s)=%s"%(L(hi),L(F.subs(x,hi)),L(lo),L(F.subs(x,lo))))
# ===== 例題1 定積分の計算 =====
def b1(co,lo,hi):
    f=poly(co); F=F_(f); v=defint(f,lo,hi); assert sp.simplify(F.subs(x,hi)-F.subs(x,lo)-v)==0
    terms=sp.Add.make_args(sp.expand(f))
    st=[("各項を積分する","<p>"+I(r"\int x^n\,dx=\dfrac{x^{n+1}}{n+1}+C")+"。</p>"+D(r"\int\left(%s\right)dx=%s"%(L(f),r"+".join(L(sp.integrate(t_,x)) for t_ in terms).replace("+-","-")+"+C"))),
        ("不定積分","<p>積分定数を $C$ として</p>"+D(r"\int\left(%s\right)dx=%s+C"%(L(f),L(F)))),
        ("定積分：両端の値を代入","<p>定積分では $C$ は不要。</p>"+D(r"\int_{%s}^{%s}\left(%s\right)dx=\Big[%s\Big]_{%s}^{%s}"%(L(lo),L(hi),L(f),L(F),L(lo),L(hi)))+evalF(f,lo,hi)),
        ("値を求める",D(r"F(%s)-F(%s)=%s-\left(%s\right)=%s"%(L(hi),L(lo),L(F.subs(x,hi)),L(F.subs(x,lo)),L(v))))]
    return r"(1) 不定積分 $\displaystyle\int\left(%s\right)dx$ を求めよ。(2) 定積分 $\displaystyle\int_{%s}^{%s}\left(%s\right)dx$ の値を求めよ。"%(L(f),L(lo),L(hi),L(f)),st,r"\text{(1) }%s+C\quad\text{(2) }%s"%(L(F),L(v))
V=[([3,-4,5],-1,2),([6,-4,1],1,3),([4,3,-2],0,2),([4,-3,2,1],-1,2),([6,2,-3],-2,1)]
o=[b1(*v) for v in V]
build(Z,CH,"不定積分と定積分の計算",o,
 r"<p>$\displaystyle\int x^n\,dx=\dfrac{x^{n+1}}{n+1}+C$。定積分は $F(x)$ を1つ求め、<b>$F(b)-F(a)$</b>。$\Big[F(x)\Big]_a^b$ と書く。</p>",
 "積分は微分の逆。$F'(x)=f(x)$ となる $F$ を探し、ゴールの値からスタートの値を引く。",1)
# ===== 例題2 絶対値の定積分 =====
def b2(al,be,lo,hi):
    f=sp.expand((x-al)*(x-be)); zs=sorted([z for z in (al,be) if lo<z<hi]); pts=[lo]+zs+[hi]
    segs=[]; tot=0
    for i in range(len(pts)-1):
        s=1 if f.subs(x,sp.Rational(pts[i]+pts[i+1],2))>0 else -1; val=s*defint(f,pts[i],pts[i+1]); segs.append((pts[i],pts[i+1],s,val)); tot+=val
    for xx in np.linspace(lo,hi,5):
        pass
    num=sp.integrate(sp.Abs(f),(x,lo,hi)) if False else None
    _fl=sp.lambdify(x,f,'numpy'); _xs=np.linspace(lo,hi,200001); assert abs(float(tot)-float(np.trapezoid(np.abs(_fl(_xs)),_xs)))<1e-3
    _c[0]+=1; nm="i252_a%d"%_c[0]; yr,ys=rngs([f],lo,hi)
    def dr(ax): shade(ax,f,sp.Integer(0),lo,hi); curve(ax,f,(lo-.6,hi+.6)); [mark(ax,z,0) for z in zs]
    fig=gplane(nm,(lo-1,hi+1),yr,dr,ys=ys)
    st=[("絶対値の中の符号を調べる","<p>"+I(r"%s=%s"%(L(f),L(sp.factor(f))))+"。"+"$x=%s$ が境目。</p>"%(r",\ ".join(L(z) for z in zs))+"<p>"+"、".join("$%s\\leqq x\\leqq %s$ で $%s$"%(L(a_),L(b_),("f(x)\\geqq0" if s>0 else "f(x)\\leqq0")) for a_,b_,s,v in segs)+"。</p>"),
        ("絶対値をはずして区間を分ける",D(r"\int_{%s}^{%s}\left|%s\right|dx=%s"%(L(lo),L(hi),L(f),r"+".join((r"\int_{%s}^{%s}"%(L(a_),L(b_)))+(r"\left(%s\right)dx"%L(f) if s>0 else r"\left\{-\left(%s\right)\right\}dx"%L(f)) for a_,b_,s,v in segs)))),
        ("不定積分を求める",D(r"\int\left(%s\right)dx=%s"%(L(f),L(F_(f))))),
        ("各区間の値",D(r"\\ ".join(r"\int_{%s}^{%s}=%s"%(L(a_),L(b_),L(v)) for a_,b_,s,v in segs) if False else r",\quad ".join(r"%s"%L(v) for a_,b_,s,v in segs))+"<p>（左の区間から順に）</p>"),
        ("合計",D(r"%s=%s"%(r"+".join(L(v) for a_,b_,s,v in segs),L(tot)))+fig)]
    return r"定積分 $\displaystyle\int_{%s}^{%s}\left|%s\right|dx$ の値を求めよ。"%(L(lo),L(hi),L(f)),st,L(tot)
V=[(0,2,0,3),(1,3,0,4),(-1,2,-2,3),(0,3,-1,4),(-2,1,-3,2)]
o=[b2(*v) for v in V]
build(Z,CH,"絶対値を含む定積分",o,
 r"<p>$|f(x)|$ は、$f(x)\geqq0$ なら $f(x)$、$f(x)\leqq0$ なら $-f(x)$。<b>$f(x)=0$ となる $x$ で区間を分け</b>、各区間で絶対値をはずして積分し、足す。グラフをかくと符号が一目で分かる。</p>",
 "谷（負の部分）は折り返して正にしてから足す。境目はグラフがx軸と交わる点。",2)
# ===== 例題3 放物線とx軸で囲む面積 =====
def b3(co):
    f=poly(co); rs=sorted(sp.solve(f,x)); al,be=rs; assert al.is_integer and be.is_integer
    up=f.subs(x,(al+be)/2)>0; g=f if up else -f; S=defint(g,al,be); assert S>0
    assert sp.simplify(S-sp.Abs(co[0])*(be-al)**3/6)==0
    _c[0]+=1; nm="i252_b%d"%_c[0]; yr,ys=rngs([f],al,be)
    def dr(ax): shade(ax,f,sp.Integer(0),al,be); curve(ax,f,(al-1,be+1)); [mark(ax,z,0) for z in rs]
    fig=gplane(nm,(float(al)-1.2,float(be)+1.2),yr,dr,ys=ys)
    st=[("$x$ 軸との交点を求める",D(L(f)+r"=0\ \Rightarrow\ %s=0\ \Rightarrow\ x=%s,\ %s"%(L(sp.factor(f)),L(al),L(be)))),
        ("上下関係を調べる","<p>$%s\\leqq x\\leqq %s$ では曲線は $x$ 軸の"%(L(al),L(be))+("上側" if up else "下側")+"。例：$x=%s$ で "%L((al+be)/2)+I(r"y=%s"%L(f.subs(x,(al+be)/2)))+"。</p>"),
        ("面積を定積分で表す","<p>"+("面積 = （上）−（下）= $f(x)-0$。" if up else "面積 = （上）−（下）= $0-f(x)$。")+"</p>"+D(r"S=\int_{%s}^{%s}\left(%s\right)dx"%(L(al),L(be),L(g)))),
        ("計算する",D(r"S=\Big[%s\Big]_{%s}^{%s}=%s-\left(%s\right)=%s"%(L(F_(g)),L(al),L(be),L(F_(g).subs(x,be)),L(F_(g).subs(x,al)),L(S)))+fig)]
    return r"放物線 $y=%s$ と $x$ 軸で囲まれた部分の面積 $S$ を求めよ。"%L(f),st,r"S=%s"%L(S)
V=[[-1,4,-3],[1,-2,-3],[-1,2,3],[-2,8,0],[1,-6,5]]
o=[b3(v) for v in V]
build(Z,CH,"放物線とx軸で囲まれた面積",o,
 r"<p>①$x$ 軸との交点 $\alpha,\beta$ を求める ②区間で曲線が $x$ 軸の上か下かを調べる ③$S=\displaystyle\int_\alpha^\beta\{(\text{上})-(\text{下})\}dx$ ④計算。<b>面積は必ず正</b>。下側にあるときは符号を逆にする。</p>",
 "面積は「上の線 − 下の線」を足し合わせたもの。下側にあるときは引き算の順を入れ替えるだけ。",3)
# ===== 例題4 放物線と直線 =====
def b4(cf_,cg):
    f=poly(cf_); g=poly(cg); h=sp.expand(g-f); rs=sorted(sp.solve(h,x)); al,be=rs; assert al.is_integer and be.is_integer
    gu=g.subs(x,(al+be)/2)>f.subs(x,(al+be)/2); U,Lw=(g,f) if gu else (f,g); I_=sp.expand(U-Lw); S=defint(I_,al,be); assert S>0
    _c[0]+=1; nm="i252_c%d"%_c[0]; yr,ys=rngs([f,g],al,be)
    def dr(ax):
        shade(ax,f,g,al,be); curve(ax,f,(al-1,be+1)); curve(ax,g,(al-1,be+1),"#1f6fb8"); [mark(ax,z,f.subs(x,z)) for z in rs]
    fig=gplane(nm,(float(al)-1.2,float(be)+1.2),yr,dr,ys=ys)
    st=[("交点の $x$ 座標を求める","<p>"+I(r"%s=%s"%(L(f),L(g)))+" を解く。</p>"+D(L(sp.expand(f-g))+r"=0\ \Rightarrow\ %s=0\ \Rightarrow\ x=%s,\ %s"%(L(sp.factor(f-g)),L(al),L(be)))),
        ("上下関係を調べる","<p>"+I("x=%s"%L((al+be)/2))+" で "+I(r"f=%s,\ g=%s"%(L(f.subs(x,(al+be)/2)),L(g.subs(x,(al+be)/2))))+"。区間で「"+("直線 $y=g(x)$ が上、放物線 $y=f(x)$ が下" if gu else "放物線 $y=f(x)$ が上、直線 $y=g(x)$ が下")+"」。</p>"),
        ("面積を定積分で表す",D(r"S=\int_{%s}^{%s}\left\{\left(%s\right)-\left(%s\right)\right\}dx=\int_{%s}^{%s}\left(%s\right)dx"%(L(al),L(be),L(U),L(Lw),L(al),L(be),L(I_)))),
        ("計算する",D(r"S=\Big[%s\Big]_{%s}^{%s}=%s-\left(%s\right)=%s"%(L(F_(I_)),L(al),L(be),L(F_(I_).subs(x,be)),L(F_(I_).subs(x,al)),L(S)))+fig)]
    return r"放物線 $y=%s$ と直線 $y=%s$ で囲まれた部分の面積 $S$ を求めよ。"%(L(f),L(g)),st,r"S=%s"%L(S)
V=[([1,0,0],[1,2]),([-1,3,0],[1,0]),([1,-4,3],[-1,3]),([2,0,0],[2,4]),([1,-1,0],[1,3])]
o=[b4(*v) for v in V]
build(Z,CH,"放物線と直線で囲まれた面積",o,
 r"<p>①2つの式を連立して<b>交点</b>の $x$ 座標 $\alpha,\beta$ を求める ②区間内の1点で<b>どちらが上か</b>調べる ③$S=\displaystyle\int_\alpha^\beta\{(\text{上})-(\text{下})\}dx$ ④計算。</p>",
 "2本の線にはさまれた帯の面積＝ふくらみの合計。上から下を引いて足し合わせる。",4)
# ===== 例題5 関数の決定 =====
def b5(co,a_,b_):
    p=poly(co); k=sp.Symbol('k'); t=sp.Symbol('t'); ks=sp.solve(sp.Eq(k,defint(p,a_,b_)+k*(b_-a_)),k)[0]; f=sp.expand(p+ks)
    assert sp.simplify(defint(f,a_,b_)-ks)==0
    I0=defint(p,a_,b_)
    st=[("定積分を定数 $k$ とおく","<p>"+I(r"\int_{%s}^{%s}f(t)\,dt=k"%(L(a_),L(b_)))+"（$k$ は定数）とおくと</p>"+D(r"f(x)=%s+k"%L(p))),
        ("$k$ についての方程式を作る","<p>"+I(r"f(t)=%s+k"%L(p.subs(x,t)))+" を、$t$ で "+I(r"%s"%L(a_))+" から "+I(r"%s"%L(b_))+" まで積分する。</p>"+D(r"k=\int_{%s}^{%s}\left(%s+k\right)dt=\Big[%s+kt\Big]_{%s}^{%s}"%(L(a_),L(b_),L(p.subs(x,t)),L(F_(p).subs(x,t)),L(a_),L(b_)))+D(r"k=%s%s"%(L(I0),("" if (b_-a_)==0 else ("+%sk"%L(b_-a_) if (b_-a_)>0 else "%sk"%L(b_-a_)))))),
        ("$k$ を求める",D(r"k(1-%s)=%s\ \Rightarrow\ k=%s"%(L(b_-a_),L(I0),L(ks)))),
        ("答え",D(r"f(x)=%s%s=%s"%(L(p),("+" if ks>0 else "")+L(ks),L(f))))]
    return r"関数 $f(x)$ が $f(x)=%s+\displaystyle\int_{%s}^{%s}f(t)\,dt$ を満たすとき、$f(x)$ を求めよ。"%(L(p),L(a_),L(b_)),st,r"f(x)=%s"%L(f)
V=[([3,2,0],0,2),([6,-4,0],0,3),([3,-2,0],-1,1),([3,-4,0],1,3),([6,1,0],0,2)]
o=[b5(*v) for v in V]
build(Z,CH,"積分を含む関数の決定",o,
 r"<p>$\displaystyle\int_a^b f(t)\,dt$ は<b>定数</b>。$=k$ とおくと $f(x)=(\text{既知の式})+k$。これを $k=\displaystyle\int_a^b f(t)\,dt$ に代入して $k$ の方程式にする。</p>",
 "積分の結果はただの数。まず「その数」に名前（$k$）をつけ、式の中に戻して解く。",5)
UNIT=finish(Z,CH,4,1,"微分・積分","積分法（定積分・面積）","定積分の計算、絶対値つきの積分、放物線・直線で囲まれた面積、積分を含む関数決定まで、積分法の総合力を問う難問に挑みます。")
