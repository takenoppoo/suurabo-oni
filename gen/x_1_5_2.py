# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational; s=sp.sqrt
# 6 分散の公式
def b6(n,Sx,Sxx):
    m=R(Sx,n); var=R(Sxx,n)-m**2; assert var>0
    st=[("平均","<p>"+I(r"\bar x=\dfrac{%d}{%d}=%s"%(Sx,n,L(m)))+"。</p>"),
        ("分散の公式","<p>"+I(r"s^2=\overline{x^2}-(\bar x)^2")+"（2乗の平均 − 平均の2乗）。</p>"+D(r"\overline{x^2}=\dfrac{%d}{%d}=%s"%(Sxx,n,L(R(Sxx,n))))),
        ("計算",D(r"s^2=%s-\left(%s\right)^2=%s"%(L(R(Sxx,n)),L(m),L(var)))+"<p>標準偏差 "+I(r"s=%s"%L(s(var)))+"。</p>")]
    return r"$%d$ 個のデータ $x_1,\cdots,x_{%d}$ について、$\sum x_i=%d$、$\sum x_i^2=%d$ である。分散と標準偏差を求めよ。"%(n,n,Sx,Sxx),st,r"s^2=%s,\ \ s=%s"%(L(var),L(s(var)))
o=[b6(*v) for v in [(5,30,200),(8,48,340),(10,80,700),(6,36,250),(4,40,420)]]
build(Z,CH,"分散の公式（2乗の平均−平均の2乗）",o,r"<p>$s^2=\overline{x^2}-(\bar x)^2$。値が分からなくても、<b>合計と2乗の合計</b>だけで分散が求まる。</p>","個々を見ずに、集計値だけで散らばりを出す。",6)
# 7 残りの2つ
def b7(known,m,var):
    n=len(known)+2; S=n*m; Sq=n*(var+m*m); rest_sum=S-sum(known); rest_sq=Sq-sum(v*v for v in known)
    # u+v=rest_sum, u^2+v^2=rest_sq
    p_=R(rest_sum**2-rest_sq,2); X=sp.Symbol('X'); sols=sp.solve(X**2-rest_sum*X+p_,X); assert all(v.is_integer for v in sols)
    data=known+sols; assert sum(data)==S and sum(v*v for v in data)==Sq
    st=[("合計の条件","<p>残り2つを "+I("a,\\ b")+" とする。平均が "+I(str(m))+"、"+I(str(n))+" 個の合計は "+I(str(S))+"。</p>"+D(r"a+b=%d-(%s)=%d"%(S,"+".join(str(v) for v in known),rest_sum))),
        ("2乗の合計の条件","<p>分散が "+I(str(var))+" なので "+I(r"\overline{x^2}=%d+%d^2=%d"%(var,m,var+m*m))+"。2乗の合計は "+I(str(Sq))+"。</p>"+D(r"a^2+b^2=%d-(%s)=%d"%(Sq,"+".join(str(v*v) for v in known),rest_sq))),
        ("$a,b$ を求める","<p>"+I(r"ab=\dfrac{(a+b)^2-(a^2+b^2)}{2}=%d"%p_)+"。"+I("a,b")+" は2次方程式 "+I(r"X^2-%dX+%d=0"%(rest_sum,p_))+" の解。</p>"+D(r"X=%s"%(r",\ ".join(str(v) for v in sols))))]
    return r"%d個のデータ $%s,\ a,\ b$ の平均値が $%d$、分散が $%d$ であるとき、$a,\ b$ の値を求めよ。（$a<b$）"%(n,r",\ ".join(str(v) for v in known),m,var),st,r"a=%s,\ b=%s"%(sols[0],sols[1])
o=[b7(*v) for v in [([2,5,6],5,4),([4,7,8],6,10),([3,6,9],7,10),([2,8,9],7,10),([4,7,8],7,6)]]
build(Z,CH,"平均と分散から残りのデータを求める",o,r"<p>平均から<b>和 $a+b$</b>、分散から<b>2乗の和 $a^2+b^2$</b>。$ab=\dfrac{(a+b)^2-(a^2+b^2)}2$ を作り、$a,b$ を解とする2次方程式を解く。</p>","和と2乗の和が分かれば、2つの数は特定できる。",7)
# 8 y=ax+b の関係
def b8(a,b,d):
    xs=d; ys=[a*v+b for v in d]; n=len(d)
    mx=R(sum(xs),n); vx=R(sum(v*v for v in xs),n)-mx**2; my=a*mx+b; vy=a*a*vx
    cov=sp.Rational(sum((xv-mx)*(yv-my) for xv,yv in zip(xs,ys)),n); r_=cov/(s(vx)*s(vy)); r_=sp.simplify(r_); assert r_==(1 if a>0 else -1)
    st=[("$y$ の平均・分散","<p>"+I("y=%sx%+d"%(L(a),b))+"。</p>"+D(r"\bar y=%s\bar x%+d=%s,\qquad s_y^2=%s^2s_x^2=%s"%(L(a),b,L(my),L(a),L(vy)))),
        ("共分散","<p>"+I(r"s_{xy}=\dfrac1n\sum(x-\bar x)(y-\bar y)=%s\cdot s_x^2"%L(a))+"。</p>"+D(r"s_{xy}=%s\cdot%s=%s"%(L(a),L(vx),L(cov)))),
        ("相関係数",D(r"r=\dfrac{s_{xy}}{s_xs_y}=\dfrac{%s}{\sqrt{%s}\sqrt{%s}}=%s"%(L(cov),L(vx),L(vy),L(r_))))]
    return r"データ $x:\ %s$ と、$y=%sx%+d$ で定まるデータ $y$ について、$y$ の平均・分散と、$x,\ y$ の相関係数を求めよ。"%(r",\ ".join(str(v) for v in xs),L(a),b),st,r"\bar y=%s,\ s_y^2=%s,\ r=%s"%(L(my),L(vy),L(r_))
