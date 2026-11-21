# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; n=sp.symbols("n")
# 6 等差数列 項の条件から
def b6(a5,a9,S):
    d=R(a9-a5,4); a1=a5-4*d; an=a1+(n-1)*d
    Sn=sp.expand(n*(2*a1+(n-1)*d)/2)
    nn=[m for m in range(1,400) if Sn.subs(n,m)==S]; assert nn
    st=[("初項と公差","<p>"+D(r"a_9-a_5=4d=%d\ \Rightarrow\ d=%s"%(a9-a5,L(d)))+"<p>"+I(r"a_1=a_5-4d=%s"%L(a1))+"。</p>"),
        ("和の式","<p>"+D(r"S_n=\dfrac n2\{2\cdot%s+(n-1)\cdot%s\}=%s"%(L(a1),L(d),L(Sn)))),
        ("$S_n=%d$ を解く"%S,D(r"%s=%d\ \Rightarrow\ n=%d"%(L(Sn),S,nn[0])))]
    return r"等差数列 $\{a_n\}$ について $a_5=%d,\ a_9=%d$ である。初項と公差を求め、初項から第 $n$ 項までの和 $S_n$ が $%d$ になるときの $n$ を求めよ。"%(a5,a9,S),st,r"a_1=%s,\ d=%s,\ n=%d"%(L(a1),L(d),nn[0])
o=[b6(*v) for v in [(11,27,230) if False else (11,27,0),(7,19,0),(5,17,0),(9,25,0),(3,15,0)]] if False else None
def mk(a1,d,m):
    S=sum(a1+d*i for i in range(m)); return (a1+4*d,a1+8*d,S)
o=[b6(*mk(a1,d,m)) for a1,d,m in [(3,2,10),(5,3,8),(2,4,12),(1,5,9),(4,3,15)]]
build(Z,CH,"等差数列の2項から初項・公差・和",o,"<p>2項の差から<b>公差</b>、そこから初項。和は $S_n=\\dfrac n2\\{2a_1+(n-1)d\\}$。$S_n=$ 値 を $n$ の2次方程式として解く（$n$ は正の整数）。</p>","2つの地点の高さの差から、坂の傾きが分かる。",6)
# 7 等比数列
def b7(a2,a5,m):
    r3=R(a5,a2); r=sp.real_root(r3,3); assert r**3==r3 and r.is_rational
    a1=R(a2)/r; Sn=a1*(r**m-1)/(r-1)
    st=[("公比","<p>"+D(r"\dfrac{a_5}{a_2}=r^3=%s\ \Rightarrow\ r=%s"%(L(r3),L(r)))),
        ("初項","<p>"+D(r"a_1=\dfrac{a_2}{r}=\dfrac{%d}{%s}=%s"%(a2,L(r),L(a1)))),
        ("和",D(r"S_{%d}=\dfrac{%s(%s^{%d}-1)}{%s-1}=%s"%(m,L(a1),L(r),m,L(r),L(Sn))))]
    return r"等比数列 $\{a_n\}$ について $a_2=%d,\ a_5=%d$（公比は実数）。初項から第 $%d$ 項までの和を求めよ。"%(a2,a5,m),st,L(Sn)
o=[b7(*v) for v in [(6,162,6),(4,32,8),(12,96,7),(-3,81,5),(10,80,6)]]
build(Z,CH,"等比数列の2項から公比・和",o,"<p>$\\dfrac{a_5}{a_2}=r^3$ で公比を求め、$a_1=a_2/r$。和は $\\dfrac{a_1(r^n-1)}{r-1}$。</p>","3歩進んだ分の倍率が、1歩の倍率の3乗になる。",7)
# 8 等差数列と等比数列
def b8(a,d,r):
    # a1=a, a2=a+d, a3 = a+2d are geometric ... : three numbers (a-d,a,a+d), sum S, product P
    pass
