# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x")
# 6 割り算
def b6(P,Q):
    q,r=sp.div(P,Q,x); assert sp.expand(q*Q+r-P)==0
    st=[("筆算の要領で割る","<p>最高次の項どうしを割って商を立て、引く操作をくり返す（次数が "+I("Q")+" より下がるまで）。</p>"),
        ("商と余り",D(r"\text{商 }%s,\qquad \text{余り }%s"%(L(q),L(r)))),
        ("検算",D(r"(%s)(%s)+(%s)=%s"%(L(Q),L(q),L(r),L(sp.expand(P)))))]
    return r"$%s$ を $%s$ で割ったときの商と余りを求めよ。"%(L(P),L(Q)),st,r"\text{商 }%s,\ \text{余り }%s"%(L(q),L(r))
o=[b6(*v) for v in [(2*x**4-3*x**3+x-5,x**2-x+2),(x**4+2*x**2-3,x**2+x-1),(3*x**4-x**3+2*x**2+4,x**2+2),(x**5-x**3+2*x-1,x**2-2*x+3),(4*x**4+x**2-x+6,2*x**2-x+1)]]
build(Z,CH,"4次式を2次式で割る筆算",o,"<p>降べきの順に並べ、欠けている次数は 0 で補って筆算。余りの次数が割る式より小さくなったら終了。</p>","大きい項から順に消していく。",6)
# 7 繁分数式
def b7(a,b):
    e=1/(x-a)-1/(x+b); res=sp.factor(sp.simplify((1/(x-a)-1/(x+b))/(1/(x-a)+1/(x+b))))
    nu=sp.factor(sp.together(e)); de=sp.factor(sp.together(1/(x-a)+1/(x+b))); cm=sp.expand((x-a)*(x+b)); cmf=r"(x-%d)(x+%d)"%(a,b)
    st=[("分子を通分する","<p>分子 "+I(r"\dfrac1{x-%d}-\dfrac1{x+%d}"%(a,b))+" の分母をそろえる。</p>"+D(r"\dfrac{x+%d}{%s}-\dfrac{x-%d}{%s}=\dfrac{(x+%d)-(x-%d)}{%s}=\dfrac{%s}{%s}"%(b,cmf,a,cmf,b,a,cmf,L(sp.expand((x+b)-(x-a))),cmf))),
        ("分母を通分する","<p>分母 "+I(r"\dfrac1{x-%d}+\dfrac1{x+%d}"%(a,b))+" も同じ分母にそろえる。</p>"+D(r"\dfrac{x+%d}{%s}+\dfrac{x-%d}{%s}=\dfrac{(x+%d)+(x-%d)}{%s}=\dfrac{%s}{%s}"%(b,cmf,a,cmf,b,a,cmf,L(sp.expand((x+b)+(x-a))),cmf))),
        ("割り算にして約分","<p>分子 "+I(r"\div")+" 分母 は、分母の逆数をかける。</p>"+D(r"\dfrac{%s}{%s}\div\dfrac{%s}{%s}=\dfrac{%s}{%s}\times\dfrac{%s}{%s}"%(L(sp.expand((x+b)-(x-a))),cmf,L(sp.expand((x+b)+(x-a))),cmf,L(sp.expand((x+b)-(x-a))),cmf,cmf,L(sp.expand((x+b)+(x-a)))))+"<p>"+I(cmf)+" が約分できる。</p>"+D(r"=%s"%L(res)))]
    return r"次の式を簡単にせよ。$\dfrac{\dfrac{1}{x-%d}-\dfrac{1}{x+%d}}{\dfrac{1}{x-%d}+\dfrac{1}{x+%d}}$"%(a,b,a,b),st,L(res)
o=[b7(*v) for v in [(1,2),(2,3),(1,1),(3,1),(2,5)]]
build(Z,CH,"繁分数式の簡単化",o,"<p>分子・分母をそれぞれ<b>通分して1つの分数式</b>にしてから、$\\dfrac{A}{B}=A\\times\\dfrac1B$ と約分。</p>","上と下を別々に片づけてから割る。",7)
# 8 部分分数の和
def b8(d,n):
    k=sp.symbols("k"); terms=[1/(k*(k+d)) for _ in [0]]
    S=sum(R(1,i*(i+d)) for i in range(1,n+1))
    S1=sum(R(1,d)*(R(1,i)-R(1,i+d)) for i in range(1,n+1)); assert S==S1
    st=[("部分分数に分ける","<p>"+I(r"\dfrac1{k(k+%d)}=\dfrac1{%d}\left(\dfrac1k-\dfrac1{k+%d}\right)"%(d,d,d))+"。</p>"),
        ("和をとる","<p>"+I("k=1,\\ldots,%d"%n)+" で、%d つおきに打ち消し合う。</p>"%d+D(r"\dfrac1{%d}\left(%s-%s\right)"%(d,"+".join(r"\dfrac1{%d}"%i for i in range(1,d+1)),"-".join([])+ "+".join(r"\dfrac1{%d}"%i for i in range(n+1,n+d+1))))),
        ("計算",D(L(S)))]
    return r"$\displaystyle\sum_{k=1}^{%d}\dfrac{1}{k(k+%d)}$ の値を求めよ。"%(n,d),st,L(S)
