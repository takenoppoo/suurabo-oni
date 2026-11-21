# -*- coding: utf-8 -*-
from bh import *
from math import comb
Z=U_(); CH=[]
R=sp.Rational
TBL=r"（正規分布表）$p(u)=P(0\leqq Z\leqq u)$：$p(0.5)=0.1915,\ p(1.0)=0.3413,\ p(1.5)=0.4332,\ p(2.0)=0.4772,\ p(2.5)=0.4938,\ p(3.0)=0.4987$"
PT={R(1,2):R(1915,10000),R(1):R(3413,10000),R(3,2):R(4332,10000),R(2):R(4772,10000),R(5,2):R(4938,10000),R(3):R(4987,10000)}
def pu(u): return PT[abs(u)]
def dec(q,nd=4): return ("%."+str(nd)+"f")%float(q)
def sig(v): return L(sp.nsimplify(sp.sqrt(v)))
# 例題1 二項分布
def b1(n,p,r):
    p=R(p); q=1-p; pr=comb(n,r)*p**r*q**(n-r); E=n*p; V=n*p*q
    assert sum(comb(n,i)*p**i*q**(n-i) for i in range(n+1))==1
    st=[("二項分布の確率","<p>"+I(r"X\sim B(%d,\ %s)"%(n,L(p)))+"。"+I(r"P(X=k)={}_n\mathrm{C}_kp^kq^{n-k}\ (q=1-p)")+"。</p>"),
        ("$P(X=%d)$"%r,D(r"P(X=%d)={}_{%d}\mathrm{C}_{%d}\left(%s\right)^{%d}\left(%s\right)^{%d}=%d\times%s=%s"%(r,n,r,L(p),r,L(q),n-r,comb(n,r),L(p**r*q**(n-r)),L(pr)))),
        ("期待値・分散・標準偏差","<p>"+I(r"E(X)=np,\ V(X)=npq,\ \sigma(X)=\sqrt{npq}")+"。</p>"+D(r"E(X)=%d\times%s=%s,\quad V(X)=%d\times%s\times%s=%s,\quad \sigma(X)=%s"%(n,L(p),L(E),n,L(p),L(q),L(V),sig(V))))]
    return r"1回の試行で事象 $A$ が起こる確率が $%s$ である。この試行を $%d$ 回くり返すとき、$A$ が起こる回数 $X$ について、$P(X=%d)$、$E(X)$、$V(X)$、$\sigma(X)$ を求めよ。"%(L(p),n,r),st,r"P=%s,\ E=%s,\ V=%s,\ \sigma=%s"%(L(pr),L(E),L(V),sig(V))
V_=[(6,R(1,2),2),(4,R(1,3),2),(3,R(1,4),1),(5,R(2,3),3),(5,R(1,6),2)]
o=[b1(*v) for v in V_]
build(Z,CH,"二項分布の確率・期待値・分散",o,r"<p>$X\sim B(n,p)$：$P(X=k)={}_n\mathrm{C}_kp^k(1-p)^{n-k}$、$E(X)=np$、$V(X)=np(1-p)$。</p>","「$n$ 回中 $k$ 回成功」の並べ方（${}_n\\mathrm{C}_k$）× 成功確率 × 失敗確率。",1)
# 例題2 k回以上
def b2(n,p,k):
    p=R(p); q=1-p; ps=[comb(n,i)*p**i*q**(n-i) for i in range(n+1)]; ans=sum(ps[k:]); comp=1-sum(ps[:k])
    assert ans==comp
    use_c=(k<=n-k+1 and False) or (k<n/2)
    if k<=n//2+0:
        st=[("余事象を考える","<p>「"+I(r"%d"%k+r"\text{ 回以上}")+"」の余事象は「"+I(r"%d"%(k-1)+r"\text{ 回以下}")+"」。</p>"+D(r"P(X\geqq%d)=1-P(X\leqq%d)=1-\left(%s\right)"%(k,k-1,"+".join(r"P(X=%d)"%i for i in range(0,k))))),
            ("各確率",D(r"\\ ".join(r"P(X=%d)=%s"%(i,L(ps[i])) for i in range(0,k)))),
            ("答え",D(r"1-%s=%s"%(L(sum(ps[:k])),L(ans))))]
    else:
        st=[("直接たす","<p>"+I(r"X\geqq%d"%k)+" は "+I(r"X=%s"%",\\ ".join(str(i) for i in range(k,n+1)))+" の和。</p>"),
            ("各確率",D(r"\\ ".join(r"P(X=%d)=%s"%(i,L(ps[i])) for i in range(k,n+1)))),
            ("答え",D(r"P(X\geqq%d)=%s=%s"%(k,"+".join(L(ps[i]) for i in range(k,n+1)),L(ans))))]
    return r"1回の試行で事象 $A$ が起こる確率が $%s$ である。この試行を $%d$ 回くり返すとき、$A$ が $%d$ 回以上起こる確率を求めよ。"%(L(p),n,k),st,L(ans)
