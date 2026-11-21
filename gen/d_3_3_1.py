# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
def chk(F,f): assert sp.simplify(sp.diff(F,x)-f)==0
# 1 置換 (x^2+a)^n x
def b1(a,n,c):
    u=x**2+a; f=c*x*u**n; F=R(c,2*(n+1))*u**(n+1); chk(F,f)
    st=[("置換を決める","<p>"+I(r"u=%s"%L(u))+" とおくと "+I(r"du=2x\,dx")+"、すなわち "+I(r"x\,dx=\dfrac12du")+"。</p>"),
        ("$u$ で積分",D(r"\int %s x(%s)^{%d}dx=%s\int u^{%d}\cdot\dfrac12du=%s\cdot\dfrac{u^{%d}}{%d}+C"%(L(c) if c!=1 else "",L(u),n,L(c) if c!=1 else "",n,L(R(c,2)),n+1,n+1))),
        ("$x$ に戻す",D(r"=%s(%s)^{%d}+C"%(L(R(c,2*(n+1))) if c!=2*(n+1) else "",L(u),n+1)))]
    return r"不定積分 $\displaystyle\int %sx(%s)^{%d}\,dx$ を求めよ。"%(L(c) if c!=1 else "",L(u),n),st,r"%s(%s)^{%d}+C"%(L(F/u**(n+1)),L(u),n+1)
V=[(1,3,2),(2,4,3),(3,2,6),(1,5,4),(4,3,5)]
o=[b1(*v) for v in V]
build(Z,CH,"置換積分（累乗の形）",o,r"<p>$u=g(x)$ とおき、$du=g'(x)dx$ を作る。<b>$x\,dx$ が $\dfrac12du$</b> のように、係数合わせを忘れない。最後は $x$ に戻す。</p>","中身の塊を1文字に置きかえて、見通しをよくする。",1)
# 2 f'/f
def b2(a,b,c):
    f=(a*x+b)/(x**2+c*x+1+0); 
    u=x**2+c*x+1
    # 分子が u' の定数倍
    k=R(a,2); num=sp.expand(k*sp.diff(u,x)); F=k*sp.log(u); f=num/u; chk(F,f)
    st=[("分子と分母の関係","<p>分母 "+I(r"g(x)=%s"%L(u))+" の導関数は "+I(r"g'(x)=%s"%L(sp.diff(u,x)))+"。分子はその "+I(L(k))+" 倍。</p>"),
        ("公式",D(r"\int\dfrac{g'(x)}{g(x)}dx=\log|g(x)|+C")),
        ("積分",D(r"\int\dfrac{%s}{%s}dx=%s\int\dfrac{%s}{%s}dx=%s\log(%s)+C"%(L(num),L(u),L(k),L(sp.diff(u,x)),L(u),L(k),L(u))))]
    return r"不定積分 $\displaystyle\int\dfrac{%s}{%s}\,dx$ を求めよ。"%(L(num),L(u)),st,r"%s\log(%s)+C"%(L(k),L(u))
V=[(2,0,1),(4,0,2),(6,0,3),(3,0,2),(8,0,1)]
V=[(2,0,2),(4,0,3),(6,0,4),(3,0,2),(8,0,6)]
o=[b2(*v) for v in V]
build(Z,CH,"分子が分母の導関数になる積分",o,r"<p>$\displaystyle\int\dfrac{g'}{g}dx=\log|g|+C$。分母の導関数を計算し、分子との<b>定数倍の関係</b>を見抜く。$x^2+cx+1>0$ なので絶対値は不要。</p>","分子が分母の導関数なら、対数に直行。",2)
# 3 部分積分 x e^{kx}
def b3(k,c):
    f=(x+c)*sp.exp(k*x); F=sp.exp(k*x)*(R(1,k)*(x+c)-R(1,k**2)); chk(F,f)
    st=[("部分積分の公式",D(r"\int f g'\,dx=fg-\int f'g\,dx")),
        ("$f,g'$ を決める","<p>"+I(r"f=%s"%L(x+c))+"、"+I(r"g'=e^{%sx}"%L(k))+"（"+I(r"g=%se^{%sx}"%(L(R(1,k)),L(k)))+"）。多項式の方を $f$ にして、微分で次数を下げる。</p>"),
        ("計算",D(r"\int(%s)e^{%sx}dx=(%s)\cdot%se^{%sx}-\int%se^{%sx}dx"%(L(x+c),L(k),L(x+c),L(R(1,k)),L(k),L(R(1,k)),L(k)))+D(r"=%s\,e^{%sx}+C"%(r"\left(%s\right)"%L(sp.expand(R(1,k)*(x+c)-R(1,k**2))),L(k))))]
    return r"不定積分 $\displaystyle\int(%s)e^{%sx}\,dx$ を求めよ。"%(L(x+c),L(k)),st,r"\left(%s\right)e^{%sx}+C"%(L(sp.expand(R(1,k)*(x+c)-R(1,k**2))),L(k))
