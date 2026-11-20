# -*- coding: utf-8 -*-
# 二項定理（数学II いろいろな式）
from bh import *
from math import comb, factorial
Z=U_(); CH=[]
# ===== 例題1 特定の項の係数 =====
def b1(A,B,n_,i,j):
    expr=sp.expand((A*x+B*y)**n_); co=expr.coeff(x,i).coeff(y,j); rr=j
    val=comb(n_,rr)*A**(n_-rr)*B**rr; assert val==co and i+j==n_
    steps=[("一般項を書く","<p>"+I(P(A*x+B*y)+"^{%d}"%n_)+" の展開式の一般項は"+D(r"{}_{%d}\mathrm{C}_{r}"%n_+P(A*x)+"^{%d-r}"%n_+P(B*y)+"^{r}")+"<p>$r$ は 0 から %d までの整数。</p>"%n_),
           ("目的の項になる $r$ を決める","<p>"+I("x^{%d}y^{%d}"%(i,j))+" の "+I("y")+" の指数が "+I(str(j))+" なので "+I("r=%d"%rr)+"。（"+I("x")+" の指数は "+I("%d-%d=%d"%(n_,rr,i))+" で一致。）</p>"),
           ("係数を計算する",D(Cn(n_,rr)+P(A*x)+"^{%d}"%(n_-rr)+P(B*y)+"^{%d}"%rr+"="+str(comb(n_,rr))+r"\times"+str(A**(n_-rr))+r"\times"+str(B**rr)+"="+str(co))+"<p>よって係数は "+I(str(co))+"。</p>")]
    prob=r"$"+P(A*x+B*y)+"^{%d}$ の展開式における $x^{%d}y^{%d}$ の項の係数を求めよ。"%(n_,i,j)
    return prob,steps,str(co)
V=[(2,-3,6,4,2),(3,-1,7,3,4),(-2,5,5,2,3),(4,3,5,4,1),(5,-2,6,2,4)]
o=[b1(*v) for v in V]
build(Z,CH,"二項定理で特定の項の係数",o,
 r"<p><b>二項定理</b>：$$(a+b)^n=\sum_{r=0}^{n}{}_n\mathrm{C}_r\,a^{n-r}b^{r}$$ 一般項 ${}_n\mathrm{C}_r\,a^{n-r}b^r$ を書き、求めたい項になる $r$ を決める。係数には $a,b$ の係数も入れて計算する。</p>",
 "「n個のかっこから、b を選ぶ個数が r」。選び方の数が ${}_n\\mathrm{C}_r$ 通り。",1)
# ===== 例題2 定数項・指定の次数 =====
def b2(A,e1,B,e2,n_,T):
    base=A*x**e1+B*x**e2; expr=sp.expand(base**n_); co=expr.coeff(x,T)
    rr=sp.symbols('r'); sol=sp.solve(sp.Eq(e1*(n_-rr)+e2*rr,T),rr); assert len(sol)==1 and sol[0]==int(sol[0]) and 0<=sol[0]<=n_
    rv=int(sol[0]); val=comb(n_,rv)*A**(n_-rv)*B**rv; assert val==co
    steps=[("一般項を書く",D(r"{}_{%d}\mathrm{C}_{r}"%n_+P(A*x**e1)+"^{%d-r}"%n_+P(B*x**e2)+"^{r}="+r"{}_{%d}\mathrm{C}_{r}\cdot %d^{%d-r}\cdot (%d)^{r}\cdot x^{%d(%d-r)+(%d)r}"%(n_,A,n_,B,e1,n_,e2))),
           ("$x$ の指数を整理して、条件の式を作る",D(r"%d(%d-r)+(%d)\cdot r="%(e1,n_,e2)+L(sp.expand(e1*n_+(e2-e1)*rr)))+"<p>これが "+I(str(T))+" に等しいので</p>"+D(L(sp.expand(e1*n_+(e2-e1)*rr))+"="+str(T)+r"\ \Rightarrow\ r="+str(rv))),
           ("係数を計算する",D(Cn(n_,rv)+r"\cdot %d^{%d}\cdot(%d)^{%d}="%(A,n_-rv,B,rv)+str(comb(n_,rv))+r"\times"+str(A**(n_-rv))+r"\times"+(str(B**rv) if B**rv>=0 else "("+str(B**rv)+")")+"="+str(co)))]
    tgt="定数項" if T==0 else "$x^{%d}$ の項の係数"%T
    prob=r"$"+P(base)+"^{%d}$ の展開式における"%n_+tgt+"を求めよ。"
    return prob,steps,str(co)
