# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational; xx=sp.Symbol('x',real=True)
def chk(e,d): assert sp.simplify(sp.diff(e,xx)-d)==0
# 1 積の微分
def b1(a,b,c,m):
    u=a*xx**2+b*xx+c; v=sp.exp(m*xx); e=u*v; d=sp.expand((sp.diff(u,xx)+m*u)); ans=d*v; chk(e,ans)
    st=[("積の微分",D(r"\{f(x)g(x)\}'=f'(x)g(x)+f(x)g'(x)")),
        ("各部分を微分","<p>"+I(r"u=%s"%L(u))+"、"+I(r"v=e^{%sx}"%L(m))+"。</p>"+D(r"u'=%s,\qquad v'=%se^{%sx}"%(L(sp.diff(u,xx)),L(m),L(m)))),
        ("組み合わせる",D(r"y'=(%s)e^{%sx}+(%s)\cdot %se^{%sx}=\left(%s\right)e^{%sx}"%(L(sp.diff(u,xx)),L(m),L(u),L(m),L(m),L(d),L(m))))]
    return r"$y=(%s)e^{%sx}$ を微分せよ。"%(L(u),L(m)),st,r"y'=\left(%s\right)e^{%sx}"%(L(d),L(m))
V=[(1,2,3,2),(2,-1,1,3),(1,0,-4,-3),(3,1,0,2),(1,-3,2,-2)]
o=[b1(*v) for v in V]
build(Z,CH,"積の微分（多項式×指数関数）",o,r"<p>$\{fg\}'=f'g+fg'$。$(e^{kx})'=ke^{kx}$ に注意して、$e^{kx}$ をくくり出す。</p>","2つの要素の積は、片方ずつ動かして足す。",1)
# 2 商の微分
def b2(a,b,c,d_):
    e=(a*xx+b)/(xx**2+c); ans=sp.simplify(sp.diff(e,xx)); chk(e,ans)
    N=sp.expand(a*(xx**2+c)-2*xx*(a*xx+b)); assert sp.simplify(N/(xx**2+c)**2-ans)==0
    st=[("商の微分",D(r"\left\{\dfrac{f}{g}\right\}'=\dfrac{f'g-fg'}{g^2}")),
        ("代入",D(r"y'=\dfrac{%s(%s)-(%s)\cdot 2x}{(%s)^2}"%(L(a),L(xx**2+c),L(a*xx+b),L(xx**2+c)))),
        ("整理",D(r"y'=\dfrac{%s}{(%s)^2}"%(L(N),L(xx**2+c))))]
    return r"$y=\dfrac{%s}{%s}$ を微分せよ。"%(L(a*xx+b),L(xx**2+c)),st,r"y'=\dfrac{%s}{(%s)^2}"%(L(N),L(xx**2+c))
V=[(1,2,1,0),(2,-1,3,0),(3,1,2,0),(1,-4,4,0),(2,5,1,0)]
o=[b2(*v) for v in V]
build(Z,CH,"商の微分",o,r"<p>$\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}$。分子の順序（$f'g-fg'$）に注意。</p>","分子は「上を動かして下はそのまま」引く「上はそのまま下を動かす」。",2)
# 3 合成関数
def b3(a,b,n):
    inner=a*xx**2+b*xx; e=sp.sin(inner)**n; ans=n*sp.sin(inner)**(n-1)*sp.cos(inner)*sp.diff(inner,xx); chk(e,ans)
    st=[("合成関数の微分",D(r"\{f(g(x))\}'=f'(g(x))\,g'(x)")),
        ("外側から順に","<p>外側 "+I(r"(\ \ )^{%d}"%n)+"、中 "+I(r"\sin(\ \ )")+"、内側 "+I(L(inner))+"。</p>"+D(r"y'=%d\sin^{%d}(%s)\cdot\cos(%s)\cdot(%s)"%(n,n-1,L(inner),L(inner),L(sp.diff(inner,xx))))),
        ("整理",D(r"y'=%s\sin^{%d}(%s)\cos(%s)"%(L(n*sp.diff(inner,xx)),n-1,L(inner),L(inner))))]
    return r"$y=\sin^{%d}(%s)$ を微分せよ。"%(n,L(inner)),st,r"y'=%s\sin^{%d}(%s)\cos(%s)"%(L(n*sp.diff(inner,xx)),n-1,L(inner),L(inner))
