# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
def Q(e): return L(e) if e>=0 else r'\left('+L(e)+r'\right)'
def co(c): return '' if c==1 else ('-' if c==-1 else L(c))
R=sp.Rational; n=sp.Symbol('n',positive=True); k_=sp.Symbol('k'); xx=sp.Symbol('x',real=True); _c=[0]
# 例題1 部分分数の級数
def b1(c,k):
    S=sp.together(R(c,k)*(sum(R(1,j) for j in range(1,k+1))-sum(1/(n+j) for j in range(1,k+1)))); ans=R(c,k)*sum(R(1,j) for j in range(1,k+1))
    assert all(sum(R(c,i*(i+k)) for i in range(1,N+1))==S.subs(n,N) for N in (1,4,9))
    head=r"\left(\dfrac11-\dfrac1{%d}\right)+\left(\dfrac12-\dfrac1{%d}\right)+\cdots+\left(\dfrac1n-\dfrac1{n+%d}\right)"%(1+k,2+k,k)
    st=[("部分分数に分ける","<p>"+I(r"\dfrac1n-\dfrac1{n+%d}=\dfrac{(n+%d)-n}{n(n+%d)}=\dfrac{%d}{n(n+%d)}"%(k,k,k,k,k))+" だから、"+I(r"\dfrac1{n(n+%d)}=\dfrac1{%d}\left(\dfrac1n-\dfrac1{n+%d}\right)"%(k,k,k))+"。</p>"+D(r"\dfrac{%d}{n(n+%d)}=%s\left(\dfrac1n-\dfrac1{n+%d}\right)"%(c,k,co(R(c,k)),k))),
        ("部分和 $S_n$ を求める","<p>初項から第 $n$ 項までの和は、途中の項が消えて</p>"+D(r"S_n=%s\left\{%s\right\}"%(co(R(c,k)),head))+D(r"S_n=%s\left\{\left(%s\right)-\left(%s\right)\right\}"%(co(R(c,k)),"+".join(r"\dfrac1{%d}"%j for j in range(1,k+1)),"-".join(["0"]) if False else "+".join(r"\dfrac1{n+%d}"%j for j in range(1,k+1))))),
        ("$n\\to\\infty$","<p>"+I(r"n\to\infty")+" のとき "+I(r"\dfrac1{n+j}\to0")+"（"+I("j=1,\\dots,%d"%k)+"）。</p>"+D(r"\sum_{n=1}^{\infty}\dfrac{%d}{n(n+%d)}=\lim_{n\to\infty}S_n=%s\left(%s\right)=%s"%(c,k,co(R(c,k)),"+".join(r"\dfrac1{%d}"%j for j in range(1,k+1)),L(ans))))]
    return r"無限級数 $\displaystyle\sum_{n=1}^{\infty}\dfrac{%d}{n(n+%d)}$ の和を求めよ。"%(c,k),st,L(ans)
V=[(1,1),(2,2),(1,2),(3,3),(1,3)]
o=[b1(*v) for v in V]
build(Z,CH,"部分分数で表せる無限級数",o,r"<p>無限級数の和 $=$ <b>部分和 $S_n$ の極限</b>。部分分数に分けて書き並べ、消える項を除いて $S_n$ を $n$ の式で求めてから $n\to\infty$ とする。</p>","望遠鏡のように縮む和。端に残った項だけが $n\\to\\infty$ で勝負する。",1)
# 例題2 等比級数の和
def b2(a,r1,b,r2):
    r1=R(r1); r2=R(r2); assert abs(r1)<1 and abs(r2)<1; S1=a*r1/(1-r1); S2=b*r2/(1-r2); S=S1+S2
    assert abs(float(sum(a*r1**i+b*r2**i for i in range(1,200)))-float(S))<1e-9
    st=[("収束を確認","<p>公比 "+I(L(r1))+"、"+I(L(r2))+" はどちらも絶対値が 1 より小さいので、2つの無限等比級数は収束する。</p>"),
        ("それぞれの和","<p>"+I(r"\sum_{n=1}^\infty ar^{n}=\dfrac{ar}{1-r}")+"（初項 $ar$、公比 $r$）。</p>"+D(r"\sum_{n=1}^{\infty}%s\left(%s\right)^n:\ \text{初項 }%s,\ \text{公比 }%s\ \Rightarrow\ \dfrac{%s}{1-%s}=\dfrac{%s}{%s}=%s"%(co(a),L(r1),L(a*r1),L(r1),L(a*r1),Q(r1),L(a*r1),L(1-r1),L(S1)))+D(r"\sum_{n=1}^{\infty}%s\left(%s\right)^n:\ \text{初項 }%s,\ \text{公比 }%s\ \Rightarrow\ \dfrac{%s}{1-%s}=\dfrac{%s}{%s}=%s"%(co(b),L(r2),L(b*r2),L(r2),L(b*r2),Q(r2),L(b*r2),L(1-r2),L(S2)))),
        ("たし合わせる","<p>収束する2つの級数は項ごとにたしてよい。</p>"+D(r"%s+%s=%s"%(L(S1),Q(S2),L(S))))]
    return r"無限級数 $\displaystyle\sum_{n=1}^{\infty}\left\{%s\left(%s\right)^n+%s\left(%s\right)^n\right\}$ の和を求めよ。"%(L(a),L(r1),L(b),L(r2)),st,L(S)
