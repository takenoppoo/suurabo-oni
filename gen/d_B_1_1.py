# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
n=sp.Symbol('n')
def an_(a,d): return sp.expand(a+(n-1)*d)
def sn_(a,d,N): return sp.Rational(N)*(2*a+(N-1)*d)/2
# 例題1 等差数列
def b1(p,A,q,B,N):
    d=sp.Rational(B-A,q-p); a=A-(p-1)*d; assert d.is_integer and a.is_integer
    g=an_(a,d); S=sn_(a,d,N); assert sum(g.subs(n,k) for k in range(1,N+1))==S
    st=[("初項 $a$ と公差 $d$ の式を作る","<p>"+I(r"a_n=a+(n-1)d")+" より</p>"+D(r"\begin{cases}a+%s d=%d\\ a+%s d=%d\end{cases}"%(L(p-1),A,L(q-1),B))),
        ("連立方程式を解く","<p>辺々ひく：</p>"+D(r"%s d=%d\ \Rightarrow\ d=%s"%(L(q-p),B-A,L(d)))+D(r"a=%d-%s\times %s=%s"%(A,L(p-1),L(d),L(a)))),
        ("一般項",D(r"a_n=%s+(n-1)\times%s=%s"%(L(a),P(d),L(g)))),
        ("初項から第 %d 項までの和"%N,"<p>"+I(r"S_n=\dfrac{n\{2a+(n-1)d\}}{2}")+"。</p>"+D(r"S_{%d}=\dfrac{%d\{2\times%s+%d\times%s\}}{2}=%s"%(N,N,L(a),N-1,P(d),L(S))))]
    return r"等差数列 $\{a_n\}$ は第 %d 項が $%d$、第 %d 項が $%d$ である。一般項 $a_n$ と、初項から第 %d 項までの和 $S_{%d}$ を求めよ。"%(p,A,q,B,N,N),st,r"a_n=%s,\ S_{%d}=%s"%(L(g),N,L(S))
V=[(3,11,8,31,20),(2,-1,6,-17,15),(4,14,9,-6,12),(5,20,10,45,16),(3,-5,7,3,25)]
o=[b1(*v) for v in V]
build(Z,CH,"等差数列の一般項と和",o,r"<p>等差数列：$a_n=a+(n-1)d$、和 $S_n=\dfrac{n(a+l)}2=\dfrac{n\{2a+(n-1)d\}}2$。2つの項の値から $a,d$ の連立方程式を作る。</p>","階段の1段の高さが公差。何段目の高さが分かれば、1段目と段差が決まる。",1)
# 例題2 等比数列
def b2(p,A,q,B,N):
    r=sp.Integer(round((sp.Rational(B,A))**sp.Rational(1,q-p))) if B/A>0 else -sp.Integer(round(abs(sp.Rational(B,A))**sp.Rational(1,q-p)))
    assert r**(q-p)==sp.Rational(B,A); a=sp.Rational(A)/r**(p-1); assert a.is_integer
    g=sp.expand(a*r**(n-1)) ; S=a*(r**N-1)/(r-1)
    assert sum(a*r**(k-1) for k in range(1,N+1))==S
    st=[("$a,\\ r$ の式を作る","<p>"+I(r"a_n=ar^{n-1}")+" より</p>"+D(r"ar^{%d}=%d,\quad ar^{%d}=%d"%(p-1,A,q-1,B))),
        ("公比を求める","<p>辺々わる：</p>"+D(r"r^{%d}=\dfrac{%d}{%d}=%s\ \Rightarrow\ r=%s"%(q-p,B,A,L(sp.Rational(B,A)),L(r)))+"<p>（$%d$ 乗が $%s$ になる実数は1つだけ。）</p>"%(q-p,L(sp.Rational(B,A)))),
        ("初項と一般項",D(r"a=\dfrac{%d}{%s^{%d}}=%s"%(A,P(r),p-1,L(a)))+D(r"a_n=%s\cdot %s^{n-1}"%(L(a),P(r)))),
        ("初項から第 %d 項までの和"%N,"<p>"+I(r"S_n=\dfrac{a(r^n-1)}{r-1}\ (r\neq1)")+"。</p>"+D(r"S_{%d}=\dfrac{%s\left(%s^{%d}-1\right)}{%s-1}=%s"%(N,L(a),P(r),N,P(r),L(S))))]
    return r"等比数列 $\{a_n\}$ は第 %d 項が $%d$、第 %d 項が $%d$ である。一般項 $a_n$ と、初項から第 %d 項までの和 $S_{%d}$ を求めよ。"%(p,A,q,B,N,N),st,r"a_n=%s\cdot%s^{n-1},\ S_{%d}=%s"%(L(a),P(r),N,L(S))
