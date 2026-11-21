# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
s=sp.sqrt
# 6
def b6(p,q):
    A=s(p)+s(q); B=s(p)-s(q); xx_=A/B; yy=B/A
    S=sp.simplify(xx_+yy); Pd=sp.simplify(xx_*yy); S2=sp.simplify(xx_**2+yy**2); assert S2==S**2-2
    x2=sp.radsimp(xx_)
    st=[("$x$ を有理化","<p>分母・分子に "+I(r"\sqrt{%d}+\sqrt{%d}"%(p,q))+" をかける。</p>"+D(r"x=\dfrac{(\sqrt{%d}+\sqrt{%d})^2}{%d-%d}=\dfrac{%s}{%d}=%s"%(p,q,p,q,L(sp.expand((s(p)+s(q))**2)),p-q,L(x2)))),
        ("$y=\\dfrac1x$ も同様","<p>"+I(r"y=\dfrac{\sqrt{%d}-\sqrt{%d}}{\sqrt{%d}+\sqrt{%d}}=%s"%(p,q,p,q,L(sp.radsimp(yy))))+"。</p>"),
        ("$x+y,\\ xy$ から値を出す","<p>"+I(r"x+y=%s,\ \ xy=1"%L(S))+"。</p>"+D(r"x^2+y^2=(x+y)^2-2xy=%s^2-2=%s"%(L(S),L(S2))))]
    return r"$x=\dfrac{\sqrt{%d}+\sqrt{%d}}{\sqrt{%d}-\sqrt{%d}},\ y=\dfrac{\sqrt{%d}-\sqrt{%d}}{\sqrt{%d}+\sqrt{%d}}$ のとき、$x^2+y^2$ の値を求めよ。"%(p,q,p,q,p,q,p,q),st,L(S2)
o=[b6(*v) for v in [(3,2),(5,3),(7,5),(6,2),(5,2)]]
build(Z,CH,"有理化と対称式（x と 1/x）",o,r"<p>$x$ と $y$ が逆数の関係なら $xy=1$。$x+y$ だけを有理化して求め、$x^2+y^2=(x+y)^2-2xy$ で値を出す。</p>","個別に計算せず、和と積の2つの情報にまとめる。",6)
# 7
def b7(a,b,c):
    # |x-a|+|x-b|<c , a<b
    lo=sp.Rational(a+b-c,2); hi=sp.Rational(a+b+c,2); assert c>b-a
    xs=np.linspace(float(lo)-3,float(hi)+3,200001); mask=(np.abs(xs-a)+np.abs(xs-b)<c)
    assert abs(xs[mask].min()-float(lo))<1e-3 and abs(xs[mask].max()-float(hi))<1e-3
    st=[("場合分けの境目","<p>"+I("x=%d,\ %d"%(a,b))+" を境に3つに分ける。</p>"),
        ("3つの場合","<p>"+I("x<%d"%a)+"：左辺 "+I("-(x-%d)-(x-%d)=%s"%(a,b,L(-2*x+a+b)))+"。"+I("%s<%d"%(L(-2*x+a+b),c))+" より "+I("x>%s"%L(lo))+"（"+I("x<%d"%a)+" との共通部分あり）。</p>"+"<p>"+I("%d\\leqq x<%d"%(a,b))+"：左辺 "+I("%d"%(b-a))+" は一定で "+I("%d<%d"%(b-a,c))+" 常に成立。</p>"+"<p>"+I("x\\geqq %d"%b)+"：左辺 "+I("%s"%L(2*x-a-b))+"。"+I("%s<%d"%(L(2*x-a-b),c))+" より "+I("x<%s"%L(hi))+"。</p>"),
        ("合わせる",D(r"%s<x<%s"%(L(lo),L(hi))))]
    return r"不等式 $|x-%d|+|x-%d|<%d$ を解け。"%(a,b,c),st,r"%s<x<%s"%(L(lo),L(hi))
