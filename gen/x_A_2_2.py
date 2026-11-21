# -*- coding: utf-8 -*-
from bh import *
import math, itertools
from math import comb
Z=U_(); CH=[]; R=sp.Rational; _c=[0]
# 6 ランダムウォーク
def b6(n,k):
    assert (n+k)%2==0 and abs(k)<=n; r_=(n+k)//2; p=R(comb(n,r_),2**n)
    cnt=sum(1 for w in itertools.product([1,-1],repeat=n) if sum(w)==k); assert R(cnt,2**n)==p
    def fn(ax):
        ax.annotate("",xy=(n+1,0),xytext=(-n-1,0),arrowprops=dict(arrowstyle="->",lw=1.3,color="#333"))
        for t in range(-n,n+1): ax.plot([t,t],[-.08,.08],color="#333"); ax.text(t,-.3,str(t),ha="center",fontsize=9)
        ax.plot(0,0,"o",color="#b81f36",ms=8); ax.text(0,.25,"出発",ha="center",fontsize=9,color="#b81f36")
        ax.plot(k,0,"s",color="#2a7fd0",ms=8); ax.text(k,.25,"ゴール",ha="center",fontsize=9,color="#2a7fd0")
        ax.set_xlim(-n-1.5,n+1.5); ax.set_ylim(-.7,.8); ax.axis("off")
    make_fig("ax22r%d_%d"%(n,k),fn,size=(5,1.4)); fig=img("ax22r%d_%d"%(n,k),70)
    st=[("動きを数える","<p>表で "+I("+1")+"、裏で "+I("-1")+" 動く。"+I(str(n))+" 回のうち表が "+I("r")+" 回なら位置は "+I(r"r-(%d-r)=2r-%d"%(n,n))+"。</p>"+fig),
        ("表の回数",D(r"2r-%d=%d\ \Rightarrow\ r=%d"%(n,k,r_))),
        ("確率","<p>表が "+I(str(r_))+" 回の確率（反復試行）。</p>"+D(r"{}_{%d}\mathrm{C}_{%d}\left(\dfrac12\right)^{%d}=%s"%(n,r_,n,L(p))))]
    return r"数直線上の原点にある点 $P$ が、硬貨を投げて表が出れば $+1$、裏が出れば $-1$ だけ移動する。硬貨を $%d$ 回投げたとき、$P$ が座標 $%d$ にある確率を求めよ。"%(n,k),st,L(p)
o=[b6(*v) for v in [(6,2),(8,0),(7,3),(8,4),(6,-2)]]
build(Z,CH,"数直線上の点の移動（反復試行）",o,r"<p>位置を<b>表の回数 $r$</b>で表す：$r-(n-r)=2r-n$。目標の位置から $r$ を求め、反復試行の確率 ${}_n\mathrm{C}_rp^rq^{n-r}$ に入れる。</p>","進んだ回数と戻った回数に分ければ、位置は引き算。",6)
# 7 取り出し（非復元）
def b7(a,b,k):
    # a red b white, draw 3 without replacement: exactly k red
    tot=a+b; p=R(comb(a,k)*comb(b,3-k),comb(tot,3))
    st=[("全体","<p>"+I(str(tot))+" 個から3個を同時に取り出す：</p>"+D(r"{}_{%d}\mathrm{C}_3=%d"%(tot,comb(tot,3)))),
        ("赤 %d 個・白 %d 個を取り出す"%(k,3-k),D(r"{}_{%d}\mathrm{C}_{%d}\times{}_{%d}\mathrm{C}_{%d}=%d\times%d=%d"%(a,k,b,3-k,comb(a,k),comb(b,3-k),comb(a,k)*comb(b,3-k)))),
        ("確率",D(r"\dfrac{%d}{%d}=%s"%(comb(a,k)*comb(b,3-k),comb(tot,3),L(p))))]
    return r"赤玉 $%d$ 個と白玉 $%d$ 個が入った袋から、同時に $3$ 個の玉を取り出すとき、赤玉がちょうど $%d$ 個である確率を求めよ。"%(a,b,k),st,L(p)
o=[b7(*v) for v in [(5,4,2),(6,4,1),(4,6,2),(7,3,3),(5,5,2)]]
build(Z,CH,"同時に取り出す確率（組合せ）",o,r"<p>同時に取り出すときは<b>組合せ</b>：確率 $=\dfrac{\text{条件に合う選び方}}{\text{全体の選び方}}$。赤・白それぞれの選び方の積。</p>","全体の数え方と、条件に合う数え方を同じ基準で。",7)
# 8 くじ
def b8(n,a):
    # n本 a本あたり. 2人が順に1本ずつ(戻さない). P(少なくとも1人当たり)
    P=1-R(comb(n-a,2),comb(n,2)); p2=R(a,n)
    cnt=0; tot=0
    for p in itertools.permutations(range(n),2):
        tot+=1
        if p[0]<a or p[1]<a: cnt+=1
    assert R(cnt,tot)==P
    st=[("2人目も $\\dfrac an$","<p>くじは引く順に関係なく、1人目が当たる確率も2人目が当たる確率も "+I(r"\dfrac{%d}{%d}"%(a,n))+"。</p>"),
        ("余事象","<p>「少なくとも1人当たる」の余事象は<b>2人ともはずれる</b>。</p>"+D(r"\dfrac{%d}{%d}\times\dfrac{%d}{%d}=%s"%(n-a,n,n-a-1,n-1,L(R((n-a)*(n-a-1),n*(n-1)))))),
        ("答え",D(r"1-%s=%s"%(L(R((n-a)*(n-a-1),n*(n-1))),L(P))))]
    return r"当たりが $%d$ 本入った $%d$ 本のくじを、$A,\ B$ の2人がこの順に1本ずつ引く（引いたくじは戻さない）。少なくとも1人が当たる確率を求めよ。"%(a,n),st,L(P)
