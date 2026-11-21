# -*- coding: utf-8 -*-
from bh import *
import math, itertools
from math import comb
Z=U_(); CH=[]; R=sp.Rational; _c=[0]
# 6 検査（ベイズ）
def b6(p,a,b):
    # P(病気)=p, 感度 P(陽性|病気)=a, 偽陽性 P(陽性|健康)=b
    pos=p*a+(1-p)*b; v=p*a/pos
    def fn(ax):
        ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,6)
        ax.text(.2,3,"全体",fontsize=11,va="center")
        for (y,lab,pr) in [(4.5,"病気",p),(1.5,"健康",1-p)]:
            ax.plot([1,3.5],[3,y],color="#333"); ax.text(2.2,(3+y)/2+.3*(1 if y>3 else -1),str(float(pr)),fontsize=9,ha="center"); ax.text(3.6,y,lab,fontsize=11,va="center")
        for (y0,ys) in [(4.5,[(5.3,"陽性",a),(3.7,"陰性",1-a)]),(1.5,[(2.3,"陽性",b),(.7,"陰性",1-b)])]:
            for (y,lab,pr) in ys:
                ax.plot([5.2,7.2],[y0,y],color="#333"); ax.text(6.2,(y0+y)/2+.2,str(float(pr)),fontsize=9,ha="center"); ax.text(7.3,y,lab,fontsize=11,va="center",color="#b81f36" if lab=="陽性" else "#333")
    make_fig("ax23t%d_%d_%d"%(int(p*1000),int(a*100),int(b*100)),fn,size=(4.4,2.6)); fig=img("ax23t%d_%d_%d"%(int(p*1000),int(a*100),int(b*100)),55)
    st=[("樹形図で整理","<p>病気 "+I("D")+"、陽性 "+I("T")+"。</p>"+fig),
        ("陽性になる確率",D(r"P(T)=%s\cdot%s+%s\cdot%s=%s"%(L(p),L(a),L(1-p),L(b),L(pos)))),
        ("条件付き確率",D(r"P(D\mid T)=\dfrac{P(D\cap T)}{P(T)}=\dfrac{%s}{%s}=%s"%(L(p*a),L(pos),L(v))))]
    return r"ある病気にかかっている人の割合は $%s$ である。この病気の検査では、病気の人が陽性になる確率が $%s$、病気でない人が陽性になる確率が $%s$ である。検査で陽性だった人が、実際に病気である確率を求めよ。"%(L(p),L(a),L(b)),st,L(v)
o=[b6(*v) for v in [(R(1,100),R(9,10),R(1,20)),(R(2,100),R(95,100),R(3,100)),(R(1,50),R(4,5),R(1,10)),(R(3,100),R(9,10),R(2,100)),(R(1,200),R(99,100),R(1,100))]]
build(Z,CH,"検査の陽性反応から病気の確率（原因の確率）",o,r"<p>$P(D\mid T)=\dfrac{P(D\cap T)}{P(T)}$。<b>陽性になる経路をすべて足して</b>分母にし、病気で陽性になる経路を分子にする。樹形図が有効。</p>","陽性の人全員のうち、本当に病気の人の割合。",6)
# 7 くじの期待値と公平な値段
def b7(prizes,n):
    # prizes list of (amount,count) ; n total tickets ; fair price = expectation
    E=R(sum(a*c for a,c in prizes),n)
    st=[("確率分布","<p>賞金と本数：</p>"+D(r"\begin{array}{c|%s}\text{賞金}&%s\\\hline\text{本数}&%s\end{array}"%("c"*(len(prizes)+1),"&".join(str(a) for a,c in prizes)+"&0","&".join(str(c) for a,c in prizes)+"&%d"%(n-sum(c for a,c in prizes))))),
        ("期待値","<p>期待値 "+I(r"E=\sum(\text{賞金})\times(\text{確率})")+"。</p>"+D(r"E=%s=%s"%("+".join(r"%d\cdot\dfrac{%d}{%d}"%(a,c,n) for a,c in prizes),L(E)))),
        ("公平な値段","<p>1回の値段が期待値に等しいとき、損も得もない。</p>"+D(r"%s\ \text{円}"%L(E)))]
    return r"$%d$ 本のくじに、%s が入っている（残りははずれ）。このくじ1本の賞金の期待値を求めよ。損得なしとなるくじ1本の値段はいくらか。"%(n,"、".join("賞金 $%d$ 円が $%d$ 本"%(a,c) for a,c in prizes)),st,r"E=%s\ \text{円（値段も }%s\text{ 円）}"%(L(E),L(E))