o=[b8(*v) for v in [(2,10),(3,9),(2,20),(3,12),(4,8)]]
build(Z,CH,"間隔が d の部分分数の和",o,"<p>$\\dfrac1{k(k+d)}=\\dfrac1d\\left(\\dfrac1k-\\dfrac1{k+d}\\right)$。和をとると、<b>最初の $d$ 個と最後の $d$ 個</b>だけが残る。</p>","ドミノのように途中が全部打ち消される。",8)
# 9 係数決定（割り切れる）
def b9(a,b,Q):
    A,B=sp.symbols("A B"); P=x**4+A*x**3+B*x**2-x+6 if False else x**4+A*x**2+B*x-6
    q,r=sp.div(P,Q,x); sol=sp.solve([sp.expand(r).coeff(x,1),sp.expand(r).coeff(x,0)],[A,B],dict=True)[0]
    P2=P.subs(sol)
    assert sp.rem(P2,Q,x)==0
    st=[("割り算して余りを求める","<p>"+I("x^4+Ax^2+Bx-6")+" を "+I(L(Q))+" で割った余り：</p>"+D(L(sp.expand(r)))),
        ("余り $=0$ より","<p>"+I("x")+" の係数と定数項がともに 0。</p>"+D(r"A=%s,\quad B=%s"%(L(sol[A]),L(sol[B]))))]
    return r"整式 $x^4+Ax^2+Bx-6$ が $%s$ で割り切れるように、定数 $A,\ B$ の値を定めよ。"%L(Q),st,r"A=%s,\ B=%s"%(L(sol[A]),L(sol[B]))
o=[b9(0,0,Q) for Q in [x**2-x-2,x**2+x-2,x**2-3*x+2,x**2-4,x**2+2*x-3]]
build(Z,CH,"割り切れる条件から係数を決める",o,"<p>割り算を実行し、余り（1次式）が <b>恒等的に 0</b> となる条件、つまり $x$ の係数と定数項がともに 0 として連立。</p>","余りを0にする2つの条件で、未知数2つが決まる。",9)
# 10 分数式が整数
def b10(a,b):
    f=lambda n:R(n**2+a*n+b,n+1) if False else None
    N=sp.symbols("N"); 
    # (n^2+a n+b)/(n+1)=n+(a-1)+(b-a+1)/(n+1)
    c=b-a+1; ans=[n for n in range(-300,300) if n!=-1 and (n*n+a*n+b)%(n+1)==0]
    divs=sp.divisors(abs(c)); assert sorted(ans)==sorted({d-1 for d in divs}|{-d-1 for d in divs}) 
    st=[("割り算","<p>"+D(r"\dfrac{n^2+%dn+%d}{n+1}=n+%d+\dfrac{%d}{n+1}"%(a,b,a-1,c))),
        ("整数になる条件","<p>"+I("n+1")+" が "+I(str(c))+" の約数："+I(r"n+1=%s"%(r",\ ".join("\\pm%d"%d for d in divs)))+"。</p>"),
        ("答え",D(r"n=%s"%(r",\ ".join(str(v) for v in sorted(ans)))))]
    return r"整数 $n$ について、$\dfrac{n^2+%dn+%d}{n+1}$ が整数となるような $n$ をすべて求めよ。"%(a,b),st,r"n=%s"%(r",\ ".join(str(v) for v in sorted(ans)))
o=[b10(*v) for v in [(3,8),(2,9),(4,11),(1,7),(5,12)]]
build(Z,CH,"分数式が整数となる整数 n",o,"<p>分子を分母で割って<b>（整式）＋（定数）／（分母）</b>の形にする。定数が $n+1$ で割り切れる、つまり $n+1$ が定数の約数。</p>","余りの部分だけが問題。それが割り切れる条件を探す。",10)
XU=finishx(Z,CH)
