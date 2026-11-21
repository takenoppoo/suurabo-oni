# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
# 6 解がない
def b6(p,q,r_,s_):
    # a x + p > q?  : ax > b and x < c  no solution ... use  p x - q < ... Let x > A (from p x > q) and x <= a + c
    # 連立: x < a, 3x + p > ... → simple: 2x-1>5 (x>3) and x<=a+ ... : 解をもたない a の範囲
    A=R(q+p,r_)  # r_ x - p > q
    st=[("それぞれ解く","<p>"+I(r"%dx-%d>%d"%(r_,p,q))+"：</p>"+D(r"%dx>%d+%d=%d\ \Longrightarrow\ x>%s"%(r_,q,p,q+p,L(A)))+"<p>"+I(r"x\leqq a")+" はそのまま。</p>"),
        ("解がない条件","<p>"+I("x>%s"%L(A))+" と "+I(r"x\leqq a")+" の共通部分が空になる。</p>"+D(r"a\leqq %s"%L(A))+"<p>端点 "+I("a=%s"%L(A))+" のとき "+I("x>%s,\ x\\leqq %s"%(L(A),L(A)))+" で共通部分なし（等号が入ることに注意）。</p>"),
        ("答え","<p>"+I(r"a\leqq %s"%L(A))+"。</p>")]
    return r"連立不等式 $%dx-%d>%d,\ \ x\leqq a$ が解をもたないような定数 $a$ の範囲を求めよ。"%(r_,p,q),st,r"a\leqq %s"%L(A)
o=[b6(*v) for v in [(1,2,3,0),(2,3,5,0),(1,5,2,0),(3,4,7,0),(2,1,6,0)]]
build(Z,CH,"連立不等式が解をもたない条件",o,r"<p>各不等式の解を数直線に図示し、<b>共通部分が空</b>になる条件を考える。端点が一致したとき、等号の有無で<b>解があるか</b>を必ず確かめる。</p>","2つの範囲がぴったりすれ違う瞬間に、解があるかないか確認する。",6)
# 7 |ax-b|<=c の解から a,b
def b7(a,b,lo,hi):
    # |a x - b| < c has solution lo<x<hi : (b-c)/a=lo,(b+c)/a=hi
    c=sp.Rational(a*(hi-lo),2); b_=sp.Rational(a*(hi+lo),2); 
    st=[("絶対値をはずす","<p>"+I(r"|%dx-b|<c"%a)+" は "+I(r"-c<%dx-b<c"%a)+" より</p>"+D(r"\dfrac{b-c}{%d}<x<\dfrac{b+c}{%d}"%(a,a))),
        ("係数比較","<p>解が "+I("%s<x<%s"%(L(lo),L(hi)))+" なので</p>"+D(r"\dfrac{b-c}{%d}=%s,\qquad \dfrac{b+c}{%d}=%s"%(a,L(lo),a,L(hi)))),
        ("連立して解く",D(r"b-c=%s,\quad b+c=%s\ \Rightarrow\ b=%s,\ c=%s"%(L(a*lo),L(a*hi),L(b_),L(c))))]
    return r"不等式 $|%dx-b|<c\ (c>0)$ の解が $%s<x<%s$ であるとき、定数 $b,\ c$ の値を求めよ。"%(a,L(lo),L(hi)),st,r"b=%s,\ c=%s"%(L(b_),L(c))
o=[b7(*v) for v in [(2,0,-1,4),(3,0,-2,5),(2,0,1,6),(4,0,-3,1),(3,0,2,7)]]
build(Z,CH,"絶対値不等式の解から定数を決める",o,r"<p>$|ax-b|<c$ は $-c<ax-b<c$ に直して $x$ の範囲を $b,c$ で表し、与えられた解と<b>両端を比べて</b>連立方程式を作る。</p>","範囲の左端と右端、2つの情報から2つの未知数を決める。",7)
# 8 A⊂B
def b8(a1,a2,b1):
    # A: x^... A={x | a1<=x<=a2}? B={x| b1< x < a}? 包含: a>a2
    st=[("集合を不等式で表す","<p>"+I(r"A:\ %d\leqq x\leqq %d"%(a1,a2))+"、"+I(r"B:\ %s<x<a"%L(b1))+"。</p>"),
        ("包含の条件","<p>"+I(r"A\subset B")+" となるのは、数直線で "+I("A")+" が "+I("B")+" の内側にあるとき。</p>"+D(r"%s<%d\ \text{かつ}\ %d<a"%(L(b1),a1,a2))),
        ("等号に注意","<p>"+I("x=%d"%a2)+" が "+I("B")+" に入るには "+I("a>%d"%a2)+"（"+I("a=%d"%a2)+" だと "+I("x<%d"%a2)+" で "+I("x=%d"%a2)+" が入らない）。</p>"+D(r"a>%d"%a2))]
    return r"$A=\{x\mid %d\leqq x\leqq %d\}$、$B=\{x\mid %s<x<a\}$ について、$A\subset B$ となる定数 $a$ の範囲を求めよ。"%(a1,a2,L(b1)),st,r"a>%d"%a2
