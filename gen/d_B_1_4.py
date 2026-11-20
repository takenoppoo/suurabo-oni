# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
n=sp.Symbol('n'); k=sp.Symbol('k'); j=sp.Symbol('j')
R=sp.Rational
DONE=r"\text{すべての自然数 }n\text{ で成り立つ（数学的帰納法）}"
def steps_sum(t,Rn,sumtex,eqtex):
    ok1=t.subs(k,1)==Rn.subs(n,1); assert ok1
    nxt=sp.simplify(Rn.subs(n,k)+t.subs(k,k+1)-Rn.subs(n,k+1)); assert nxt==0
    return [("[1] $n=1$ のとき",D(r"\text{左辺}=%s,\quad \text{右辺}=%s"%(L(t.subs(k,1)),L(Rn.subs(n,1))))+"<p>一致するので成り立つ。</p>"),
            ("[2] $n=k$ で成り立つと仮定","<p>"+I(r"\sum_{j=1}^{k}%s=%s"%(sumtex,L(Rn.subs(n,k))))+" が成り立つと仮定する。</p>"),
            ("[3] $n=k+1$ のとき","<p>左辺に仮定を使う。</p>"+D(r"\sum_{j=1}^{k+1}%s=%s+%s"%(sumtex,L(Rn.subs(n,k)),L(t.subs(k,k+1))))+"<p>通分・因数分解して整理すると</p>"+D(r"=%s"%L(sp.factor(sp.simplify(Rn.subs(n,k+1)))))+"<p>これは右辺で "+I(r"n=k+1")+" とした式に等しい。</p>"),
            ("結論","<p>[1][2] より、すべての自然数 $n$ で成り立つ。</p>")]
# 例題1 和の等式
SUMS=[(2*k-1,n**2),(k*(k+1),n*(n+1)*(n+2)/3),(k*2**(k-1),(n-1)*2**n+1),(1/(k*(k+1)),n/(n+1)),(k**3,n**2*(n+1)**2/4)]
def b1(i):
    t,Rn=SUMS[i]; tj=t.subs(k,j); sumtex=L(tj)
    return r"次の等式が、すべての自然数 $n$ で成り立つことを数学的帰納法で証明せよ。 $$\sum_{k=1}^{n}%s=%s$$"%(L(t),L(sp.factor(Rn))),steps_sum(t,Rn,"\\left("+L(tj)+"\\right)",""),DONE
o=[b1(i) for i in range(5)]
build(Z,CH,"和の等式の証明",o,r"<p>数学的帰納法：[1] $n=1$ で成り立つ。[2] $n=k$ で成り立つと仮定して $n=k+1$ でも成り立つ。→ すべての自然数で成り立つ。和の等式では <b>(左辺の $n=k$ の和)＋(第 $k+1$ 項)</b> に仮定を代入して、右辺の $n=k+1$ の形になることを示す。</p>","ドミノ倒し。最初の1枚が倒れ（[1]）、$k$ 枚目が倒れれば次も倒れる（[2]）なら、全部倒れる。",1)
# 例題2 倍数
def b2(a):
    m=sp.Symbol('m'); ok=all((a**N-1)%(a-1)==0 for N in range(1,15))
    st=[("[1] $n=1$ のとき",D(r"%d^1-1=%d=%d\times1"%(a,a-1,a-1))+"<p>%d の倍数。</p>"%(a-1)),
        ("[2] $n=k$ で成り立つと仮定","<p>"+I(r"%d^k-1=%d\,m"%(a,a-1))+"（$m$ は整数）とおく。すなわち "+I(r"%d^k=%d\,m+1"%(a,a-1))+"。</p>"),
        ("[3] $n=k+1$ のとき",D(r"%d^{k+1}-1=%d\cdot%d^k-1=%d\left(%d\,m+1\right)-1"%(a,a,a,a,a-1))+D(r"=%d\,m\cdot%d+%d-1=%d\left(%d\,m+1\right)"%(a-1,a,a,a-1,a))+"<p>$%dm+1$ は整数だから %d の倍数。</p>"%(a,a-1)),
        ("結論","<p>[1][2] より、すべての自然数 $n$ で $%d^n-1$ は %d の倍数。</p>"%(a,a-1))]
    assert ok
    return r"すべての自然数 $n$ について、$%d^n-1$ が $%d$ の倍数であることを数学的帰納法で証明せよ。"%(a,a-1),st,DONE
