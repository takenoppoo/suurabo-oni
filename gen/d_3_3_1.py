# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
def chk(F,f): assert sp.simplify(sp.diff(F,x)-f)==0
def co(c): return "" if c==1 else ("-" if c==-1 else L(c))
def pw(base,n): return r"\left(%s\right)^{%d}"%(base,n)
# 1 置換 (x^2+a)^n x
def b1(a,n,c):
    u=x**2+a; f=c*x*u**n; k=R(c,2*(n+1)); F=k*u**(n+1); chk(F,f)
    st=[("置換を決める","<p>"+I(r"u=%s"%L(u))+" とおいて両辺を "+I("x")+" で微分する。</p>"+D(r"\dfrac{du}{dx}=2x\ \Rightarrow\ du=2x\,dx")+"<p>積分の中にある "+I(r"x\,dx")+" をそのまま使えるよう、両辺を2でわる。</p>"+D(r"x\,dx=\dfrac12\,du")),
        ("$u$ で書きかえる","<p>"+I("x^2+%d"%a if a>0 else "x^2%d"%a)+" を "+I("u")+"、"+I(r"x\,dx")+" を "+I(r"\dfrac12du")+" に置きかえる。</p>"+D(r"\int %s%s\,x\,dx=%s\int %s\cdot x\,dx"%(co(c),pw(L(u),n),co(c),pw(L(u),n)))+D(r"=%s\int u^{%d}\cdot\dfrac12\,du=%s\int u^{%d}\,du"%(co(c),n,L(R(c,2)) if c!=2 else "",n))),
        ("$u$ で積分","<p>"+I(r"\int u^{n}du=\dfrac{u^{n+1}}{n+1}")+" を使う。</p>"+D(r"%s\cdot\dfrac{u^{%d}}{%d}+C=%su^{%d}+C"%(L(R(c,2)) if c!=2 else "1",n+1,n+1,co(k),n+1))),
        ("$x$ に戻す","<p>"+I(r"u=%s"%L(u))+" を戻す。</p>"+D(r"=%s%s+C"%(co(k),pw(L(u),n+1)))),
        ("検算（微分して確かめる）",D(r"\left\{%s%s\right\}'=%s\cdot%d%s\cdot2x=%sx%s"%(co(k),pw(L(u),n+1),L(k),n+1,pw(L(u),n),co(c),pw(L(u),n))))]
    return r"不定積分 $\displaystyle\int %sx(%s)^{%d}\,dx$ を求めよ。"%(co(c),L(u),n),st,r"%s(%s)^{%d}+C"%(co(k),L(u),n+1)
V=[(1,3,2),(2,4,3),(3,2,6),(1,5,4),(4,3,5)]
o=[b1(*v) for v in V]
build(Z,CH,"置換積分（累乗の形）",o,r"<p>$u=g(x)$ とおき、$du=g'(x)dx$ を作る。<b>$x\,dx$ が $\dfrac12du$</b> のように、係数合わせを忘れない。最後は $x$ に戻す。</p>","中身の塊を1文字に置きかえて、見通しをよくする。",1)
# 2 f'/f
def b2(a,b,c):
    u=x**2+c*x+1; k=R(a,2); gp=sp.diff(u,x); num=sp.expand(k*gp); F=k*sp.log(u); f=num/u; chk(F,f)
    one=(k==1)
    st=[("分母を微分する","<p>"+I(r"g(x)=%s"%L(u))+" とおき、導関数を求める。</p>"+D(r"g'(x)=%s"%L(gp))),
        ("分子と見比べる","<p>分子 "+I(L(num))+" と "+I(r"g'(x)=%s"%L(gp))+" を比べる。</p>"+(D(r"%s=g'(x)"%L(num))+"<p>分子は "+I("g'(x)")+" そのもの。</p>" if one else D(r"%s=%s\left(%s\right)=%s\,g'(x)"%(L(num),L(k),L(gp),L(k)))+"<p>分子は "+I("g'(x)")+" の "+I(L(k))+" 倍。</p>"))]
    if not one: st.append(("定数を外に出す","<p>定数 "+I(L(k))+" は積分の外に出せる。</p>"+D(r"\int\dfrac{%s}{%s}dx=%s\int\dfrac{%s}{%s}dx"%(L(num),L(u),L(k),L(gp),L(u)))))
    st.append(("公式を使う","<p>"+I(r"\int\dfrac{g'(x)}{g(x)}dx=\log|g(x)|+C")+"（"+I("g(x)")+" は負になることもあるので絶対値をつける）。</p>"+D(r"=%s\log|%s|+C"%(co(k),L(u)))))
    return r"不定積分 $\displaystyle\int\dfrac{%s}{%s}\,dx$ を求めよ。"%(L(num),L(u)),st,r"%s\log|%s|+C"%(co(k),L(u))