o=[b7(*v) for v in [([(1000,1),(500,3),(100,10)],100),([(2000,2),(300,8)],200),([(5000,1),(1000,4),(200,15)],150),([(10000,1),(1000,9)],500),([(800,5),(100,20)],250)]]
build(Z,CH,"くじの期待値と公平な値段",o,r"<p>期待値 $=\sum(\text{賞金}\times\text{確率})$。はずれ（賞金0円）は0をかけるので書かなくてよい。値段が期待値と等しいとき、平均して損得なし。</p>","長い目で見た「1回あたりの平均」が期待値。",7)
# 8 初めて赤が出るまでの回数
def b8(a,b):
    n=a+b; E=R(n+1,a+1)
    # brute: draw without replacement until first red
    tot=0;cnt=0
    for perm in itertools.permutations(range(n)):
        k=next(i for i,v in enumerate(perm) if v<a)+1; tot+=k; cnt+=1
    assert R(tot,cnt)==E
    P=[R(math.perm(n-1,0),1)]  # placeholder
    st=[("確率分布","<p>赤玉 "+I(str(a))+"、白玉 "+I(str(b))+"。"+I("k")+" 回目に初めて赤が出る確率 "+I("P_k")+"。</p>"),
        ("期待値の公式","<p>"+I(a)+" 個の赤が、"+I(str(b))+" 個の白を "+I(str(a+1))+" 個のすき間に等しく分ける。白の数の期待値は1つのすき間あたり "+I(r"\dfrac{%d}{%d}"%(b,a+1))+"。</p>"+D(r"E=1+\dfrac{%d}{%d}=%s"%(b,a+1,L(E)))),
        ("答え",D(r"E=\dfrac{%d+1}{%d+1}=%s"%(n,a,L(E))))] if False else [("考え方","<p>赤 "+I(str(a))+" 個・白 "+I(str(b))+" 個を1列に並べたとみる。赤が "+I(str(a))+" 個あると、白が入るすき間は "+I(str(a+1))+" か所。</p>"),
        ("最初の赤の前にある白の個数","<p>白は各すき間に対称にふり分けられるので、最初の赤の前の白の期待値は "+I(r"\dfrac{%d}{%d}"%(b,a+1))+"。</p>"),
        ("期待値","<p>最初の赤が出る回数 = 前の白の個数 + 1。</p>"+D(r"E=1+\dfrac{%d}{%d}=\dfrac{%d}{%d}=%s"%(b,a+1,n+1,a+1,L(E))))]
    return r"赤玉 $%d$ 個と白玉 $%d$ 個が入った袋から、玉を1個ずつ取り出していく（取り出した玉はもどさない）。はじめて赤玉が出るまでに取り出す回数の期待値を求めよ。"%(a,b),st,L(E)
o=[b8(*v) for v in [(2,4),(3,5),(2,6),(4,4),(1,5)]]
build(Z,CH,"はじめて赤玉が出るまでの回数の期待値",o,r"<p>全部を1列に並べたと考える。赤 $a$ 個で白が入るすき間は $a+1$ か所、<b>対称性</b>から白の数の期待値は等分。$E=1+\dfrac{b}{a+1}=\dfrac{a+b+1}{a+1}$。</p>","列に並べて、赤がつくる区切りに白を等しく配る。",8)
# 9 先に2勝
def b9(p):
    q=1-p; E=2*(p*p+q*q)+3*(2*p*q); P3=2*p*q; PA=p*p+2*p*p*q
    st=[("試合数の確率","<p>先に2勝したほうが優勝。"+I("A")+" が1試合に勝つ確率を "+I("p=%s"%L(p))+"。</p>"+D(r"P(2\text{試合})=p^2+q^2=%s,\qquad P(3\text{試合})=2pq=%s"%(L(p*p+q*q),L(P3)))),
        ("期待値",D(r"E=2\cdot%s+3\cdot%s=%s"%(L(p*p+q*q),L(P3),L(E)))),
        ("$A$ が優勝する確率","<p>2連勝、または1敗をはさんで2勝。</p>"+D(r"p^2+2p^2q=%s"%L(PA)))]
    return r"$A,\ B$ が試合を行い、先に2勝したほうが優勝とする。1試合で $A$ が勝つ確率は $%s$ で、引き分けはない。試合数の期待値と、$A$ が優勝する確率を求めよ。"%L(p),st,r"E=%s,\ \ P(A\text{優勝})=%s"%(L(E),L(PA))
o=[b9(p) for p in [R(1,2),R(3,5),R(2,3),R(3,4),R(1,3)]]
build(Z,CH,"先に2勝する勝負の試合数の期待値",o,r"<p>試合数は2か3。<b>2試合で決まる確率</b> $p^2+q^2$、<b>3試合になる確率</b> $2pq$。期待値は各試合数×確率の和。</p>","場合を全部書き出して、確率で重みづけ。",9)
# 10 条件付き確率（さいころ2個）
def b10(s_,ev):
    A=[(i,j) for i in range(1,7) for j in range(1,7) if i+j>=s_]
    conds={"ひとつは6":lambda t:6 in t,"2つの目が等しい":lambda t:t[0]==t[1],"少なくとも1つは偶数":lambda t:t[0]%2==0 or t[1]%2==0,"2つとも奇数":lambda t:t[0]%2==1 and t[1]%2==1,"差が2以上":lambda t:abs(t[0]-t[1])>=2}
    B=[t for t in A if conds[ev](t)]; p=R(len(B),len(A))
    st=[("条件 $A$","<p>2つのさいころ（区別する）の目の和が "+I(str(s_))+" 以上：</p>"+D(r"n(A)=%d"%len(A))),
        ("$A\\cap B$ の個数","<p>"+I("B")+"：「"+ev+"」。</p>"+D(r"n(A\cap B)=%d"%len(B))),
        ("条件付き確率",D(r"P_A(B)=\dfrac{n(A\cap B)}{n(A)}=\dfrac{%d}{%d}=%s"%(len(B),len(A),L(p))))]
    return r"大小2つのさいころを投げる。目の和が $%d$ 以上であったとき、「%s」である確率を求めよ。"%(s_,ev),st,L(p)
o=[b10(*v) for v in [(8,"ひとつは6"),(9,"2つの目が等しい"),(7,"少なくとも1つは偶数"),(6,"2つとも奇数"),(8,"差が2以上")]]
build(Z,CH,"さいころ2個の条件付き確率",o,r"<p>$P_A(B)=\dfrac{n(A\cap B)}{n(A)}$。<b>分母は条件 $A$ をみたす場合の数</b>（全体36通りではない）。表で書き出して数える。</p>","条件がついたら、その条件を新しい全体とみなす。",10)
XU=finishx(Z,CH)
