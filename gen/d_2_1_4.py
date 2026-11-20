# -*- coding: utf-8 -*-
# 複素数と2次方程式（数学II いろいろな式）
from bh import *
Z=U_(); CH=[]
I_=sp.I
# ===== 例題1 複素数の計算 =====
def b1(p_,q_,r_,s_,e_,f_,g_,h_):
    E=(p_+q_*I_)/(r_+s_*I_)+(e_+f_*I_)*(g_+h_*I_); E=sp.simplify(sp.expand(E)); re,im=sp.re(E),sp.im(E)
    d=r_**2+s_**2; n1=sp.expand((p_+q_*I_)*(r_-s_*I_)); m1=sp.expand((e_+f_*I_)*(g_+h_*I_))
    steps=[("割り算を有理化する（分母の共役複素数を掛ける）","<p>"+I(cx(r_,s_))+" の共役複素数は "+I(cx(r_,-s_))+"。分母・分子に掛ける。</p>"+D(fr("("+cx(p_,q_)+")("+cx(r_,-s_)+")","("+cx(r_,s_)+")("+cx(r_,-s_)+")"))+D(r"\text{分母}=%d^2+(%d)^2=%d"%(r_,s_,d))+D(r"\text{分子}="+sx([(p_*r_,""),(-p_*s_,"i"),(q_*r_,"i"),(-q_*s_,"i^2")])+"="+sx([(p_*r_+q_*s_,""),(q_*r_-p_*s_,"i")]))),
           ("割り算の結果",D(fr(cx(sp.re(n1),sp.im(n1)),str(d))+"="+cx(sp.re(n1)/d,sp.im(n1)/d))),
           ("掛け算を展開する",D("("+cx(e_,f_)+")("+cx(g_,h_)+")="+sx([(e_*g_,""),(e_*h_,"i"),(f_*g_,"i"),(f_*h_,"i^2")])+"="+cx(sp.re(m1),sp.im(m1)))),
           ("足し合わせる",D(cx(sp.re(n1)/d,sp.im(n1)/d)+"+("+cx(sp.re(m1),sp.im(m1))+")="+cx(re,im)))]
    prob=r"次の計算をして、$a+bi$ の形で表せ。 $$"+fr(cx(p_,q_),cx(r_,s_))+"+("+cx(e_,f_)+")("+cx(g_,h_)+")$$"
    return prob,steps,cx(re,im)
V=[(2,3,1,-2,1,-2,3,1),(3,-1,2,1,2,3,1,-1),(1,4,3,-1,-1,2,2,3),(5,2,1,1,3,-1,2,2),(4,-3,2,-1,1,1,-2,3)]
o=[b1(*v) for v in V]
build(Z,CH,"複素数の計算",o,
 r"<p>$i^2=-1$。掛け算は展開して $i^2$ を $-1$ に置きかえる。割り算は<b>分母の共役複素数</b>を分母・分子に掛けて実数にする。$$(a+bi)(a-bi)=a^2+b^2$$</p>",
 "分母に $i$ が残るのは「分母にルートが残る」のと同じ。共役を掛けて $i$ を消す。",1)
# ===== 例題2 判別式 =====
def b2(r1,r2):
    k_=sp.symbols('k'); eq=x**2-2*k_*x+(r1+r2)*k_-r1*r2; D4=sp.expand(k_**2-((r1+r2)*k_-r1*r2)); assert sp.expand(D4-(k_-r1)*(k_-r2))==0
    s,l=sorted([r1,r2])
    steps=[("判別式を作る","<p>"+I(r"ax^2+2b'x+c=0")+" の判別式は "+I("D/4=b'^2-ac")+"。ここでは "+I("b'=-k")+"。</p>"+D(r"\dfrac D4=(-k)^2-1\cdot"+P((r1+r2)*k_-r1*r2)+"="+L(D4)+"="+P(k_-s)+P(k_-l))),
           ("(1) 異なる2つの実数解 $\\iff D>0$",D(P(k_-s)+P(k_-l)+r">0\ \Rightarrow\ k<%d,\ %d<k"%(s,l))),
           ("(2) 異なる2つの虚数解 $\\iff D<0$",D(P(k_-s)+P(k_-l)+r"<0\ \Rightarrow\ %d<k<%d"%(s,l))),
           ("(3) 重解 $\\iff D=0$",D(P(k_-s)+P(k_-l)+r"=0\ \Rightarrow\ k=%d,\ %d"%(s,l)))]
    prob=r"$x$ の2次方程式 $"+L(eq)+r"=0$ について、次の条件を満たす実数 $k$ の値の範囲（(3) は値）を求めよ。(1) 異なる2つの実数解をもつ (2) 異なる2つの虚数解をもつ (3) 重解をもつ"
    return prob,steps,r"\text{(1) }k<%d,\ %d<k\quad \text{(2) }%d<k<%d\quad \text{(3) }k=%d,\ %d"%(s,l,s,l,s,l)
