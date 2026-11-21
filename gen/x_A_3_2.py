# -*- coding: utf-8 -*-
from bh import *
import math, itertools
Z=U_(); CH=[]; R=sp.Rational
# 6 ax+by=c の整数解
def b6(a,b,c):
    g=math.gcd(a,b); assert c%g==0
    a1,b1,c1=a//g,b//g,c//g
    _order=[0]+[s*k for k in range(1,400) for s in (1,-1)]
    _tried=[]
    for x0 in _order:
        _tried.append(x0)
        if (c1-a1*x0)%b1==0: break
    y0=(c1-a1*x0)//b1
    assert a*x0+b*y0==c
    st=[("特殊解を1つ見つける","<p>"+I("%dx+%dy=%d"%(a,b,c))+(" は両辺を "+I(str(g))+" で割って "+I("%dx+%dy=%d"%(a1,b1,c1)) if g>1 else "")+"。</p>"+"<p>"+I("x")+" に 0, 1, -1, 2, … を順に入れて、"+I("y=\\dfrac{%d-%dx}{%d}"%(c1,a1,b1))+" が整数になるものを探す。</p>"+wtable([I("x")]+[I(str(t)) for t in _tried],[[I(r"%d-%dx"%(c1,a1))]+[I(str(c1-a1*t)) for t in _tried],["%dの倍数か"%b1]+["○" if (c1-a1*t)%b1==0 else "×" for t in _tried]])+D(r"x=%d,\ y=\dfrac{%d-%d\cdot(%d)}{%d}=%d"%(x0,c1,a1,x0,b1,y0))+D(r"%d\cdot(%d)+%d\cdot%d=%d"%(a1,x0,b1,y0,c1))),
        ("差をとる","<p>"+I("%d(x-%d)+%d(y-%d)=0"%(a1,x0,b1,y0))+" より "+I("%d(x-%d)=%d(%d-y)"%(a1,x0,b1,y0))+"。"+I(str(a1))+" と "+I(str(b1))+" は互いに素。</p>"),
        ("一般解","<p>"+I("x-%d=%dk"%(x0,b1))+"（"+I("k")+" は整数）。</p>"+D(r"x=%dk%+d,\quad y=%dk%+d"%(b1,x0,-a1,y0)))]
    return r"不定方程式 $%dx+%dy=%d$ のすべての整数解を求めよ。"%(a,b,c),st,r"x=%dk%+d,\ y=%dk%+d\ (k\text{は整数})"%(b1,x0,-a1,y0)
