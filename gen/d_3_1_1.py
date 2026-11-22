# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational; n=sp.Symbol('n',positive=True)
def lim(a): return r"\lim_{n\to\infty}"
# 例題1 分数式の極限
def b1(p,q,r_,s,t,u):
    num=p*n**2+q*n+r_; den=s*n**2+t*n+u; ans=R(p,s); assert abs(float((num/den).subs(n,10**7))-float(ans))<1e-5
    st=[("最高次の項でわる","<p>分母の最高次は "+I("n^2")+"。分母・分子を "+I("n^2")+" でわる。</p>"+D(r"\dfrac{%s}{%s}=\dfrac{%s}{%s}"%(L(num),L(den),L(sp.expand(num/n**2)),L(sp.expand(den/n**2))))),
        ("$\\dfrac1n,\\ \\dfrac1{n^2}\\to0$ を使う","<p>"+I(r"\lim_{n\to\infty}\dfrac1n=0,\ \ \lim_{n\to\infty}\dfrac1{n^2}=0")+"。</p>"+D(r"\lim_{n\to\infty}\dfrac{%s}{%s}=\dfrac{%s+0+0}{%s+0+0}=%s"%(L(sp.expand(num/n**2)),L(sp.expand(den/n**2)),L(p),L(s),L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{n\to\infty}\dfrac{%s}{%s}$$"%(L(num),L(den)),st,L(ans)
V=[(3,2,1,2,-1,5),(5,-3,2,4,1,1),(2,7,-1,6,3,2),(7,1,0,3,-2,4),(4,-5,6,8,0,1)]
o=[b1(*v) for v in V]
build(Z,CH,"分数式の極限（最高次でわる）",o,r"<p>分母・分子を<b>分母の最高次の項</b>でわる。$\dfrac1n,\ \dfrac1{n^2},\cdots\to0$ を使う。$\dfrac{\infty}{\infty}$ のまま判断しない。</p>","一番強い項（最高次）だけが、$n$ が大きいときの勝負を決める。",1)
# 例題2 有理化
def IN(p,q):
    return "1"+("" if p==0 else r"%s\dfrac{%s}{n}"%("+" if p>0 else "-",L(abs(p))))+("" if q==0 else r"%s\dfrac{%s}{n^2}"%("+" if q>0 else "-",L(abs(q))))
def b2(p,q,r_,s):
    e=sp.sqrt(n**2+p*n+q)-sp.sqrt(n**2+r_*n+s); ans=R(p-r_,2); assert abs(float(e.subs(n,10**7))-float(ans))<1e-5
    st=[("$\\infty-\\infty$ の形","<p>そのままでは不定形。<b>分子の有理化</b>をする。</p>"),
        ("有理化する",D(r"\sqrt{%s}-\sqrt{%s}=\dfrac{(%s)-(%s)}{\sqrt{%s}+\sqrt{%s}}=\dfrac{%s}{\sqrt{%s}+\sqrt{%s}}"%(L(n**2+p*n+q),L(n**2+r_*n+s),L(n**2+p*n+q),L(n**2+r_*n+s),L(n**2+p*n+q),L(n**2+r_*n+s),L(sp.expand((p-r_)*n+q-s)),L(n**2+p*n+q),L(n**2+r_*n+s)))),
        ("根号の中から $n$ をくくり出す","<p>"+I(r"n>0")+" なので "+I(r"\sqrt{n^2}=n")+"。</p>"+D(r"\sqrt{%s}=n\sqrt{%s},\qquad \sqrt{%s}=n\sqrt{%s}"%(L(n**2+p*n+q),IN(p,q),L(n**2+r_*n+s),IN(r_,s)))+"<p>分母・分子を "+I("n")+" でわる。</p>"),
        ("$n$ でわる",D(r"=\dfrac{%s}{\sqrt{%s}+\sqrt{%s}}"%(L(sp.expand(((p-r_)*n+q-s)/n)),IN(p,q),IN(r_,s)))),
        ("極限を求める","<p>"+I(r"\dfrac1n\to0,\ \dfrac1{n^2}\to0")+" だから、</p>"+D(r"\to\dfrac{%s}{\sqrt1+\sqrt1}=\dfrac{%s}{2}=%s"%(L(p-r_),L(p-r_),L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{n\to\infty}\left(\sqrt{%s}-\sqrt{%s}\right)$$"%(L(n**2+p*n+q),L(n**2+r_*n+s)),st,L(ans)
V=[(4,1,0,2),(6,0,2,3),(5,2,1,1),(8,3,2,0),(3,1,-1,2)]
o=[b2(*v) for v in V]
build(Z,CH,"無理式の極限（有理化）",o,r"<p>$\sqrt{A}-\sqrt{B}$ の形（$\infty-\infty$）は <b>$\dfrac{A-B}{\sqrt A+\sqrt B}$ に有理化</b>してから、分母・分子を $n$ でわる。</p>","引き算で大きさが消える形は、「差を和でわる」形に変えて安定させる。",2)
# 例題3 等比型
def b3(A,B,p,q,r_,s):
    e=lambda N: (p*A**N+q*B**N)/(r_*A**N+s*B**N); big=A if A>B else B; ans=R(p,r_) if A>B else R(q,s)
    assert abs(float(e(200))-float(ans))<1e-9
    sm=B if A>B else A
    st=[("底の大きい方でわる","<p>底が大きい "+I("%d^n"%big)+" で分母・分子をわる。</p>"+D(r"\dfrac{%s\cdot%d^n+%s\cdot%d^n}{%s\cdot%d^n+%s\cdot%d^n}=\dfrac{%s}{%s}"%(L(p),A,L(q),B,L(r_),A,L(s),B,r"%s+%s\left(\dfrac{%d}{%d}\right)^n"%(L(p),L(q),B,A) if A>B else r"%s\left(\dfrac{%d}{%d}\right)^n+%s"%(L(p),A,B,L(q)),r"%s+%s\left(\dfrac{%d}{%d}\right)^n"%(L(r_),L(s),B,A) if A>B else r"%s\left(\dfrac{%d}{%d}\right)^n+%s"%(L(r_),A,B,L(s))))),
        ("$|r|<1$ なら $r^n\\to0$","<p>"+I(r"\left(\dfrac{%d}{%d}\right)^n\to0"%((sm,big)))+"。</p>"+D(r"\to\dfrac{%s}{%s}=%s"%(L(p if A>B else q),L(r_ if A>B else s),L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{n\to\infty}\dfrac{%s\cdot%d^n+%s\cdot%d^n}{%s\cdot%d^n+%s\cdot%d^n}$$"%(L(p),A,L(q),B,L(r_),A,L(s),B),st,L(ans)
V=[(3,2,2,5,1,4),(2,5,3,1,2,7),(4,3,1,6,2,5),(2,7,5,3,4,1),(5,3,3,2,1,6)]
o=[b3(*v) for v in V]
build(Z,CH,"$r^n$ を含む極限",o,r"<p>$|r|<1$ なら $r^n\to0$、$|r|>1$ なら発散。<b>底の最も大きい項でわって</b>、$\left(\dfrac{\text{小}}{\text{大}}\right)^n\to0$ を使う。</p>","指数の世界では、底が一番大きい項がほぼ全部。他は無視できるほど小さい。",3)
# 例題4 漸化式
def b4(p,q,a1):
    al=R(q)/(1-p); an=al+(a1-al)*sp.Rational(p)**(n-1)
    s=[R(a1)]
    for _ in range(10): s.append(p*s[-1]+q)
    assert all(sp.simplify(an.subs(n,i+1)-s[i])==0 for i in range(11))
    st=[("特性方程式で $\\alpha$","<p>"+I(r"\alpha=%s\alpha+%s"%(L(p),L(q)))+"。</p>"+D(r"\alpha=%s"%L(al))),
        ("一般項","<p>"+I(r"a_{n+1}-\alpha=%s(a_n-\alpha)"%L(p))+"。</p>"+D(r"a_n=%s%s\left(%s\right)^{n-1}"%(L(al),("+" if a1-al>=0 else "")+L(a1-al),L(p)))),
        ("極限","<p>"+I(r"|%s|<1"%L(p))+" なので "+I(r"\left(%s\right)^{n-1}\to0"%L(p))+"。</p>"+D(r"\lim_{n\to\infty}a_n=%s"%L(al)))]
    return r"$a_1=%d,\ \ a_{n+1}=%s a_n+%s$ で定められる数列 $\{a_n\}$ の一般項と、極限値 $\displaystyle\lim_{n\to\infty}a_n$ を求めよ。"%(a1,L(p),L(q)),st,r"a_n=%s+%s\left(%s\right)^{n-1},\ \ \lim a_n=%s"%(L(al),L(a1-al),L(p),L(al))
V=[(R(1,2),3,2),(R(1,3),4,1),(R(-1,2),3,0),(R(2,3),2,1),(R(3,4),1,2)]
o=[b4(*v) for v in V]
build(Z,CH,"漸化式で定まる数列の極限",o,r"<p>$a_{n+1}=pa_n+q$ は $\alpha=\dfrac q{1-p}$ を使って $a_n=\alpha+(a_1-\alpha)p^{n-1}$。<b>$|p|<1$ なら $a_n\to\alpha$</b>。（極限値 $\alpha$ は $\alpha=p\alpha+q$ の解でもある。）</p>","行き着く先（$\\alpha$）は、これ以上動かない値。そこへ公比 $p$ の速さで近づく。",4)
# 例題5 はさみうち
def b5(p,q,r_,s,fn):
    f={'sin':sp.sin,'cos':sp.cos}[fn]; an=(p*n+q*f(n))/(r_*n+s); ans=R(p,r_)
    assert abs(float(an.subs(n,10**7))-float(ans))<1e-5
    st=[("有界な項を不等式ではさむ","<p>"+I(r"-1\leqq\%s n\leqq1"%fn)+"。$n>0$、"+I(r"%s n+%s>0"%(L(r_),L(s)))+" なので、各辺に %s をかけて %s をたし、"%(L(q),L(p)+"n") if False else "<p>"+I(r"-1\leqq\%s n\leqq1"%fn)+" の各辺に "+I(L(q))+" をかけて "+I(L(p)+"n")+" をたし、"+I(L(r_)+"n+"+L(s))+" でわる。</p>"+D(r"\dfrac{%sn-%s}{%sn+%s}\leqq a_n\leqq\dfrac{%sn+%s}{%sn+%s}"%(L(p),L(q),L(r_),L(s),L(p),L(q),L(r_),L(s)))),
        ("両側の極限を求める","<p>両側とも "+I(r"n")+" でわって</p>"+D(r"\lim_{n\to\infty}\dfrac{%sn-%s}{%sn+%s}=\dfrac{%s}{%s}=%s,\qquad \lim_{n\to\infty}\dfrac{%sn+%s}{%sn+%s}=%s"%(L(p),L(q),L(r_),L(s),L(p),L(r_),L(ans),L(p),L(q),L(r_),L(s),L(ans)))),
        ("はさみうちの原理","<p>両側の極限が一致するので</p>"+D(r"\lim_{n\to\infty}a_n=%s"%L(ans)))]
    return r"数列 $a_n=\dfrac{%sn+%s\%s n}{%sn+%s}$ の極限値を求めよ。"%(L(p),L(q),fn,L(r_),L(s)),st,L(ans)
V=[(3,2,2,1,'sin'),(5,1,4,3,'cos'),(2,3,1,2,'sin'),(6,2,3,1,'cos'),(4,1,5,2,'sin')]
o=[b5(*v) for v in V]
build(Z,CH,"はさみうちの原理",o,r"<p>$b_n\leqq a_n\leqq c_n$ で $\lim b_n=\lim c_n=\alpha$ ならば $\lim a_n=\alpha$（<b>はさみうちの原理</b>）。$\sin n,\cos n$ は $-1$ 以上 $1$ 以下であることを使い、上下を作る。</p>","求めにくい数列を、極限が分かる2つの数列でサンドイッチする。",5)
UNIT=finish(Z,CH,0,0,"極限","数列の極限","分数式、有理化、r^n型、漸化式、はさみうちまで、数列の極限の難問に挑みます。",subject="3")