V=[(1,0,3),(1,1,2),(2,0,3),(1,-1,4),(3,0,2)]
V=[(1,0,3),(1,1,2),(2,1,3),(1,-1,4),(3,2,2)]
o=[b3(*v) for v in V]
build(Z,CH,"合成関数の微分（三角関数）",o,r"<p>外側から順に微分し、<b>内側の導関数</b>をかけていく。$(\sin u)'=\cos u\cdot u'$。</p>","タマネギの皮むき：外から順にむいて、むいた分だけ掛けていく。",3)
# 4 対数
def b4(a,b):
    e=sp.log(xx**2+a)+b*sp.log(xx); ans=2*xx/(xx**2+a)+b/xx; chk(e,ans)
    st=[("公式",D(r"(\log x)'=\dfrac1x,\qquad \{\log g(x)\}'=\dfrac{g'(x)}{g(x)}")),
        ("各項を微分",D(r"\{\log(%s)\}'=\dfrac{%s}{%s},\qquad (%s\log x)'=\dfrac{%s}{x}"%(L(xx**2+a),L(2*xx),L(xx**2+a),L(b),L(b)))),
        ("たす",D(r"y'=\dfrac{2x}{%s}+\dfrac{%s}{x}"%(L(xx**2+a),L(b))))]
    return r"$y=\log(%s)+%s\log x\ (x>0)$ を微分せよ。"%(L(xx**2+a),L(b)),st,r"y'=\dfrac{2x}{%s}+\dfrac{%s}{x}"%(L(xx**2+a),L(b))
V=[(1,2),(3,-3),(4,3),(2,5),(5,-2)]
o=[b4(*v) for v in V]
build(Z,CH,"対数関数の微分",o,r"<p>$\{\log g\}'=\dfrac{g'}{g}$。和は項ごとに微分する。</p>","対数の微分は「中身の変化率÷中身」。",4)
# 5 対数微分法
def b5(n,m):
    e=xx**n*sp.exp(m*xx); d=sp.diff(e,xx); ans=sp.expand_func(sp.simplify(d)); chk(e,ans)
    # 対数微分
    st=[("両辺の対数をとる（$x>0$）",D(r"\log y=%d\log x+%sx"%(n,L(m)))),
        ("両辺を $x$ で微分",D(r"\dfrac{y'}{y}=\dfrac{%d}{x}+%s"%(n,L(m)))),
        ("$y'$ を求める",D(r"y'=y\left(\dfrac{%d}{x}+%s\right)=x^{%d}e^{%sx}\left(\dfrac{%d}{x}+%s\right)=%sx^{%d}e^{%sx}"%(n,L(m),n,L(m),n,L(m),L(sp.expand(m*xx+n)/xx*1) if False else "("+L(m)+"x+"+str(n)+")",n-1,L(m))))]
    return r"$y=x^{%d}e^{%sx}\ (x>0)$ を、対数微分法で微分せよ。"%(n,L(m)),st,r"y'=(%sx+%d)x^{%d}e^{%sx}"%(L(m),n,n-1,L(m))
V=[(3,2),(2,-3),(4,3),(5,2),(3,-2)]
o=[b5(*v) for v in V]
build(Z,CH,"対数微分法",o,r"<p>積・累乗の形は、<b>両辺の対数をとって微分</b>：$\dfrac{y'}y=(\log y)'$。最後に $y$ をかけて戻す。</p>","かけ算を足し算に変えてから微分する、遠回りのようで近道。",5)
UNIT=finish(Z,CH,1,0,"微分法","導関数の計算","積・商・合成関数・対数微分法まで、導関数の計算の難問に挑みます。",subject="3")
