# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational; xx=sp.Symbol('x',real=True)
def co(c): return '' if c==1 else ('-' if c==-1 else L(c))
def chk(e,d): assert sp.simplify(sp.diff(e,xx)-d)==0
# 1 積の微分
def b1(a,b,c,m):
    u=a*xx**2+b*xx+c; v=sp.exp(m*xx); e=u*v; d=sp.expand((sp.diff(u,xx)+m*u)); ans=d*v; chk(e,ans)
    up=sp.diff(u,xx); mu=sp.expand(m*u); E_="e^{%sx}"%co(m) if m!=1 else "e^{x}"
    st=[("積の微分の公式を書く",D(r"\{f(x)g(x)\}'=f'(x)g(x)+f(x)g'(x)")),
        ("$f,\\ g$ を決める","<p>"+I(r"f=%s"%L(u))+"、"+I(r"g=%s"%E_)+" とする。</p>"),
        ("$f'$ を求める","<p>"+D(r"f'=%s"%L(up))),
        ("$g'$ を求める","<p>"+I(r"(e^{u})'=e^{u}\cdot u'")+" を使う。"+I(r"u=%sx"%co(m))+" の導関数は "+I(L(m))+"。</p>"+D(r"g'=%s\cdot e^{%sx}=%s%s"%(L(m),co(m),co(m),E_))),
        ("公式に代入する",D(r"y'=(%s)%s+(%s)\cdot %s%s"%(L(up),E_,L(u),co(m),E_))),
        ("$%s$ でくくる"%E_,"<p>共通因数 "+I(E_)+" でくくる。</p>"+D(r"y'=\left\{(%s)+%s(%s)\right\}%s"%(L(up),co(m) if abs(m)!=1 else ("-" if m==-1 else ""),L(u),E_))+"<p>かっこをはずして整理する。</p>"+D(r"=\left\{%s+%s\right\}%s=\left(%s\right)%s"%(L(up),L(mu),E_,L(d),E_)))]
    return r"$y=(%s)e^{%sx}$ を微分せよ。"%(L(u),co(m)),st,r"y'=\left(%s\right)e^{%sx}"%(L(d),co(m))
V=[(1,2,3,2),(2,-1,1,3),(1,0,-4,-3),(3,1,0,2),(1,-3,2,-2)]
o=[b1(*v) for v in V]
build(Z,CH,"積の微分（多項式×指数関数）",o,r"<p>$\{fg\}'=f'g+fg'$。$(e^{kx})'=ke^{kx}$ に注意して、$e^{kx}$ をくくり出す。</p>","2つの要素の積は、片方ずつ動かして足す。",1)
# 2 商の微分
def b2(a,b,c,d_):
    e=(a*xx+b)/(xx**2+c); ans=sp.simplify(sp.diff(e,xx)); chk(e,ans)
    N=sp.expand(a*(xx**2+c)-2*xx*(a*xx+b)); assert sp.simplify(N/(xx**2+c)**2-ans)==0
    f_=a*xx+b; g_=xx**2+c
    st=[("商の微分の公式を書く",D(r"\left\{\dfrac{f}{g}\right\}'=\dfrac{f'g-fg'}{g^2}")),
        ("$f,\\ g$ とその導関数","<p>"+I(r"f=%s,\ \ g=%s"%(L(f_),L(g_)))+"。</p>"+D(r"f'=%s,\qquad g'=2x"%L(a))),
        ("公式に代入する",D(r"y'=\dfrac{%s\cdot(%s)-(%s)\cdot2x}{(%s)^2}"%(L(a),L(g_),L(f_),L(g_)))),
        ("分子を展開する","<p>"+D(r"%s(%s)=%s,\qquad (%s)\cdot2x=%s"%(L(a),L(g_),L(sp.expand(a*g_)),L(f_),L(sp.expand(2*xx*f_))))+"<p>引き算に注意して、かっこをはずす。</p>"+D(r"(%s)-(%s)=%s"%(L(sp.expand(a*g_)),L(sp.expand(2*xx*f_)),L(N)))),
        ("答え",D(r"y'=\dfrac{%s}{(%s)^2}"%(L(N),L(g_))))]
    return r"$y=\dfrac{%s}{%s}$ を微分せよ。"%(L(a*xx+b),L(xx**2+c)),st,r"y'=\dfrac{%s}{(%s)^2}"%(L(N),L(xx**2+c))
V=[(1,2,1,0),(2,-1,3,0),(3,1,2,0),(1,-4,4,0),(2,5,1,0)]
o=[b2(*v) for v in V]
build(Z,CH,"商の微分",o,r"<p>$\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}$。分子の順序（$f'g-fg'$）に注意。</p>","分子は「上を動かして下はそのまま」引く「上はそのまま下を動かす」。",2)
# 3 合成関数
def b3(a,b,n):
    inner=a*xx**2+b*xx; e=sp.sin(inner)**n; ans=n*sp.sin(inner)**(n-1)*sp.cos(inner)*sp.diff(inner,xx); chk(e,ans)
    ip=sp.diff(inner,xx)
    st=[("合成関数の微分の公式を書く",D(r"\{f(g(x))\}'=f'(g(x))\,g'(x)")),
        ("層に分ける","<p>"+I(r"u=%s"%L(inner))+"、"+I(r"v=\sin u")+"、"+I(r"y=v^{%d}"%n)+" とおく。</p>"),
        ("各層を微分する","<p>"+D(r"\dfrac{dy}{dv}=%dv^{%d}=%d\sin^{%d}u,\qquad \dfrac{dv}{du}=\cos u,\qquad \dfrac{du}{dx}=%s"%(n,n-1,n,n-1,L(ip))).replace("v^{1}","v")),
        ("かけ合わせる","<p>"+D(r"y'=\dfrac{dy}{dv}\cdot\dfrac{dv}{du}\cdot\dfrac{du}{dx}=%d\sin^{%d}(%s)\cdot\cos(%s)\cdot(%s)"%(n,n-1,L(inner),L(inner),L(ip))).replace(r"\sin^{1}",r"\sin")),
        ("係数をまとめる",D(r"y'=%s\sin^{%d}(%s)\cos(%s)"%(L(n*ip),n-1,L(inner),L(inner))).replace(r"\sin^{1}",r"\sin"))]
    return r"$y=\sin^{%d}(%s)$ を微分せよ。"%(n,L(inner)),st,r"y'=%s\sin^{%d}(%s)\cos(%s)"%(L(n*sp.diff(inner,xx)),n-1,L(inner),L(inner))