o=[b6(*v) for v in [(7,5,3),(12,18,30),(9,4,1),(15,11,2),(8,13,5)]]
build(Z,CH,"1次不定方程式の整数解",o,r"<p>特殊解 $(x_0,y_0)$ を1つ見つけ、<b>差をとって</b> $a(x-x_0)=-b(y-y_0)$ に。$a,b$ が互いに素なら $x-x_0$ は $b$ の倍数。</p>","1組の解から、ずらしながら全部の解を出す。",6)
# 7 x,y 正の整数解の個数
def b7(a,b,c):
    sol=[(x,y) for x in range(1,c) for y in range(1,c) if a*x+b*y==c]
    st=[("$y$ の範囲","<p>"+I("%dx+%dy=%d"%(a,b,c))+"、"+I("x,y\\geqq1")+"。</p>"+D(r"y=\dfrac{%d-%dx}{%d}"%(c,a,b))),
        ("条件をみたす $x$","<p>"+I(str(b))+" で割り切れる "+I("x")+" を探す。</p>"+"<p>"+I(r"y\geqq1")+" より "+I(r"%d-%dx\geqq%d"%(c,a,b))+"、すなわち "+I(r"x\leqq%s"%L(R((c-b),a)))+"。"+I("x=1,2,\\dots,%d"%((c-b)//a))+" を順に代入する。</p>"+wtable([I("x")]+[I(str(t)) for t in range(1,(c-b)//a+1)],[[I(r"%d-%dx"%(c,a))]+[I(str(c-a*t)) for t in range(1,(c-b)//a+1)],[I(r"y")]+[I(r"\dfrac{%d}{%d}"%(c-a*t,b)) if (c-a*t)%b else I(str((c-a*t)//b)) for t in range(1,(c-b)//a+1)],["整数か"]+["○" if (c-a*t)%b==0 else "×" for t in range(1,(c-b)//a+1)]])+D(r"(x,y)=%s"%(r",\ ".join("(%d,%d)"%s for s in sol) if sol else r"\text{なし}"))),
        ("個数",D(r"%d\text{ 個}"%len(sol)))]
    return r"$%dx+%dy=%d$ をみたす正の整数の組 $(x,y)$ をすべて求めよ。"%(a,b,c),st,r"%s\ （%d個）"%(r",\ ".join("(%d,%d)"%s for s in sol),len(sol))
o=[b7(*v) for v in [(3,5,41),(4,7,60),(5,6,70),(7,4,57),(6,11,100)]]
build(Z,CH,"正の整数解の個数",o,r"<p>$y$ を $x$ で表し、$y\geqq1$ から $x$ の上限を決める。残りの候補を順に代入して整数になるものを数える。</p>","範囲をしぼってから、1つずつ確かめる。",7)
# 8 払えない金額（硬貨）
def b8(a,b):
    ng=a*b-a-b
    st=[("互いに素","<p>"+I("%d"%a)+" と "+I("%d"%b)+" は互いに素。</p>"),
        ("公式","<p>互いに素な2つの正の整数 "+I("a,b")+" を使って作れない最大の整数は "+I("ab-a-b")+"。</p>"+D(r"%d\cdot%d-%d-%d=%d"%(a,b,a,b,ng))),
        ("確認","<p>"+I(str(ng))+" は作れず、それより大きい整数は全部作れる。</p>")]
    for n in range(ng+1,ng+a*b): assert any((n-a*x)%b==0 and n-a*x>=0 for x in range(0,n//a+1))
    assert not any((ng-a*x)%b==0 and ng-a*x>=0 for x in range(0,ng//a+1))
    return r"%d 円硬貨と %d 円硬貨を何枚でも使えるとき、ちょうど支払うことができない最大の金額を求めよ。"%(a,b),st,str(ng)
o=[b8(*v) for v in [(5,8),(4,7),(7,9),(3,11),(6,13)]]
build(Z,CH,"2種類の硬貨で払えない最大金額",o,r"<p>互いに素な $a,b$ で作れない最大の金額は $ab-a-b$。$a$ で割った余りごとに「最初に作れる金額」を考えると導ける。</p>","余りのパターンを全部カバーできる金額から先は全部OK。",8)
# 9 n進法の計算
def b9(n,x,y):
    xs=sp.Integer(x); 
    def tb(v,b):
        d=[]
        while v: d.append(v%b); v//=b
        return "".join(str(t) for t in d[::-1]) or "0"
    s=x+y; p=x*y
    st=[("10進法に直す","<p>"+I("%s_{(%d)}=%d"%(tb(x,n),n,x))+"、"+I("%s_{(%d)}=%d"%(tb(y,n),n,y))+"。</p>"),
        ("計算","<p>和と積を10進法で。</p>"+D(r"%d+%d=%d,\qquad %d\times%d=%d"%(x,y,s,x,y,p))),
        ("%d進法に戻す"%n,D(r"%d=%s_{(%d)},\qquad %d=%s_{(%d)}"%(s,tb(s,n),n,p,tb(p,n),n)))]
    return r"%d進法で $%s$ と $%s$ の和と積を、同じ%d進法で表せ。"%(n,tb(x,n),tb(y,n),n),st,r"\text{和 }%s_{(%d)},\ \text{積 }%s_{(%d)}"%(tb(s,n),n,tb(p,n),n)
o=[b9(*v) for v in [(5,37,19),(6,41,23),(7,52,17),(4,29,11),(8,45,27)]]
build(Z,CH,"n進法どうしの和と積",o,r"<p>いったん<b>10進法に直して</b>計算し、最後に $n$ 進法に戻す。戻すときは $n$ で割った余りを下から並べる。</p>","いったん共通の言葉（10進法）に翻訳して計算する。",9)
# 10 未知の進数
def b10(a,b,c,d):
    # a n^2 + b n + c = d*(n+1) ... find n
    n=sp.symbols("n"); eq=sp.Eq(a*n**2+b*n+c,d*n**2+ (a+b-d)*n+c) if False else None
    # choose: (a b c)_(n) = k * (xy)_(n) with known n
    return None
def b10(N,x,y):
    n=sp.symbols("n"); v=x*N+y
    # (x y)_n = x n + y = v  with n unknown: given value in decimal
    sols=[m for m in range(max(x,y)+1,v+1) if x*m+y==v]
    st=[("10進法で表す","<p>"+I("%d%d_{(n)}=%dn+%d"%(x,y,x,y))+"。</p>"),
        ("等式","<p>"+I("%dn+%d=%d"%(x,y,v))+"。</p>"+D(r"n=\dfrac{%d-%d}{%d}=%d"%(v,y,x,(v-y)//x))),
        ("条件の確認","<p>各位の数字は "+I("n")+" 未満でなければならない。"+I("n=%d>%d"%((v-y)//x,max(x,y)))+" で適する。</p>")]
    assert sols==[N]
    return r"$n$ 進法で表された $%d%d_{(n)}$ を10進法で表すと $%d$ になる。$n$ を求めよ。"%(x,y,v),st,"n=%d"%N
o=[b10(*v) for v in [(7,3,5),(9,4,6),(6,2,5),(8,5,3),(11,3,7)]]
build(Z,CH,"未知の進数 n の決定",o,r"<p>$n$ 進法の数を $n$ の式で表して等式をつくる。<b>各位の数字は $n$ より小さい</b>ことを必ず確認。</p>","桁の数が $n$ 以上なら、その進数では存在しない。",10)
XU=finishx(Z,CH)