V=[(2,R(1,2),3,R(1,3)),(1,R(1,3),4,R(-1,2)),(3,R(2,3),2,R(-1,3)),(5,R(1,4),1,R(3,4)),(4,R(-1,2),6,R(1,5))]
o=[b2(*v) for v in V]
build(Z,CH,"無限等比級数の和",o,r"<p>初項 $a$、公比 $r$ の無限等比級数は <b>$|r|<1$ のとき収束</b>し、和は $\dfrac a{1-r}$。$|r|\geqq1$（$a\neq0$）なら発散。2つの収束する級数は項ごとに足してよい。</p>","毎回少しずつ縮む足し算は、有限の値に落ち着く。落ち着く値が $\\frac a{1-r}$。",2)
# 例題3 循環小数
def b3(i):
    cases=[(r"0.\dot4\dot5",R(45,99),r"0.45+0.0045+\cdots",R(45,100),R(1,100)),(r"0.\dot3",R(1,3),r"0.3+0.03+\cdots",R(3,10),R(1,10)),(r"1.\dot2\dot7",R(14,11),r"1+(0.27+0.0027+\cdots)",R(27,100),R(1,100)),(r"0.\dot1\dot8",R(18,99),r"0.18+0.0018+\cdots",R(18,100),R(1,100)),(r"2.\dot6",R(8,3),r"2+(0.6+0.06+\cdots)",R(6,10),R(1,10))]
    tx,val,ser,a,r=cases[i]; whole=0 if i not in (2,4) else (1 if i==2 else 2)
    S=a/(1-r)+whole; assert S==val and S==sp.nsimplify(val)
    st=[("無限級数で表す","<p>循環する部分を、等比数列の和として書く。</p>"+D(r"%s=%s"%(tx,ser))),
        ("初項と公比","<p>"+("整数部分 "+I(str(whole))+" をのぞいた部分は、" if whole else "")+"初項 "+I(L(a))+"、公比 "+I(L(r))+"。</p>"),
        ("和を求める",D(r"\dfrac{%s}{1-%s}=%s"%(L(a),L(r),L(a/(1-r))))+(D(r"%d+%s=%s"%(whole,L(a/(1-r)),L(S))) if whole else ""))]
    return r"循環小数 $%s$ を、無限等比級数の和を用いて分数で表せ。"%tx,st,L(S)
o=[b3(i) for i in range(5)]
build(Z,CH,"循環小数を分数に直す",o,r"<p>循環小数は無限等比級数。$0.\dot a\dot b=0.ab+0.00ab+\cdots$ は初項 $\dfrac{ab}{100}$、公比 $\dfrac1{100}$。和の公式 $\dfrac a{1-r}$ を使う。整数部分は別に足す。</p>","同じ並びがくり返す小数は、くり返しごとに $\\frac1{10}$ や $\\frac1{100}$ になる等比数列。",3)
# 例題4 収束条件
def b4(kind):
    cases=[((xx-1)/2,"(x-1)/2",None),((xx+2)/3,"(x+2)/3",None),(xx**2-1,"x^2-1",None),(xx**2-2,"x^2-2",None),(2*xx/(1+xx**2)*0+xx/(1+xx),"x/(1+x)",None)]
    r,rt,_=cases[kind]
    xs=np.linspace(-6,6,240001); import numpy as np_
    f=sp.lambdify(xx,r,"numpy")
    with np.errstate(all="ignore"): rv=f(xs)
    mask=(np.abs(rv)<1)&np.isfinite(rv)
    # 区間（ex: -2..)
    idx=np.where(mask)[0]; segs=[]; start=idx[0]; prev=idx[0]
    for i in idx[1:]:
        if i!=prev+1: segs.append((xs[start],xs[prev])); start=i
        prev=i
    segs.append((xs[start],xs[prev]))
    S=sp.simplify(r/(1-r))
    ineq={0:(r"-2<x<3",r"-1<\dfrac{x-1}{2}<1\ \Rightarrow\ -2<x-1<2"),1:(r"-5<x<1",r"-1<\dfrac{x+2}{3}<1\ \Rightarrow\ -3<x+2<3"),2:(r"-\sqrt2<x<\sqrt2,\ x\neq0",r"-1<x^2-1<1\ \Rightarrow\ 0<x^2<2"),3:(r"-\sqrt3<x<-1,\ 1<x<\sqrt3",r"-1<x^2-2<1\ \Rightarrow\ 1<x^2<3"),4:(r"x>-\dfrac12",r"-1<\dfrac{x}{1+x}<1")}[kind]
    ans_rng,derive=ineq
    if kind==0: assert abs(segs[0][0]-(-1))<1e-3 and abs(segs[0][1]-3)<1e-3
    if kind==4: assert abs(segs[0][0]-(-0.5))<1e-3
    st=[("公比を読みとる","<p>"+I(r"\sum_{n=1}^\infty %s^n"%("\\left(%s\\right)"%L(r)))+" は初項 "+I(L(r))+"、公比 "+I(L(r))+" の無限等比級数。</p>"),
        ("収束条件","<p>"+I(r"|r|<1")+" のとき収束する。</p>"+D(r"\left|%s\right|<1"%L(r))+D(derive)+D(ans_rng)),
        ("和","<p>収束するとき "+I(r"\dfrac{r}{1-r}")+"。</p>"+D(r"S=\dfrac{%s}{1-%s}=%s"%(L(r),"\\left(%s\\right)"%L(r),L(S))))]
    # 修正: 公比 x/(1+x) の場合は範囲を別途
    return r"無限級数 $\displaystyle\sum_{n=1}^{\infty}\left(%s\right)^n$ が収束するような $x$ の範囲を求め、そのときの和を $x$ で表せ。"%L(r),st,r"%s,\ \ S=%s"%(ans_rng,L(S))