o=[b7(*v) for v in [(1,4,7),(-1,3,6),(2,5,9),(0,4,10),(-2,1,5)]]
build(Z,CH,"絶対値が2つある不等式",o,r"<p>絶対値の中が0になる $x$ を境に<b>3つに場合分け</b>し、各場合で絶対値をはずして解く。<b>場合の範囲との共通部分</b>をとり、最後に和集合。</p>","数直線を境目で3つの部屋に分けて、部屋ごとに解く。",7)
# 8 最小値
def b8(a,b,c):
    # |x-a|+|x-b|+|x-c|, a<b<c  min at x=b value c-a
    f=lambda t:abs(t-a)+abs(t-b)+abs(t-c); xs=np.linspace(a-3,c+3,60001); v=[f(t) for t in xs]; assert abs(min(v)-(c-a))<1e-3 and abs(xs[int(np.argmin(v))]-b)<1e-3
    st=[("数直線で考える","<p>"+I("|x-%d|"%a)+" は "+I("x")+" と "+I(str(a))+" の距離。"+I("f(x)")+" は点 "+I("x")+" から3点 "+I("%d,\ %d,\ %d"%(a,b,c))+" までの距離の和。</p>"),
        ("両端の2点の距離の和は一定","<p>"+I("x")+" が "+I("%d\\leqq x\\leqq %d"%(a,c))+" にあれば "+I("|x-%d|+|x-%d|=%d"%(a,c,c-a))+"（一定）。</p>"),
        ("真ん中の点を足す","<p>残りの "+I("|x-%d|"%b)+" は "+I("x=%d"%b)+" のとき最小値 0。</p>"+D(r"f(%d)=%d+0+%d=%d"%(b,b-a,c-b,c-a)))]
    return r"$f(x)=|x-%d|+|x-%d|+|x-%d|$ の最小値と、そのときの $x$ を求めよ。"%(a,b,c),st,r"x=%d\ \text{のとき最小値 }%d"%(b,c-a)
o=[b8(*v) for v in [(1,3,8),(-2,1,6),(0,5,7),(2,4,11),(-3,0,4)]]
build(Z,CH,"絶対値の和の最小値（距離で考える）",o,r"<p>$|x-a|$ は $x$ と $a$ の距離。<b>3点の距離の和</b>は、真ん中の点で最小になる。両端2点の距離の和は、その間では一定。</p>","3軒の家から等しく近い所を探す。真ん中の家の前が最短。",8)
# 9 √(n/ ...) が整数
def b9(N):
    fs=sp.factorint(N); n0=1
    for p_,e in fs.items():
        if e%2: n0*=p_
    # n such that sqrt(N n) integer → minimal n0 ; "√(N/n) 整数となる自然数n": n divides N and N/n square
    ns=[d for d in sp.divisors(N) if sp.sqrt(sp.Integer(N)//d).is_integer]
    st=[("素因数分解する","<p>"+I("%d=%s"%(N,r"\times".join(str(p_)+("^{%d}"%e if e>1 else "") for p_,e in sorted(fs.items()))))+"。</p>"),
        ("$\\dfrac{%d}{n}$ が平方数になる条件","<p>各素因数の指数がすべて<b>偶数</b>になるように "+I("n")+" で割る。</p>"+D(r"n=%s"%(r",\ ".join(str(d) for d in ns)))),
        ("個数・最大","<p>条件をみたす "+I("n")+" は "+I(str(len(ns)))+" 個。最大は "+I(str(max(ns)))+"。</p>")]
    return r"自然数 $n$ で、$\sqrt{\dfrac{%d}{n}}$ が自然数となるものをすべて求めよ。"%N,st,r"n=%s"%(r",\ ".join(str(d) for d in ns))
o=[b9(N) for N in [180,360,600,720,1000]]
build(Z,CH,"根号が整数になる自然数 n",o,r"<p>$\sqrt{\dfrac Nn}$ が自然数 $\iff \dfrac Nn$ が平方数。$N$ を素因数分解し、<b>各素因数の指数が偶数</b>になる $n$（$N$ の約数）を調べる。</p>","指数が全部偶数なら、ペアになって根号の外に出られる。",9)
# 10 telescoping
def b10(n):
    S=sum(1/(sp.sqrt(i)+sp.sqrt(i+1)) for i in range(1,n)); v=sp.sqrt(n)-1; assert abs(float(S)-float(v))<1e-9
    st=[("各項を有理化","<p>"+I(r"\dfrac1{\sqrt k+\sqrt{k+1}}=\dfrac{\sqrt{k+1}-\sqrt k}{(k+1)-k}=\sqrt{k+1}-\sqrt k")+"。</p>"),
        ("並べて消える",D(r"(\sqrt2-\sqrt1)+(\sqrt3-\sqrt2)+\cdots+(\sqrt{%d}-\sqrt{%d})"%(n,n-1)))
        ,("残る項",D(r"=\sqrt{%d}-1=%s"%(n,L(v))))]
    return r"$\dfrac1{\sqrt1+\sqrt2}+\dfrac1{\sqrt2+\sqrt3}+\cdots+\dfrac1{\sqrt{%d}+\sqrt{%d}}$ の値を求めよ。"%(n-1,n),st,L(v)
o=[b10(n) for n in [10,26,17,50,101]]
build(Z,CH,"有理化で消える和",o,r"<p>各項を有理化すると $\sqrt{k+1}-\sqrt k$ になり、<b>隣どうしで消えて</b>両端だけが残る。</p>","望遠鏡を縮めるように、途中が重なって消える。",10)
XU=finishx(Z,CH)