o=[b8(*v) for v in [(2,3,[1,3,4,6,6]),(-3,10,[2,4,5,7,2]),(4,-1,[1,2,3,6]),(-2,8,[3,5,4,2,6]),(3,5,[2,4,6,8])]]
build(Z,CH,"変量の1次変換と相関係数（r=±1）",o,r"<p>$y=ax+b$ なら $\bar y=a\bar x+b$、$s_y^2=a^2s_x^2$、<b>$s_{xy}=a\,s_x^2$</b>。相関係数は $a>0$ で $1$、$a<0$ で $-1$。</p>","点が1本の直線上に並べば、相関は完全。右上がりなら+1、右下がりなら−1。",8)
# 9 度数分布表の分散
def b9(cls,freq):
    n=sum(freq); mid=[R(a+b,2) for a,b in cls]; m=sum(f*v for f,v in zip(freq,mid))/n; Sxx=sum(f*v*v for f,v in zip(freq,mid)); var=Sxx/n-m**2
    hdr="".join("<th>%d以上%d未満</th>"%(a,b) for a,b in cls)+"<th>計</th>"; row="".join("<td>%d</td>"%f for f in freq)+"<td>%d</td>"%n
    tbl='<table class="tbl"><tr>%s</tr><tr>%s</tr></table>'%(hdr,row)
    st=[("階級値と平均","<p>階級値 "+I(r"%s"%(r",\ ".join(L(v) for v in mid)))+"。</p>"+D(r"\bar x=\dfrac{%s}{%d}=%s"%("+".join("%s\\times%d"%(L(v),f) for v,f in zip(mid,freq)),n,L(m)))),
        ("2乗の平均","<p>"+I(r"\overline{x^2}=\dfrac{%s}{%d}"%("+".join("%s^2\\times%d"%(L(v),f) for v,f in zip(mid,freq)),n))+"。</p>"+D(r"=\dfrac{%s}{%d}=%s"%(L(Sxx),n,L(Sxx/n)))),
        ("分散と標準偏差",D(r"s^2=%s-\left(%s\right)^2=%s"%(L(Sxx/n),L(m),L(var)))+"<p>"+I(r"s=%s"%L(s(var)))+"。</p>")]
    return r"次の度数分布表のデータの平均値と分散を、階級値を使って求めよ。"+tbl,st,r"\bar x=%s,\ \ s^2=%s"%(L(m),L(var))
o=[b9(*v) for v in [([(0,10),(10,20),(20,30),(30,40)],[2,6,8,4]),([(10,20),(20,30),(30,40),(40,50)],[3,7,7,3]),([(0,20),(20,40),(40,60),(60,80)],[2,5,10,3]),([(50,60),(60,70),(70,80),(80,90)],[4,8,6,2]),([(0,4),(4,8),(8,12),(12,16)],[5,10,3,2])]]
build(Z,CH,"度数分布表から分散を求める",o,r"<p>階級値を使い、<b>度数を重みにして</b>平均 $\bar x$ と $\overline{x^2}$ を出し、$s^2=\overline{x^2}-\bar x^2$。</p>","まとめた表でも、重み（度数）を使えば同じ公式。",9)
# 10 平均を足したとき
def b10(n,m,var,v):
    n2=n+1; m2=R(n*m+v,n2); S2=n*(var+m*m)+v*v; var2=R(S2,n2)-m2**2
    st=[("もとの量","<p>合計 "+I(str(n*m))+"、2乗の合計 "+I(r"%d\times(%d+%d^2)=%d"%(n,var,m,n*(var+m*m)))+"。</p>"),
        ("1つ加えたあの量","<p>"+I("%d"%v)+" を加えて "+I(str(n2))+" 個。</p>"+D(r"\bar x'=\dfrac{%d+%d}{%d}=%s"%(n*m,v,n2,L(m2)))+D(r"\overline{x^2}'=\dfrac{%d+%d}{%d}=%s"%(n*(var+m*m),v*v,n2,L(R(S2,n2))))),
        ("新しい分散",D(r"s'^2=%s-\left(%s\right)^2=%s"%(L(R(S2,n2)),L(m2),L(var2))))]
    return r"%d個のデータの平均値が $%d$、分散が $%d$ である。ここに値 $%d$ のデータを1つ加えたとき、新しい平均値と分散を求めよ。"%(n,m,var,v),st,r"\bar x'=%s,\ \ s'^2=%s"%(L(m2),L(var2))
o=[b10(*v) for v in [(9,10,6,10),(5,20,8,26),(7,15,4,15),(11,8,10,8),(4,12,5,17)]]
build(Z,CH,"データを1つ加えたときの平均・分散",o,r"<p>平均・分散から<b>合計と2乗の合計</b>に戻して、新しいデータを加え、もう一度 $s^2=\overline{x^2}-\bar x^2$。平均値を加えると平均は変わらず分散は小さくなる。</p>","足し算の世界（合計）に戻してから、また平均の世界へ。",10)
XU=finishx(Z,CH)