V_=[(5,R(1,2),3),(4,R(1,3),1),(6,R(1,2),5),(4,R(2,3),3),(5,R(1,3),4)]
o=[b2(*v) for v in V_]
build(Z,CH,"「k回以上」の確率",o,r"<p>「少なくとも1回」「$k$ 回以上」は、<b>余事象</b>（$1-$ 起こる回数が少ない場合）か、<b>直接足す</b>のどちらか簡単な方で。二項分布の確率 $P(X=i)$ を並べて計算する。</p>","足す項が少ないほうを選ぶ。多いときは 1 から引く（余事象）。",2)
# 例題3 正規分布
def b3(m,s,lo,hi):
    zl=R(lo-m,s) if lo is not None else None; zh=R(hi-m,s) if hi is not None else None
    def pf(z): return (pu(z) if z>=0 else -pu(z))
    if lo is None: prob=R(1,2)+pf(zh); form=r"P(X\leqq%d)=P(Z\leqq%s)"%(hi,L(zh)); setup=r"P(Z\leqq %s)=0.5%s"%(L(zh),("+" if zh>=0 else "-")+"p(%s)"%L(abs(zh)))
    elif hi is None: prob=R(1,2)-pf(zl); form=r"P(X\geqq%d)=P(Z\geqq%s)"%(lo,L(zl)); setup=r"P(Z\geqq %s)=0.5%s"%(L(zl),("-" if zl>=0 else "+")+"p(%s)"%L(abs(zl)))
    else: prob=pf(zh)-pf(zl); form=r"P(%d\leqq X\leqq%d)=P(%s\leqq Z\leqq%s)"%(lo,hi,L(zl),L(zh)); setup=r"=p(%s)+p(%s)"%(L(abs(zl)),L(abs(zh))) if zl<0<zh else r"=p(%s)-p(%s)"%(L(abs(zh)),L(abs(zl)))
    vl=("0.5+%s"%dec(pu(zh)) if zh is not None and lo is None and zh>=0 else "0.5-%s"%dec(pu(zh)) if lo is None else "0.5-%s"%dec(pu(zl)) if hi is None and zl>=0 else "0.5+%s"%dec(pu(zl)) if hi is None else "%s+%s"%(dec(pu(zl)),dec(pu(zh))) if zl<0<zh else "%s-%s"%(dec(pu(zh)),dec(pu(zl))))
    rng=("X\\leqq %d"%hi if lo is None else "X\\geqq %d"%lo if hi is None else "%d\\leqq X\\leqq %d"%(lo,hi))
    st=[("標準化する","<p>"+I(r"Z=\dfrac{X-m}{\sigma}")+" は標準正規分布 "+I("N(0,1)")+" に従う。</p>"+D(r"Z=\dfrac{X-%d}{%d}"%(m,s))),
        ("$Z$ の範囲に直す",D(form)),
        ("正規分布表を使う","<p>"+I(r"p(u)=P(0\leqq Z\leqq u)")+"、左右対称で "+I("P(Z\\geqq0)=0.5")+"。</p>"+"<p>標準正規分布の曲線で、求める面積（青い部分）を図にする。</p>"+normfig("nb3_%s_%s"%(("m" if zl is None else "%g"%float(zl)),("m" if zh is None else "%g"%float(zh))),zl,zh)+D(setup)+D(r"=%s=%s"%(vl,dec(prob))))]
    return r"確率変数 $X$ が正規分布 $N(%d,\ %d^2)$ に従うとき、$P(%s)$ を求めよ。%s"%(m,s,rng,TBL),st,dec(prob)