o=[b8(*v) for v in [(10,3),(8,2),(12,4),(9,3),(15,5)]]
build(Z,CH,"くじ引きの確率（少なくとも1人）",o,r"<p>くじは<b>引く順番によらず当たる確率は同じ</b>。「少なくとも1人」は<b>余事象（全員はずれ）</b>を引く。戻さないので、2人目の分母・分子が1ずつ減る。</p>","順番が後でも有利・不利はない。",8)
# 9 積が6の倍数
def b9(n):
    p=1-(R(1,2)**n+R(2,3)**n-R(1,3)**n)
    cnt=sum(1 for t in itertools.product(range(1,7),repeat=n) if math.prod(t)%6==0); assert R(cnt,6**n)==p
    st=[("余事象","<p>「積が6の倍数」でない = 「積が2の倍数でない」または「3の倍数でない」。</p>"),
        ("それぞれの確率","<p>積が2の倍数でない（すべて奇数）："+I(r"\left(\dfrac12\right)^{%d}"%n)+"。積が3の倍数でない（3,6が出ない）："+I(r"\left(\dfrac23\right)^{%d}"%n)+"。両方（1か5だけ）："+I(r"\left(\dfrac13\right)^{%d}"%n)+"。</p>"),
        ("包除",D(r"1-\left\{\left(\dfrac12\right)^{%d}+\left(\dfrac23\right)^{%d}-\left(\dfrac13\right)^{%d}\right\}=%s"%(n,n,n,L(p))))]
    return r"さいころを $%d$ 回投げて、出た目の積が $6$ の倍数になる確率を求めよ。"%n,st,L(p)
o=[b9(n) for n in [2,3,4,5,6]]
build(Z,CH,"さいころの積が6の倍数になる確率",o,r"<p>「6の倍数」$=$「2の倍数かつ3の倍数」。余事象は「2の倍数でない<b>または</b>3の倍数でない」。<b>和事象</b>の確率は $P(A)+P(B)-P(A\cap B)$。</p>","「かつ」の否定は「または」。重なりを引く。",9)
# 10 最大の確率
def b10(n,p):
    q=1-p; pr=[comb(n,k)*p**k*q**(n-k) for k in range(n+1)]; kmax=max(range(n+1),key=lambda k:pr[k]); assert pr.count(max(pr))==1
    ratio=R(n-kmax+1,kmax)*p/q if kmax>0 else 0
    st=[("隣り合う項の比","<p>"+I(r"P_k={}_{%d}\mathrm{C}_{k}\left(%s\right)^k\left(%s\right)^{%d-k}"%(n,L(p),L(q),n))+"。</p>"+D(r"\dfrac{P_{k+1}}{P_k}=\dfrac{%d-k}{k+1}\cdot\dfrac{%s}{%s}=\dfrac{%d-k}{k+1}\cdot%s"%(n,L(p),L(q),n,L(p/q)))),
        ("増える・減る","<p>"+I(r"\dfrac{P_{k+1}}{P_k}>1")+" となる "+I("k")+" の範囲を調べる。</p>"+D(r"%s(%d-k)>k+1\ \iff\ k<%s"%(L(p/q),n,L(R((n*p/q-1),1+p/q))))),
        ("最大になる $k$","<p>"+I(r"k=%d"%kmax)+" で最大。</p>"+D(r"P_{%d}=%s"%(kmax,L(pr[kmax]))))]
    return r"1回の試行で成功する確率が $%s$ の試行を $%d$ 回くり返すとき、成功の回数が $k$ である確率が最大となる $k$ を求めよ。"%(L(p),n),st,"k=%d"%kmax
o=[b10(*v) for v in [(10,R(1,3)),(12,R(1,4)),(15,R(2,5)),(20,R(1,5)),(11,R(3,5))]]
build(Z,CH,"反復試行の確率が最大となる回数",o,r"<p>隣り合う確率の比 $\dfrac{P_{k+1}}{P_k}$ を作り、<b>1より大きい間は増加、小さくなったら減少</b>。比が1を横切る所が最大。</p>","山のてっぺんは、比が1を下回る直前。",10)
XU=finishx(Z,CH)
