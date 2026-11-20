# -*- coding: utf-8 -*-
from bh import *
from math import comb
Z=U_(); CH=[]
R=sp.Rational
def tab(xs,ps):
    r1="<th>"+I("X")+"</th>"+"".join("<td>"+I(L(v))+"</td>" for v in xs)+"<td>"+"計"+"</td>"
    r2="<th>"+I("P")+"</th>"+"".join("<td>"+I(L(v))+"</td>" for v in ps)+"<td>"+I("1")+"</td>"
    return '<table class="tbl"><tr>'+r1+"</tr><tr>"+r2+"</tr></table>"
def sig(v):
    s=sp.sqrt(v); return L(sp.nsimplify(s))
# 例題1
def b1(xs,ws):
    tot=sum(ws); a=R(1,tot); ps=[a*w for w in ws]; E=sum(x_*p for x_,p in zip(xs,ps)); E2=sum(x_**2*p for x_,p in zip(xs,ps)); V=E2-E**2
    assert sum(ps)==1 and V==sum((x_-E)**2*p for x_,p in zip(xs,ps))
    pr=", ".join(r"P(X=%d)=%s"%(x_,("a" if w==1 else "%da"%w)) for x_,w in zip(xs,ws))
    st=[("確率の和が1","<p>"+I(r"%s=1"%("+".join(("a" if w==1 else "%da"%w) for w in ws)))+" より</p>"+D(r"%da=1\ \Rightarrow\ a=%s"%(tot,L(a)))+tab(xs,ps)),
        ("期待値 $E(X)$","<p>"+I(r"E(X)=\sum x_ip_i")+"。</p>"+D(r"E(X)=%s=%s"%("+".join(r"%s\cdot%s"%(P(x_),L(p)) for x_,p in zip(xs,ps)),L(E)))),
        ("$E(X^2)$ と分散","<p>"+I(r"V(X)=E(X^2)-\{E(X)\}^2")+"。</p>"+D(r"E(X^2)=%s=%s"%("+".join(r"%d\cdot%s"%(x_**2,L(p)) for x_,p in zip(xs,ps)),L(E2)))+D(r"V(X)=%s-\left(%s\right)^2=%s"%(L(E2),L(E),L(V)))),
        ("標準偏差",D(r"\sigma(X)=\sqrt{V(X)}=\sqrt{%s}=%s"%(L(V),sig(V))))]
    return r"確率変数 $X$ の確率分布が $%s$ で与えられる（$a$ は定数）。$a$ の値、$E(X)$、$V(X)$、$\sigma(X)$ を求めよ。"%pr,st,r"a=%s,\ E(X)=%s,\ V(X)=%s,\ \sigma(X)=%s"%(L(a),L(E),L(V),sig(V))
V_=[([1,2,3,4],[1,2,3,4]),([0,1,2,3],[1,3,3,1]),([-1,0,1,2],[2,3,3,2]),([2,4,6,8],[4,3,2,1]),([1,3,5],[1,2,1])]
o=[b1(*v) for v in V_]
build(Z,CH,"確率分布と期待値・分散",o,r"<p>$\sum p_i=1$、$E(X)=\sum x_ip_i$、$V(X)=E(X^2)-\{E(X)\}^2$、$\sigma(X)=\sqrt{V(X)}$。まず確率の和＝1 で未知の定数を決める。</p>","期待値は「平均してこのくらい」、分散は「平均からのばらつき」。分散は2乗の平均−平均の2乗。",1)
# 例題2 1次変換
def b2(m,v,a,b):
    m=R(m); v=R(v); EY=a*m+b; VY=a**2*v; EX2=v+m**2
    st=[("$E(X^2)$","<p>"+I(r"V(X)=E(X^2)-\{E(X)\}^2")+" より</p>"+D(r"E(X^2)=V(X)+\{E(X)\}^2=%s+%s^2=%s"%(L(v),L(m),L(EX2)))),
        ("$E(aX+b)$","<p>"+I(r"E(aX+b)=aE(X)+b")+"。</p>"+D(r"E(Y)=%s\times%s%s=%s"%(P(a),L(m),("+"+L(b) if b>0 else L(b)),L(EY)))),
        ("$V(aX+b)$","<p>"+I(r"V(aX+b)=a^2V(X)")+"（$b$ は分散に影響しない）。</p>"+D(r"V(Y)=%s^2\times%s=%s"%(P(a),L(v),L(VY)))),
        ("標準偏差",D(r"\sigma(Y)=|%s|\,\sigma(X)=%s\times%s=%s"%(L(a),L(abs(a)),sig(v),L(abs(a)*sp.sqrt(v)))))]
    return r"確率変数 $X$ について $E(X)=%s,\ V(X)=%s$ である。$Y=%sX%s$ のとき、$E(X^2)$、$E(Y)$、$V(Y)$、$\sigma(Y)$ を求めよ。"%(L(m),L(v),L(a),("+"+L(b) if b>0 else L(b))),st,r"E(X^2)=%s,\ E(Y)=%s,\ V(Y)=%s,\ \sigma(Y)=%s"%(L(EX2),L(EY),L(VY),L(abs(a)*sp.sqrt(v)))