V_=[(50,10,40,65),(60,20,100,None),(170,6,158,176),(100,16,None,76),(30,4,26,38)]
o=[b3(*v) for v in V_]
build(Z,CH,"正規分布の確率（標準化）",o,r"<p>$X\sim N(m,\sigma^2)$ のとき $Z=\dfrac{X-m}{\sigma}\sim N(0,1)$。<b>標準化</b>して正規分布表で調べる。左右対称なので、負の $u$ は絶対値で調べ、$0$ をはさむか片側かで足し引きする。</p>","どんな正規分布も、平均を0・ばらつきを1にそろえれば同じ表で読める。",3)
# 例題4 正規近似
def b4(n,p,lo,hi):
    p=R(p); q=1-p; m=n*p; s2=n*p*q; s=sp.sqrt(s2); assert s.is_rational
    st=[("平均と標準偏差","<p>"+I(r"X\sim B(%d,\ %s)"%(n,L(p)))+"。$n$ が大きいので正規分布 "+I(r"N(m,\sigma^2)")+" で近似できる。</p>"+D(r"m=np=%s,\quad \sigma=\sqrt{npq}=\sqrt{%s}=%s"%(L(m),L(s2),L(s))))]
    zl=R(lo-m)/s if lo is not None else None; zh=R(hi-m)/s if hi is not None else None
    def pf(z): return (pu(z) if z>=0 else -pu(z))
    if hi is None: prob=R(1,2)-pf(zl); rng=r"X\geqq%d"%lo; zz=r"Z\geqq%s"%L(zl); fm=r"0.5%sp(%s)"%("-" if zl>=0 else "+",L(abs(zl)))
    elif lo is None: prob=R(1,2)+pf(zh); rng=r"X\leqq%d"%hi; zz=r"Z\leqq%s"%L(zh); fm=r"0.5%sp(%s)"%("+" if zh>=0 else "-",L(abs(zh)))
    else: prob=pf(zh)-pf(zl); rng=r"%d\leqq X\leqq%d"%(lo,hi); zz=r"%s\leqq Z\leqq%s"%(L(zl),L(zh)); fm=r"p(%s)+p(%s)"%(L(abs(zl)),L(abs(zh))) if zl<0<zh else r"p(%s)-p(%s)"%(L(abs(zh)),L(abs(zl)))
    st+= [("標準化する",D(r"Z=\dfrac{X-%s}{%s}"%(L(m),L(s)))+D(r"P(%s)=P(%s)"%(rng,zz))),
          ("正規分布表で求める","<p>求める面積（青い部分）を図にする。</p>"+normfig("nb45_%s_%s"%(("m" if zl is None else "%g"%float(zl)),("m" if zh is None else "%g"%float(zh))),zl,zh)+D(r"=%s=%s"%(fm,dec(prob))))]
    return r"1回の試行で事象 $A$ が起こる確率が $%s$ である。この試行を $%d$ 回くり返すとき、$A$ が起こる回数を $X$ とする。正規分布で近似して $P(%s)$ を求めよ。%s"%(L(p),n,rng,TBL),st,dec(prob)
