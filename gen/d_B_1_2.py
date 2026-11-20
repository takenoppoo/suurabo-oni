# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
n=sp.Symbol('n'); k=sp.Symbol('k')
def tex_poly(a,b,c,v="k"):
    return L(sp.expand(a*sp.Symbol(v)**2+b*sp.Symbol(v)+c))
# 例題1 Σ公式
def b1(a,b,c):
    t=a*k**2+b*k+c; S=sp.factor(a*n*(n+1)*(2*n+1)/6+b*n*(n+1)/2+c*n); assert all(sum(t.subs(k,j) for j in range(1,N+1))==S.subs(n,N) for N in (1,2,5,9))
    parts=[]
    if a: parts.append(r"%s\cdot\dfrac{n(n+1)(2n+1)}{6}"%("" if a==1 else L(a)))
    if b: parts.append(r"%s\cdot\dfrac{n(n+1)}{2}"%("" if b==1 else L(b)))
    if c: parts.append(r"%s\,n"%L(c))
    ex_=("+".join(parts)).replace("+-","-")
    st=[("公式を使えるように分ける","<p>"+I(r"\sum_{k=1}^n k^2=\dfrac{n(n+1)(2n+1)}6,\ \ \sum_{k=1}^n k=\dfrac{n(n+1)}2,\ \ \sum_{k=1}^n c=cn")+"。</p>"),
        ("公式に代入する",D(r"\sum_{k=1}^n\left(%s\right)=%s"%(L(t),ex_))),
        ("共通因数でくくる","<p>"+I(r"n")+" を くくり、通分して整理する。</p>"+D(r"=%s"%L(S)))]
    return r"次の和を $n$ の式で表せ（因数分解した形で答えよ）。 $$\sum_{k=1}^{n}\left(%s\right)$$"%L(t),st,r"%s"%L(S)
V=[(3,-1,2),(6,3,-2),(2,-3,1),(12,-6,0),(4,2,3)]
o=[b1(*v) for v in V]
build(Z,CH,"Σの公式と計算",o,r"<p>$\displaystyle\sum_{k=1}^nk=\dfrac{n(n+1)}2,\ \sum_{k=1}^nk^2=\dfrac{n(n+1)(2n+1)}6,\ \sum_{k=1}^nk^3=\left\{\dfrac{n(n+1)}2\right\}^2$、$\displaystyle\sum_{k=1}^n c=cn$。項ごとに分けて代入し、共通因数でくくる。</p>","$k$ の何乗かごとに「型」が決まっている。型に当てはめて、最後にまとめる。",1)
# 例題2 階差数列
def b2(a1,p,q):
    an=lambda m: a1+sum(p*j+q for j in range(1,m)); terms=[an(m) for m in range(1,6)]
    g=sp.expand(a1+p*(n-1)*n/2+q*(n-1)); assert all(g.subs(n,m)==an(m) for m in range(1,12))
    b=[terms[i+1]-terms[i] for i in range(4)]
    assert all(b[i+1]-b[i]==p for i in range(3))
    st=[("階差数列を調べる","<p>隣り合う項の差 "+I(r"b_n=a_{n+1}-a_n")+" を求める。</p>"+D(r"b_1=%d,\ b_2=%d,\ b_3=%d,\ b_4=%d"%tuple(b))+"<p>公差 "+I(str(p))+" の等差数列だから</p>"+D(r"b_n=%d+(n-1)\times%s=%s"%(b[0],P(p),L(p*n+q)))),
        ("公式を使う","<p>$n\\geqq2$ のとき</p>"+D(r"a_n=a_1+\sum_{k=1}^{n-1}b_k=%d+\sum_{k=1}^{n-1}\left(%s\right)"%(a1,L(p*k+q)))),
        ("Σを計算する",D(r"=%d+%s\cdot\dfrac{(n-1)n}{2}+%s(n-1)=%s"%(a1,P(p),P(q),L(g)))),
        ("$n=1$ のとき","<p>"+I(r"a_1=%s"%L(g.subs(n,1)))+" で、与えられた初項 "+I(r"a_1=%d"%a1)+" と一致するので、$n=1$ でも成り立つ。</p>")]
    return r"数列 $%d,\ %d,\ %d,\ %d,\ %d,\ \cdots$ の一般項 $a_n$ を求めよ。"%tuple(terms),st,r"a_n=%s"%L(g)