V=[(1,0,3),(1,1,2),(2,0,3),(1,-1,4),(3,0,2)]
V=[(1,0,3),(1,1,2),(2,1,3),(1,-1,4),(3,2,2)]
o=[b3(*v) for v in V]
build(Z,CH,"合成関数の微分（三角関数）",o,r"<p>外側から順に微分し、<b>内側の導関数</b>をかけていく。$(\sin u)'=\cos u\cdot u'$。</p>","タマネギの皮むき：外から順にむいて、むいた分だけ掛けていく。",3)
# 4 対数
def b4(a,b):
    e=sp.log(xx**2+a)+b*sp.log(xx); ans=2*xx/(xx**2+a)+b/xx; chk(e,ans)
    g_=xx**2+a
    st=[("公式を確認する",D(r"(\log x)'=\dfrac1x,\qquad \{\log g(x)\}'=\dfrac{g'(x)}{g(x)}")),
        ("第1項を微分する","<p>"+I(r"g=%s"%L(g_))+" とおくと "+I(r"g'=2x")+"。</p>"+D(r"\{\log(%s)\}'=\dfrac{g'}{g}=\dfrac{2x}{%s}"%(L(g_),L(g_)))),
        ("第2項を微分する","<p>定数 "+I(L(b))+" はそのまま外に出す。</p>"+D(r"(%s\log x)'=%s\cdot\dfrac1x=\dfrac{%s}{x}"%(L(b),L(b),L(b)))),
        ("たす",D(r"y'=\dfrac{2x}{%s}+\dfrac{%s}{x}"%(L(g_),L(b))))]
    return r"$y=\log(%s)+%s\log x\ (x>0)$ を微分せよ。"%(L(xx**2+a),L(b)),st,r"y'=\dfrac{2x}{%s}+\dfrac{%s}{x}"%(L(xx**2+a),L(b))
V=[(1,2),(3,-3),(4,3),(2,5),(5,-2)]
o=[b4(*v) for v in V]
build(Z,CH,"対数関数の微分",o,r"<p>$\{\log g\}'=\dfrac{g'}{g}$。和は項ごとに微分する。</p>","対数の微分は「中身の変化率÷中身」。",4)
# 5 対数微分法
def b5(n,m):
    e=xx**n*sp.exp(m*xx); d=sp.diff(e,xx); ans=sp.expand_func(sp.simplify(d)); chk(e,ans)
    # 対数微分
    m_=co(m)
    st=[("両辺の対数をとる（$x>0$）","<p>"+I(r"y=x^{%d}e^{%sx}"%(n,m_))+" の両辺の対数をとり、積を和に直す。</p>"+D(r"\log y=\log x^{%d}+\log e^{%sx}=%d\log x+%sx"%(n,m_,n,m_))),
        ("両辺を $x$ で微分する","<p>左辺は "+I("y")+" が "+I("x")+" の関数なので、合成関数の微分で "+I(r"\dfrac{y'}{y}")+"。</p>"+D(r"\dfrac{y'}{y}=\dfrac{%d}{x}+%s"%(n,L(m)))),
        ("$y'$ について解く","<p>両辺に "+I("y")+" をかけ、"+I(r"y=x^{%d}e^{%sx}"%(n,m_))+" を代入する。</p>"+D(r"y'=y\left(\dfrac{%d}{x}+%s\right)=x^{%d}e^{%sx}\left(\dfrac{%d}{x}+%s\right)"%(n,L(m),n,m_,n,L(m)))),
        ("かっこをはずして整理","<p>"+D(r"x^{%d}\cdot\dfrac{%d}{x}=%dx^{%d},\qquad x^{%d}\cdot%s=%sx^{%d}"%(n,n,n,n-1,n,L(m),L(m),n)).replace("x^{1}","x")+"<p>"+I(r"x^{%d}=x\cdot x^{%d}"%(n,n-1))+" として "+I(r"x^{%d}"%(n-1))+" でくくる。</p>"+D(r"y'=\left(%d+%sx\right)x^{%d}e^{%sx}"%(n,L(m),n-1,m_)).replace("x^{1}","x"))]
    return r"$y=x^{%d}e^{%sx}\ (x>0)$ を、対数微分法で微分せよ。"%(n,m_),st,r"y'=(%sx+%d)x^{%d}e^{%sx}"%(m_,n,n-1,m_)
V=[(3,2),(2,-3),(4,3),(5,2),(3,-2)]
o=[b5(*v) for v in V]
build(Z,CH,"対数微分法",o,r"<p>積・累乗の形は、<b>両辺の対数をとって微分</b>：$\dfrac{y'}y=(\log y)'$。最後に $y$ をかけて戻す。</p>","かけ算を足し算に変えてから微分する、遠回りのようで近道。",5)
UNIT=finish(Z,CH,1,0,"微分法","導関数の計算","積・商・合成関数・対数微分法まで、導関数の計算の難問に挑みます。",subject="3")
