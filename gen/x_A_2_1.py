# -*- coding: utf-8 -*-
from bh import *
import math, itertools
from math import comb, factorial as fa
Z=U_(); CH=[]; R=sp.Rational; _c=[0]
# 6 円順列 隣り合わない
def b6(n):
    v=fa(n-1)-2*fa(n-2)
    # brute
    cnt=0
    for perm in itertools.permutations(range(1,n)):
        seq=(0,)+perm  # 0 fixed (A), 1 = B
        i=seq.index(1)
        adj=(i==1 or i==n-1)
        if not adj: cnt+=1
    assert cnt==v
    st=[("全体（円順列）","<p>"+I("n=%d"%n)+" 人の円順列は "+I(r"(%d-1)!=%d"%(n,fa(n-1)))+" 通り。</p>"),
        ("A と B が隣り合う場合","<p>"+I("A,B")+" をひとまとめにして "+I("%d"%(n-1))+" 人の円順列、中の並びが 2 通り。</p>"+D(r"(%d-2)!\times2=%d"%(n,2*fa(n-2)))),
        ("引く",D(r"%d-%d=%d"%(fa(n-1),2*fa(n-2),v)))]
    return r"%d 人が円形のテーブルに座る。特定の2人 $A,\ B$ が隣り合わない座り方は何通りあるか。"%n,st,str(v)
o=[b6(n) for n in [6,7,8,9,5]]
build(Z,CH,"円順列（特定の2人が隣り合わない）",o,r"<p>「隣り合わない」は<b>全体 $-$ 隣り合う</b>。隣り合う2人は<b>ひとまとめ</b>にして円順列、中の入れかわり $2$ 通りをかける。</p>","直接数えにくいときは、反対側（余事象）を引く。",6)
# 7 同じものを含む順列
def b7(letters):
    from collections import Counter
    cn=Counter(letters); n=len(letters)
    tot=fa(n)
    for v in cn.values(): tot//=fa(v)
    seen=set(itertools.permutations(letters)); cntnoadj=sum(1 for p in seen if not any(p[i]=='A' and p[i+1]=='A' for i in range(n-1))); 
    a=cn['A']; rest=n-a; ways=comb(rest+1,a)  # rest letters arrangement count × gaps
    rr=fa(rest)
    for k,v in cn.items():
        if k!='A': rr//=fa(v)
    v=rr*ways; assert v==cntnoadj
    st=[("A 以外を先に並べる","<p>"+I(r"%s"%(r",\ ".join(k for k in cn if k!='A')))+" の並べ方は "+I(str(rr))+" 通り（同じ文字を区別しない）。</p>"),
        ("A を入れる場所","<p>"+I("%d"%rest)+" 文字の前後・間の "+I(str(rest+1))+" か所から "+I(str(a))+" か所を選んで "+I("A")+" を1つずつ入れる。</p>"+D(r"{}_{%d}\mathrm{C}_{%d}=%d"%(rest+1,a,ways))),
        ("積",D(r"%d\times%d=%d"%(rr,ways,v)))]
    return r"文字 $%s$ をすべて使って1列に並べる。$A$ どうしが隣り合わない並べ方は何通りあるか。"%(r"\ ".join(letters)),st,str(v)
o=[b7(list(x)) for x in ["AAABBC","AABBCC","AAABBCD" ,"AAABBB","AABBBCC"]]
build(Z,CH,"同じ文字を含む順列（隣り合わない）",o,r"<p>「隣り合わない」は<b>先に他を並べて、すき間に入れる</b>。他の文字の数 $r$ なら入れる場所は $r+1$ か所。同じ文字は区別しない。</p>","席を先に並べてから、あいた間に1人ずつ座る。",7)
# 8 多角形の三角形
def b8(n):
    v=n*(n-4)*(n-5)//6
    cnt=0
    for t in itertools.combinations(range(n),3):
        sides=sum(1 for i in range(3) if (t[(i+1)%3]-t[i])%n in (1,n-1))
        if sides==0: cnt+=1
    assert cnt==v
    ang=[(2*math.pi*k/n+math.pi/2) for k in range(n)]; pts=[(math.cos(a),math.sin(a)) for a in ang]
    tri=[pts[0],pts[2],pts[5%n if n>5 else 4]]
    fig=geo("ax21p%d"%n,circles=[],polys=[(pts,"#333"),(tri,"#b81f36")],w=34,size=(3,3))
    st=[("全体","<p>"+I(r"{}_{%d}\mathrm{C}_3=%d"%(n,comb(n,3)))+" 通り。</p>"+fig),
        ("辺を2本共有する三角形","<p>隣り合う3頂点 "+I(str(n))+" 通り。</p>"),
        ("辺を1本だけ共有する三角形","<p>辺 "+I("%d"%n)+" 本のそれぞれに、残りの頂点（その辺の両端と隣り合わない）"+I(str(n-4))+" 通り。</p>"+D(r"%d\times%d=%d"%(n,n-4,n*(n-4)))),
        ("引く",D(r"%d-%d-%d=%d"%(comb(n,3),n,n*(n-4),v)))]
    return r"正%d角形の頂点から3つを選んで三角形をつくる。正%d角形の辺を1本も共有しない三角形は何個できるか。"%(n,n),st,str(v)