V=[(-1,4),(1,3),(-3,2),(-2,5),(0,6)]
o=[b2(*v) for v in V]
build(Z,CH,"判別式と解の種類",o,
 r"<p>実数係数の2次方程式 $ax^2+bx+c=0$ の<b>判別式</b> $D=b^2-4ac$ で解の種類が決まる。$$D>0:\text{異なる2つの実数解},\quad D=0:\text{重解},\quad D<0:\text{異なる2つの虚数解}$$ $x$ の係数が偶数のときは $D/4=b'^2-ac$ が楽。</p>",
 "判別式は「ルートの中身」。正なら2本、0なら1本、負なら実数の世界には解がいない（虚数解）。",2)
# ===== 例題3 解と係数の関係（対称式） =====
def b3(A,B,C):
    al,be=sp.symbols('alpha beta'); s=R(-B,A); pr=R(C,A)
    v1=s**2-2*pr; v2=s**3-3*pr*s; v3=s/pr; assert sp.simplify(v3-(s/pr))==0
    steps=[("解と係数の関係","<p>"+I("%s x^2%+dx%+d=0"%(A if A!=1 else "",B,C))+" の2解を "+I(r"\alpha,\beta")+" とすると</p>"+D(r"\alpha+\beta=-\dfrac{%d}{%d}=%s,\qquad \alpha\beta=\dfrac{%d}{%d}=%s"%(B,A,L(s),C,A,L(pr)))),
           ("$\\alpha^2+\\beta^2$",D(r"\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=%s^2-2\cdot%s=%s"%("("+L(s)+")",L(pr) if pr>=0 else "("+L(pr)+")",L(v1)))),
           ("$\\alpha^3+\\beta^3$",D(r"\alpha^3+\beta^3=(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)=%s^3-3\cdot%s\cdot%s=%s"%("("+L(s)+")","("+L(pr)+")","("+L(s)+")",L(v2)))),
           ("$\\dfrac1\\alpha+\\dfrac1\\beta$",D(r"\dfrac1\alpha+\dfrac1\beta=\dfrac{\alpha+\beta}{\alpha\beta}=%s\div%s=%s"%(L(s),"("+L(pr)+")",L(v3))))]
    eq=sp.expand(A*x**2+B*x+C)
    prob=r"2次方程式 $"+L(eq)+r"=0$ の2つの解を $\alpha,\ \beta$ とするとき、次の値を求めよ。 $$\alpha^2+\beta^2,\qquad \alpha^3+\beta^3,\qquad \dfrac1\alpha+\dfrac1\beta$$"
    return prob,steps,r"\alpha^2+\beta^2=%s,\quad \alpha^3+\beta^3=%s,\quad \dfrac1\alpha+\dfrac1\beta=%s"%(L(v1),L(v2),L(v3))
V=[(2,-6,3),(1,4,-2),(3,5,-6),(2,-3,-4),(4,8,3)]
o=[b3(*v) for v in V]
build(Z,CH,"解と係数の関係と対称式の値",o,
 r"<p>$ax^2+bx+c=0$ の2解を $\alpha,\beta$ とすると $$\alpha+\beta=-\dfrac ba,\qquad \alpha\beta=\dfrac ca$$ 対称式は和と積で表す：$\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta$、$\alpha^3+\beta^3=(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)$。</p>",
 "解そのものを求めなくても、和と積さえ分かれば、対称式は全部決まる。",3)
