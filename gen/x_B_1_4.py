# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; n,k=sp.symbols("n k")
def ind_eq(term,closed,label):
    assert all(sp.summation(term,(k,1,m))==closed.subs(n,m) for m in range(1,9))
    tn1=term.subs(k,n+1); c1=closed.subs(n,n+1); step=sp.simplify(closed+tn1-c1); assert step==0
    st=[("$n=1$ のとき","<p>左辺 "+I(L(term.subs(k,1)))+"、右辺 "+I(L(closed.subs(n,1)))+"。一致。</p>"),
        ("$n=m$ で成り立つと仮定","<p>"+D(r"\sum_{k=1}^{m}%s=%s"%(L(term),L(closed.subs(n,sp.Symbol("m")))))+"</p>"),
        ("$n=m+1$ のとき","<p>両辺に "+I(L(term.subs(k,sp.Symbol("m")+1)))+" を加える。</p>"+D(r"%s+%s=%s"%(L(closed.subs(n,sp.Symbol("m"))),L(term.subs(k,sp.Symbol("m")+1)),L(sp.factor(closed.subs(n,sp.Symbol("m")+1)))))+"<p>これは "+I("n=m+1")+" の右辺に等しい。</p>"),
        ("結論","<p>数学的帰納法により、すべての自然数 "+I("n")+" で成り立つ。</p>")]
    return st
CASES=[(k*sp.factorial(k),sp.factorial(n+1)-1),(sp.Rational(1,1)/(k*(k+1)),n/(n+1)),((2*k-1)**2,n*(2*n-1)*(2*n+1)/3),(k**3,(n*(n+1)/2)**2),(k*(k+1)*(k+2),n*(n+1)*(n+2)*(n+3)/4)]
def b6(i):
    t,c=CASES[i]; st=ind_eq(t,c,"")
    return r"数学的帰納法で、すべての自然数 $n$ について $\displaystyle\sum_{k=1}^{n}%s=%s$ を証明せよ。"%(L(t),L(c)),st,r"\text{証明終}"
o=[b6(i) for i in range(5)]
build(Z,CH,"和の等式の数学的帰納法",o,"<p>① $n=1$ ② $n=m$ を仮定して $n=m+1$ を導く。「右辺(m) + 追加項 = 右辺(m+1)」を<b>因数分解で確認</b>。</p>","ドミノ倒し。最初の1枚と、隣へ倒れる仕組みを示す。",6)
# 7 倍数
def b7(a,m,c):
    # a^n - c divisible? use  5^n+? specific: (a^n + b) multiple of m
    pass
CASES7=[("4^n-1",3,lambda N:4**N-1,"4^{m+1}-1=4(4^m-1)+3"),("5^n+3",4,lambda N:5**N+3,"5^{m+1}+3=5(5^m+3)-12"),("7^n-1",6,lambda N:7**N-1,"7^{m+1}-1=7(7^m-1)+6"),("6^n+4",5,lambda N:6**N+4,"6^{m+1}+4=6(6^m+4)-20"),("9^n-1",8,lambda N:9**N-1,"9^{m+1}-1=9(9^m-1)+8")]
def b7(i):
    ex,mm,f,idn=CASES7[i]; assert all(f(N)%mm==0 for N in range(1,20))
    st=[("$n=1$","<p>"+I("%s=%d"%(ex.replace("n","1"),f(1)))+" は "+I(str(mm))+" の倍数。</p>"),
        ("仮定","<p>"+I("%s=%d\\,l"%(ex.replace("n","m"),mm))+"（"+I("l")+" は整数）とおく。</p>"),
        ("$n=m+1$","<p>"+D(idn)+"<p>"+"仮定を代入すると "+I(str(mm))+" でくくれる。</p>"),
        ("結論","<p>数学的帰納法により、すべての自然数 "+I("n")+" で "+I(str(mm))+" の倍数。</p>")]
    return r"数学的帰納法で、すべての自然数 $n$ について $%s$ は $%d$ の倍数であることを証明せよ。"%(ex,mm),st,r"\text{証明終}"