o=[b8(n) for n in [8,9,10,11,12]]
build(Z,CH,"正多角形の頂点でつくる三角形（辺を共有しない）",o,r"<p>全体から「辺を共有する三角形」を引く。<b>辺を2本共有</b>（隣り合う3頂点）は $n$ 個、<b>1本だけ共有</b>は $n(n-4)$ 個。</p>","共有の仕方を、2本・1本・0本で分けて数える。",8)
# 9 塗り分け
def b9(k,c):
    m=c-1; cyc=(m-1)**k+(-1)**k*(m-1); v=c*cyc
    cnt=0
    for center in range(c):
        cols=[x for x in range(c) if x!=center]
        for p in itertools.product(cols,repeat=k):
            if all(p[i]!=p[(i+1)%k] for i in range(k)): cnt+=1
    assert cnt==v
    ang=[2*math.pi*i/k+math.pi/2 for i in range(k)]
    def fn(ax):
        import matplotlib.patches as mp
        ax.add_patch(mp.Circle((0,0),.45,fc="#fbe3e7",ec="#333")); ax.text(0,0,"A",ha="center",va="center",fontsize=12)
        for i,a in enumerate(ang):
            x_=1.0*math.cos(a);y_=1.0*math.sin(a)
            ax.add_patch(mp.Circle((x_,y_),.35,fc="#e6f0fb",ec="#333")); ax.text(x_,y_,chr(66+i),ha="center",va="center",fontsize=11)
            ax.plot([.45*math.cos(a),.65*math.cos(a)],[.45*math.sin(a),.65*math.sin(a)],color="#888")
            a2=ang[(i+1)%k]; ax.plot([x_,1.0*math.cos(a2)],[y_,1.0*math.sin(a2)],color="#888",lw=1)
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.5,1.5)
    make_fig("ax21w%d_%d"%(k,c),fn,size=(3,3)); fig=img("ax21w%d_%d"%(k,c),34)
    st=[("図の読み取り","<p>中央 "+I("A")+" は周りの "+I(str(k))+" 個すべてと隣り合い、周りの領域は円環状に隣り合う。</p>"+fig),
        ("中央の色","<p>"+I("A")+" の色は "+I("%d"%c)+" 通り。残りは "+I("%d"%(c-1))+" 色から選ぶ。</p>"),
        ("周りの環の塗り方","<p>"+I(str(k))+" 個を円環に、隣どうし異なる色で、"+I(str(m))+" 色から。"+I(r"B\to C\to\cdots")+" と順に決めると（最後だけ場合分け）</p>"+D(r"(%d-1)^{%d}+(-1)^{%d}(%d-1)=%d"%(m,k,k,m,cyc))),
        ("積",D(r"%d\times%d=%d"%(c,cyc,v)))]
    return r"図のように、中央の領域 $A$ のまわりに $%d$ 個の領域が円環状にならんでいる。隣り合う領域は異なる色で塗る。$%d$ 色を使うとき（使わない色があってもよい）、塗り方は何通りあるか。"%(k,c),st,str(v)
o=[b9(*v) for v in [(4,5),(5,5),(5,6),(6,5),(4,6)]]
build(Z,CH,"領域の塗り分け（円環状）",o,r"<p>中央を先に決め、周りの環を<b>順に塗る</b>。最後の領域は最初の領域とも隣り合うので、<b>色の使い方で場合分け</b>、または公式 $(m-1)^k+(-1)^k(m-1)$ を用いる。</p>","隣り合う所を先に確認してから、順番に色を決める。",9)
# 10 数字の和
def b10(s_):
    v=sum(1 for n in range(100,1000) if sum(map(int,str(n)))==s_)
    # 百の位a>=1: a'=a-1 >=0 ; a'+b+c=s-1, each <=8,<=9,<=9
    st=[("方程式にする","<p>百の位 "+I("a")+"（"+I(r"1\leqq a\leqq9")+"）、十の位 "+I("b")+"、一の位 "+I("c")+"（"+I(r"0\leqq b,c\leqq9")+"）。</p>"+D(r"a+b+c=%d"%s_)),
        ("$a'=a-1$ で非負にする",D(r"a'+b+c=%d\quad(a'\geqq0,\ b\geqq0,\ c\geqq0)"%(s_-1))+"<p>重複組合せ：</p>"+D(r"{}_{%d}\mathrm{H}_{%d}={}_{%d}\mathrm{C}_{2}=%d"%(3,s_-1,s_-1+2,comb(s_+1,2)))),
        ("上限を超える場合を引く",(lambda t: "<p>"+I(r"a'\geqq9")+"：残り "+I(str(t-9))+" を配る "+I(r"{}_{3}\mathrm{H}_{%d}=%d"%(max(t-9,0),comb(t-9+2,2) if t>=9 else 0))+"。"+I(r"b\geqq10")+"、"+I(r"c\geqq10")+"：それぞれ "+I(r"%d"%(comb(t-10+2,2) if t>=10 else 0))+"。2つ同時に超えることはない（和が "+I(str(t))+" 以下のため）。</p>"+D(r"%d-%d-%d-%d=%d"%(comb(t+2,2),comb(t-9+2,2) if t>=9 else 0,comb(t-10+2,2) if t>=10 else 0,comb(t-10+2,2) if t>=10 else 0,v)))(s_-1))]
    return r"各位の数字の和が $%d$ である3けたの自然数は何個あるか。"%s_,st,str(v)
o=[b10(s_) for s_ in [8,10,12,15,18]]
build(Z,CH,"各位の和が一定の3けたの整数",o,r"<p>$a+b+c=s$ の整数解の個数（重複組合せ）。<b>百の位は $a\geqq1$</b> なので $a'=a-1$ とおく。各位が<b>9以下</b>という上限の条件を超える場合を引く。</p>","配る問題に直して、上限を超えた分を取り除く。",10)
XU=finishx(Z,CH)