V=[(2,6,5,48,8),(3,12,6,-96,7),(3,18,6,486,6),(2,-4,5,-256,6),(4,-16,7,128,8)]
o=[b2(*v) for v in V]
build(Z,CH,"等比数列の一般項と和",o,r"<p>等比数列：$a_n=ar^{n-1}$、和 $S_n=\dfrac{a(r^n-1)}{r-1}\ (r\neq1)$。2つの項の比から公比 $r$ を求める。</p>","毎回同じ倍率でふえていく。離れた2項の比が、その間の倍率の積。",2)
# 例題3 和の最大
def b3(a,d):
    g=a+(n-1)*d; m=int(sp.floor(sp.Rational(a-d,-d)))  # a+(n-1)d>0 -> n<(a-d)/(-d)
    Sn=lambda k: sp.Rational(k)*(2*a+(k-1)*d)/2
    best=max(range(1,60),key=Sn); assert best==m and a+(m-1)*d>0 and a+m*d<0
    bnd=sp.Rational(a-d,-d)
    st=[("一般項",D(r"a_n=%d+(n-1)\times(%d)=%s"%(a,d,L(sp.expand(g))))),
        ("正の項はどこまでか","<p>公差が負なので減少数列。"+I(r"a_n>0")+" となる $n$ を調べる。</p>"+D(r"%s>0\ \Rightarrow\ n<%s=%.2f\cdots"%(L(sp.expand(g)),L(bnd),float(bnd)))+"<p>よって第 "+I(str(m))+" 項までが正、第 "+I(str(m+1))+" 項からは負。</p>"),
        ("最大になる $n$","<p>正の項をすべて足したとき和が最大。</p>"+D(r"n=%d"%m)),
        ("最大値",D(r"S_{%d}=\dfrac{%d\{2\times%d+%d\times(%d)\}}{2}=%s"%(m,m,a,m-1,d,L(Sn(m)))))]
    return r"初項 $%d$、公差 $%d$ の等差数列の初項から第 $n$ 項までの和を $S_n$ とする。$S_n$ が最大となる $n$ と、その最大値を求めよ。"%(a,d),st,r"n=%d,\ \text{最大値 }%s"%(m,L(Sn(m)))
