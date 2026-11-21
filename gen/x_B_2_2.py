# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational
def Phi(z): return 0.5*(1+math.erf(z/math.sqrt(2)))
def f4(v): return "%.4f"%v
# 6 二項分布で確率最大の k
def b6(n,p):
    pr=[math.comb(n,k)*float(p)**k*float(1-p)**(n-k) for k in range(n+1)]; km=max(range(n+1),key=lambda k:pr[k])
    c=(n+1)*p
    st=[("比をとる","<p>"+D(r"\dfrac{P(X=k+1)}{P(X=k)}=\dfrac{(%d-k)\cdot%s}{(k+1)\cdot%s}"%(n,L(p),L(1-p)))),
        ("1より大きい条件","<p>"+D(r"\dfrac{%d-k}{k+1}\cdot\dfrac{%s}{%s}>1\iff k<%s"%(n,L(p),L(1-p),L(c-1)))+"</p>"),
        ("最大の $k$","<p>"+I("(n+1)p=%s"%L(c))+" の整数部分 "+I("k=%d"%km)+" のとき確率が最大。</p>")]
    return r"二項分布 $B\left(%d,\ %s\right)$ に従う確率変数 $X$ について、$P(X=k)$ が最大になる $k$ を求めよ。"%(n,L(p)),st,"k=%d"%km
o=[b6(*v) for v in [(10,R(1,3)),(20,R(1,4)),(15,R(2,5)),(12,R(1,2)),(25,R(1,5))]]
build(Z,CH,"二項分布で確率が最大になる k",o,"<p>$\\dfrac{P(X=k+1)}{P(X=k)}=\\dfrac{(n-k)p}{(k+1)(1-p)}$ を1と比べる。確率が最大の $k$ は $\\lfloor(n+1)p\\rfloor$（$(n+1)p$ が整数のときは2つ）。</p>","ふえる間は上り坂、ふえなくなる所が頂上。",6)
# 7 正規分布の逆
def b7(mu,sg,z,pct):
    x_=mu+z*sg
    st=[("標準化","<p>"+I("Z=\\dfrac{X-%d}{%d}"%(mu,sg))+" は標準正規分布 "+I("N(0,1)")+" に従う。</p>"),
        ("正規分布表","<p>"+I("P(Z\\geqq %s)=%s"%(("%.2f"%z),f4(1-Phi(z))))+"。つまり上位 "+I(pct.replace("%","\\%"))+" に入る境界は "+I("Z=%.2f"%z)+"。</p>"),
        ("元に戻す","<p>"+D(r"X=%d+%.2f\times%d=%s"%(mu,z,sg,("%.1f"%x_))))]
    return r"ある試験の得点 $X$ は、平均 $%d$、標準偏差 $%d$ の正規分布に従う。上位 $%s$ に入るには何点以上必要か。（$P(Z\geqq%.2f)=%s$ を用いてよい）"%(mu,sg,pct.replace("%","\\%"),z,f4(1-Phi(z))),st,r"%.1f\text{点以上}"%x_
o=[b7(*v) for v in [(60,10,1.64,"5%"),(70,8,1.28,"10%"),(50,12,1.96,"2.5%"),(65,9,2.33,"1%"),(55,15,0.67,"25%")]]
build(Z,CH,"正規分布で上位の得点ライン",o,"<p>上位 $a\\%$ の境界の $Z$ を正規分布表から読み、$X=\\mu+Z\\sigma$ で元の得点に戻す。</p>","標準化の逆をたどって、元のものさしに戻す。",7)
# 8 正規近似
def b8(n,p,a):
    mu=n*float(p); sg=math.sqrt(n*float(p)*(1-float(p))); z=(a-0.5-mu)/sg
    ex=sum(math.comb(n,k)*float(p)**k*float(1-p)**(n-k) for k in range(a,n+1))
    ap=1-Phi((a-0.5-mu)/sg)
    st=[("近似","<p>"+I("np=%s"%("%g"%mu))+"、"+I("\\sqrt{np(1-p)}=%.2f"%sg)+"。"+I("X")+" は "+I("N(%g,\\ %.2f^2)"%(mu,sg))+" で近似。</p>"),
        ("標準化","<p>"+I(r"P(X\geqq %d)\fallingdotseq P(Z\geqq %.2f)"%(a,(a-mu)/sg))+"。</p>"),
        ("確率","<p>"+D(r"P(Z\geqq %.2f)=%s"%((a-mu)/sg,f4(1-Phi((a-mu)/sg)))))]
    return r"1個のさいころを $%d$ 回投げるとき、1の目が $%d$ 回以上出る確率を、正規分布で近似して求めよ（連続修正なし）。"%(n,a) if p==R(1,6) else r"成功確率 $%s$ の試行を $%d$ 回くり返すとき、成功が $%d$ 回以上となる確率を、正規分布で近似して求めよ（連続修正なし）。"%(L(p),n,a),st,f4(1-Phi((a-mu)/sg))