V=[7,5,9,4,11]
o=[b2(v) for v in V]
build(Z,CH,"倍数であることの証明",o,r"<p>「$a^n-1$ は $a-1$ の倍数」は、<b>$n=k$ の仮定を『$=(\text{倍数})\times m$』と置く</b>。$n=k+1$ の式を、仮定の形（$a^k$ や $m$）で書き直して、倍数の形にくくり出す。</p>","仮定を文字（$m$）で置いて、次の式にそのまま代入できる形にしておく。",2)
# 例題3 不等式
def b3(h):
    base=1+h
    st=[("[1] $n=1$ のとき",D(r"\text{左辺}=%d^1=%d,\quad \text{右辺}=1+%d\times1=%d"%(base,base,h,base))+"<p>左辺 $\\geqq$ 右辺。成り立つ。</p>"),
        ("[2] $n=k$ で成り立つと仮定","<p>"+I(r"%d^k\geqq1+%dk"%(base,h))+" が成り立つと仮定する。</p>"),
        ("[3] $n=k+1$ のとき","<p>仮定の両辺に正の数 "+I(str(base))+" をかける。</p>"+D(r"%d^{k+1}=%d\cdot%d^k\geqq%d\left(1+%dk\right)=%s"%(base,base,base,base,h,L(sp.expand(base*(1+h*k)))))+"<p>右辺の差を調べる。</p>"+D(r"%s-\left\{1+%d(k+1)\right\}=%s>0"%(L(sp.expand(base*(1+h*k))),h,L(sp.expand(base*(1+h*k)-(1+h*(k+1))))))+"<p>よって "+I(r"%d^{k+1}\geqq1+%d(k+1)"%(base,h))+"。</p>"),
        ("結論","<p>[1][2] より、すべての自然数 $n$ で成り立つ。</p>")]
    assert all(base**N>=1+h*N for N in range(1,20))
    return r"すべての自然数 $n$ について、不等式 $%d^n\geqq1+%dn$ が成り立つことを数学的帰納法で証明せよ。"%(base,h),st,DONE
V=[1,2,3,4,5]
o=[b3(v) for v in V]
build(Z,CH,"不等式の証明",o,r"<p>不等式では、仮定の両辺に<b>正の数をかけて</b> $n=k+1$ の形を作り、<b>目標の式との差</b>が $0$ 以上（または正）になることを示す。</p>","目標との「差」を計算して、差が正だと分かれば、次の段も同じ不等式が成り立つ。",3)
# 例題4 一般項の推定
def b4(p):
    a1=p-1; s=[a1]
    for _ in range(4): s.append(p*s[-1]+p-1)
    assert all(s[i]==p**(i+1)-1 for i in range(5))
    st=[("初めの数項を計算する",D(r"a_1=%d,\quad a_2=%d\cdot%d+%d=%d,\quad a_3=%d\cdot%d+%d=%d"%(a1,p,a1,p-1,s[1],p,s[1],p-1,s[2]))),
        ("一般項を推定する","<p>"+I(r"%d=%d^1-1,\ \ %d=%d^2-1,\ \ %d=%d^3-1"%(s[0],p,s[1],p,s[2],p))+" より</p>"+D(r"a_n=%d^n-1\quad\cdots(*)"%p)),
        ("[1] $n=1$ のとき","<p>"+I(r"%d^1-1=%d=a_1"%(p,a1))+" で $(*)$ は成り立つ。</p>"),
        ("[2] $n=k$ で $(*)$ を仮定して $n=k+1$",D(r"a_{k+1}=%d\,a_k+%d=%d\left(%d^k-1\right)+%d=%d^{k+1}-1"%(p,p-1,p,p,p-1,p))+"<p>$n=k+1$ でも $(*)$ が成り立つ。</p>"),
        ("結論","<p>[1][2] より、すべての自然数 $n$ で $a_n=%d^n-1$。</p>"%p)]
    return r"$a_1=%d,\ \ a_{n+1}=%d a_n+%d$ で定められる数列について、一般項を推定し、それを数学的帰納法で証明せよ。"%(a1,p,p-1),st,r"a_n=%d^n-1"%p
V=[2,3,4,5,6]
o=[b4(v) for v in V]
build(Z,CH,"一般項を推定して証明する",o,r"<p>①初めの数項を計算 ②規則を見つけて $a_n$ を<b>推定</b> ③推定が正しいことを帰納法で証明。$n=k+1$ では漸化式 $a_{k+1}=\cdots a_k\cdots$ に仮定を代入する。</p>","見つけた規則は「予想」にすぎない。帰納法で証明して初めて「定理」になる。",4)
# 例題5 等差×等比の和
def b5(r):
    t=k*sp.Integer(r)**(k-1); Rn=(1-(n+1)*sp.Integer(r)**n+n*sp.Integer(r)**(n+1))/(1-r)**2
    Rs=sp.simplify(Rn)
    assert all(sum(t.subs(k,i) for i in range(1,N+1))==Rn.subs(n,N) for N in range(1,9))
    tj=t.subs(k,j)
    return r"次の等式が、すべての自然数 $n$ で成り立つことを数学的帰納法で証明せよ。 $$\sum_{k=1}^{n}k\cdot%d^{k-1}=%s$$"%(r,L(Rs)),steps_sum(t,Rs,"\\left("+L(tj)+"\\right)",""),DONE
V=[2,3,4,5,6]
o=[b5(v) for v in V]
build(Z,CH,"（等差）×（等比）の和の証明",o,r"<p>和の等式の証明。<b>(右辺の $n=k$)＋(第 $k+1$ 項)</b> が <b>(右辺の $n=k+1$)</b> と一致することを、通分して確かめる。</p>","式が長くなっても手順は同じ。仮定を代入して、目標の形になるまで整理する。",5)
UNIT=finish(Z,CH,0,3,"数列","数学的帰納法","等式・倍数・不等式・一般項の推定と、数学的帰納法の証明を型で身につける難問に挑みます。",subject="B")