V=[(1,2,1),(3,4,-1),(2,1,3),(5,3,-2),(1,6,0)]
o=[b2(*v) for v in V]
build(Z,CH,"階差数列と一般項",o,r"<p>階差数列 $b_n=a_{n+1}-a_n$ が分かるとき、<b>$n\geqq2$ で $a_n=a_1+\displaystyle\sum_{k=1}^{n-1}b_k$</b>。最後に $n=1$ でも成り立つか確かめる。</p>","1歩ごとの上がり幅（階差）を足し合わせれば、今いる高さ（一般項）になる。",2)
# 例題3 部分分数
def b3(c,d):
    t=sp.Rational(c)/(k*(k+d)); S=sp.factor(sp.together(sp.Rational(c,d)*(sum(sp.Rational(1,j) for j in range(1,d+1))-sum(1/(n+j) for j in range(1,d+1))))); assert all(sum(t.subs(k,j) for j in range(1,N+1))==S.subs(n,N) for N in (1,3,7))
    cd=sp.Rational(c,d)
    head=r"\left(\dfrac11-\dfrac1{%d}\right)+\left(\dfrac12-\dfrac1{%d}\right)+\left(\dfrac13-\dfrac1{%d}\right)+\cdots+\left(\dfrac1{n}-\dfrac1{n+%d}\right)"%(1+d,2+d,3+d,d)
    rest=r"\left(%s\right)-\left(%s\right)"%("+".join(r"\dfrac1{%d}"%j for j in range(1,d+1)),"+".join(r"\dfrac1{n+%d}"%j for j in range(1,d+1)))
    st=[("部分分数に分ける",D(r"\dfrac{%d}{k(k+%d)}=%s\left(\dfrac1k-\dfrac1{k+%d}\right)"%(c,d,L(cd),d))),
        ("書き並べる","<p>" +I(r"\sum_{k=1}^n\dfrac{%d}{k(k+%d)}"%(c,d))+" は、"+I(L(cd))+" と次の和の積。</p>"+D(head)),
        ("消える項に注意","<p>"+("途中の項は消え、"+("最初の %d 個の正の項と最後の %d 個の負の項"%(d,d)+"だけ残る。" if d>1 else "最初の $\\frac11$ と最後の $-\\frac1{n+1}$ だけ残る。"))+"</p>"+D(rest)),
        ("まとめる",D(r"S_n=%s\times\{\cdots\}=%s"%(L(cd),L(S))))]
    return r"次の和を $n$ の式で表せ。 $$\sum_{k=1}^{n}\dfrac{%d}{k(k+%d)}$$"%(c,d),st,r"%s"%L(S)