V=[(2,0,2),(4,0,3),(6,0,4),(3,0,2),(8,0,6)]
o=[b2(*v) for v in V]
build(Z,CH,"分子が分母の導関数になる積分",o,r"<p>$\displaystyle\int\dfrac{g'}{g}dx=\log|g|+C$。分母の導関数を計算し、分子との<b>定数倍の関係</b>を見抜く。$g(x)$ が負になることもあるので、$\log|g(x)|$ と<b>絶対値</b>をつける。</p>","分子が分母の導関数なら、対数に直行。",2)
# 3 部分積分 x e^{kx}
def b3(k,c):
    f=(x+c)*sp.exp(k*x); G=sp.expand(R(1,k)*(x+c)-R(1,k**2)); F=sp.exp(k*x)*G; chk(F,f)
    ik=R(1,k)
    st=[("部分積分の公式",D(r"\int f\,g'\,dx=f\,g-\int f'\,g\,dx")),
        ("$f,g'$ を決める","<p>多項式の方を "+I("f")+"（微分すると次数が下がる）、"+I(r"e^{%sx}"%L(k))+" の方を "+I("g'")+" にする。</p>"+D(r"f=%s,\qquad f'=1"%L(x+c))+D(r"g'=e^{%sx}\ \Rightarrow\ g=\int e^{%sx}dx=%se^{%sx}"%(L(k),L(k),L(ik),L(k)))),
        ("公式に代入","<p>"+D(r"\int(%s)e^{%sx}dx=(%s)\cdot%se^{%sx}-\int1\cdot%se^{%sx}dx"%(L(x+c),L(k),L(x+c),L(ik),L(k),L(ik),L(k)))),
        ("残りの積分を計算","<p>"+I(r"\int e^{%sx}dx=%se^{%sx}"%(L(k),L(ik),L(k)))+" なので、</p>"+D(r"\int%se^{%sx}dx=%s\cdot%se^{%sx}=%se^{%sx}"%(L(ik),L(k),L(ik),L(ik),L(k),L(R(1,k**2)),L(k)))+D(r"\int(%s)e^{%sx}dx=%s(%s)e^{%sx}-%se^{%sx}+C"%(L(x+c),L(k),L(ik),L(x+c),L(k),L(R(1,k**2)),L(k)))),
        ("$e^{%sx}$ でくくる"%L(k),"<p>"+D(r"=\left\{%s(%s)-%s\right\}e^{%sx}+C"%(L(ik),L(x+c),L(R(1,k**2)),L(k)))+D(r"=\left(%s\right)e^{%sx}+C"%(L(G),L(k))))]
    return r"不定積分 $\displaystyle\int(%s)e^{%sx}\,dx$ を求めよ。"%(L(x+c),L(k)),st,r"\left(%s\right)e^{%sx}+C"%(L(G),L(k))