o=[b7(i) for i in range(5)]
build(Z,CH,"a^n+b が倍数であることの数学的帰納法",o,"<p>$n=m+1$ の式を $a^{m+1}\\pm\\cdots=a(a^m\\pm\\cdots)+(\\text{倍数})$ のように、<b>仮定の式を含む形に変形</b>して倍数を示す。</p>","前の段の倍数を使って、次の段を組み立てる。",7)
# 8 不等式
CASES8=[("2^n>n^2",5,lambda N:2**N>N*N,"2^{m+1}=2\\cdot2^m>2m^2\\geqq(m+1)^2"),("3^n>n^3",4,lambda N:3**N>N**3,"3^{m+1}=3\\cdot3^m>3m^3\\geqq(m+1)^3"),("2^n>2n+1",3,lambda N:2**N>2*N+1,"2^{m+1}=2\\cdot2^m>2(2m+1)\\geqq2(m+1)+1"),("3^n\\geqq2n+1",1,lambda N:3**N>=2*N+1,"3^{m+1}\\geqq3(2m+1)\\geqq2(m+1)+1"),("2^n>n(n+1)/2\\cdot ?",0,None,"")][:4]
def b8(i):
    ex,n0,f,idn=CASES8[i]; assert all(f(N) for N in range(n0,30))
    st=[("$n=%d$"%n0,"<p>成り立つことを確認する。</p>"),
        ("仮定","<p>"+I(ex.replace("n","m"))+"（"+I("m\\geqq%d"%n0)+"）。</p>"),
        ("$n=m+1$","<p>"+D(idn)+"<p>最後の不等号は "+I("m\\geqq%d"%n0)+" を使う。</p>"),
        ("結論","<p>"+I("n\\geqq%d"%n0)+" のすべての自然数で成り立つ。</p>")]
    return r"$n\geqq%d$ をみたすすべての自然数 $n$ について $%s$ が成り立つことを、数学的帰納法で証明せよ。"%(n0,ex),st,r"\text{証明終}"
o=[b8(i) for i in [0,1,2,3]]+[b8(0)]
build(Z,CH,"不等式の数学的帰納法",o,"<p>$n=m+1$ の左辺を仮定を使って<b>下から評価</b>し、右辺以上であることを $m\\geqq n_0$ で示す。出発点が $n=1$ でないことに注意。</p>","仮定で一段下から押し上げて、次の段に届かせる。",8)
# 9 一般項の推定
def b9(a1,p,q):
    A=[a1]
    for j in range(6): A.append(p*A[-1]+q)
    an=sp.expand((a1+R(q,p-1))*p**(n-1)-R(q,p-1))
    assert all(an.subs(n,j+1)==A[j] for j in range(7))
    st=[("最初の数項","<p>"+D(r"%s"%(r",\ ".join("a_{%d}=%d"%(j+1,A[j]) for j in range(5))))+"<p>"+"から 一般項を推定する：</p>"+D(r"a_n=%s"%L(an))),
        ("帰納法で証明","<p>"+I("n=1")+" で "+I("a_1=%d"%a1)+" 一致。"+I("a_m=%s"%L(an.subs(n,sp.Symbol('m'))))+" を仮定して："+D(r"a_{m+1}=%da_m%+d=%s"%(p,q,L(sp.expand(an.subs(n,sp.Symbol('m')+1))))))]
    return r"$a_1=%d,\ a_{n+1}=%da_n%+d$ で定まる数列について、一般項を推定し、数学的帰納法で証明せよ。"%(a1,p,q),st,r"a_n=%s"%L(an)
o=[b9(*v) for v in [(1,2,1),(2,3,1),(1,3,2),(3,2,-1),(2,2,3)]]
build(Z,CH,"漸化式から一般項を推定して証明",o,"<p>最初の数項から<b>規則を予想</b>し、$a_m$ が予想の式で書けると仮定して漸化式から $a_{m+1}$ が予想の式になることを示す。</p>","まず見当をつけて、あとで確かに正しいと確かめる。",9)
# 10 ベルヌーイ
def b10(h):
    assert all((1+h)**N>=1+N*h for N in range(1,15))
    st=[("$n=1$","<p>"+I("(1+%s)^1=1+1\\cdot%s"%(L(h),L(h)))+"。等号で成り立つ。</p>"),
        ("仮定","<p>"+I("(1+%s)^m\\geqq1+m%s"%(L(h),L(h)))+"。</p>"),
        ("$n=m+1$","<p>"+D(r"(1+%s)^{m+1}=(1+%s)(1+%s)^m\geqq(1+%s)(1+m%s)=1+(m+1)%s+m%s^2\geqq1+(m+1)%s"%(L(h),L(h),L(h),L(h),L(h),L(h),L(h),L(h)))+"<p>"+I("1+%s>0"%L(h))+" を両辺にかけてよい。</p>")]
    return r"$h=%s$ のとき、すべての自然数 $n$ について $(1+h)^n\geqq1+nh$ を数学的帰納法で証明せよ。"%L(h),st,r"\text{証明終}"
o=[b10(h) for h in [R(1,2),R(1,3),R(2,3),R(1,4),R(3,2)]]
build(Z,CH,"(1+h)^n ≥ 1+nh の証明",o,"<p>仮定に <b>$(1+h)>0$ をかけて</b>評価する。$h^2$ の項は $\\geqq0$ なので捨てて下から押さえる。</p>","元本に利息がつく。複利は単利より必ず大きい。",10)
XU=finishx(Z,CH)