o=[b8(*v) for v in [(1,4,0),(-2,3,-5),(2,6,1),(0,5,-1),(-1,2,-3)]]
build(Z,CH,"集合の包含と不等式",o,r"<p>$A\subset B$ は<b>$A$ の端点が $B$ の内側</b>にあること。端点を含むか（$\leqq$ か $<$）で、$a$ の範囲の等号の有無が決まる。</p>","小さい箱が大きい箱にすっぽり入る。ふち同士が接するときだけ要注意。",8)
# 9 文章題 (最大の個数)
def b9(p1,p2,total,box):
    # 1個p1円 のりんごと 1個 p2円 のなし. 合計n個, 予算total. 
    # りんごx個 なし (n-x) 個 ... answer max x with p1 x + p2 (n-x) +box <= total
    n=10; xs=[xi for xi in range(0,n+1) if p1*xi+p2*(n-xi)+box<=total]; mx=max(xs)
    st=[("文字を決める","<p>りんごを "+I("x")+" 個とすると、なしは "+I("(%d-x)"%n)+" 個。</p>"),
        ("不等式を立てる","<p>代金の合計が予算以下：</p>"+D(r"%d x+%d(%d-x)+%d\leqq %d"%(p1,p2,n,box,total))),
        ("解く",D(r"%d-%dx\leqq%d\ \Rightarrow\ x\geqq %s"%(n*p2+box if False else (p1-p2)*0+n*p2+box,p2-p1,total,"?")) if False else D(r"%s\ x\leqq %d"%(L(p1-p2),total-n*p2-box))+"<p>"+(I("x\\leqq %s"%L(R(total-n*p2-box,p1-p2))) if p1>p2 else I("x\\geqq %s"%L(R(total-n*p2-box,p1-p2))))+"。"+I("0\\leqq x\\leqq%d"%n)+" の整数で最大は "+I(str(mx))+"。</p>")]
    return r"1個 $%d$ 円のりんごと1個 $%d$ 円のなしを合わせて $%d$ 個買い、$%d$ 円の箱に入れる。代金の合計を $%d$ 円以下にするとき、りんごは最大で何個買えるか。"%(p1,p2,n,box,total),st,str(mx)
o=[b9(*v) for v in [(120,80,1100,150),(150,90,1300,200),(130,70,1000,100),(180,100,1500,250),(140,60,900,100)]]
build(Z,CH,"不等式の文章題（最大の個数）",o,r"<p>個数を $x$ とおき、<b>代金＋箱代 $\leqq$ 予算</b>の不等式を作る。解いたあと、<b>整数で、$0\leqq x\leqq$ 合計の個数</b>という条件で絞る。</p>","まず式、次に整数・範囲のチェック。計算の最後で答えが現実に合うか見る。",9)
# 10 濃度
def b10(w,c1,c2):
    # 濃度c1% の食塩水 w g に 水 x g 加えて 濃度 c2% 以下に: w*c1/(w+x)<=c2 → x >= w*c1/c2 - w
    xmin=R(w*c1,c2)-w
    st=[("食塩の量","<p>食塩の量は "+I(r"%d\times\dfrac{%d}{100}=%s\ \text{(g)}"%(w,c1,L(R(w*c1,100))))+"（水を加えても変わらない）。</p>"),
        ("不等式",D(r"\dfrac{%s}{%d+x}\times100\leqq %d"%(L(R(w*c1,100)),w,c2))),
        ("解く","<p>"+I("%d+x>0"%w)+" なので両辺にかけて</p>"+D(r"%d\leqq %d(%d+x)\ \Rightarrow\ x\geqq %s"%(w*c1,c2,w,L(xmin))))]
    return r"濃度 $%d\%%$ の食塩水 $%d$ g に水を加えて、濃度を $%d\%%$ 以下にしたい。水を何 g 以上加えればよいか。"%(c1,w,c2),st,r"%s\ \text{g以上}"%L(xmin)
o=[b10(*v) for v in [(200,12,8),(300,10,6),(150,20,12),(400,15,9),(250,8,5)]]
build(Z,CH,"濃度の不等式",o,r"<p>水を加えても<b>食塩の量は変わらない</b>。濃度 $=\dfrac{\text{食塩}}{\text{全体}}\times100$ を不等式にし、分母は正なので両辺にかけて解く。</p>","薄めても塩の量は不変。変わるのは全体の重さだけ。",10)
XU=finishx(Z,CH)
