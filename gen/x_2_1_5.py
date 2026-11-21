# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x"); i_=sp.I
def b6(a,b,c):
    P=x**3+a*x**2+b*x+c; rts=sp.Poly(P,x).nroots(); s=-a; t=b; u=-c
    v=s*s-2*t
    st=[("解と係数の関係","<p>"+D(r"\alpha+\beta+\gamma=%d,\quad \alpha\beta+\beta\gamma+\gamma\alpha=%d,\quad \alpha\beta\gamma=%d"%(s,t,u))),
        ("変形","<p>"+D(r"\alpha^2+\beta^2+\gamma^2=(\alpha+\beta+\gamma)^2-2(\alpha\beta+\beta\gamma+\gamma\alpha)")),
        ("値",D(r"%d^2-2\cdot%d=%d"%(s,t,v)))]
    num=sum(complex(r)**2 for r in rts); assert abs(num-v)<1e-6
    return r"3次方程式 $%s=0$ の3つの解を $\alpha,\beta,\gamma$ とするとき、$\alpha^2+\beta^2+\gamma^2$ の値を求めよ。"%L(P),st,str(v)
o=[b6(*v) for v in [(-2,3,5),(1,-4,2),(-3,1,-6),(2,2,-1),(-1,-5,3)]]
build(Z,CH,"3次方程式の解の2乗の和",o,"<p>解と係数の関係（和・2つずつの積の和・積）を書き、$\\alpha^2+\\beta^2+\\gamma^2=(\\text{和})^2-2(\\text{2つずつの積の和})$ に代入。</p>","解を求めず、3つの基本量だけで答えを出す。",6)
def b7(n):
    w=sp.Rational(-1,2)+sp.sqrt(3)*i_/2
    v=sp.simplify(sp.expand(w**n+w**(2*n)))
    st=[("基本性質","<p>"+I(r"\omega^3=1,\quad \omega^2+\omega+1=0")+"（"+I(r"x^3=1")+" の虚数解）。</p>"),
        ("指数を3で割る","<p>"+I(r"\omega^{%d}=\omega^{%d}"%(n,n%3))+"、"+I(r"\omega^{%d}=\omega^{%d}"%(2*n,(2*n)%3))+"。</p>"),
        ("値","<p>"+D(r"\omega^{%d}+\omega^{%d}=%s"%(n,2*n,L(v))))]
    return r"$x^3=1$ の虚数解の1つを $\omega$ とする。$\omega^{%d}+\omega^{%d}$ の値を求めよ。"%(n,2*n),st,L(v)
o=[b7(n) for n in [7,10,12,20,25]]
build(Z,CH,"1の3乗根 ω の累乗",o,"<p>$\\omega^3=1$ なので指数を $3$ で割った余りにできる。$\\omega^2+\\omega+1=0$ で $\\omega^2$ を消す。</p>","ωは3回で元に戻る。指数は3で割った余りだけ見る。",7)
def b8(r1,r2,a,b):
    Q=(x-r1)*(x-r2); P=x**3+a*x**2+b*x+7
    # remainder of P divided by Q: linear m x + n with P(r1)=m r1+n
    m=R(P.subs(x,r1)-P.subs(x,r2),r1-r2); nn=P.subs(x,r1)-m*r1
    q,r=sp.div(P,Q,x); assert sp.expand(r-(m*x+nn))==0
    st=[("余りは1次式","<p>"+I("P(x)=%s"%L(P))+" を "+I("(x-%d)(x-%d)"%(r1,r2))+" で割った余りを "+I("mx+n")+" とおく。</p>"),
        ("剰余定理","<p>"+D(r"P(%d)=%s=%dm+n,\qquad P(%d)=%s=%dm+n"%(r1,L(P.subs(x,r1)),r1,r2,L(P.subs(x,r2)),r2))),
        ("連立",D(r"m=%s,\quad n=%s"%(L(m),L(nn))))]
    return r"整式 $P(x)=%s$ を $%s$ で割った余りを求めよ。"%(L(P),L(sp.expand(Q))),st,L(m*x+nn)