V_=[(100,R(1,2),60,None),(400,R(1,2),180,215),(100,R(1,5),26,None),(900,R(1,10),None,72),(64,R(1,2),28,40)]
o=[b4(*v) for v in V_]
build(Z,CH,"二項分布の正規近似",o,r"<p>$n$ が大きいとき $B(n,p)$ は $N(np,\ npq)$ で近似できる。$m=np$、$\sigma=\sqrt{npq}$ を求め、標準化して表で確率を求める。</p>","回数が多くなるほど、二項分布のグラフはベル型（正規分布）に近づく。",4)
# 例題5 標本平均
def b5(m,s,n,lo,hi):
    sb=R(s)/sp.sqrt(n); assert sb.is_rational
    zl=R(lo-m)/sb if lo is not None else None; zh=R(hi-m)/sb if hi is not None else None
    def pf(z): return (pu(z) if z>=0 else -pu(z))
    if hi is None: prob=R(1,2)-pf(zl); rng=r"\overline X\geqq%s"%L(lo); zz=r"Z\geqq%s"%L(zl); fm=r"0.5%sp(%s)"%("-" if zl>=0 else "+",L(abs(zl)))
    elif lo is None: prob=R(1,2)+pf(zh); rng=r"\overline X\leqq%s"%L(hi); zz=r"Z\leqq%s"%L(zh); fm=r"0.5%sp(%s)"%("+" if zh>=0 else "-",L(abs(zh)))
    else: prob=pf(zh)-pf(zl); rng=r"%s\leqq\overline X\leqq%s"%(L(lo),L(hi)); zz=r"%s\leqq Z\leqq%s"%(L(zl),L(zh)); fm=r"p(%s)+p(%s)"%(L(abs(zl)),L(abs(zh))) if zl<0<zh else r"p(%s)-p(%s)"%(L(abs(zh)),L(abs(zl)))
    st=[("標本平均の分布","<p>母平均 "+I("m=%d"%m)+"、母標準偏差 "+I(r"\sigma=%d"%s)+"、標本の大きさ "+I("n=%d"%n)+"。</p>"+D(r"E(\overline X)=m=%d,\quad \sigma(\overline X)=\dfrac{\sigma}{\sqrt n}=\dfrac{%d}{\sqrt{%d}}=%s"%(m,s,n,L(sb)))+"<p>$n$ が大きいので $\\overline X$ は "+I(r"N\left(%d,\ %s^2\right)"%(m,L(sb)))+" に従うとみなせる。</p>"),
        ("標準化する",D(r"Z=\dfrac{\overline X-%d}{%s}"%(m,L(sb)))+D(r"P(%s)=P(%s)"%(rng,zz))),
        ("正規分布表で求める","<p>求める面積（青い部分）を図にする。</p>"+normfig("nb45_%s_%s"%(("m" if zl is None else "%g"%float(zl)),("m" if zh is None else "%g"%float(zh))),zl,zh)+D(r"=%s=%s"%(fm,dec(prob))))]
    return r"母平均 $%d$、母標準偏差 $%d$ の母集団から、大きさ $%d$ の標本を無作為に抽出する。標本平均 $\overline X$ について $P(%s)$ を求めよ。%s"%(m,s,n,rng,TBL),st,dec(prob)
V_=[(50,20,100,54,None),(200,30,36,190,R(415,2)),(60,12,16,None,54),(80,15,25,77,86),(10,4,64,R(43,4),None)]
o=[b5(*v) for v in V_]
build(Z,CH,"標本平均の分布",o,r"<p>標本平均 $\overline X$ は $E(\overline X)=m$、<b>$\sigma(\overline X)=\dfrac{\sigma}{\sqrt n}$</b>。$n$ が大きいと $N\!\left(m,\dfrac{\sigma^2}{n}\right)$ に従う。標準化して表で確率を求める。</p>","平均をとると、ばらつきは $\\frac1{\\sqrt n}$ に縮む。人数が多いほど、平均は母平均に近づく。",5)
UNIT=finish(Z,CH,1,1,"統計的な推測","二項分布・正規分布","二項分布、正規分布、正規近似、標本平均の分布まで、確率分布の応用を問う難問に挑みます。",subject="B")