V=[(50,-6),(31,-4),(40,-7),(25,-3),(62,-9)]
o=[b3(*v) for v in V]
build(Z,CH,"等差数列の和の最大",o,r"<p>公差が負の等差数列は減っていく。<b>正の項だけを足したとき</b>和が最大。$a_n>0$ を満たす最大の $n$ を求めて $S_n$ に代入する。</p>","貯金から毎月一定額ずつ使うイメージ。残高が正のうちは足し続けるのが得。",3)
# 例題4 3数が等差
def b4(S,Pd):
    a=sp.Rational(S,3); d2=a**2-sp.Rational(Pd)/a; d=sp.sqrt(d2); assert d2>=0 and sp.sqrt(d2).is_rational
    nums=sorted([a-d,a,a+d]); assert sum(nums)==S and nums[0]*nums[1]*nums[2]==Pd
    st=[("3数を文字でおく","<p>等差数列をなす3数は、公差を $d$、中央を $a$ として</p>"+D(r"a-d,\quad a,\quad a+d")),
        ("和から $a$",D(r"(a-d)+a+(a+d)=3a=%d\ \Rightarrow\ a=%s"%(S,L(a)))),
        ("積から $d$",D(r"(a-d)\,a\,(a+d)=a(a^2-d^2)=%d"%Pd)+D(r"%s\left(%s-d^2\right)=%d\ \Rightarrow\ d^2=%s\ \Rightarrow\ d=\pm%s"%(L(a),L(a**2),Pd,L(d2),L(d)))),
        ("3数を答える",D(r"%s,\ %s,\ %s"%tuple(L(t) for t in nums))+"<p>（$d$ の符号が逆でも同じ3数）</p>")]
    return r"等差数列をなす3つの数があり、和が $%d$、積が $%d$ である。この3数を求めよ。"%(S,Pd),st,r"%s,\ %s,\ %s"%tuple(L(t) for t in nums)
V=[(15,105),(18,192),(21,315),(12,60),(9,-21)]
o=[b4(*v) for v in V]
build(Z,CH,"3数が等差数列をなす",o,r"<p>等差数列をなす3数は <b>$a-d,\ a,\ a+d$</b> とおくと、和が $3a$ になって扱いやすい。</p>","真ん中を基準にして、左右に同じだけずらす。ずらした分は和で消える。",4)
# 例題5 3数が等比
def b5(x1,x2,x3):
    S=x1+x2+x3; Pd=x1*x2*x3; b=sp.Integer(round(abs(Pd)**(1/3.0)))*(1 if Pd>0 else -1); assert b**3==Pd
    t=sp.Symbol('t'); s_=S-b; pr=b**2; rts=sorted(sp.solve(t**2-s_*t+pr,t)); assert rts==sorted([x1,x3])
    st=[("3数を文字でおく","<p>等比数列をなす3数を $a,\\ b,\\ c$ とすると "+I("b^2=ac")+"。</p>"+D(r"a+b+c=%d,\quad abc=%d"%(S,Pd))),
        ("積から $b$",D(r"abc=b\cdot b^2=b^3=%d\ \Rightarrow\ b=%s"%(Pd,L(b)))),
        ("$a,\\ c$ の和と積",D(r"a+c=%d-%s=%s,\quad ac=b^2=%s"%(S,P(b),L(s_),L(pr)))),
        ("2次方程式で $a,\\ c$ を求める","<p>$a,c$ は次の2次方程式の解。</p>"+D(r"t^2-%st+%s=0"%(P(s_),L(pr)))+D(L(sp.factor(t**2-s_*t+pr))+r"=0\ \Rightarrow\ t=%s,\ %s"%(L(rts[0]),L(rts[1])))+"<p>3数は 小さい方から順に</p>"+D(r"%s,\ %s,\ %s"%(L(x1),L(x2),L(x3))+r"\quad(\text{または逆順})"))]
    return r"等比数列をなす3つの数があり、和が $%d$、積が $%d$ である。この3数を求めよ。"%(S,Pd),st,r"%s,\ %s,\ %s"%(L(x1),L(x2),L(x3))
V=[(2,4,8),(3,6,12),(1,5,25),(2,6,18),(1,-3,9)]
o=[b5(*v) for v in V]
build(Z,CH,"3数が等比数列をなす",o,r"<p>3数 $a,b,c$ が等比数列 $\iff b^2=ac$。積 $abc=b^3$ から<b>中央の $b$</b>がすぐ決まり、$a+c$ と $ac$ から2次方程式で $a,c$ を求める。</p>","真ん中を決めれば、両端は「和と積」が分かっている2数探しに変わる。",5)
UNIT=finish(Z,CH,0,0,"数列","等差数列・等比数列","一般項と和、和の最大、3数をおく工夫まで、等差・等比数列の難問に挑みます。",subject="B")