def b8(a,d):
    S=3*a; Pr=a*(a*a-d*d)
    st=[("3数をおく","<p>等差数列をなす3数を "+I("a-d,\\ a,\\ a+d")+" とおく。</p>"),
        ("和","<p>"+D(r"(a-d)+a+(a+d)=3a=%d\ \Rightarrow\ a=%d"%(S,a))),
        ("積","<p>"+D(r"a(a^2-d^2)=%d\ \Rightarrow\ %d^2-d^2=%d\ \Rightarrow\ d^2=%d"%(Pr,a,Pr//a,a*a-Pr//a))+"<p>"+I("d=\\pm%d"%abs(d))+"。</p>"),
        ("3数",D(r"%d,\ %d,\ %d"%tuple(sorted([a-abs(d),a,a+abs(d)]))))]
    return r"等差数列をなす3つの数があり、和が $%d$、積が $%d$ である。この3数を小さい順に求めよ。"%(S,Pr),st,r"%d,\ %d,\ %d"%tuple(sorted([a-abs(d),a,a+abs(d)]))
o=[b8(*v) for v in [(5,3),(6,4),(4,2),(7,3),(8,5)]]
build(Z,CH,"和と積から等差数列をなす3数",o,"<p>等差数列の3数は<b>$a-d,\\ a,\\ a+d$</b> とおくと和が $3a$ になって楽。積は $a(a^2-d^2)$。</p>","真ん中を基準に左右へ同じだけ。",8)
# 9 初めて超える項
def b9(a1,r,N):
    k=next(m for m in range(1,100) if a1*r**(m-1)>N)
    st=[("一般項","<p>"+D(r"a_n=%d\cdot%d^{n-1}"%(a1,r))),
        ("不等式","<p>"+D(r"%d\cdot%d^{n-1}>%d"%(a1,r,N))+"<p>"+I("n")+" を順に調べる：</p>"+D(r"%s"%(r",\ ".join(r"a_{%d}=%d"%(m,a1*r**(m-1)) for m in range(max(1,k-2),k+1))))),
        ("答え","<p>初めて "+I(str(N))+" を超えるのは 第 "+I(str(k))+" 項。</p>")]
    return r"初項 $%d$、公比 $%d$ の等比数列 $\{a_n\}$ について、初めて $%d$ を超えるのは第何項か。"%(a1,r,N),st,"第 %d 項"%k
o=[b9(*v) for v in [(3,2,1000),(5,3,5000),(2,4,10000),(7,2,5000),(1,5,3000)]]
build(Z,CH,"等比数列が初めて N を超える項",o,"<p>$a_n=a_1r^{n-1}$ を不等式にし、2の冪・3の冪を<b>順に計算して</b>最初に超える $n$ を見つける。（対数が使えるなら対数でも可）</p>","2倍・3倍とふえていくので、実際にたどればすぐ。",9)
# 10 等差数列の和の最大
def b10(a1,d):
    # a_n = a1 - d(n-1): positive until ...
    an=lambda m:a1-d*(m-1); mx=max(m for m in range(1,200) if an(m)>0)
    S=lambda m:m*(2*a1-d*(m-1))//2
    best=max(range(1,200),key=S)
    st=[("一般項","<p>"+D(r"a_n=%d-%d(n-1)=%d"%(a1,d,a1+d)+r"-%dn"%d)+"<p>"+I("a_n>0\\iff n<%s"%L(R(a1+d,d)))+"。</p>"),
        ("正の項まで","<p>"+I("a_{%d}=%d>0"%(mx,an(mx)))+"、"+I("a_{%d}=%d<0"%(mx+1,an(mx+1)))+"。"+I("S_n")+" は第 "+I(str(mx))+" 項まで増え続ける。</p>"),
        ("最大値",D(r"S_{%d}=\dfrac{%d}{2}\{2\cdot%d+(%d-1)\cdot(-%d)\}=%d"%(mx,mx,a1,mx,d,S(mx))))]
    assert best==mx or S(best)==S(mx)
    return r"初項 $%d$、公差 $-%d$ の等差数列の初項から第 $n$ 項までの和 $S_n$ が最大になる $n$ と、その最大値を求めよ。"%(a1,d),st,r"n=%d,\ S_{%d}=%d"%(mx,mx,S(mx))
o=[b10(*v) for v in [(50,4),(47,5),(61,6),(35,3),(80,7)]]
build(Z,CH,"等差数列の和の最大",o,"<p>公差が負なので項はだんだん減る。<b>正の項だけを足し切った</b>ところで和が最大。$a_n>0$ をみたす最大の $n$ を求める。</p>","プラスの項を全部足したところが最高点。",10)
XU=finishx(Z,CH)