V_=[(3,4,2,-1),(5,9,-3,2),(4,25,2,3),(-2,4,-1,5),(6,36,-2,7)]
o=[b2(*v) for v in V_]
build(Z,CH,"aX+b の期待値・分散",o,r"<p>$E(aX+b)=aE(X)+b$、<b>$V(aX+b)=a^2V(X)$</b>、$\sigma(aX+b)=|a|\sigma(X)$。定数 $b$ は平均をずらすだけで、ばらつきは変えない。</p>","全体をずらす（$+b$）とばらつきは不変。$a$ 倍に拡大すると、ばらつきは $a^2$ 倍。",2)
# 例題3 独立な和
def b3(m1,v1,m2,v2,a,b):
    EZ=a*m1+b*m2; VZ=a**2*v1+b**2*v2; EXY=m1*m2
    st=[("期待値（独立でなくても成り立つ）","<p>"+I(r"E(aX+bY)=aE(X)+bE(Y)")+"。</p>"+D(r"E(Z)=%s\times%s+%s\times%s=%s"%(P(a),L(m1),P(b),L(m2),L(EZ)))),
        ("分散（独立のとき）","<p>"+I(r"X,Y")+" が独立なら "+I(r"V(aX+bY)=a^2V(X)+b^2V(Y)")+"。</p>"+D(r"V(Z)=%s^2\times%s+%s^2\times%s=%s"%(P(a),L(v1),P(b),L(v2),L(VZ)))),
        ("積の期待値","<p>独立なら "+I(r"E(XY)=E(X)E(Y)")+"。</p>"+D(r"E(XY)=%s\times%s=%s"%(L(m1),L(m2),L(EXY))))]
    return r"独立な確率変数 $X,Y$ について、$E(X)=%s,\ V(X)=%s,\ E(Y)=%s,\ V(Y)=%s$ である。$Z=%sX%s Y$ として、$E(Z)$、$V(Z)$、$E(XY)$ を求めよ。"%(L(m1),L(v1),L(m2),L(v2),L(a),("+"+L(b) if b>0 else L(b))),st,r"E(Z)=%s,\ V(Z)=%s,\ E(XY)=%s"%(L(EZ),L(VZ),L(EXY))
V_=[(3,4,5,9,2,3),(2,1,4,2,3,-1),(6,5,1,3,-2,4),(10,16,5,4,1,-2),(4,2,3,6,5,2)]
o=[b3(*v) for v in V_]
build(Z,CH,"独立な確率変数の和",o,r"<p>$E(X+Y)=E(X)+E(Y)$（常に）。独立なら $V(X+Y)=V(X)+V(Y)$、$E(XY)=E(X)E(Y)$。<b>差でも分散は足す</b>：$V(X-Y)=V(X)+V(Y)$。</p>","平均はふつうに足し引き。ばらつきは、独立なら足し算（引いても足す）。",3)
# 例題4 くじ
def b4(prizes,N,fee):
    tot=sum(c for pz,c in prizes); EXv=R(sum(pz*c for pz,c in prizes),N)
    st=[("賞金の確率分布","<p>"+"、".join("%d 円が %d 本（確率 "%(pz,c)+I(L(R(c,N)))+"）" for pz,c in prizes)+"、はずれ（0円）が %d 本（確率 "%(N-tot)+I(L(R(N-tot,N)))+"）。</p>"),
        ("賞金の期待値",D(r"E(X)=%s=%s"%("+".join(r"%d\times%s"%(pz,L(R(c,N))) for pz,c in prizes),L(EXv)))+"<p>1本引いたときの賞金の期待値は "+I(L(EXv)+r"\text{ 円}")+"。</p>"),
        ("参加料との比較","<p>参加料が期待値と等しければ得も損もしない（公平）。</p>"+D(r"\text{公平な参加料}=%s\ \text{円}"%L(EXv))+"<p>参加料 "+I("%d"%fee+r"\text{ 円}")+" のとき、1回あたりの期待される損益は "+I(r"%s-%d=%s\text{ 円}"%(L(EXv),fee,L(EXv-fee)))+("（得）" if EXv>fee else "（損）")+"。</p>")]
    return r"%d 本のくじの中に、賞金 %s のくじが入っている（残りははずれ）。1本引いたときの賞金 $X$ 円の期待値を求めよ。また、参加料が $%d$ 円のとき、得か損かを答えよ。"%(N,"、".join("%d 円が %d 本"%(pz,c) for pz,c in prizes),fee),st,r"E(X)=%s,\ %s"%(L(EXv),"得" if EXv>fee else "損")
