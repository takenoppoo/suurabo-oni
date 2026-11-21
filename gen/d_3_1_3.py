# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational; xx=sp.Symbol('x',real=True); _c=[0]
def lm(e,a): return sp.limit(e,xx,a)
# 例題1 因数分解型
def b1(a,p,q,r_):
    num=sp.expand((xx-a)*(p*xx+q)); den=sp.expand((xx-a)*(xx+r_)); ans=R(p*a+q,a+r_); assert lm(num/den,a)==ans
    st=[("0/0 の不定形","<p>"+I(r"x\to%s"%L(a))+" で分母・分子とも 0。共通因数 "+I(r"x-%s"%L(a) if a>=0 else r"x+%s"%L(-a))+" をくくり出す。</p>"),
        ("約分する",D(r"\dfrac{%s}{%s}=\dfrac{(%s)(%s)}{(%s)(%s)}=\dfrac{%s}{%s}\quad(x\neq%s)"%(L(num),L(den),L(xx-a),L(p*xx+q),L(xx-a),L(xx+r_),L(p*xx+q),L(xx+r_),L(a)))),
        ("代入する",D(r"\lim_{x\to%s}\dfrac{%s}{%s}=\dfrac{%s}{%s}=%s"%(L(a),L(p*xx+q),L(xx+r_),L(p*a+q),L(a+r_),L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{x\to%s}\dfrac{%s}{%s}$$"%(L(a),L(num),L(den)),st,L(ans)
V=[(2,3,1,1),(3,2,-1,2),(1,4,3,2),(-1,5,2,3),(4,1,2,-1)]
o=[b1(*v) for v in V]
build(Z,CH,"0/0 の不定形（約分）",o,r"<p>$x\to a$ で $\dfrac00$ の形は、分母・分子に共通因数 $(x-a)$ がある。<b>因数分解して約分</b>してから $x=a$ を代入する。</p>","行き止まり（0÷0）の原因は共通の因数。取り除けば道が開ける。",1)
# 例題2 有理化
def b2(a,k):
    # (sqrt(x+k)-s)/(x-a), s=sqrt(a+k)
    s=sp.sqrt(a+k); e=(sp.sqrt(xx+k)-s)/(xx-a); ans=1/(2*s); assert sp.simplify(lm(e,a)-ans)==0
    st=[("0/0 の不定形","<p>"+I(r"x\to%d"%a)+" で分母・分子とも 0。分子を有理化する。</p>"),
        ("分子を有理化",D(r"\dfrac{\sqrt{x+%d}-%s}{x-%d}\cdot\dfrac{\sqrt{x+%d}+%s}{\sqrt{x+%d}+%s}=\dfrac{(x+%d)-%d}{(x-%d)(\sqrt{x+%d}+%s)}=\dfrac{1}{\sqrt{x+%d}+%s}"%(k,L(s),a,k,L(s),k,L(s),k,a+k,a,k,L(s),k,L(s)))),
        ("代入する",D(r"\lim_{x\to%d}\dfrac1{\sqrt{x+%d}+%s}=\dfrac1{%s+%s}=%s"%(a,k,L(s),L(s),L(s),L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{x\to%d}\dfrac{\sqrt{x+%d}-%s}{x-%d}$$"%(a,k,L(s),a),st,L(ans)
V=[(2,2),(3,1),(5,4),(1,3),(6,3)]
o=[b2(*v) for v in V]
build(Z,CH,"根号を含む 0/0 型（有理化）",o,r"<p>根号を含む $\dfrac00$ 型は、<b>根号のある側を有理化</b>して分子の $(x-a)$ を作り、約分する。</p>","根号が邪魔なときは、共役な式をかけて消す。",2)
# 例題3 x→∞
def b3(p,q,r_,s):
    e=(sp.sqrt(p*xx**2+q*xx)-sp.sqrt(p*xx**2+r_*xx)); a=R(q-r_,2)/sp.sqrt(p); ans=sp.simplify(a); assert abs(float(e.subs(xx,10**8))-float(ans))<1e-3
    sq=sp.sqrt(p)
    st=[("$\\infty-\\infty$ の形","<p>有理化する。</p>"),
        ("有理化",D(r"\sqrt{%s}-\sqrt{%s}=\dfrac{%s}{\sqrt{%s}+\sqrt{%s}}"%(L(p*xx**2+q*xx),L(p*xx**2+r_*xx),L((q-r_)*xx),L(p*xx**2+q*xx),L(p*xx**2+r_*xx)))),
        ("$x$ でわって $x\\to\\infty$",D(r"=\dfrac{%s}{\sqrt{%s+\frac{%s}{x}}+\sqrt{%s+\frac{%s}{x}}}\to\dfrac{%s}{2%s}=%s"%(L(q-r_),L(p),L(q),L(p),L(r_),L(q-r_),L(sq) if p!=1 else "",L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{x\to\infty}\left(\sqrt{%s}-\sqrt{%s}\right)$$"%(L(p*xx**2+q*xx),L(p*xx**2+r_*xx)),st,L(ans)
V=[(1,6,2,0),(4,8,0,0),(1,3,-1,0),(9,6,-6,0),(1,5,1,0)]
o=[b3(*v) for v in V]
build(Z,CH,"$x\\to\\infty$ の無理式の極限",o,r"<p>$\sqrt A-\sqrt B$ 型は有理化し、分母・分子を $x$ でわる（$x>0$ のとき $\sqrt{x^2}=x$）。</p>","大きい項どうしの引き算は、差を和でわる形にして安定させる。",3)
# 例題4 三角関数
def b4(a,b):
    ans=R(a,b); assert lm(sp.sin(a*xx)/(b*xx),0)==ans
    st=[("公式を使う形にする","<p>"+I(r"\lim_{\theta\to0}\dfrac{\sin\theta}{\theta}=1")+"。"+I(r"\sin %sx"%L(a))+" の中身 "+I(r"%sx"%L(a))+" を分母にそろえる。</p>"),
        ("変形",D(r"\dfrac{\sin %sx}{%sx}=\dfrac{\sin %sx}{%sx}\cdot\dfrac{%s}{%s}"%(L(a),L(b),L(a),L(a),L(a),L(b)))),
        ("極限",D(r"\lim_{x\to0}\dfrac{\sin %sx}{%sx}=1\cdot\dfrac{%s}{%s}=%s"%(L(a),L(a),L(a),L(b),L(ans))))]
    return r"次の極限値を求めよ。 $$\lim_{x\to0}\dfrac{\sin %sx}{%sx}$$"%(L(a),L(b)),st,L(ans)
V=[(3,2),(5,4),(7,3),(2,5),(4,9)]
o=[b4(*v) for v in V]
build(Z,CH,"三角関数の極限",o,r"<p>$\displaystyle\lim_{\theta\to0}\dfrac{\sin\theta}{\theta}=1$。$\sin kx$ なら分母を $kx$ にそろえる。</p>","同じ中身をそろえれば、$\\frac{\\sin\\theta}{\\theta}\\to1$ が使える。",4)
# 例題5 連続
def b5(a,c):
    m=sp.Symbol('m')
    # f(x)=(x^2-a^2)/(x-a) (x≠a), m (x=a) 連続 ⇒ m=2a ; use shape (x^2+bx+c)/(x-a)
    k=a+c
    num=sp.expand((xx-a)*(xx+k)); b=num.coeff(xx,1); cc=num.coeff(xx,0); val=a+k
    assert lm(num/(xx-a),a)==val
    st=[("連続の条件","<p>"+I(r"x=%s"%L(a))+" で連続 "+I(r"\iff \lim_{x\to%s}f(x)=f(%s)"%(L(a),L(a)))+"。</p>"),
        ("極限値",D(r"\lim_{x\to%s}\dfrac{%s}{x-%s}=\lim_{x\to%s}\dfrac{(x-%s)(x+%s)}{x-%s}=\lim_{x\to%s}(x+%s)=%s"%(L(a),L(num),L(a),L(a),L(a),L(k),L(a),L(a),L(k),L(val)))),
        ("定数を決める","<p>"+I(r"f(%s)=m"%L(a))+" なので</p>"+D(r"m=%s"%L(val)))]
    return r"関数 $f(x)=\begin{cases}\dfrac{%s}{x-%s}&(x\neq %s)\\[2mm] m&(x=%s)\end{cases}$ が $x=%s$ で連続となるように、定数 $m$ の値を定めよ。"%(L(num),L(a),L(a),L(a),L(a)),st,r"m=%s"%L(val)
V=[(2,3),(3,1),(1,5),(4,2),(-1,3)]
o=[b5(*v) for v in V]
build(Z,CH,"連続となる定数の決定",o,r"<p>$x=a$ で連続 $\iff \lim_{x\to a}f(x)=f(a)$。左辺は約分して求め、$f(a)$ と等しいとおく。</p>","グラフがつながる＝穴の高さにぴったり値を置く。",5)
UNIT=finish(Z,CH,0,2,"極限","関数の極限・連続","0/0型、有理化、三角関数の極限、連続の条件まで、関数の極限の難問に挑みます。",subject="3")