o=[b4(i) for i in range(5)]
build(Z,CH,"無限等比級数の収束条件",o,r"<p>$\displaystyle\sum r^n$（公比 $r$ は $x$ の式）が収束 $\iff |r|<1$。$-1<r<1$ を $x$ について解き、収束するときの和 $\dfrac r{1-r}$ を求める。</p>","公比の絶対値が1より小さければ収束。条件を $x$ の不等式に翻訳して解く。",4)
# 例題5 図形への応用
def b5(a):
    a=sp.Integer(a); ca=sp.pi*a**2/4; Sa=ca/(1-R(1,2)); Sq=a**2/(1-R(1,2))
    _c[0]+=1
    def fn(ax):
        s=float(a); cx=cy=0; ang=0
        for i in range(5):
            half=s/2
            sq=np.array([[-half,-half],[half,-half],[half,half],[-half,half],[-half,-half]]); ca_,sa_=np.cos(ang),np.sin(ang)
            xs_=sq[:,0]*ca_-sq[:,1]*sa_; ys_=sq[:,0]*sa_+sq[:,1]*ca_; ax.plot(xs_,ys_,color="#b81f36",lw=1.6)
            t=np.linspace(0,2*np.pi,200); ax.plot(half*np.cos(t),half*np.sin(t),color="#1f6fb8",lw=1.4)
            s=s/np.sqrt(2); ang+=np.pi/4
        ax.set_aspect("equal"); ax.axis("off")
    make_fig("ic31_e%d"%_c[0],fn,size=(3.4,3.4)); fig=img("ic31_e%d"%_c[0],40)
    st=[("面積の比を求める","<p>1辺 "+I(str(a))+" の正方形の内接円（半径 "+I(L(a/2))+"）の内接正方形は、1辺が円の半径の $\\sqrt2$ 倍。</p>"+D(r"\text{次の正方形の1辺}=\dfrac{a}{\sqrt2}\ \Rightarrow\ \text{面積比 }\dfrac12")),
        ("円の面積の総和","<p>第1の円：初項 "+I(r"\pi\left(\dfrac{%s}{2}\right)^2=%s"%(L(a),L(ca)))+"、公比 "+I(r"\dfrac12")+"。</p>"+D(r"\dfrac{%s}{1-\frac12}=%s"%(L(ca),L(Sa)))),
        ("正方形の面積の総和","<p>初項 "+I(r"%s^2=%s"%(L(a),L(a**2)))+"、公比 "+I(r"\dfrac12")+"。</p>"+D(r"\dfrac{%s}{1-\frac12}=%s"%(L(a**2),L(Sq)))+fig)]
    return r"1辺の長さが $%d$ の正方形に内接する円をかき、その円に内接する正方形をかき、さらにその正方形に内接する円をかく……という操作を限りなくくり返す。円の面積の総和と、正方形の面積の総和を求めよ。"%a,st,r"\text{円 }%s,\ \text{正方形 }%s"%(L(Sa),L(Sq))
V=[2,4,6,3,8]
o=[b5(v) for v in V]
build(Z,CH,"図形の面積の総和",o,r"<p>くり返しの図形では、<b>面積比（相似比の2乗）</b>が公比。初項と公比を求めて $\dfrac a{1-r}$。内接円の内接正方形は辺の比が $\dfrac1{\sqrt2}$、面積比 $\dfrac12$。</p>","同じ操作のくり返しは相似。相似比の2乗が面積の縮み方（公比）。",5)
UNIT=finish(Z,CH,0,1,"極限","無限級数","部分分数の和、等比級数、循環小数、収束条件、図形への応用まで、無限級数の難問に挑みます。",subject="3")