V_=[([(1000,1),(100,5)],100,12),([(500,2),(100,8)],200,10),([(10000,1),(1000,4),(100,20)],500,20),([(300,3),(50,12)],100,15),([(2000,1),(500,3)],250,10)]
o=[b4(*v) for v in V_]
build(Z,CH,"くじの期待値",o,r"<p>期待値 $E(X)=\sum(\text{賞金})\times(\text{確率})$。期待値と参加料を比べ、<b>期待値 $>$ 参加料なら得、$<$ なら損</b>。はずれ（賞金0）は式に入れなくてよい。</p>","何度も引いたときの1回あたりの平均が期待値。参加料より大きければ、続けるほど得。",4)
# 例題5 超幾何
def b5(w,r_,d):
    ps=[R(comb(w,i)*comb(r_,d-i),comb(w+r_,d)) for i in range(0,d+1) if i<=w and d-i<=r_]; xs=[i for i in range(0,d+1) if i<=w and d-i<=r_]
    assert sum(ps)==1; E=sum(x_*p for x_,p in zip(xs,ps)); E2=sum(x_**2*p for x_,p in zip(xs,ps)); V=E2-E**2
    st=[("確率を求める","<p>"+I(r"X=k")+" のとき、白 $k$ 個、赤 $%d-k$ 個。</p>"%d+D(r"P(X=k)=\dfrac{{}_{%d}\mathrm{C}_k\cdot{}_{%d}\mathrm{C}_{%d-k}}{{}_{%d}\mathrm{C}_{%d}}"%(w,r_,d,w+r_,d))+D(r"\ ,\ ".join(r"P(X=%d)=%s"%(x_,L(p)) for x_,p in zip(xs,ps)))+tab(xs,ps)),
        ("期待値",D(r"E(X)=%s=%s"%("+".join(r"%d\cdot%s"%(x_,L(p)) for x_,p in zip(xs,ps)),L(E)))),
        ("分散",D(r"E(X^2)=%s,\quad V(X)=%s-\left(%s\right)^2=%s"%(L(E2),L(E2),L(E),L(V))))]
    return r"白玉 $%d$ 個と赤玉 $%d$ 個が入った袋から、同時に $%d$ 個を取り出すとき、取り出した白玉の個数を $X$ とする。$X$ の確率分布、$E(X)$、$V(X)$ を求めよ。"%(w,r_,d),st,r"E(X)=%s,\ V(X)=%s"%(L(E),L(V))
V_=[(3,2,2),(4,3,3),(5,3,3),(4,2,3),(3,4,3)]
o=[b5(*v) for v in V_]
build(Z,CH,"組合せから作る確率分布",o,r"<p>$P(X=k)=\dfrac{{}_{w}\mathrm{C}_k\,{}_{r}\mathrm{C}_{d-k}}{{}_{w+r}\mathrm{C}_d}$ で分布表を作る。確率の和が1か確認して、$E(X)$、$E(X^2)$、$V(X)$ へ。</p>","取り出し方の総数（分母）のうち、条件に合う組合せ（分子）を数える。",5)
UNIT=finish(Z,CH,1,0,"統計的な推測","確率分布","期待値・分散、1次変換、独立な和、くじ、組合せから作る分布まで、確率分布の総合力を問う難問に挑みます。",subject="B")