V=[(1,1),(2,2),(1,2),(3,3),(1,3)]
o=[b3(*v) for v in V]
build(Z,CH,"部分分数に分けるΣ（消える和）",o,r"<p>$\dfrac1{k(k+d)}=\dfrac1d\left(\dfrac1k-\dfrac1{k+d}\right)$ と分け、$k=1,2,3,\cdots$ を書き並べて<b>消える項</b>を見つける。残るのは最初と最後の何項か。</p>","隣どうしで打ち消し合う「望遠鏡の和」。縮んだ後に残る端だけ数える。",3)
# 例題4 等差×等比
def b4(r):
    r=sp.Rational(r); S=sum(j*r**j for j in range(1,1))  # dummy
    Sn=r*(1-(n+1)*r**n+n*r**(n+1))/(1-r)**2
    assert all(sum(j*r**j for j in range(1,N+1))==Sn.subs(n,N) for N in (1,2,5,8))
    st=[("和を書き並べる",D(r"S_n=%s+2\cdot%s^2+3\cdot%s^3+\cdots+n\cdot%s^n"%(P(r),P(r),P(r),P(r)))),
        ("$%s$ 倍して1項ずらす"%L(r),D(r"%sS_n=%s^2+2\cdot%s^3+\cdots+(n-1)%s^n+n\cdot%s^{n+1}"%(P(r),P(r),P(r),P(r),P(r)))),
        ("辺々ひく","<p>"+I(r"(1-r)S_n")+" は等比数列の和と端の項だけになる。</p>"+D(r"(1-%s)S_n=%s+%s^2+\cdots+%s^n-n\cdot%s^{n+1}"%(P(r),P(r),P(r),P(r),P(r)))+D(r"%s\,S_n=\dfrac{%s\left(%s^n-1\right)}{%s-1}-n\cdot%s^{n+1}"%(L(1-r),P(r),P(r),P(r),P(r)))),
        ("$S_n$ を求める",D(r"S_n=%s"%L(sp.simplify(Sn))))]
    return r"次の和 $S_n$ を求めよ。 $$S_n=\sum_{k=1}^{n}k\cdot%s^{k}$$"%P(r),st,r"S_n=%s"%L(sp.simplify(Sn))
V=[2,3,-2,sp.Rational(1,2),4]
o=[b4(v) for v in V]
build(Z,CH,"（等差）×（等比）の和",o,r"<p>$S_n=\sum k\,r^k$ のように<b>等差×等比</b>の和は、$S_n$ と $rS_n$ を<b>1項ずらして引く</b>。$(1-r)S_n$ が等比数列の和になる。</p>","公比をかけて1つずらして引くと、係数の「$k$」が消えて等比数列だけが残る。",4)
# 例題5 S_n から a_n
def b5(p,q,c):
    Sn=p*n**2+q*n+c; a1=Sn.subs(n,1); an=sp.expand(Sn-Sn.subs(n,n-1)); same=(an.subs(n,1)==a1)
    st=[("$a_1$ を求める","<p>"+I(r"a_1=S_1")+"。</p>"+D(r"a_1=%s"%L(a1))),
        ("$n\\geqq2$ のとき","<p>"+I(r"a_n=S_n-S_{n-1}")+"。</p>"+D(r"a_n=\left(%s\right)-\left\{%s\right\}=%s"%(L(Sn),L(sp.expand(Sn.subs(n,n-1))),L(an)))),
        ("$n=1$ を確かめる","<p>"+I(r"%s"%L(an))+" に $n=1$ を代入すると "+I(L(an.subs(n,1)))+"。"+("$a_1$ と一致するので $n=1$ でも成り立つ。" if same else "<b>$a_1=%s$ と一致しない</b>ので、$a_1$ は別に書く。"%L(a1))+"</p>")]
    ans=("a_n=%s"%L(an)) if same else (r"a_1=%s,\ \ n\geqq2\ \text{のとき}\ a_n=%s"%(L(a1),L(an)))
    return r"数列 $\{a_n\}$ の初項から第 $n$ 項までの和 $S_n$ が $S_n=%s$ で表されるとき、一般項 $a_n$ を求めよ。"%L(Sn),st,ans
V=[(1,2,0),(3,-1,0),(2,1,1),(1,0,-2),(2,-3,2)]
o=[b5(*v) for v in V]
build(Z,CH,"和Snから一般項を求める",o,r"<p>$a_1=S_1$、$n\geqq2$ で $a_n=S_n-S_{n-1}$。最後に<b>$n\geqq2$ の式が $n=1$ でも成り立つか</b>を確かめる（成り立たなければ場合分けして答える）。</p>","$n$ 番目までの合計から $n-1$ 番目までの合計を引くと、$n$ 番目だけが残る。",5)
UNIT=finish(Z,CH,0,1,"数列","和の記号Σ","Σの公式、階差数列、部分分数、等差×等比、S_nと一般項まで、Σの総合力を問う難問に挑みます。",subject="B")