# ===== 例題4 2解の比 =====
def b4(s,m_,n_):
    t_=sp.Rational(s,m_+n_); assert t_.q==1; al=m_*t_; be=n_*t_; kk=al*be
    steps=[("2解を文字でおく","<p>2解の比が "+I("%d:%d"%(m_,n_))+" なので "+I(r"\alpha=%dt,\ \beta=%dt"%(m_,n_))+"（"+I(r"t\ne0")+"）とおく。</p>"),
           ("解と係数の関係を使う",D(r"\alpha+\beta=%dt+%dt=%dt=%d\ \Rightarrow\ t=%d"%(m_,n_,m_+n_,s,t_))+D(r"k=\alpha\beta=%dt\cdot%dt=%dt^2=%d\cdot%d=%d"%(m_,n_,m_*n_,m_*n_,t_**2,kk))),
           ("確かめ",D(r"x^2-%dx+%d=(x-%d)(x-%d)"%(s,kk,al,be))+"<p>解は "+I("%d,\\ %d"%(al,be))+"で、比は "+I("%d:%d"%(m_,n_))+"。</p>")]
    prob=r"$x$ の2次方程式 $x^2-%dx+k=0$ の2つの解の比が $%d:%d$ であるとき、定数 $k$ の値と2つの解を求めよ。"%(s,m_,n_)
    return prob,steps,r"k=%d,\quad \text{解 }%d,\ %d"%(kk,al,be)
V=[(12,3,1),(10,3,2),(14,4,3),(18,5,1),(21,4,3)]
o=[b4(*v) for v in V]
build(Z,CH,"2解の関係から定数を決める",o,
 r"<p>2解の関係（比・差・和・積）が与えられたら、2解を文字でおいて<b>解と係数の関係</b>の2式に代入する。比 $m:n$ なら $\alpha=mt,\ \beta=nt$ とおくと文字が1つにまとまる。</p>",
 "比が与えられたら「1個分の大きさ $t$」を決める。全体の和から $t$ が1つに決まる。",4)
# ===== 例題5 正の解・負の解の条件 =====
def b5(c):
    k_=sp.symbols('k'); eq=x**2-2*k_*x+k_+c; D4=sp.expand(k_**2-k_-c); f=sp.factor(D4); rts=sorted(sp.solve(D4,k_)); assert len(rts)==2 and all(sp.im(z)==0 for z in rts)
    r1,r2=rts; big=r2; assert big>0
    steps=[("条件を3つに分ける","<p>2つの解が<b>ともに正</b> "+I(r"\iff D\geqq0,\ \alpha+\beta>0,\ \alpha\beta>0")+"。（重解を含めて「ともに正」とする。）</p>"),
           ("判別式","<p>"+I(r"\dfrac D4=k^2-(k+%d)=%s=%s\geqq0"%(c,L(D4),L(f)))+" より "+I(r"k\leqq %d,\ %d\leqq k"%(r1,r2))+"。</p>"),
           ("和と積",D(r"\alpha+\beta=2k>0\ \Rightarrow\ k>0")+D(r"\alpha\beta=k+%d>0\ \Rightarrow\ k>-%d"%(c,c))),
           ("共通範囲をとる","<p>3つの条件の共通部分：</p>"+D(r"k\geqq %d"%r2))]
    prob=r"$x$ の2次方程式 $x^2-2kx+k+%d=0$ が、ともに正の解（重解を含む）をもつような実数 $k$ の値の範囲を求めよ。"%c
    return prob,steps,r"k\geqq %d"%r2
V=[6,2,12,20,30]
o=[b5(c) for c in V]
build(Z,CH,"2つの解がともに正となる条件",o,
 r"<p>2解 $\alpha,\beta$ がともに正：$D\geqq0$ かつ $\alpha+\beta>0$ かつ $\alpha\beta>0$。<br>異符号：$\alpha\beta<0$（このとき $D>0$ は自動的に成り立つ）。</p>",
 "実数解を持ち（$D$）、足して正、掛けて正。3つの関門を全部通る範囲が答え。",5)
k_=1
fig=nl("i21_4_nl",-4,8,[-2,0,3,6],["-2","0","3","6"],segs=[(3,None)],pts=[(3,"closed")],w=60,size=(5.6,1.2))
addfig(Z.E[4],3,fig)
UNIT=finish(Z,CH,0,3,"いろいろな式","複素数と2次方程式","複素数の計算、判別式、解と係数の関係、2解の条件、解の符号まで、2次方程式の総合力を問う難問に挑みます。")