V=[(2,1),(3,-2),(2,-3),(4,2),(3,5)]
o=[b3(*v) for v in V]
build(Z,CH,"部分積分（多項式×指数関数）",o,r"<p>$\int fg'dx=fg-\int f'g\,dx$。<b>微分して簡単になる方（多項式）を $f$</b>、積分しやすい方を $g'$ にする。</p>","「微分でやせる方」と「積分してもふとらない方」に役を分ける。",3)
# 4 x log x
def b4(n):
    f=x**n*sp.log(x); F=x**(n+1)/(n+1)*sp.log(x)-x**(n+1)/(n+1)**2; chk(F,f)
    st=[("部分積分の公式",D(r"\int f\,g'\,dx=f\,g-\int f'\,g\,dx")),
        ("役割分担","<p>"+I(r"\log x")+" は積分しにくいので "+I("f")+"（微分する側）にする。</p>"+D(r"f=\log x,\qquad f'=\dfrac1x")+D(r"g'=x^{%d}\ \Rightarrow\ g=\int x^{%d}dx=\dfrac{x^{%d}}{%d}"%(n,n,n+1,n+1))),
        ("公式に代入",D(r"\int x^{%d}\log x\,dx=\log x\cdot\dfrac{x^{%d}}{%d}-\int\dfrac1x\cdot\dfrac{x^{%d}}{%d}dx"%(n,n+1,n+1,n+1,n+1))),
        ("残りの積分を整える","<p>"+I(r"\dfrac1x\cdot x^{%d}=x^{%d}"%(n+1,n))+"、"+I(r"\dfrac1{%d}"%(n+1))+" は外に出す。</p>"+D(r"\int\dfrac1x\cdot\dfrac{x^{%d}}{%d}dx=\dfrac1{%d}\int x^{%d}dx=\dfrac1{%d}\cdot\dfrac{x^{%d}}{%d}=\dfrac{x^{%d}}{%d}"%(n+1,n+1,n+1,n,n+1,n+1,n+1,n+1,(n+1)**2))),
        ("答え",D(r"\int x^{%d}\log x\,dx=\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}+C"%(n,n+1,n+1,n+1,(n+1)**2)))]
    return r"不定積分 $\displaystyle\int x^{%d}\log x\,dx\ (x>0)$ を求めよ。"%n,st,r"\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}+C"%(n+1,n+1,n+1,(n+1)**2)
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"部分積分（多項式×対数）",o,r"<p>$\log x$ は<b>微分する側（$f$）</b>に。$\int x^n\log x$ は $\log x$ を微分して $\dfrac1x$ にすることで、残りの積分が簡単になる。</p>","対数は積分しにくいので、微分する側に回す。",4)
# 5 三角関数
def b5(m):
    f=sp.sin(m*x)**2; F=x/2-sp.sin(2*m*x)/(4*m); chk(F,f)
    st=[("次数を下げる","<p>半角の公式 "+I(r"\sin^2\theta=\dfrac{1-\cos2\theta}{2}")+" に "+I(r"\theta=%sx"%L(m))+" を代入する。</p>"+D(r"\sin^2%sx=\dfrac{1-\cos(2\cdot%sx)}{2}=\dfrac{1-\cos%sx}{2}"%(L(m),L(m),L(2*m)))),
        ("積分を2つに分ける",D(r"\int\sin^2%sx\,dx=\int\dfrac{1-\cos%sx}{2}dx=\dfrac12\int dx-\dfrac12\int\cos%sx\,dx"%(L(m),L(2*m),L(2*m)))),
        ("それぞれ積分","<p>"+I(r"\int dx=x")+"、"+I(r"\int\cos kx\,dx=\dfrac{\sin kx}{k}")+" を使う（"+I("k=%s"%L(2*m))+"）。</p>"+D(r"\dfrac12\cdot x-\dfrac12\cdot\dfrac{\sin%sx}{%s}"%(L(2*m),L(2*m)))),
        ("答え",D(r"=\dfrac{x}{2}-\dfrac{\sin%sx}{%s}+C"%(L(2*m),L(4*m))))]
    return r"不定積分 $\displaystyle\int\sin^2%sx\,dx$ を求めよ。"%L(m),st,r"\dfrac{x}{2}-\dfrac{\sin%sx}{%s}+C"%(L(2*m),L(4*m))
V=[2,3,4,5,6]
o=[b5(v) for v in V]
build(Z,CH,"三角関数の積分（半角の公式）",o,r"<p>$\sin^2,\cos^2$ は<b>半角の公式</b>で $\cos2\theta$ の 1次式に直してから積分。$\cos k x$ の積分は $\dfrac1k\sin kx$。</p>","2乗は次数を下げてから積分。公式1つで見通しが開ける。",5)
UNIT=finish(Z,CH,2,0,"積分法","不定積分・置換積分・部分積分","置換積分、部分積分、三角関数の積分まで、不定積分の難問に挑みます。",subject="3")