V=[(1,2,2,-1,9,0),(1,3,-1,-1,8,4),(2,1,3,-2,6,0),(1,2,-2,-1,10,5),(3,2,1,-1,7,2)]
# 条件確認
for v in V: b2(*v)
o=[b2(*v) for v in V]
build(Z,CH,"定数項・指定した次数の項の係数",o,
 r"<p>$x$ の指数が複雑な式では、一般項の <b>$x$ の指数だけ</b>を先に整理して、目的の指数と等しいとおき $r$ を求める。$$x^{e_1(n-r)+e_2 r}=x^{T}$$ 定数項は $T=0$ の場合。</p>",
 "まず「$x$ が何乗になるか」だけを見る。係数は $r$ が決まってから計算すればよい。",2)
# ===== 例題3 三項の展開 =====
def b3(al,be,n_,kk):
    base=x**2+al*x+be; expr=sp.expand(base**n_); co=expr.coeff(x,kk)
    cases=[(i,j,l) for i in range(n_+1) for j in range(n_+1) for l in range(n_+1) if i+j+l==n_ and 2*i+j==kk]
    tot=0; lines=[]
    for i,j,l in cases:
        v=factorial(n_)//(factorial(i)*factorial(j)*factorial(l))*al**j*be**l; tot+=v
        lines.append(r"(i,j,l)=(%d,%d,%d)"%(i,j,l)+r":\ \dfrac{%d!}{%d!\,%d!\,%d!}\cdot 1^{%d}(%d)^{%d}(%d)^{%d}=%d"%(n_,i,j,l,i,al,j,be,l,v))
    assert tot==co
    steps=[("一般項（多項定理）を書く","<p>"+I("x^2")+" を "+I("i")+" 個、"+I("%dx"%al if al!=1 else "x")+" を "+I("j")+" 個、"+I(str(be))+" を "+I("l")+" 個とる（"+I("i+j+l=%d"%n_)+"）。係数は</p>"+D(r"\dfrac{%d!}{i!\,j!\,l!}\,(x^2)^i(%dx)^j(%d)^l"%(n_,al,be))),
           ("$x^{%d}$ になる組 $(i,j,l)$ を数え上げる"%kk,"<p>"+I("x")+" の指数："+I("2i+j=%d"%kk)+"、個数："+I("i+j+l=%d"%n_)+" を同時に満たす非負整数の組は</p>"+D(r",\ ".join("("+str(c_[0])+","+str(c_[1])+","+str(c_[2])+")" for c_ in cases))),
           ("各組の係数を計算する",D(r"\begin{aligned}"+r"\\ ".join(lines)+r"\end{aligned}")),
           ("合計する",D("+".join(str(factorial(n_)//(factorial(i)*factorial(j)*factorial(l))*al**j*be**l) if (factorial(n_)//(factorial(i)*factorial(j)*factorial(l))*al**j*be**l)>=0 else "("+str(factorial(n_)//(factorial(i)*factorial(j)*factorial(l))*al**j*be**l)+")" for i,j,l in cases)+"="+str(co)))]
    prob=r"$"+P(base)+"^{%d}$ の展開式における $x^{%d}$ の項の係数を求めよ。"%(n_,kk)
    return prob,steps,str(co)
V=[(1,1,5,4),(2,-1,4,3),(-1,2,5,5),(1,-2,4,4),(3,1,4,2)]
o=[b3(*v) for v in V]
build(Z,CH,"3つの項をもつ式の展開",o,
 r"<p>項が3つのときは、<b>多項定理</b>の考え方で「どの項を何個ずつとるか」を数える。$a^i b^j c^l$ の係数は $\dfrac{n!}{i!\,j!\,l!}$（$i+j+l=n$）。</p>",
 "3種類のカードを n 枚並べる並べ方の数。同じカードどうしは区別しないので、階乗で割る。",3)
# ===== 例題4 二項係数の和 =====
def b4(n_,cc,evenn):
    s1=sum(cc**r_*comb(n_,r_) for r_ in range(n_+1)); assert s1==(1+cc)**n_
    s2=sum(comb(n_,r_) for r_ in range(0,n_+1,2)); assert s2==2**(n_-1)
    terms="+".join((Cn(n_,r_) if cc**r_==1 else str(cc**r_)+Cn(n_,r_)) for r_ in range(0,3))+r"+\cdots+"+str(cc**n_)+Cn(n_,n_)
    ev="+".join(Cn(n_,r_) for r_ in range(0,n_+1,2))
    steps=[("二項定理に $a=1,\\ b=%d$ を代入する"%cc,"<p>$(1+x)^n=\\sum_{r}{}_n\\mathrm{C}_r x^r$ に $x=%d$ を入れる。</p>"%cc+D(r"(1+%d)^{%d}=\sum_{r=0}^{%d}%d^{r}\,{}_{%d}\mathrm{C}_{r}"%(cc,n_,n_,cc,n_))),
           ("(1) の値",D(terms+"=%d^{%d}=%d"%(1+cc,n_,s1))),
           ("(2) $x=1$ と $x=-1$ を代入して差・和を作る","<p>"+I("(1+1)^{%d}=C_0+C_1+C_2+\\cdots+C_{%d}"%(n_,n_))+"、"+I("(1-1)^{%d}=C_0-C_1+C_2-\\cdots-C_{%d}=0"%(n_,n_))+"。2式を足すと、偶数番目の和の2倍：</p>"+D(r"2\,(C_0+C_2+C_4+\cdots)=2^{%d}\ \Rightarrow\ C_0+C_2+C_4+\cdots=2^{%d}=%d"%(n_,n_-1,s2)))]
    prob=r"$n=%d$ とする。(1) $"%n_+terms+r"$ の値を求めよ。(2) $"+ev+r"$ の値を求めよ。"
    return prob,steps,r"\text{(1) }%d,\quad \text{(2) }%d"%(s1,s2)
V=[(8,2,0),(9,3,0),(10,4,0),(6,5,0),(7,2,0)]
o=[b4(*v) for v in V]
build(Z,CH,"二項係数の和",o,
 r"<p>$(1+x)^n=\sum_{r=0}^{n}{}_n\mathrm{C}_r x^r$ は <b>$x$ についての恒等式</b>。ここに $x=1$、$x=-1$、$x=2$ などを代入すると、二項係数の和が一気に求まる。</p>",
 "恒等式は「どんな値を入れても成り立つ魔法の箱」。うまい値を入れて、欲しい和を取り出す。",4)
# ===== 例題5 余り =====
def b5(p_,n_):
    rem=pow(p_+1,n_,p_*p_); assert rem==(1+n_*p_)%(p_*p_)
    steps=[("底を $p+1$ の形に直して二項定理を使う","<p>"+I("%d=%d+1"%(p_+1,p_))+" なので</p>"+D(r"%d^{%d}=(%d+1)^{%d}=1+{}_{%d}\mathrm{C}_{1}\cdot %d+{}_{%d}\mathrm{C}_{2}\cdot %d^2+\cdots"%(p_+1,n_,p_,n_,n_,p_,n_,p_))),
           ("$%d^2$ で割り切れる部分を見分ける"%p_,"<p>"+I("%d^2"%p_)+" 以降の項はすべて "+I("%d^2=%d"%(p_,p_*p_))+" の倍数。残るのは最初の2項：</p>"+D("1+%d\\times%d=%d"%(n_,p_,1+n_*p_))),
           ("余りを求める",D("%d=%d\\times%d+%d"%(1+n_*p_,p_*p_,(1+n_*p_)//(p_*p_),(1+n_*p_)%(p_*p_)))+"<p>よって余りは "+I(str(rem))+"。</p>")]
    prob=r"$%d^{%d}$ を $%d$ で割った余りを求めよ。"%(p_+1,n_,p_*p_)
    return prob,steps,str(rem)
V=[(7,30),(6,25),(9,20),(5,40),(8,27)]
o=[b5(*v) for v in V]
build(Z,CH,"累乗を割った余り（二項定理の利用）",o,
 r"<p>$(p+1)^n=1+np+{}_n\mathrm{C}_2\,p^2+\cdots$ と展開すると、$p^2$ 以降は <b>$p^2$ の倍数</b>。割る数が $p^2$ のとき、余りは最初の2項 $1+np$ を $p^2$ で割った余りで決まる。</p>",
 "大きな累乗は、二項定理で「割り切れる部分」と「残りカス」に分け、残りカスだけ見る。",5)
UNIT=finish(Z,CH,0,1,"いろいろな式","二項定理","二項定理による係数の決定、定数項、3項の展開、二項係数の和、累乗の余りまで、一般項の扱いを鍛える難問に挑みます。")