o=[b8(*v) for v in [(1,2,3,-5),(1,-1,2,4),(2,3,-1,5),(-1,2,1,-3),(1,3,-2,6)]]
build(Z,CH,"2次式で割った余りを剰余定理で",o,"<p>余りを $mx+n$ とおき、割る式を $0$ にする $x$（2か所）で $P(x)=mx+n$ とする。連立して $m,n$。</p>","割り算を実行せず、2点の値だけで余りを決める。",8)
def b9(a,b,c):
    P=x**3+a*x**2+b*x+c; rts=sp.roots(P,x)
    ints=[r for r in rts if r.is_integer]; assert ints
    cand=sp.divisors(abs(c)); cand=[d for d in cand]+[-d for d in cand]
    r0=[d for d in cand if P.subs(x,d)==0][0]
    q,_=sp.div(P,x-r0,x); sol=sp.solve(P,x)
    st=[("整数解の候補","<p>整数解は定数項 "+I(str(c))+" の約数："+I(r",\ ".join("\\pm%d"%d for d in sp.divisors(abs(c))))+"。</p>"),
        ("因数定理","<p>"+I("P(%d)=0"%r0)+" より "+I("x-%d"%r0)+" を因数にもつ。</p>"+D(r"%s=(x-%d)(%s)"%(L(P),r0,L(q)))),
        ("残りを解く","<p>"+D(r"x=%s"%(r",\ ".join(L(s) for s in sol))))]
    return r"3次方程式 $%s=0$ を解け。"%L(P),st,r"x=%s"%(r",\ ".join(L(s) for s in sol))
o=[b9(*v) for v in [(-6,11,-6),(-2,-5,6),(1,-8,-12),(-5,8,-6),(2,5,-8)]]
build(Z,CH,"整数解をもつ3次方程式",o,"<p>整数解は<b>定数項の約数</b>から探す。$P(k)=0$ の $k$ を見つけたら因数定理で $(x-k)$ を因数にして、残りの2次方程式を解く。</p>","候補は定数項の約数だけ。1つ当たれば残りは2次。",9)
def b10(k):
    # x^3 - 3x^2 + k : has double root ; f'=3x(x-2): x=0 => k=0 ; x=2 => -4+k=0
    a=sp.symbols("a")
    P=x**3-3*x**2+k; 
    d=sp.discriminant(P,x)
    ks=sp.solve(sp.discriminant(x**3-3*x**2+a,x),a)
    return None
def b10(a):
    k=sp.symbols("k"); P=x**3-3*a*x**2+4*a**3 if False else None
    # f=x^3-3x+k double root: f'=3x^2-3=0 -> x=±1; f(1)=k-2=0 ->k=2 ; f(-1)=k+2=0->k=-2
    P=x**3-3*a*a*x+k
    return None
def b10(m):
    # f=x^3 - 3 m^2 x + k has double root: f'=3x^2-3m^2=0 x=±m ; f(m)=-2m^3+k=0 -> k=2m^3 ; f(-m)=2m^3+k -> k=-2m^3
    k=sp.symbols("k"); P=x**3-3*m**2*x+k
    ks=sorted(sp.solve(sp.discriminant(P,x),k)); assert ks==sorted([2*m**3,-2*m**3])
    st=[("重解の条件","<p>重解 $\\alpha$ は "+I("P(\\alpha)=0")+" かつ "+I("P'(\\alpha)=0")+"。</p>"),
        ("導関数","<p>"+D(r"P'(x)=3x^2-%d=0\ \Longrightarrow\ x=\pm%d"%(3*m*m,m))),
        ("P(α)=0 から k","<p>"+D(r"P(%d)=%s=0\Rightarrow k=%d,\qquad P(-%d)=0\Rightarrow k=%d"%(m,"k-%d"%(2*m**3),2*m**3,m,-2*m**3)))]
    return r"3次方程式 $x^3-%dx+k=0$ が重解をもつような定数 $k$ の値を求めよ。"%(3*m*m),st,r"k=%d,\ %d"%(2*m**3,-2*m**3)
o=[b10(m) for m in [1,2,3,4,5]]
build(Z,CH,"3次方程式が重解をもつ条件",o,"<p>重解 $\\alpha$ のとき $P(\\alpha)=0$ かつ $P'(\\alpha)=0$。<b>導関数 $=0$</b> から候補の $\\alpha$ を出し、$P(\\alpha)=0$ から $k$ を決める。</p>","重なる解は、グラフがx軸に接する点。",10)
XU=finishx(Z,CH)