V=[(2,1),(3,-2),(2,-3),(4,2),(3,5)]
o=[b3(*v) for v in V]
build(Z,CH,"部分積分（多項式×指数関数）",o,r"<p>$\int fg'dx=fg-\int f'g\,dx$。<b>微分して簡単になる方（多項式）を $f$</b>、積分しやすい方を $g'$ にする。</p>","「微分でやせる方」と「積分してもふとらない方」に役を分ける。",3)
# 4 x log x
def b4(n):
    f=x**n*sp.log(x); F=x**(n+1)/(n+1)*sp.log(x)-x**(n+1)/(n+1)**2; chk(F,f)
    st=[("役割分担","<p>"+I(r"f=\log x")+"（微分すると "+I(r"\dfrac1x")+"）、"+I(r"g'=x^{%d}"%n)+"（"+I(r"g=\dfrac{x^{%d}}{%d}"%(n+1,n+1))+"）。</p>"),
        ("部分積分",D(r"\int x^{%d}\log x\,dx=\dfrac{x^{%d}}{%d}\log x-\int\dfrac1x\cdot\dfrac{x^{%d}}{%d}dx"%(n,n+1,n+1,n+1,n+1))),
        ("残りを積分",D(r"=\dfrac{x^{%d}}{%d}\log x-\dfrac1{%d}\int x^{%d}dx=\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}+C"%(n+1,n+1,n+1,n,n+1,n+1,n+1,(n+1)**2)))]
    return r"不定積分 $\displaystyle\int x^{%d}\log x\,dx\ (x>0)$ を求めよ。"%n,st,r"\dfrac{x^{%d}}{%d}\log x-\dfrac{x^{%d}}{%d}+C"%(n+1,n+1,n+1,(n+1)**2)
V=[2,3,1,4,5]
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"部分積分（多項式×対数）",o,r"<p>$\log x$ は<b>微分する側（$f$）</b>に。$\int x^n\log x$ は $\log x$ を微分して $\dfrac1x$ にすることで、残りの積分が簡単になる。</p>","対数は積分しにくいので、微分する側に回す。",4)
# 5 三角関数
def b5(m):
    # ∫ sin^2(mx) dx , ∫ cos^3 x
    f=sp.sin(m*x)**2; F=x/2-sp.sin(2*m*x)/(4*m); chk(F,f)
    st=[("次数を下げる","<p>半角の公式 "+I(r"\sin^2\theta=\dfrac{1-\cos2\theta}{2}")+" を使う。</p>"+D(r"\sin^2%sx=\dfrac{1-\cos%sx}{2}"%(L(m),L(2*m)))),
        ("積分",D(r"\int\sin^2%sx\,dx=\dfrac12\int(1-\cos%sx)dx=\dfrac12\left(x-\dfrac{\sin%sx}{%s}\right)+C"%(L(m),L(2*m),L(2*m),L(2*m))))]
    return r"不定積分 $\displaystyle\int\sin^2%sx\,dx$ を求めよ。"%L(m),st,r"\dfrac{x}{2}-\dfrac{\sin%sx}{%s}+C"%(L(2*m),L(4*m))
V=[2,3,4,5,6]
o=[b5(v) for v in V]
build(Z,CH,"三角関数の積分（半角の公式）",o,r"<p>$\sin^2,\cos^2$ は<b>半角の公式</b>で $\cos2\theta$ の 1次式に直してから積分。$\cos k x$ の積分は $\dfrac1k\sin kx$。</p>","2乗は次数を下げてから積分。公式1つで見通しが開ける。",5)
UNIT=finish(Z,CH,2,0,"積分法","不定積分・置換積分・部分積分","置換積分、部分積分、三角関数の積分まで、不定積分の難問に挑みます。",subject="3")