o=[b8(*v) for v in [(180,R(1,6),40),(100,R(1,2),60),(400,R(1,4),120),(300,R(1,5),70),(200,R(1,10),30)]]
build(Z,CH,"二項分布の正規近似",o,"<p>$n$ が大きいとき $B(n,p)$ は $N(np,\\ np(1-p))$ で近似できる。平均 $np$ と標準偏差 $\\sqrt{np(1-p)}$ で標準化し、正規分布表を読む。</p>","回数が多いと、二項分布は釣り鐘の形に近づく。",8)
# 9 標本平均
def b9(mu,sg,n,a):
    se=sg/math.sqrt(n); z=(a-mu)/se
    st=[("標本平均の分布","<p>"+I(r"E(\overline X)=%d,\quad \sigma(\overline X)=\dfrac{%d}{\sqrt{%d}}=%.2f"%(mu,sg,n,se))+"。</p>"),
        ("標準化","<p>"+I(r"Z=\dfrac{\overline X-%d}{%.2f}"%(mu,se))+"。"+I(r"\overline X\geqq%d"%a)+" は "+I("Z\\geqq %.2f"%z)+"。</p>"),
        ("確率","<p>"+D(r"P(Z\geqq %.2f)=%s"%(z,f4(1-Phi(z)))))]
    return r"母平均 $%d$、母標準偏差 $%d$ の母集団から大きさ $%d$ の無作為標本を抽出する。標本平均 $\overline X$ が $%d$ 以上となる確率を求めよ。"%(mu,sg,n,a),st,f4(1-Phi(z))
o=[b9(*v) for v in [(50,10,25,52),(100,15,36,103),(70,12,16,73),(30,6,49,31),(80,20,100,83)]]
build(Z,CH,"標本平均が基準以上になる確率",o,"<p>標本平均 $\\overline X$ の平均は $\\mu$、標準偏差は $\\dfrac{\\sigma}{\\sqrt n}$。これで標準化して正規分布表を使う。</p>","標本が多いほど平均は母平均に近づく。",9)
# 10 連続確率変数
def b10(c,a):
    x=sp.symbols("x"); f=c*x*(a-x)
    tot=sp.integrate(f,(x,0,a)); cc=1/sp.integrate(x*(a-x),(x,0,a)); EX=sp.integrate(cc*x*x*(a-x),(x,0,a)); EX2=sp.integrate(cc*x**3*(a-x),(x,0,a)); VX=sp.simplify(EX2-EX**2)
    st=[("全体で1","<p>"+D(r"\int_0^{%d}kx(%d-x)dx=1\ \Rightarrow\ k\cdot\dfrac{%d^3}{6}=1\ \Rightarrow\ k=%s"%(a,a,a,L(cc)))),
        ("期待値","<p>"+D(r"E(X)=\int_0^{%d}x\cdot%s\,x(%d-x)dx=%s"%(a,L(cc),a,L(EX)))),
        ("分散","<p>"+D(r"E(X^2)=%s,\qquad V(X)=%s-\left(%s\right)^2=%s"%(L(EX2),L(EX2),L(EX),L(VX))))]
    return r"確率密度関数が $f(x)=kx(%d-x)\ (0\leqq x\leqq%d)$、それ以外で $0$ である連続型確率変数 $X$ がある。$k$、$E(X)$、$V(X)$ を求めよ。"%(a,a),st,r"k=%s,\ E(X)=%s,\ V(X)=%s"%(L(cc),L(EX),L(VX))
o=[b10(1,a) for a in [2,3,4,6,5]]
build(Z,CH,"連続型確率変数の期待値・分散（確率密度関数）",o,"<p>① 全区間の積分が $1$ から $k$。② $E(X)=\\int xf(x)dx$。③ $V(X)=E(X^2)-\\{E(X)\\}^2$。</p>","面積が1になるように高さを調整して、重心が期待値。",10)
XU=finishx(Z,CH)
